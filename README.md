# MACI 2026 - Grupo 03: Match-IA Regional

Este repositorio contiene informacion publica sobre las caracteristicas de la titulacion en Universidades, asi como su ubicacion, red de vialidad y otros servicios publicos, asi como indicaciones sobre otras fuentes de datos (e.g. OpenStreetMap).

Esto permitirá al Ministerio sugerir la re-dirección de programas públicos de fomento, evaluar la continuidad de subsidios y focalizar inversiones en polos estratégicos de innovación y desarrollo tecnológico a nivel regional.

Como contraparte a la consultoria del Ministerio de Economia, se necesita utilizar la información disponible en este repositorio, junto con datos adicionales sobre los focos de desarrollo estrategico regional por industria, para identificar de manera objetiva qué carreras podrían beneficiarse en mayor medida de los subsidios públicos orientados al desarrollo de habilidades de IA complementarias, a nivel regional. Esto permitirá priorizar la asignación de recursos, focalizando los apoyos en aquellas carreras e industrias que presentan mayores necesidades según criterios basados en datos y evidencia territorial.

### Objetivos
- Acceso a bases de datos relevantes sobre la oferta y demanda laboral, desarrollo regional estrategico y su entorno físico.
- Herramientas o scripts que permitan analizar y cruzar la información de manera eficiente usando modelos de Aprendizaje Automatico.
- Visualizaciones o reportes que faciliten la toma de decisiones para la asignación de subsidios.

### Sprint 1  - 26/09 a 16/10
Scrum Master: Yenny Sánchez

Product Owner: Hernán Leiva

### MVP

Analizar la oferta de titulados y los sectores productivos de las regiones seleccionadas, identificando patrones y definiendo indicadores relevantes para Match-IA Regional.

Entrega: análisis exploratorio con gráficos, indicadores definidos y un resumen de hallazgos que sirva de base para el dashboard.

### Sprint 2  - 17/10 a 30/10
Scrum Master: Marian Garcia

Product Owner: Jaisson Torres

### MVP  

Presentar los resultados del primer MVP en un dashboard que permita seleccionar y comparar regiones, explorando la oferta de titulados y su contexto productivo.

Entrega: dashboard funcional con filtros regionales, indicadores y visualizaciones que apoyen el análisis de oportunidades de formación en habilidades complementarias a la IA.

## Resumen de actividades y estimación de horas

| Historia | Tarea | Actividad principal | Responsable | Horas |
|---|---|---|---|---:|
| **User_01 — Oferta de titulados** | **#8:** Preparar titulados y sedes | Configurar entorno, cargar y estandarizar datos; preparar información geográfica | Marian | 8 |
| **User_01 — Oferta de titulados** | **#9:** Indicadores, mapas y metodología | Calcular indicadores y LQ formativo; generar gráficos, mapas y hallazgos | Jaisson y Yenny | 12 |
| **User_02 — Sectores productivos e IA** | **#10:** Preparar empresas, empleo e índice de IA | Cargar datos productivos y documentar correspondencias con exposición a IA | Yenny y Marian | 12 |
| **User_02 — Sectores productivos e IA** | **#11:** Indicadores y matriz Match-IA | Calcular LQ productivo, exposición regional y cuadrantes; validar el notebook | Hernán | 12 |
| **User_03 — Base integrada** | Integrar y validar indicadores regionales | Unificar resultados de #9 y #11 y comprobar totales, duplicados y faltantes | Jaisson | 6 |
| **User_03 — Base integrada** | Exportar y documentar la base | Generar tablas para el dashboard y documentar variables, fuentes y períodos | Jaisson y Yenny | 4 |
| **User_04 — Infraestructura** | Recopilar y preparar datos territoriales | Preparar red vial y servicios; revisar disponibilidad de conectividad digital | Hernán | 6 |
| **User_04 — Infraestructura** | Calcular indicadores territoriales | Medir accesibilidad y disponibilidad de servicios y documentar metodología | Jaisson y Marian | 8 |
| **User_04 — Infraestructura** | Generar mapas y hallazgos | Comparar territorios y resumir posibles brechas de infraestructura | Jaisson y Marian | 6 |
| **User_05 — Dashboard** | Configurar dashboard y selector regional | Conectar tablas procesadas y habilitar selección de las tres regiones | Hernán | 6 |
| **User_05 — Dashboard** | Incorporar indicadores y gráficos | Mostrar oferta, estructura productiva y comparación regional | Yenny | 10 |
| **User_05 — Dashboard** | Documentar y validar el dashboard | Incorporar fuentes y hallazgos; comprobar filtros y consistencia con el notebook | Jaisson y Marian | 6 |
| | | **Total estimado** | | **96** |

## Totales por historia y sprint

| Sprint | Historia | Responsables de las tareas | Horas |
|---|---|---|---:|
| Sprint 1 | **User_01 — Oferta de titulados** | Marian, Jaisson y Yenny | 20 |
| Sprint 1 | **User_02 — Sectores productivos e IA** | Yenny, Marian y Hernán | 24 |
| Sprint 1 | **User_03 — Base integrada y trazable** | Jaisson y Yenny | 10 |
| | **Subtotal Sprint 1** | | **54** |
| Sprint 2 | **User_04 — Brechas de infraestructura** | Hernán, Jaisson y Marian | 20 |
| Sprint 2 | **User_05 — Dashboard regional** | Hernán, Yenny, Jaisson y Marian | 22 |
| | **Subtotal Sprint 2** | | **42** |
| | **Total general** | | **96** |

## Distribución estimada por integrante


| Integrante | Sprint 1 | Sprint 2 | Total HH |
|---|---:|---:|---:|
| **Yenny** | 14 | 10 | **24** |
| **Marian** | 14 | 10 | **24** |
| **Jaisson** | 14 | 10 | **24** |
| **Hernán** | 12 | 12 | **24** |
| **Total** | **54** | **42** | **96** |
