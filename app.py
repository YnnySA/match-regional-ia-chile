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
from src.dashboard.metrics import filter_offer, filter_offer_detail, summarize_offer_detail
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
st.markdown(f"INTELIGENCIA TERRITORIAL  /  {view}", unsafe_allow_html=False)
st.title(APP_TITLE)
st.markdown(f'<p class="dashboard-subtitle">{APP_SUBTITLE}</p>', unsafe_allow_html=True)
st.caption(f"{DATA_CUTOFF}  ·  16 REGIONES  ·  TODOS LOS NIVELES")

offer, offer_status = load_available("match_regional")
infrastructure, infrastructure_status = load_available("infraestructura_sedes")
offer_detail, offer_detail_status = load_available("oferta_fina")
lq_detail, lq_status = load_available("lq_cine_regional")
demand, demand_status = load_available("demanda_regional")
infrastructure_regional, infrastructure_regional_status = load_available("infraestructura_regional")

if offer is None:
    st.warning(f"{offer_status.state}: {offer_status.message}")
    offer = __import__("pandas").DataFrame()

filtered_offer = filter_offer(offer, region_orders, gratuidad, areas, levels)
filtered_detail = filter_offer_detail(offer_detail, region_orders, gratuidad, areas, levels)
filtered_offer = summarize_offer_detail(filtered_detail, filtered_offer)
filtered_match_master = (
    offer[offer["region_orden"].isin(region_orders)].copy()
    if offer is not None and "region_orden" in offer.columns
    else offer
)
filtered_infrastructure = (
    infrastructure[infrastructure["region_orden"].isin(region_orders)]
    if infrastructure is not None and "region_orden" in infrastructure.columns
    else infrastructure
)
filtered_lq = (
    lq_detail[lq_detail["region_orden"].isin(region_orders)]
    if lq_detail is not None and "region_orden" in lq_detail.columns
    else lq_detail
)
filtered_demand = (
    demand[demand["region_orden"].isin(region_orders)]
    if demand is not None and "region_orden" in demand.columns
    else demand
)
filtered_infrastructure_regional = (
    infrastructure_regional[infrastructure_regional["region_orden"].isin(region_orders)]
    if infrastructure_regional is not None and "region_orden" in infrastructure_regional.columns
    else infrastructure_regional
)
render_kpis(filtered_offer, filtered_infrastructure)

render_tabs(
    filtered_offer,
    filtered_infrastructure,
    infrastructure_status,
    filtered_detail,
    filtered_lq,
    filtered_demand,
    filtered_infrastructure_regional,
    infrastructure_regional_status,
    filtered_match_master,
    view,
)

st.divider()
st.caption(
    "Fuente única de resultados: data/processed · "
    "Trazabilidad técnica: notebooks/sprint1_match_ia_regional.ipynb"
)
