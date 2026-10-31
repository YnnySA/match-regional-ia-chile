# MACI 2026 · Grupo 03

## Match-IA Regional

Aplicación de análisis territorial que relaciona la oferta regional de
formación afín a Inteligencia Artificial con la estructura productiva, la
exposición sectorial a IA y la infraestructura de educación superior.

El proyecto entrega dos productos relacionados:

- un notebook técnico reproducible;
- un dashboard Streamlit para explorar los mismos resultados.

## Objetivo

Identificar diferencias territoriales entre la oferta de titulados en áreas
afines a IA y la demanda productiva regional expuesta a IA, considerando
gratuidad institucional, especialización formativa, Match-IA y sedes
georreferenciadas.

## Estructura del proyecto

| Ruta | Contenido |
|---|---|
| `app.py` | Punto de entrada del dashboard Streamlit |
| `.streamlit/` | Configuración visual y de ejecución de Streamlit |
| `src/dashboard/` | Loaders, contratos, métricas, vistas, tema y validación de paridad |
| `data/oferta/` | Fuentes de oferta y nómina institucional de gratuidad |
| `data/demanda/` | Fuentes de empresas, trabajadores y homologación sectorial |
| `data/geo/` | Fuente geográfica de sedes |
| `data/infraestructura/` | Contratos, diccionarios y fuentes de infraestructura |
| `data/processed/` | Artefactos procesados consumidos por el dashboard |
| `notebooks/` | Notebook técnico principal del Sprint 1 |
| `reports/figures/` | Figuras de resultados y mapas |
| `docs/` | Trazabilidad, paridad, datos y rendimiento |
| `openspec/` | Especificaciones y cambios del proyecto |

La aplicación no lee ni limpia los archivos crudos durante la interacción.
Consume únicamente artefactos procesados registrados en
`data/processed/dashboard_manifest.json`.

## Integrantes y roles

| Integrante | Rol Sprint 1 | Rol Sprint 2 |
|---|---|---|
| Yenny Sánchez | Scrum Master | Developer |
| Hernán Leiva | Product Owner | Developer |
| Marian García | Developer | Scrum Master |
| Jaisson Torres | Developer | Developer |

## Dashboard

El dashboard incluye:

- visión general y ranking regional de oferta afín a IA;
- composición de titulados por área CINE-F-13 y nivel;
- gratuidad institucional;
- matriz y resumen de especialización regional mediante LQ;
- indicadores de demanda y exposición productiva;
- matriz Match-IA regional;
- distribución regional y mapa de sedes georreferenciadas con silueta de Chile.

Las capas de red vial, servicios en radio de 5 km y conectividad fueron
excluidas del producto final por no contar con una fuente validada común para
el notebook y el dashboard.

## Datos procesados principales

- `data/processed/dashboard_manifest.json`
- `data/processed/oferta_fina_region_cine_nivel_gratuidad.csv`
- `data/processed/matriz_lq_cine_regional.csv`
- `data/processed/reporte_cruce_gratuidad.csv`
- `data/processed/chile_outline.geojson`
- `data/processed/infraestructura/`

Los artefactos regionales de oferta, demanda, Match-IA e infraestructura se
validan mediante el manifest antes de renderizarse.

## Ejecución local

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

Iniciar la aplicación:

```powershell
streamlit run app.py
```

Abrir `http://localhost:8501/`.

## Validaciones

Validar la correspondencia entre notebook y dashboard:

```powershell
python -m src.dashboard.parity
```

Preparar nuevamente los artefactos finos de oferta y LQ:

```powershell
python -m src.dashboard.prepare_offer
```

La validación de paridad cubre las regiones MVP Valparaíso (6),
Metropolitana de Santiago (7) y Biobío (11).

## Despliegue en Streamlit Community Cloud

En Streamlit Community Cloud, seleccionar el repositorio del proyecto y
establecer `app.py` como archivo principal. La aplicación debe desplegarse
desde la rama que el equipo haya definido como estable.

## Documentación técnica

- [Datos y trazabilidad del dashboard](docs/dashboard-data.md)
- [Paridad notebook-dashboard](docs/dashboard-parity.md)
- [Auditoría notebook-dashboard](docs/notebook-dashboard-audit.md)
- [Rendimiento del dashboard](docs/dashboard-performance.md)
- [Notebook técnico](notebooks/sprint1_match_ia_regional.ipynb)
