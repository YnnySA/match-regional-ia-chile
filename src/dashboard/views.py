"""Native Streamlit views shared by the dashboard entry point."""

from __future__ import annotations

import pandas as pd
import json
from pathlib import Path
import streamlit as st
import altair as alt

from .constants import AREA_FILTER_OPTIONS, COLORS, DATA_CUTOFF, LEVEL_FILTER_OPTIONS, REGIONS
from .loaders import load_available
from .metrics import IA_AREAS, calculate_kpis, filter_offer, national_reference
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
        selected_names = st.multiselect(
            "Región",
            list(region_options.values()),
            default=list(region_options.values()),
        )
        selected_orders = [order for order, name in region_options.items() if name in selected_names] or list(region_options)
        gratuidad = st.radio("Gratuidad", ("Todas", "Con", "Sin"), horizontal=True)
        area_labels = st.multiselect(
            "Área CINE-F-13",
            tuple(AREA_FILTER_OPTIONS),
            default=list(AREA_FILTER_OPTIONS),
        )
        level_labels = st.multiselect("Nivel", tuple(LEVEL_FILTER_OPTIONS), default=[])
        areas = [AREA_FILTER_OPTIONS[label] for label in area_labels]
        levels = [LEVEL_FILTER_OPTIONS[label] for label in level_labels]
        st.divider()
        st.caption("Chile · Cobertura nacional")
        st.caption("CORTE 2025 · 16 REGIONES")
    return view, selected_orders, gratuidad, areas, levels


def render_overview(offer: pd.DataFrame) -> None:
    panel_title("Ranking territorial: % afín a IA", "Participación sobre titulados de cada región")
    if offer.empty:
        status_message("sin datos", "No hay registros para la selección territorial.")
        return
    chart_data = offer[["region_nombre", "pct_afin_ia"]].sort_values("pct_afin_ia")
    chart_data = chart_data.rename(
        columns={"region_nombre": "Región", "pct_afin_ia": "% afín a IA"}
    )
    bars = alt.Chart(chart_data).mark_bar(color=COLORS["accent"]).encode(
        x=alt.X("% afín a IA:Q", title="% de titulados afines a IA", scale=alt.Scale(domain=[0, 100])),
        y=alt.Y("Región:N", sort=None, title=None),
        tooltip=["Región:N", alt.Tooltip("% afín a IA:Q", format=".2f")],
    )
    labels = alt.Chart(chart_data).mark_text(align="left", dx=5, color=COLORS["text"]).encode(
        x="% afín a IA:Q",
        y=alt.Y("Región:N", sort=None),
        text=alt.Text("% afín a IA:Q", format=".1f"),
    )
    st.altair_chart((bars + labels).properties(height=max(360, len(chart_data) * 28)), width="stretch")
    reference = national_reference(offer)
    if reference is not None:
        st.caption(f"Referencia nacional calculada desde conteos aditivos: {reference:.2f}%")


def render_notebook_ranking(offer: pd.DataFrame) -> None:
    panel_title(
        "Notebook · ranking regional de oferta afín a IA",
        "Misma métrica del notebook: porcentaje de titulados afines a IA por región.",
    )
    if offer.empty:
        status_message("sin datos", "No hay datos de oferta para construir el ranking.")
        return
    chart_data = offer[["region_nombre", "pct_afin_ia"]].rename(
        columns={"region_nombre": "Región", "pct_afin_ia": "% afín a IA"}
    )
    bars = alt.Chart(chart_data).mark_bar(color=COLORS["accent"]).encode(
        x=alt.X("% afín a IA:Q", title="% de titulados afines a IA", scale=alt.Scale(domain=[0, 50])),
        y=alt.Y("Región:N", sort="-x", title=None),
        tooltip=["Región:N", alt.Tooltip("% afín a IA:Q", format=".2f")],
    )
    labels = alt.Chart(chart_data).mark_text(align="left", dx=5, color=COLORS["text"]).encode(
        x="% afín a IA:Q",
        y=alt.Y("Región:N", sort="-x"),
        text=alt.Text("% afín a IA:Q", format=".1f"),
    )
    st.altair_chart((bars + labels).properties(height=max(420, len(chart_data) * 28)), width="stretch")
    st.caption("Fuente compartida: `dataset_match_ia_regional_sprint1.csv` · corte 2025.")


def render_notebook_gratuidad(detail: pd.DataFrame | None) -> None:
    panel_title(
        "Notebook · titulados afines: gratuidad vs. no gratuidad",
        "Porcentaje dentro de cada región; misma clasificación institucional por `cod_inst`.",
    )
    if detail is None or detail.empty:
        status_message("sin datos", "No hay tabla fina para la comparación de gratuidad.")
        return
    data = detail[detail["area_cine_f13"].isin(IA_AREAS)].copy()
    if data.empty:
        status_message("sin datos", "No hay áreas afines a IA en la selección.")
        return
    data = data.groupby(["region_nombre", "inst_gratuidad"], as_index=False)["n_titulados"].sum()
    data["condición"] = data["inst_gratuidad"].map({1: "Con gratuidad", 0: "Sin gratuidad"})
    data["porcentaje"] = data["n_titulados"] / data.groupby("region_nombre")["n_titulados"].transform("sum") * 100
    chart = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            x=alt.X("condición:N", title=None),
            y=alt.Y("porcentaje:Q", title="% titulados afines a IA"),
            color=alt.Color("condición:N", scale=alt.Scale(
                domain=["Con gratuidad", "Sin gratuidad"],
                range=["#1b7837", "#7570b3"],
            )),
            column=alt.Column("region_nombre:N", title="Región"),
            tooltip=["region_nombre:N", "condición:N", alt.Tooltip("porcentaje:Q", format=".2f")],
        )
        .properties(height=280)
    )
    st.altair_chart(chart, width="stretch")
    st.caption("Fuente compartida: `oferta_fina_region_cine_nivel_gratuidad.csv` · corte 2025.")


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


def render_offer_composition(detail: pd.DataFrame | None) -> None:
    panel_title(
        "Composición de titulados por área y nivel",
        "Conteos aditivos desde la tabla fina; corte 2025.",
    )
    if detail is None or detail.empty:
        status_message("sin datos", "No hay tabla fina para la selección.")
        return
    chart = (
        detail.groupby(["area_cine_f13", "nivel_formativo"], as_index=False)["n_titulados"]
        .sum()
        .pivot(index="area_cine_f13", columns="nivel_formativo", values="n_titulados")
        .fillna(0)
    )
    chart = chart.reset_index().rename(columns={"area_cine_f13": "Área CINE"})
    chart = chart.melt(id_vars="Área CINE", var_name="Nivel", value_name="Titulados")
    chart["Área corta"] = chart["Área CINE"].map(
        {
            "Administración de Empresas y Derecho": "Administración",
            "Agricultura, Silvicultura, Pesca y Veterinaria": "Agricultura",
            "Artes y Humanidades": "Artes",
            "Ciencias naturales, matemáticas y estadística": "Ciencias naturales",
            "Ciencias Sociales, Periodismo e Información": "Ciencias sociales",
            "Educación": "Educación",
            "Ingeniería, Industria y Construcción": "Ingeniería",
            "Salud y Bienestar": "Salud",
            "Servicios": "Servicios",
            "Tecnología de la Información y la Comunicación (TIC)": "TIC",
        }
    )
    bars = alt.Chart(chart).mark_bar().encode(
        x=alt.X("Área corta:N", sort=list(chart["Área corta"].drop_duplicates()), title=None),
        y=alt.Y("Titulados:Q", title="Titulados"),
        color=alt.Color("Nivel:N", scale=alt.Scale(
            domain=["Posgrado", "Técnico", "Universitario"],
            range=[COLORS["accent"], COLORS["success"], "#7d91b3"],
        )),
        tooltip=["Área CINE:N", "Nivel:N", "Titulados:Q"],
    )
    st.altair_chart(
        bars.properties(height=400).configure_axisX(labelAngle=0, labelLimit=140),
        width="stretch",
    )
    st.caption(
        "Fuente: SIES-Mineduc 2025. Los porcentajes se reconstruyen desde "
        "conteos y no representan beneficio individual de gratuidad."
    )


def render_gratuidad(detail: pd.DataFrame | None) -> None:
    panel_title(
        "Gratuidad institucional",
        "Cruce de cod_inst con la nómina oficial Mineduc 2025.",
    )
    if detail is None or detail.empty:
        status_message("sin datos", "No hay tabla fina para la selección.")
        return
    result = (
        detail.groupby("inst_gratuidad", as_index=False)["n_titulados"]
        .sum()
        .assign(condicion=lambda frame: frame["inst_gratuidad"].map({0: "Sin gratuidad", 1: "Con gratuidad"}))
    )
    st.dataframe(result[["condicion", "n_titulados"]], use_container_width=True, hide_index=True)
    st.caption(
        "La condición es institucional. Una institución sin coincidencia en la "
        "nómina no prueba ausencia de beneficio individual."
    )


def render_specialization(lq: pd.DataFrame | None) -> None:
    panel_title(
        "Especialización regional (LQ)",
        "La matriz reproduce el cálculo del notebook: LQ = proporción regional / proporción nacional.",
    )
    if lq is None or lq.empty:
        status_message("sin datos", "No hay LQ disponibles para la selección.")
        return
    available = lq[lq["estado_disponibilidad"].eq("disponible")]
    summary = (
        available.groupby("region_nombre", as_index=False)
        .agg(lq_medio=("lq", "mean"), lq_maximo=("lq", "max"))
        .sort_values("lq_medio")
    )
    chart = alt.Chart(summary).mark_bar(color=COLORS["accent"]).encode(
        x=alt.X("lq_medio:Q", title="LQ medio de las áreas"),
        y=alt.Y("region_nombre:N", sort=None, title=None),
        tooltip=[
            "region_nombre:N",
            alt.Tooltip("lq_medio:Q", format=".2f"),
            alt.Tooltip("lq_maximo:Q", format=".2f"),
        ],
    )
    rule = alt.Chart(pd.DataFrame({"ref": [1]})).mark_rule(
        color=COLORS["warning"], strokeDash=[6, 4]
    ).encode(x="ref:Q")
    st.altair_chart((chart + rule).properties(height=max(360, len(summary) * 28)), width="stretch")


def render_lq(lq: pd.DataFrame | None) -> None:
    panel_title(
        "Especialización territorial por área CINE",
        "LQ = 1 representa la referencia nacional; LQ > 1 indica concentración relativa.",
    )
    if lq is None or lq.empty:
        status_message("sin datos", "La matriz LQ no está disponible.")
        return
    available = lq[lq["estado_disponibilidad"].eq("disponible")]
    if available.empty:
        status_message("sin datos", "No existen observaciones LQ para la selección.")
        return
    top_areas = (
        available.groupby("area_cine_f13")["n_titulados"]
        .sum()
        .sort_values(ascending=False)
        .head(8)
        .index.tolist()
    )
    region_order = [name for _, name in REGIONS if name in available["region_nombre"].unique()]
    area_short = {
        "Administración de Empresas y Derecho": "Administración",
        "Agricultura, Silvicultura, Pesca y Veterinaria": "Agricultura",
        "Artes y Humanidades": "Artes",
        "Ciencias naturales, matemáticas y estadística": "Ciencias naturales",
        "Ciencias Sociales, Periodismo e Información": "Ciencias sociales",
        "Educación": "Educación",
        "Ingeniería, Industria y Construcción": "Ingeniería",
        "Salud y Bienestar": "Salud",
        "Servicios": "Servicios",
        "Tecnología de la Información y la Comunicación (TIC)": "TIC",
    }
    heatmap_data = available[available["area_cine_f13"].isin(top_areas)].copy()
    heatmap_data["Área"] = heatmap_data["area_cine_f13"].map(area_short)
    area_order = [area_short[area] for area in top_areas]
    heatmap = alt.Chart(heatmap_data).mark_rect(stroke="#23344d").encode(
        x=alt.X("Área:N", sort=area_order, title=None, axis=alt.Axis(labelAngle=0, labelLimit=150)),
        y=alt.Y("region_nombre:N", sort=region_order, title=None, axis=alt.Axis(labelLimit=180)),
        color=alt.Color(
            "lq:Q", title="LQ",
            scale=alt.Scale(domain=[0, 2.5], scheme="redblue"),
        ),
        tooltip=[
            "region_nombre:N", "area_cine_f13:N",
            alt.Tooltip("lq:Q", format=".2f"),
        ],
    )
    values = alt.Chart(heatmap_data).mark_text(fontSize=11).encode(
        x=alt.X("Área:N", sort=area_order),
        y=alt.Y("region_nombre:N", sort=region_order),
        text=alt.Text("lq:Q", format=".2f"),
        color=alt.condition(
            "datum.lq > 1.35 || datum.lq < 0.65",
            alt.value("white"),
            alt.value("#17243a"),
        ),
    )
    heatmap = (heatmap + values).properties(height=560)
    with st.container(border=True):
        st.altair_chart(heatmap, width="stretch")
    st.caption("Fuente: SIES-Mineduc 2025 · unidad: índice LQ · denominadores aditivos.")


def render_demand(demand: pd.DataFrame | None) -> None:
    panel_title(
        "Estructura productiva regional",
        "Indicadores de demanda disponibles a nivel regional; sin desagregación comunal o por macrozona.",
    )
    if demand is None or demand.empty:
        status_message("no disponible", "No hay artefacto de demanda regional válido.")
        return
    columns = [c for c in ["region_nombre", "n_trabajadores_total", "ire_ia",
                           "pct_empleo_alta_exp", "pct_empleo_media_exp",
                           "pct_empleo_baja_exp"] if c in demand.columns]
    st.dataframe(demand[columns], use_container_width=True, hide_index=True)
    composition = demand.set_index("region_nombre")[
        [column for column in ["pct_empleo_alta_exp", "pct_empleo_media_exp", "pct_empleo_baja_exp"]
         if column in demand.columns]
    ].rename(columns={
        "pct_empleo_alta_exp": "Alta exposición (%)",
        "pct_empleo_media_exp": "Exposición media (%)",
        "pct_empleo_baja_exp": "Baja exposición (%)",
    })
    if not composition.empty:
        st.bar_chart(composition, color=[COLORS["warning"], COLORS["accent"], COLORS["reference"]])
    st.caption("El IRE-IA y la composición laboral se presentan a nivel regional; no representan una desagregación comunal.")
    st.caption("Fuente: SII; unidad territorial: región; corte y cobertura declarados en el artefacto.")


def render_match_ia(offer: pd.DataFrame) -> None:
    panel_title(
        "Matriz Match-IA regional",
        "Cruce descriptivo entre % de oferta afín a IA e IRE-IA, usando medianas nacionales.",
    )
    required = {"region_nombre", "pct_afin_ia", "ire_ia", "cuadrante_codigo"}
    if offer.empty or not required.issubset(offer.columns):
        status_message("no disponible", "El dataset maestro no contiene los campos de Match-IA.")
        return
    chart = offer[
        ["region_nombre", "pct_afin_ia", "ire_ia", "cuadrante_codigo", "n_titulados_total"]
    ].copy()
    chart = chart.rename(
        columns={
            "region_nombre": "Región",
            "pct_afin_ia": "% oferta afín a IA",
            "ire_ia": "IRE-IA",
        }
    )
    median_offer = chart["% oferta afín a IA"].median()
    median_demand = chart["IRE-IA"].median()
    x_min, x_max = chart["IRE-IA"].min() * 0.96, chart["IRE-IA"].max() * 1.04
    y_min, y_max = chart["% oferta afín a IA"].min() * 0.88, chart["% oferta afín a IA"].max() * 1.10
    quadrant_data = pd.DataFrame(
        [
            {"x0": x_min, "x1": median_demand, "y0": median_offer, "y1": y_max, "fill": "#fff7bc"},
            {"x0": median_demand, "x1": x_max, "y0": median_offer, "y1": y_max, "fill": "#edf8e9"},
            {"x0": x_min, "x1": median_demand, "y0": y_min, "y1": median_offer, "fill": "#eff3ff"},
            {"x0": median_demand, "x1": x_max, "y0": y_min, "y1": median_offer, "fill": "#fde0dd"},
        ]
    )
    backgrounds = alt.Chart(quadrant_data).mark_rect(opacity=0.55).encode(
        x=alt.X("x0:Q", scale=alt.Scale(domain=[x_min, x_max])),
        x2="x1:Q",
        y=alt.Y("y0:Q", scale=alt.Scale(domain=[y_min, y_max])),
        y2="y1:Q",
        color=alt.Color("fill:N", scale=None, legend=None),
    )
    points = (
        alt.Chart(chart)
        .mark_circle(stroke="black", strokeWidth=1, opacity=0.9)
        .encode(
            x=alt.X("IRE-IA:Q", title="IRE-IA", scale=alt.Scale(domain=[x_min, x_max])),
            y=alt.Y(
                "% oferta afín a IA:Q",
                title="% de titulados en carreras afines a IA (2025)",
                scale=alt.Scale(domain=[y_min, y_max]),
            ),
            color=alt.Color(
                "cuadrante_codigo:N",
                title="Cuadrante",
                scale=alt.Scale(
                    domain=["Q1_Polo", "Q2_Brecha", "Q3_Oferta_Sin_Demanda", "Q4_Transicion"],
                    range=["#1b7837", "#b2182b", "#d95f02", "#2166ac"],
                ),
            ),
            size=alt.Size(
                "n_titulados_total:Q",
                title="Titulados totales",
                scale=alt.Scale(range=[80, 1800]),
            ),
            tooltip=["Región:N", alt.Tooltip("% oferta afín a IA:Q", format=".2f"),
                     alt.Tooltip("IRE-IA:Q", format=".3f"), "cuadrante_codigo:N"],
        )
    )
    labels = alt.Chart(chart).mark_text(dx=8, dy=-8, align="left", fontSize=11).encode(
        x="IRE-IA:Q",
        y="% oferta afín a IA:Q",
        text="Región:N",
        color=alt.value("#263238"),
    )
    rules = alt.layer(
        alt.Chart(pd.DataFrame({"x": [median_demand]})).mark_rule(
            stroke="#444444", strokeDash=[6, 4], strokeWidth=1.5
        ).encode(x="x:Q"),
        alt.Chart(pd.DataFrame({"y": [median_offer]})).mark_rule(
            stroke="#444444", strokeDash=[6, 4], strokeWidth=1.5
        ).encode(y="y:Q"),
    )
    st.altair_chart(
        (backgrounds + rules + points + labels).properties(height=620, width=1000),
        width="stretch",
    )
    st.dataframe(
        offer[["region_nombre", "pct_afin_ia", "ire_ia", "cuadrante_match_ia"]].rename(columns={
            "region_nombre": "Región", "pct_afin_ia": "% oferta afín a IA",
            "ire_ia": "IRE-IA", "cuadrante_match_ia": "Cuadrante",
        }),
        use_container_width=True,
        hide_index=True,
    )
    st.caption("Fuente: dataset_match_ia_regional_sprint1.csv · corte 2025 · medianas nacionales como umbrales.")


def render_infrastructure(
    infrastructure: pd.DataFrame | None,
    status,
    regional: pd.DataFrame | None,
    regional_status,
) -> None:
    panel_title("Sedes georreferenciadas", "Únicamente la capa de sedes con fuente validada.")
    if infrastructure is None:
        status_message(status.state, status.message or "La tabla de infraestructura no está disponible.")
        return
    if infrastructure.empty:
        status_message("sin datos", "El artefacto de infraestructura no tiene registros.")
        return
    st.dataframe(
        infrastructure[["region_nombre", "cod_sede", "comuna_nombre", "estado_sede"]].head(100),
        use_container_width=True,
        hide_index=True,
    )
    panel_title("Distribución territorial de la infraestructura", "Sedes georreferenciadas y sedes físicas por región.")
    if regional is None or regional.empty:
        status_message(regional_status.state, regional_status.message or "El resumen regional no está disponible.")
        return
    columns = [column for column in [
        "region_nombre", "n_sedes_brutas", "n_sedes_validas", "n_sedes_excluidas",
        "cobertura_sedes_validas_pct",
    ] if column in regional.columns]
    bar_data = regional[["region_nombre", "n_sedes_validas"]].rename(
        columns={"region_nombre": "Región", "n_sedes_validas": "Sedes válidas"}
    )
    map_data = infrastructure.dropna(subset=["longitud", "latitud"]).copy()
    outline_path = Path(__file__).resolve().parents[2] / "data" / "processed" / "chile_outline.geojson"
    outline = json.loads(outline_path.read_text(encoding="utf-8")) if outline_path.exists() else None
    if outline is not None:
        outline = {
            "type": outline["type"],
            "features": outline["features"],
        }
    points = alt.Chart(map_data).mark_circle(size=30, color="#2166ac", opacity=0.72).encode(
        longitude=alt.Longitude("longitud:Q"),
        latitude=alt.Latitude("latitud:Q"),
        tooltip=["region_nombre:N", "comuna_nombre:N", "cod_sede:N"],
    )
    if outline is not None:
        country = alt.Chart(alt.Data(values=outline)).mark_geoshape(
            fill="#1d2b40",
            fillOpacity=0.42,
            stroke="#2aa9e8",
            strokeWidth=1.2,
        )
        points = country + points
    points = points.properties(
        title="Sedes de Educación Superior Georreferenciadas (N = 1.297)",
        width=420,
        height=900,
    ).project(type="mercator", scale=820, center=[-71.5, -36.5])
    bar_data = bar_data.sort_values("Sedes válidas")
    bars = alt.Chart(bar_data).mark_bar(color="#4393c3").encode(
        x=alt.X("Sedes válidas:Q", title="Cantidad de sedes físicas"),
        y=alt.Y("Región:N", sort=None, title=None),
        tooltip=["Región:N", "Sedes válidas:Q"],
    )
    values = alt.Chart(bar_data).mark_text(align="left", dx=4, color=COLORS["text"]).encode(
        x="Sedes válidas:Q",
        y=alt.Y("Región:N", sort=None),
        text=alt.Text("Sedes válidas:Q", format=".0f"),
    )
    bar = (bars + values).properties(
        title="Infraestructura Formativa Físicamente Instalada\n(Número de Sedes por Región)",
        width=620,
        height=900,
    )
    map_col, bar_col = st.columns([1, 1.5])
    with map_col:
        st.altair_chart(points, width="stretch")
    with bar_col:
        st.altair_chart(bar, width="stretch")
    st.caption(
        "Las capas de red vial, servicios y conectividad fueron excluidas por no "
        "contar con una fuente validada común para notebook y dashboard."
    )


def render_tabs(
    offer: pd.DataFrame,
    infrastructure: pd.DataFrame | None,
    infra_status,
    detail: pd.DataFrame | None = None,
    lq: pd.DataFrame | None = None,
    demand: pd.DataFrame | None = None,
    infrastructure_regional: pd.DataFrame | None = None,
    infrastructure_regional_status=None,
    match_master: pd.DataFrame | None = None,
    selected_view: str = "Visión General",
) -> None:
    if selected_view == "Visión General":
        render_overview(offer)
        render_notebook_ranking(offer)
    elif selected_view == "Oferta y Titulados":
        render_offer_composition(detail)
        render_gratuidad(detail)
        render_notebook_gratuidad(detail)
    elif selected_view == "Especialización (LQ)":
        render_specialization(lq)
        render_lq(lq)
        render_demand(demand)
        render_match_ia(match_master if match_master is not None else offer)
    elif selected_view == "Infraestructura Geo":
        render_infrastructure(
            infrastructure,
            infra_status,
            infrastructure_regional,
            infrastructure_regional_status or infra_status,
        )
