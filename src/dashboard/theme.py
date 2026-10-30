"""Minimal centralized visual layer for native Streamlit components."""

from __future__ import annotations

import streamlit as st

from .constants import COLORS, FONT_STACK


def apply_theme() -> None:
    st.markdown(
        f"""
        <style>
        :root {{
          --font-stack: {FONT_STACK};
          --bg: {COLORS["background"]};
          --surface: {COLORS["surface"]};
          --panel: {COLORS["panel"]};
          --border: {COLORS["border"]};
          --text: {COLORS["text"]};
          --muted: {COLORS["muted"]};
          --accent: {COLORS["accent"]};
        }}
        html, body, [class*="css"], [data-testid="stAppViewContainer"] {{
          font-family: var(--font-stack);
        }}
        [data-testid="stAppViewContainer"] {{ background: var(--bg); }}
        [data-testid="stSidebar"] {{ background: #101c30; border-right: 1px solid var(--border); }}
        [data-testid="stMetric"] {{
          background: var(--surface); border: 1px solid var(--border);
          border-radius: 7px; padding: 14px 16px;
        }}
        [data-testid="stMetricValue"] {{ color: var(--text); }}
        div[data-baseweb="tab-list"] {{ gap: 4px; }}
        button[data-baseweb="tab"] {{ font-family: var(--font-stack); }}
        .dashboard-breadcrumb {{ color: var(--accent); font-size: 0.78rem; letter-spacing: .04em; }}
        .dashboard-subtitle, .dashboard-note, .dashboard-footer {{
          color: var(--muted); font-size: 0.78rem;
        }}
        .dashboard-panel {{
          background: var(--surface); border: 1px solid var(--border);
          border-radius: 7px; padding: 16px; min-height: 100px;
        }}
        .status-label {{ color: var(--accent); text-transform: uppercase; font-size: .72rem; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def panel_title(title: str, subtitle: str | None = None) -> None:
    st.markdown(f"#### {title}", unsafe_allow_html=False)
    if subtitle:
        st.caption(subtitle)


def status_message(state: str, message: str) -> None:
    text = f"{state}: {message}" if message else state
    if state == "disponible":
        st.success(text)
    elif state in {"pendiente", "sin datos"}:
        st.info(text)
    else:
        st.warning(text)
