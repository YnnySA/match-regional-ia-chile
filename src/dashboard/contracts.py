"""Contract validation for dashboard artifacts.

The dashboard only consumes processed, versioned artifacts. This module keeps
validation separate from rendering so a failed source becomes a visible state.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

from .constants import REGION_BY_ORDER

MOJIBAKE_PATTERNS = (
    re.compile(r"Ã.|Â.|â€|â€™|â€œ|â€\x9d|�"),
    re.compile(r"\b(?:CrÃ|PeÃ|RegiÃ|EducaciÃ|TÃ)\w*"),
)
VALID_STATES = {"disponible", "pendiente", "sin datos", "excluido", "no disponible"}


@dataclass(frozen=True)
class ArtifactStatus:
    artifact_id: str
    state: str
    message: str
    path: str


def contains_mojibake(value: Any) -> bool:
    return any(pattern.search(str(value)) for pattern in MOJIBAKE_PATTERNS)


def validate_text_encoding(frame: pd.DataFrame) -> None:
    for column in frame.select_dtypes(include=["object", "string"]).columns:
        sample = frame[column].dropna().astype(str)
        if sample.map(contains_mojibake).any():
            bad = sample.loc[sample.map(contains_mojibake)].iloc[0]
            raise ValueError(f"texto mojibake detectado en {column}: {bad}")


def validate_region_keys(frame: pd.DataFrame, artifact_id: str) -> None:
    if "region_orden" not in frame.columns:
        return
    if frame["region_orden"].isna().any():
        raise ValueError("region_orden contiene nulos")
    orders = pd.to_numeric(frame["region_orden"], errors="coerce")
    if orders.isna().any() or not orders.astype(int).isin(REGION_BY_ORDER).all():
        raise ValueError("region_orden debe pertenecer al rango nacional 1..16")
    if "region_nombre" in frame.columns:
        mismatched = frame.loc[
            frame["region_nombre"].astype(str)
            != orders.astype(int).map(REGION_BY_ORDER).astype(str)
        ]
        if not mismatched.empty:
            raise ValueError("region_nombre no coincide con region_orden")
    if artifact_id in {"oferta_regional", "demanda_regional", "match_regional"}:
        if frame["region_orden"].duplicated().any():
            raise ValueError("la tabla regional contiene region_orden duplicados")


def validate_manifest_entry(frame: pd.DataFrame, entry: dict[str, Any], path: Path) -> None:
    required = set(entry.get("columns", {}))
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"faltan columnas: {', '.join(sorted(missing))}")
    validate_text_encoding(frame)
    validate_region_keys(frame, entry["id"])
    expected_rows = entry.get("rows")
    if expected_rows is not None and int(expected_rows) != len(frame):
        raise ValueError(f"filas esperadas {expected_rows}, observadas {len(frame)}")
    expected_hash = entry.get("sha256")
    if expected_hash:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != expected_hash:
            raise ValueError("hash sha256 no coincide con el manifest")


def load_manifest(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def artifact_status(entry: dict[str, Any], base_dir: Path) -> ArtifactStatus:
    path = base_dir / entry["path"]
    if entry.get("state") in VALID_STATES and entry["state"] in {"pendiente", "excluido"}:
        return ArtifactStatus(entry["id"], entry["state"], entry.get("note", ""), str(path))
    if not path.exists():
        return ArtifactStatus(entry["id"], "no disponible", "artefacto ausente", str(path))
    if path.stat().st_size == 0:
        return ArtifactStatus(entry["id"], "sin datos", "artefacto vacío", str(path))
    return ArtifactStatus(entry["id"], "disponible", "", str(path))
