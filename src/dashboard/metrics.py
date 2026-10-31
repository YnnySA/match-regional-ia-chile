"""Pure transformations over already aggregated dashboard tables."""

from __future__ import annotations

import pandas as pd

from .constants import MVP_REGION_ORDERS

IA_AREAS = {
    "Tecnología de la Información y la Comunicación (TIC)",
    "Ingeniería, Industria y Construcción",
    "Ciencias naturales, matemáticas y estadística",
}


def filter_offer(
    frame: pd.DataFrame,
    region_orders: list[int],
    gratuidad: str,
    areas: list[str] | None = None,
    levels: list[str] | None = None,
) -> pd.DataFrame:
    if frame.empty or "region_orden" not in frame.columns:
        return frame.copy()
    result = frame[frame["region_orden"].isin(region_orders)].copy()
    if gratuidad == "Con" and "n_titulados_gratuidad" in result.columns:
        result = result[result["n_titulados_gratuidad"] > 0]
    elif gratuidad == "Sin" and "n_titulados_gratuidad" in result.columns:
        result = result[result["n_titulados_total"] > result["n_titulados_gratuidad"]]
    # Regional rows do not carry area/level dimensions. Those filters are
    # applied to the fine-grained artifact and summarized by the caller.
    del areas, levels
    return result


def filter_offer_detail(
    frame: pd.DataFrame | None,
    region_orders: list[int],
    gratuidad: str,
    areas: list[str] | None = None,
    levels: list[str] | None = None,
) -> pd.DataFrame:
    if frame is None:
        return pd.DataFrame()
    if frame.empty:
        return frame.copy()
    result = frame[frame["region_orden"].isin(region_orders)].copy()
    if gratuidad == "Con":
        result = result[result["inst_gratuidad"].eq(1)]
    elif gratuidad == "Sin":
        result = result[result["inst_gratuidad"].eq(0)]
    if areas:
        result = result[result["area_cine_f13"].isin(areas)]
    if levels:
        result = result[result["nivel_formativo"].isin(levels)]
    return result


def aggregate_offer_detail(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return frame.copy()
    group_columns = ["region_orden", "region_nombre"]
    result = frame.groupby(group_columns, as_index=False)["n_titulados"].sum()
    result = result.rename(columns={"n_titulados": "n_titulados_total"})
    return result


def summarize_offer_detail(detail: pd.DataFrame, regional: pd.DataFrame) -> pd.DataFrame:
    if detail.empty:
        return regional.iloc[0:0].copy()
    grouped = detail.groupby("region_orden", as_index=False).agg(
        n_titulados_total=("n_titulados", "sum"),
        n_titulados_gratuidad=("n_titulados", lambda values: 0),
    )
    gratuidad = detail[detail["inst_gratuidad"].eq(1)].groupby("region_orden")["n_titulados"].sum()
    afin = detail[detail["area_cine_f13"].isin(IA_AREAS)]
    afin_counts = afin.groupby("region_orden")["n_titulados"].sum()
    afin_grat = afin[afin["inst_gratuidad"].eq(1)].groupby("region_orden")["n_titulados"].sum()
    grouped["n_titulados_gratuidad"] = grouped["region_orden"].map(gratuidad).fillna(0)
    grouped["n_titulados_afin_ia"] = grouped["region_orden"].map(afin_counts).fillna(0)
    grouped["n_titulados_afin_ia_gratuidad"] = grouped["region_orden"].map(afin_grat).fillna(0)
    regional_indexed = regional.set_index("region_orden")
    grouped["region_nombre"] = grouped["region_orden"].map(regional_indexed["region_nombre"])
    grouped["n_sedes"] = grouped["region_orden"].map(
        regional_indexed["n_sedes"] if "n_sedes" in regional else pd.Series(dtype=float)
    ).fillna(0)
    grouped["pct_afin_ia"] = (
        100 * grouped["n_titulados_afin_ia"] / grouped["n_titulados_total"]
    ).where(grouped["n_titulados_total"].ne(0), 0)
    grouped["pct_cobertura_gratuidad_afin"] = (
        100 * grouped["n_titulados_afin_ia_gratuidad"] / grouped["n_titulados_afin_ia"]
    ).where(grouped["n_titulados_afin_ia"].ne(0))
    grouped["lq_afin_ia"] = grouped["pct_afin_ia"] / (
        100 * grouped["n_titulados_afin_ia"].sum() / grouped["n_titulados_total"].sum()
    )
    return grouped


def calculate_kpis(offer: pd.DataFrame, infrastructure: pd.DataFrame | None) -> dict[str, float | int | None]:
    if offer.empty:
        return {
            "total_titulados": 0,
            "titulados_ia": 0,
            "cobertura_gratuidad": None,
            "sedes": 0,
        }
    total = int(offer["n_titulados_total"].sum())
    ia = int(offer["n_titulados_afin_ia"].sum())
    ia_gratuidad = int(offer["n_titulados_afin_ia_gratuidad"].sum())
    cobertura = round(100 * ia_gratuidad / ia, 2) if ia else None
    sedes = int(offer["n_sedes"].sum())
    if infrastructure is not None and not infrastructure.empty:
        sedes = int(infrastructure["cod_sede"].nunique())
    return {
        "total_titulados": total,
        "titulados_ia": ia,
        "cobertura_gratuidad": cobertura,
        "sedes": sedes,
    }


def national_reference(frame: pd.DataFrame) -> float | None:
    if frame.empty:
        return None
    total = frame["n_titulados_total"].sum()
    return round(100 * frame["n_titulados_afin_ia"].sum() / total, 2) if total else None


def mvp_label(region_order: int) -> str:
    return "MVP" if region_order in MVP_REGION_ORDERS else "estructura nacional"
