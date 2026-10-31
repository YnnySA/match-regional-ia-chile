"""Reproducible value and state checks between notebook artifacts and dashboard loaders."""

from __future__ import annotations

import sys

import pandas as pd

from .constants import MVP_REGION_ORDERS
from .loaders import load_available
from .metrics import IA_AREAS


def _require(artifact_id: str) -> pd.DataFrame:
    frame, status = load_available(artifact_id)
    if frame is None:
        raise AssertionError(f"{artifact_id}: {status.state}: {status.message}")
    return frame


def validate_parity() -> list[str]:
    match = _require("match_regional")
    demand = _require("demanda_regional")
    regional_infra = _require("infraestructura_regional")
    fine = _require("oferta_fina")
    lq = _require("lq_cine_regional")
    errors: list[str] = []
    if len(match) != 16:
        errors.append("ranking: expected 16 regions")
    if len(lq) != 160:
        errors.append("heatmap LQ: expected 16 regions x 10 CINE areas")
    if not fine["area_cine_f13"].isin(IA_AREAS).any():
        errors.append("gratuidad: no IA areas available in fine table")
    for region_order in MVP_REGION_ORDERS:
        match_row = match.loc[match["region_orden"].eq(region_order)].iloc[0]
        demand_row = demand.loc[demand["region_orden"].eq(region_order)].iloc[0]
        for column in ("n_trabajadores_total", "ire_ia", "pct_empleo_alta_exp",
                       "pct_empleo_media_exp", "pct_empleo_baja_exp"):
            if float(match_row[column]) != float(demand_row[column]):
                errors.append(f"{region_order}: {column} differs between match and demand")
        infra_row = regional_infra.loc[regional_infra["region_orden"].eq(region_order)].iloc[0]
        for column in ("estado_d_via_regional", "estado_servicios_regional",
                       "estado_conectividad_regional"):
            if infra_row[column] not in {"disponible", "pendiente", "sin datos", "excluido", "no disponible"}:
                errors.append(f"{region_order}: invalid infrastructure state {column}={infra_row[column]}")
        fine_total = fine.loc[fine["region_orden"].eq(region_order), "n_titulados"].sum()
        if fine_total <= 0:
            errors.append(f"{region_order}: fine offer total is zero")
    return errors


def main() -> int:
    errors = validate_parity()
    if errors:
        print("PARIDAD FALLIDA")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("PARIDAD OK: Match-IA, demanda e infraestructura MVP comparten valores y estados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
