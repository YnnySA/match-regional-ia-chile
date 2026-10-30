"""Pure transformations over already aggregated dashboard tables."""

from __future__ import annotations

import pandas as pd

from .constants import MVP_REGION_ORDERS


def filter_offer(
    frame: pd.DataFrame,
    region_orders: list[int],
    gratuidad: str,
    areas: list[str] | None = None,
    levels: list[str] | None = None,
) -> pd.DataFrame:
    del areas, levels  # Reserved for #20's area/level aggregate artifact.
    if frame.empty or "region_orden" not in frame.columns:
        return frame.copy()
    result = frame[frame["region_orden"].isin(region_orders)].copy()
    if gratuidad == "Con" and "n_titulados_gratuidad" in result.columns:
        result = result[result["n_titulados_gratuidad"] > 0]
    elif gratuidad == "Sin" and "n_titulados_gratuidad" in result.columns:
        result = result[result["n_titulados_total"] > result["n_titulados_gratuidad"]]
    return result


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
