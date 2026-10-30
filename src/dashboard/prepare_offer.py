"""Offline preparation of offer artifacts for the dashboard.

This module is intentionally not imported by Streamlit. It reads the prepared
Sprint 1 titulado extract, materializes additive counts and exports compact
artifacts consumed by the application.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OFFER_DIR = PROJECT_ROOT / "data" / "oferta"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
TITULADOS_DIR = OFFER_DIR / "Titulados-Ed-Superior-2025"
GRATUIDAD_PATH = OFFER_DIR / "instituciones_gratuidad_2025.csv"
OUTPUT_FINE = PROCESSED_DIR / "oferta_fina_region_cine_nivel_gratuidad.csv"
OUTPUT_LQ = PROCESSED_DIR / "matriz_lq_cine_regional.csv"
OUTPUT_AUDIT = PROCESSED_DIR / "reporte_cruce_gratuidad.csv"

REGIONS = (
    "Arica y Parinacota",
    "Tarapacá",
    "Antofagasta",
    "Atacama",
    "Coquimbo",
    "Valparaíso",
    "Metropolitana de Santiago",
    "Libertador General Bernardo O'Higgins",
    "Maule",
    "Ñuble",
    "Biobío",
    "La Araucanía",
    "Los Ríos",
    "Los Lagos",
    "Aysén del General Carlos Ibáñez del Campo",
    "Magallanes y de la Antártica Chilena",
)

REGION_ALIASES = {
    "Arica y Parinacota": "Arica y Parinacota",
    "Tarapacá": "Tarapacá",
    "Antofagasta": "Antofagasta",
    "Atacama": "Atacama",
    "Coquimbo": "Coquimbo",
    "Valparaíso": "Valparaíso",
    "Metropolitana": "Metropolitana de Santiago",
    "Metropolitana de Santiago": "Metropolitana de Santiago",
    "Lib. Gral. B. O'Higgins": "Libertador General Bernardo O'Higgins",
    "Libertador General Bernardo O'Higgins": "Libertador General Bernardo O'Higgins",
    "Maule": "Maule",
    "Ñuble": "Ñuble",
    "Biobío": "Biobío",
    "La Araucanía": "La Araucanía",
    "Los Ríos": "Los Ríos",
    "Los Lagos": "Los Lagos",
    "Aysén": "Aysén del General Carlos Ibáñez del Campo",
    "Aysén del General Carlos Ibáñez del Campo": "Aysén del General Carlos Ibáñez del Campo",
    "Magallanes": "Magallanes y de la Antártica Chilena",
    "Magallanes y de la Antártica Chilena": "Magallanes y de la Antártica Chilena",
}

AREAS = (
    "Administración de Empresas y Derecho",
    "Agricultura, Silvicultura, Pesca y Veterinaria",
    "Artes y Humanidades",
    "Ciencias naturales, matemáticas y estadística",
    "Ciencias Sociales, Periodismo e Información",
    "Educación",
    "Ingeniería, Industria y Construcción",
    "Salud y Bienestar",
    "Servicios",
    "Tecnología de la Información y la Comunicación (TIC)",
)


def _key(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


AREA_ALIASES = {_key(area): area for area in AREAS}


def normalize_region(value: object) -> str:
    text = str(value).strip()
    if text in REGION_ALIASES:
        return REGION_ALIASES[text]
    key = _key(text)
    for alias, region in REGION_ALIASES.items():
        if _key(alias) == key:
            return region
    raise ValueError(f"región no homologada: {value!r}")


def normalize_area(value: object) -> str:
    key = _key(value)
    if key not in AREA_ALIASES:
        raise ValueError(f"área CINE-F-13 no homologada: {value!r}")
    return AREA_ALIASES[key]


def derive_level(row: pd.Series) -> str:
    career = _key(row["nivel_carrera_1"])
    if "tecnico" in career:
        return "Técnico"
    if row["nivel_global"] == "Pregrado":
        return "Universitario"
    return "Posgrado"


def load_prepared_titulados(path: Path | None = None) -> pd.DataFrame:
    source = path or next(TITULADOS_DIR.glob("*.csv"))
    columns = [
        "mrun",
        "cod_carrera",
        "cod_inst",
        "nivel_global",
        "nivel_carrera_1",
        "cine_f_13_area",
        "region_sede",
    ]
    frame = pd.read_csv(source, sep=";", encoding="utf-8", usecols=columns, low_memory=False)
    frame["region_nombre"] = frame["region_sede"].map(normalize_region)
    frame["area_cine_f13"] = frame["cine_f_13_area"].map(normalize_area)
    frame["nivel_formativo"] = frame.apply(derive_level, axis=1)
    frame["cod_inst"] = pd.to_numeric(frame["cod_inst"], errors="raise").astype("int64")
    return frame


def apply_gratuidad(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    gratuidad = pd.read_csv(GRATUIDAD_PATH, sep=";", encoding="utf-8")
    gratuidad["cod_inst"] = pd.to_numeric(gratuidad["cod_inst"], errors="raise").astype("int64")
    if gratuidad["cod_inst"].duplicated().any():
        raise ValueError("la nómina de gratuidad contiene cod_inst duplicados")
    result = frame.merge(
        gratuidad[["cod_inst", "adscrita_gratuidad"]],
        how="left",
        on="cod_inst",
        validate="many_to_one",
        indicator=True,
    )
    result["inst_gratuidad"] = result["adscrita_gratuidad"].fillna(0).astype("int64")
    result["estado_gratuidad"] = result["_merge"].map(
        {"both": "identificada en nómina Mineduc 2025", "left_only": "sin coincidencia en nómina"}
    )
    audit = (
        result.groupby(["estado_gratuidad"], as_index=False)
        .agg(registros=("cod_inst", "size"), instituciones=("cod_inst", "nunique"))
    )
    result = result.drop(columns=["adscrita_gratuidad", "_merge"])
    return result, audit


def build_fine_table(frame: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        frame.groupby(
            ["region_orden", "region_nombre", "area_cine_f13", "nivel_formativo", "inst_gratuidad"],
            as_index=False,
            dropna=False,
        )
        .agg(n_titulados=("mrun", "size"))
        .sort_values(["region_orden", "area_cine_f13", "nivel_formativo", "inst_gratuidad"])
    )
    grouped["fuente"] = "SIES-Mineduc 2025; gratuidad institucional Mineduc 2025"
    grouped["fecha_corte"] = "2025"
    grouped["estado_disponibilidad"] = "disponible"
    grouped["unidad"] = "titulados"
    return grouped.reset_index(drop=True)


def build_lq_table(fine: pd.DataFrame) -> pd.DataFrame:
    regional = fine.groupby(["region_orden", "region_nombre", "area_cine_f13"], as_index=False)["n_titulados"].sum()
    regional_total = fine.groupby(["region_orden", "region_nombre"], as_index=False)["n_titulados"].sum()
    regional = regional.merge(
        regional_total.rename(columns={"n_titulados": "denominador_regional"}),
        on=["region_orden", "region_nombre"],
        validate="many_to_one",
    )
    national = fine.groupby("area_cine_f13", as_index=False)["n_titulados"].sum()
    national = national.rename(columns={"n_titulados": "numerador_nacional"})
    national_total = int(fine["n_titulados"].sum())
    all_regions = pd.DataFrame(
        [(order, name, area) for order, name in enumerate(REGIONS, 1) for area in AREAS],
        columns=["region_orden", "region_nombre", "area_cine_f13"],
    )
    result = all_regions.merge(
        regional,
        on=["region_orden", "region_nombre", "area_cine_f13"],
        how="left",
    ).merge(national, on="area_cine_f13", how="left", validate="many_to_one")
    result["n_titulados"] = result["n_titulados"].fillna(0).astype("int64")
    result["denominador_regional"] = result["denominador_regional"].fillna(0).astype("int64")
    result["numerador_nacional"] = result["numerador_nacional"].fillna(0).astype("int64")
    result["denominador_nacional"] = national_total
    result["proporcion_regional"] = result["n_titulados"].div(
        result["denominador_regional"].where(result["denominador_regional"] > 0)
    )
    result["proporcion_nacional"] = result["numerador_nacional"] / result["denominador_nacional"]
    result["lq"] = result["proporcion_regional"] / result["proporcion_nacional"].where(
        result["proporcion_nacional"] > 0
    )
    result["estado_disponibilidad"] = result["lq"].notna().map(
        {True: "disponible", False: "sin datos"}
    )
    result["fuente"] = "SIES-Mineduc 2025"
    result["fecha_corte"] = "2025"
    result["unidad"] = "índice LQ"
    return result


def write_artifacts(fine: pd.DataFrame, lq: pd.DataFrame, audit: pd.DataFrame) -> dict:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    fine.to_csv(OUTPUT_FINE, sep=";", index=False, encoding="utf-8")
    lq.to_csv(OUTPUT_LQ, sep=";", index=False, encoding="utf-8")
    audit.to_csv(OUTPUT_AUDIT, sep=";", index=False, encoding="utf-8")
    return {
        "fine_rows": len(fine),
        "lq_rows": len(lq),
        "fine_sha256": hashlib.sha256(OUTPUT_FINE.read_bytes()).hexdigest(),
        "lq_sha256": hashlib.sha256(OUTPUT_LQ.read_bytes()).hexdigest(),
        "audit_sha256": hashlib.sha256(OUTPUT_AUDIT.read_bytes()).hexdigest(),
    }


def prepare(path: Path | None = None) -> dict:
    frame = load_prepared_titulados(path)
    frame, audit = apply_gratuidad(frame)
    frame["region_orden"] = frame["region_nombre"].map({name: i for i, name in enumerate(REGIONS, 1)})
    fine = build_fine_table(frame)
    lq = build_lq_table(fine)
    if fine["n_titulados"].lt(0).any() or fine.duplicated(
        ["region_orden", "area_cine_f13", "nivel_formativo", "inst_gratuidad"]
    ).any():
        raise ValueError("tabla fina inválida: conteos negativos o claves duplicadas")
    if int(fine["n_titulados"].sum()) != len(frame):
        raise ValueError("los conteos de la tabla fina no son aditivos")
    if len(lq) != 16 * len(AREAS):
        raise ValueError("la matriz LQ no cubre las 16 regiones y 10 áreas esperadas")
    return write_artifacts(fine, lq, audit)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Materializa artefactos de oferta para el dashboard.")
    parser.add_argument("--source", type=Path, default=None)
    args = parser.parse_args()
    print(json.dumps(prepare(args.source), ensure_ascii=False, indent=2))
