# MACI 2026 · Grupo 03

## Match-IA Regional

Proyecto de análisis territorial para apoyar decisiones sobre formación, subsidios e inversión en capacidades complementarias a la Inteligencia Artificial.

El análisis relaciona:

- oferta regional de titulados;
- instituciones adscritas a Gratuidad;
- estructura productiva y empleo;
- exposición sectorial a la IA;
- infraestructura y servicios territoriales.

## Objetivo

Identificar regiones y sectores donde exista mayor o menor correspondencia entre la oferta de titulados en áreas afines a IA y la demanda productiva regional expuesta a la IA.

## Estructura

| Directorio | Contenido |
|---|---|
| `data/` | Datos originales y procesados |
| `notebooks/` | Análisis reproducibles |
| `reports/figures/` | Gráficos y mapas |
| `openspec/` | Especificaciones y tareas del proyecto |
| `evaluacion_sprint1.md` | Evaluación del Sprint 1 |

## Organización del proyecto

| Sprint | Scrum Master | Product Owner |
|---|---|---|
| Sprint 1 | Yenny Sánchez | Hernán Leiva |
| Sprint 2 | Marian García | Jaisson Torres |

## Sprint 1 · Oferta, demanda y Match-IA

**Periodo:** 26/09/2026–16/10/2026

El Sprint 1 entrega un análisis exploratorio de la oferta de titulados y de los sectores productivos regionales expuestos a IA, mediante indicadores, mapas, gráficos, matriz Match-IA, ficha metodológica y un notebook reproducible.

### Historias de usuario

| Historia | Objetivo | Tareas | Estado |
|---|---|---|---|
| [User_01 — Oferta de titulados con gratuidad](https://github.com/TECH-MACI/2026-G03/issues/1) | Caracterizar titulados, áreas afines a IA, gratuidad y sedes por región | #8, #9 | Done |
| [User_02 — Sectores económicos y exposición a IA](https://github.com/TECH-MACI/2026-G03/issues/2) | Caracterizar la estructura productiva y su relación con IA | #10, #11 | Done |

### Tareas del Sprint 1

| Issue | Tarea | Estimate (hours) | Estado |
|---:|---|---:|---|
| #8 | Configurar entorno, cargar y estandarizar titulados y sedes | 6 | Done |
| #9 | Calcular indicadores de oferta, mapas y ficha metodológica | 8 | Done |
| #10 | Preparar datos de empresas, empleo y exposición a IA | 12 | Done |
| #11 | Calcular indicadores, matriz Match-IA y consolidar el notebook | 10 | Done |
|  | **Total Sprint 1** | **36** |  |

## Sprint 2 · Infraestructura y dashboard

El Sprint 2 continuará el análisis territorial con indicadores de infraestructura y un dashboard para explorar y comparar regiones.

## Resultados principales

- `notebooks/sprint1_match_ia_regional.ipynb`
- `data/processed/indicadores_oferta_regional.csv`
- `data/processed/indicadores_demanda_regional.csv`
- `data/processed/dataset_match_ia_regional_sprint1.csv`
- `reports/figures/`

## Especificaciones y documentación

- [Entorno y estructura](openspec/specs/entorno-y-estructura/spec.md)
- [Oferta de titulados](openspec/specs/oferta-titulados/spec.md)
- [Demanda SII y exposición a IA](openspec/specs/demanda-sii-ia/spec.md)
- [Matriz Match-IA](openspec/specs/matriz-match-ia/spec.md)
- [Evaluación del Sprint 1](evaluacion_sprint1.md)
