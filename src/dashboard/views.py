"""Native Streamlit views shared by the dashboard entry point."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from .constants import COLORS, DATA_CUTOFF
from .loaders import load_available
from .metrics import calculate_kpis, filter_offer, national_reference
from .theme import panel_title, status_message


def render_kpis(offer: pd.DataFrame, infrastructure: pd.DataFrame | None) -> None:
    kpis = calculate_kpis(offer, infrastructure)
    columns = st.columns(4)
    cards = (
        ("Total Titulados", f"{kpis['total_titulados']:,}", f"{DATA_CUTOFF} · total nacional"),
        ("Titulados Afines a IA", f"{kpis['titulados_ia']:,}", "participación de áreas afines"),
        (
            "Cobertura Gratuidad en IA",
            f"{kpis['cobertura_gratuidad']:.2f}%" if kpis["cobertura_gratuidad"] is not None else "—",
            "titulados afines con gratuidad",
        ),
        ("Sedes Físicas Georreferenciadas", f"{kpis['sedes']:,}", "artefacto de infraestructura"),
    )
    for column, (label, value, help_text) in zip(columns, cards):
        column.metric(label, value, help_text)


def render_sidebar() -> tuple[str, list[int], str, list[str], list[str]]:
    with st.sidebar:
        st.markdown("### Match-IA Regional")
        st.caption("TECH-MACI")
        view = st.radio(
            "Navegación",
            ("Visión General", "Oferta y Titulados", "Especialización (LQ)", "Infraestructura Geo"),
            label_visibility="collapsed",
        )
        st.divider()
        st.caption("FILTROS TERRITORIALES")
        region_options = {
            1: "Arica y Parinacota", 2: "Tarapacá", 3: "Antofagasta", 4: "Atacama",
            5: "Coquimbo", 6: "Valparaíso", 7: "Metropolitana de Santiago",
            8: "Libertador General Bernardo O'Higgins", 9: "Maule", 10: "Ñuble", 11: "Biobío",
            12: "La Araucanía", 13: "Los Ríos", 14: "Los Lagos",
            15: "Aysén del General Carlos Ibáñez del Campo",
            16: "Magallanes y de la Antártica Chilena",
        }
        selected_names = st.multiselect("Región", list(region_options.values()), default=["Valparaíso"])
        selected_orders = [order for order, name in region_options.items() if name in selected_names] or list(region_options)
        gratuidad = st.radio("Gratuidad", ("Todas", "Con", "Sin"), horizontal=True)
        areas = st.multiselect("Área CINE-F-13", ("TIC", "Ingeniería, industria y construcción", "Ciencias naturales"), default=[])
        levels = st.multiselect("Nivel", ("Universitario", "Técnico"), default=[])
        st.divider()
        st.caption("Chile · Cobertura nacional")
        st.caption("CORTE 2025 · 16 REGIONES")
    return view, selected_orders, gratuidad, areas, levels


def render_overview(offer: pd.DataFrame) -> None:
    panel_title("Ranking territorial: % afín a IA", "Participación sobre titulados de cada región")
    if offer.empty:
        status_message("sin datos", "No hay registros para la selección territorial.")
        return
    chart = offer.set_index("region_nombre")["pct_afin_ia"].sort_values(ascending=True)
    st.bar_chart(chart, color=COLORS["accent"])
    reference = national_reference(offer)
    if reference is not None:
        st.caption(f"Referencia nacional calculada desde conteos aditivos: {reference:.2f}%")


def render_offer(offer: pd.DataFrame) -> None:
    panel_title("Oferta y titulados", "Resultados agregados por región; sin lectura de insumos crudos.")
    if offer.empty:
        status_message("sin datos", "La combinación de filtros no tiene registros.")
        return
    display = offer[
        ["region_nombre", "n_titulados_total", "n_titulados_afin_ia", "pct_afin_ia",
         "lq_afin_ia", "pct_cobertura_gratuidad_afin", "n_sedes"]
    ].rename(columns={
        "region_nombre": "Región", "n_titulados_total": "Titulados",
        "n_titulados_afin_ia": "Afines a IA", "pct_afin_ia": "% afín",
        "lq_afin_ia": "LQ IA", "pct_cobertura_gratuidad_afin": "% cobertura gratuidad",
        "n_sedes": "Sedes",
    })
    st.dataframe(display, use_container_width=True, hide_index=True)


def render_specialization(offer: pd.DataFrame) -> None:
    panel_title("Especialización regional (LQ)", "LQ superior a 1 indica concentración relativa sobre la referencia nacional.")
    if offer.empty:
        status_message("sin datos", "No hay LQ disponibles para la selección.")
        return
    chart = offer.set_index("region_nombre")["lq_afin_ia"]
    st.bar_chart(chart, color=COLORS["accent"])


def render_infrastructure(infrastructure: pd.DataFrame | None, status) -> None:
    panel_title("Accesibilidad territorial de las sedes", "Red vial, servicios y conectividad digital.")
    if infrastructure is None:
        status_message(status.state, status.message or "La tabla de infraestructura no está disponible.")
        return
    if infrastructure.empty:
        status_message("sin datos", "El artefacto de infraestructura no tiene registros.")
        return
    st.dataframe(
        infrastructure[["region_nombre", "cod_sede", "comuna_nombre", "estado_sede",
                         "estado_d_via", "estado_servicios", "estado_conectividad"]].head(100),
        use_container_width=True,
        hide_index=True,
    )


def render_tabs(offer: pd.DataFrame, infrastructure: pd.DataFrame | None, infra_status) -> None:
    tab_offer, tab_lq, tab_geo = st.tabs(
        ("Oferta y titulados", "Especialización regional", "Accesibilidad y entorno")
    )
    with tab_offer:
        render_overview(offer)
    with tab_lq:
        render_specialization(offer)
    with tab_geo:
        render_infrastructure(infrastructure, infra_status)
