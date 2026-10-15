# MACI 2026 - Grupo 03: Match-IA Regional

Este repositorio contiene informacion publica sobre las caracteristicas de la titulacion en Universidades, asi como su ubicacion, red de vialidad y otros servicios publicos, asi como indicaciones sobre otras fuentes de datos (e.g. OpenStreetMap).

Esto permitirá al Ministerio sugerir la re-dirección de programas públicos de fomento, evaluar la continuidad de subsidios y focalizar inversiones en polos estratégicos de innovación y desarrollo tecnológico a nivel regional.

Como contraparte a la consultoria del Ministerio de Economia, se necesita utilizar la información disponible en este repositorio, junto con datos adicionales sobre los focos de desarrollo estrategico regional por industria, para identificar de manera objetiva qué carreras podrían beneficiarse en mayor medida de los subsidios públicos orientados al desarrollo de habilidades de IA complementarias, a nivel regional. Esto permitirá priorizar la asignación de recursos, focalizando los apoyos en aquellas carreras e industrias que presentan mayores necesidades según criterios basados en datos y evidencia territorial.

### Objetivos
- Acceso a bases de datos relevantes sobre la oferta y demanda laboral, desarrollo regional estrategico y su entorno físico.
- Herramientas o scripts que permitan analizar y cruzar la información de manera eficiente usando modelos de Aprendizaje Automatico.
- Visualizaciones o reportes que faciliten la toma de decisiones para la asignación de subsidios.

## Sprint 1 — 26/09 al 16/10 de 2026

**Scrum Master:** Yenny Sánchez  
**Product Owner:** Hernán Leiva

### MVP

Analizar la oferta de titulados y los sectores productivos de las regiones seleccionadas, identificando patrones y definiendo indicadores relevantes para Match-IA Regional.

### Entrega

Análisis exploratorio con:

- Indicadores de oferta de titulados.
- Indicadores sectoriales y exposición regional a IA.
- Gráficos comparativos y mapas.
- Matriz exploratoria Match-IA.
- Fichas metodológicas y resumen de hallazgos.
- Notebook reproducible que sirva de base para el dashboard.

## Sprint 2 — 17/10 al 30/10 de 2026

**Scrum Master:** Marian García  
**Product Owner:** Jaisson Torres

### MVP

Presentar los resultados del primer MVP en un dashboard que permita seleccionar y comparar regiones, explorando la oferta de titulados y su contexto productivo.

### Entrega

Dashboard funcional para las tres regiones acordadas, con:

- Selección y comparación regional.
- Indicadores y visualizaciones de oferta y estructura productiva.
- Fuentes, definiciones y limitaciones accesibles.
- Hallazgos sobre oportunidades de formación en habilidades complementarias a IA.

El sprint incluye además el análisis de accesibilidad, infraestructura y servicios de User_04.

## Historias de usuario

Estado según la información compartida al **15 de octubre de 2026**.

| Sprint | Historia | Propósito | Tareas | Estado |
|---|---|---|---|---|
| 1 | [User_01 — Caracterización territorial de la oferta de titulados con gratuidad](https://github.com/TECH-MACI/2026-G03/issues/1) | Caracterizar la distribución regional de titulados y áreas formativas afines a IA | #8 y #9 | Completada: 2 de 2 tareas cerradas |
| 1 | [User_02 — Sectores económicos regionales según exposición y complementariedad a IA](https://github.com/TECH-MACI/2026-G03/issues/2) | Caracterizar la estructura productiva y explorar su relación con IA | #10 y #11 | En progreso: 1 de 2 tareas cerradas |
| 2 | [User_04 — Brechas de infraestructura en potenciales polos regionales de innovación](https://github.com/TECH-MACI/2026-G03/issues/4) | Analizar accesibilidad, infraestructura y servicios territoriales | #16, #17 y #18 | Abierta: 0 de 3 tareas cerradas |
| 2 | [User_05 — Dashboard de oferta y sectores productivos regionales](https://github.com/TECH-MACI/2026-G03/issues/5) | Explorar y comparar regiones mediante indicadores y visualizaciones | #19, #20 y #21 | Abierta: 0 de 3 tareas cerradas |

La historia User_03 y las tareas #14 y #15 fueron retiradas de esta planificación. Se conservan los identificadores de las historias restantes.

## Resumen de actividades y estimación de horas

Las estimaciones y la distribución de actividades se ajustan a **36 HH por sprint y 18 HH por integrante en total**. Este reparto debe reflejarse en las asignaciones de GitHub.

| Historia | Tarea | Actividad principal | Responsable y distribución | HH |
|---|---|---|---|---:|
| **User_01 — Oferta de titulados** | **#8 — Preparar titulados y sedes** | Configurar entorno, cargar y estandarizar datos; preparar información geográfica | Marian: 6 HH | 6 |
| **User_01 — Oferta de titulados** | **#9 — Indicadores, mapas y metodología** | Calcular indicadores y LQ formativo; generar gráficos, mapas y hallazgos | Jaisson: 8 HH | 8 |
| **User_02 — Sectores productivos e IA** | **#10 — Preparar empresas, empleo e índice de IA** | Cargar datos productivos y documentar correspondencias con exposición a IA | Yenny: 10 HH · Marian: 2 HH | 12 |
| **User_02 — Sectores productivos e IA** | **#11 — Indicadores y matriz Match-IA** | Calcular LQ productivo, exposición regional y cuadrantes; validar el notebook consolidado | Hernán: 10 HH | 10 |
| **User_04 — Infraestructura** | **#16 — Recopilar y preparar datos territoriales** | Preparar red vial y servicios; revisar disponibilidad de conectividad digital | Hernán: 4 HH | 4 |
| **User_04 — Infraestructura** | **#17 — Calcular indicadores territoriales** | Medir accesibilidad y disponibilidad de servicios y documentar metodología | Jaisson: 4 HH · Marian: 4 HH | 8 |
| **User_04 — Infraestructura** | **#18 — Generar mapas y hallazgos** | Comparar territorios y resumir posibles brechas de infraestructura | Jaisson: 3 HH · Marian: 3 HH | 6 |
| **User_05 — Dashboard** | **#19 — Configurar dashboard y selector regional** | Conectar tablas procesadas y habilitar selección de las tres regiones | Hernán: 4 HH | 4 |
| **User_05 — Dashboard** | **#20 — Incorporar indicadores y gráficos** | Mostrar oferta, estructura productiva y comparación regional | Yenny: 4 HH · Jaisson: 3 HH · Marian: 3 HH | 10 |
| **User_05 — Dashboard** | **#21 — Documentar y validar el dashboard — alcance propuesto** | Incorporar fuentes y hallazgos; comprobar filtros y consistencia con el notebook | Yenny: 4 HH | 4 |
| | | **Total estimado** | | **72** |

En #20, Jaisson apoyará los gráficos de oferta, Marian los gráficos productivos y Yenny la integración y comparación regional.

**Pendiente de actualización:** #21 mantiene en GitHub el mismo título que #20. Esta planificación considera sus 4 HH para documentación y validación; corresponde confirmar y actualizar su título y criterios de aceptación.

## Totales por historia y sprint

| Sprint | Historia | Responsables de las tareas | HH |
|---|---|---|---:|
| Sprint 1 | **User_01 — Oferta de titulados** | Marian y Jaisson | 14 |
| Sprint 1 | **User_02 — Sectores productivos e IA** | Yenny, Marian y Hernán | 22 |
| | **Subtotal Sprint 1** | | **36** |
| Sprint 2 | **User_04 — Brechas de infraestructura** | Hernán, Jaisson y Marian | 18 |
| Sprint 2 | **User_05 — Dashboard regional** | Hernán, Yenny, Jaisson y Marian | 18 |
| | **Subtotal Sprint 2** | | **36** |
| | **Total general** | | **72** |

## Distribución estimada por integrante

| Integrante | Sprint 1 | Sprint 2 | Total HH |
|---|---:|---:|---:|
| **Yenny** | 10 | 8 | **18** |
| **Marian** | 8 | 10 | **18** |
| **Jaisson** | 8 | 10 | **18** |
| **Hernán** | 10 | 8 | **18** |
| **Total** | **36** | **36** | **72** |
