"""Cached, lazy loaders for processed dashboard artifacts."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

try:
    import streamlit as st
except ImportError:  # pragma: no cover - allows contract tests without Streamlit
    class _StreamlitFallback:
        @staticmethod
        def cache_data(*args, **kwargs):
            def decorator(function):
                return function
            return decorator

    st = _StreamlitFallback()

from .contracts import ArtifactStatus, artifact_status, validate_manifest_entry
from .manifest import PROJECT_ROOT, PROCESSED_DIR, get_manifest


def _entry(artifact_id: str) -> dict:
    for entry in get_manifest()["artifacts"]:
        if entry["id"] == artifact_id:
            return entry
    raise KeyError(f"artefacto no declarado: {artifact_id}")


def get_artifact_status(artifact_id: str) -> ArtifactStatus:
    return artifact_status(_entry(artifact_id), PROCESSED_DIR.parent.parent)


@st.cache_data(show_spinner=False)
def load_artifact(artifact_id: str, file_signature: str = "") -> pd.DataFrame:
    del file_signature  # Included in the cache key to invalidate on mtime/hash changes.
    entry = _entry(artifact_id)
    path = PROJECT_ROOT / entry["path"]
    status = artifact_status(entry, PROCESSED_DIR.parent.parent)
    if status.state != "disponible":
        raise FileNotFoundError(f"{status.state}: {status.message}")
    frame = pd.read_csv(path, sep=entry.get("delimiter", ","), encoding="utf-8-sig")
    validate_manifest_entry(frame, entry, path)
    return frame


def load_available(artifact_id: str) -> tuple[pd.DataFrame | None, ArtifactStatus]:
    entry = _entry(artifact_id)
    status = artifact_status(entry, PROCESSED_DIR.parent.parent)
    if status.state != "disponible":
        return None, status
    path = PROJECT_ROOT / entry["path"]
    signature = f"{path.stat().st_mtime_ns}:{path.stat().st_size}"
    try:
        return load_artifact(artifact_id, signature), status
    except (OSError, ValueError, UnicodeError) as error:
        return None, ArtifactStatus(artifact_id, "no disponible", str(error), str(path))
