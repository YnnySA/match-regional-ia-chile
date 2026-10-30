"""Entry point for the Match-IA Regional Streamlit dashboard."""

from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.dashboard.constants import APP_SUBTITLE, APP_TITLE, DATA_CUTOFF
from src.dashboard.loaders import load_available
from src.dashboard.metrics import filter_offer
from src.dashboard.theme import apply_theme
from src.dashboard.views import render_kpis, render_sidebar, render_tabs

st.set_page_config(
    page_title="Match-IA Regional",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_theme()

view, region_orders, gratuidad, areas, levels = render_sidebar()
st.markdown("INTELIGENCIA TERRITORIAL  /  Visión General", unsafe_allow_html=False)
st.title(APP_TITLE)
st.markdown(f'<p class="dashboard-subtitle">{APP_SUBTITLE}</p>', unsafe_allow_html=True)
st.caption(f"{DATA_CUTOFF}  ·  16 REGIONES  ·  TODOS LOS NIVELES")

offer, offer_status = load_available("match_regional")
infrastructure, infrastructure_status = load_available("infraestructura_sedes")

if offer is None:
    st.warning(f"{offer_status.state}: {offer_status.message}")
    offer = __import__("pandas").DataFrame()

filtered_offer = filter_offer(offer, region_orders, gratuidad, areas, levels)
render_kpis(offer, infrastructure)
if "area_cine_f_13" not in offer.columns or "nivel" not in offer.columns:
    st.sidebar.info(
        "Área CINE-F-13 y nivel: pendiente de artefacto agregado. "
        "La selección se conserva sin convertir la ausencia en ceros."
    )

if view == "Visión General":
    render_tabs(filtered_offer, infrastructure, infrastructure_status)
elif view == "Oferta y Titulados":
    render_tabs(filtered_offer, infrastructure, infrastructure_status)
elif view == "Especialización (LQ)":
    render_tabs(filtered_offer, infrastructure, infrastructure_status)
else:
    render_tabs(filtered_offer, infrastructure, infrastructure_status)

st.divider()
st.caption(
    "Desgloses regionales pendientes de vincular al notebook · "
    "Fuente: data/processed y notebooks/sprint1_match_ia_regional.ipynb"
)
