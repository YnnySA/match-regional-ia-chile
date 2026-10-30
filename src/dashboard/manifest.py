"""Manifest metadata for processed dashboard artifacts."""

from __future__ import annotations

from pathlib import Path

from .contracts import load_manifest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
MANIFEST_PATH = PROCESSED_DIR / "dashboard_manifest.json"


def get_manifest() -> dict:
    return load_manifest(MANIFEST_PATH)
