# Evaluación del Sprint 1 — Match-IA Regional

**Repositorio:** `TECH-MACI/2026-G03`  
**Sprint evaluado:** Sprint 1, User_01 y User_02  
**Periodo declarado:** 26/09/2026–16/10/2026  
**Modalidad:** evaluación documental y técnica preliminar  
**Fecha de evaluación:** 16/10/2026

> **Alcance de este informe:** se evaluaron los artefactos disponibles en el clon local, las especificaciones OpenSpec, el notebook consolidado, los archivos de resultados, el README, los `tasks.md` de las tareas #8–#11, la captura del GitHub Project y las pautas de Scrum/Git/GitHub Projects entregadas.  
> **Limitación:** no se pudo consultar directamente el GitHub Project remoto porque el entorno no tiene autenticación `gh`. La ejecución del notebook sí fue validada posteriormente usando el entorno virtual del proyecto.

## 1. Resumen ejecutivo

El Sprint 1 presenta un **incremento analítico sustantivo**: existe un notebook consolidado, resultados regionales para las 16 regiones de Chile, indicadores de oferta y demanda, una matriz Match-IA, cinco visualizaciones y un dataset maestro exportado.

La evaluación es **favorable con observaciones**. La evidencia estática y la ejecución del notebook confirman la estructura principal de los resultados, pero todavía deben resolverse:

1. Resolver la discrepancia de estado de User_02 entre `README.md`, GitHub Projects y los `tasks.md` locales.
2. Verificar directamente en GitHub Projects la trazabilidad de issues, estados, PR, revisiones y eventos Scrum.
3. Revisar el problema de codificación observado en las etiquetas `Crítica` y `Transición` de los CSV exportados.

## 2. Historias y alcance evaluado

| Historia | Tareas | Objetivo | Estado documental |
|---|---|---|---|
| User_01 — Caracterización territorial de la oferta de titulados con gratuidad | #8 y #9 | Caracterizar titulados, áreas afines a IA, gratuidad y sedes por región | `README.md`: 2/2 cerradas |
| User_02 — Sectores económicos regionales según exposición y complementariedad a IA | #10 y #11 | Caracterizar estructura productiva, exposición a IA y matriz Match-IA | `README.md`: 2/2; estado del Project pendiente de confirmación remota |

User_04 y User_05 no forman parte de esta evaluación porque corresponden al Sprint 2.

## 3. Matriz de cumplimiento técnico

| Área | Evidencia encontrada | Resultado preliminar |
|---|---|---|
| Estandarización territorial | `indicadores_oferta_regional.csv`, `indicadores_demanda_regional.csv` y dataset maestro contienen 16 filas con regiones 1–16 sin duplicados | **Cumple estáticamente** |
| Oferta de titulados | El notebook contiene carga, limpieza, clasificación de áreas afines, gratuidad, indicadores y visualizaciones | **Cumple preliminarmente** |
| LQ de oferta | La OpenSpec define la fórmula y el notebook contiene la sección de indicadores de oferta; el notebook fue ejecutado en `.venv` | **Cumple preliminarmente; falta revisión numérica independiente** |
| Gratuidad | La OpenSpec exige cruce por `cod_inst` con nómina Mineduc 2025 | **Debe verificarse fuente, cobertura y ausencia de nulos** |
| Sedes geoespaciales | Existe `mapa_sedes_oferta.png`; la spec exige lectura desde ZIP y EPSG:4326 | **Cumple como salida; falta prueba limpia** |
| Datos de demanda | Existen artefactos de demanda y sección de ingesta en el notebook | **Cumple preliminarmente** |
| Reservas tributarias `*` | La spec exige conversión a `NaN` y documentación del impacto | **Debe verificarse explícitamente** |
| Homologación AIOE | La spec exige puntaje, nivel, tipo de impacto y fuente | **Debe verificarse en el archivo y el notebook** |
| IRE_IA | Existe `indicadores_demanda_regional.csv` con 16 regiones e indicador `ire_ia`; el notebook fue ejecutado en `.venv` | **Cumple preliminarmente; falta validación numérica independiente** |
| Integración oferta-demanda | `dataset_match_ia_regional_sprint1.csv` contiene 16 regiones | **Cumple estáticamente** |
| Cuadrantes Match-IA | Existen cuatro categorías y `matriz_cuadrantes_match_ia.png` | **Cumple preliminarmente** |
| Ficha metodológica | El notebook contiene una sección de ficha técnica y recomendaciones | **Cumple preliminarmente** |
| Dataset consolidado | Existe `data/processed/dataset_match_ia_regional_sprint1.csv` con 16 filas y 22 campos | **Cumple estáticamente** |
| Reproducibilidad | `requirements.txt` existe; el notebook usa `pathlib` y extracción condicional; `.venv` contiene las dependencias y la ejecución terminó con código 0 | **Cumple** |

## 4. Artefactos verificados

### 4.1 Notebook

`notebooks/sprint1_match_ia_regional.ipynb`

- JSON válido.
- 28 celdas.
- Contiene secciones de setup, oferta, demanda, Match-IA, ficha metodológica y exportación.
- Conserva salidas ejecutadas.
- Ejecutado nuevamente con el intérprete `.\.venv\Scripts\python.exe` y `nbconvert` sin errores.
- Incluye referencias al dataset maestro y a la figura de cuadrantes.

### 4.2 Resultados CSV

| Archivo | Filas | Regiones | Estado |
|---|---:|---|---|
| `data/processed/indicadores_oferta_regional.csv` | 16 | 1–16, sin duplicados | Verificado |
| `data/processed/indicadores_demanda_regional.csv` | 16 | 1–16, sin duplicados | Verificado |
| `data/processed/dataset_match_ia_regional_sprint1.csv` | 16 | 1–16, sin duplicados | Verificado |

El dataset maestro contiene las cuatro categorías de cuadrante:

- Cuadrante I: Polo Consolidado.
- Cuadrante II: Brecha Crítica.
- Cuadrante III: Oferta sin Demanda Local.
- Cuadrante IV: En Transición.

### 4.3 Figuras

Se verificó la existencia de:

- `reports/figures/ranking_oferta_ia.png`
- `reports/figures/heatmap_lq_cine.png`
- `reports/figures/comparativa_gratuidad_ia.png`
- `reports/figures/mapa_sedes_oferta.png`
- `reports/figures/matriz_cuadrantes_match_ia.png`

## 5. Rúbrica propuesta y valoración provisional

La siguiente valoración no es una calificación institucional definitiva; sirve para identificar el estado actual y las evidencias faltantes.

| Dimensión | Peso | Valoración | Puntaje provisional |
|---|---:|---|---:|
| Cumplimiento de User_01/User_02 y OpenSpec | 30% | Bien, con criterios de gestión aún pendientes | 24/30 |
| Rigor de datos e indicadores | 20% | Bien preliminar; deben verificarse fuentes, fórmulas y reservas `*` | 15/20 |
| Reproducibilidad y Definition of Done | 20% | Bien; ejecución limpia confirmada en `.venv`, con revisión menor de encoding | 18/20 |
| Sprint Review e incremento para stakeholders | 10% | Bien: existe un incremento demostrable, pero falta evidencia de presentación/validación | 7/10 |
| Git, GitHub Projects y trazabilidad | 10% | Por verificar; la captura evidencia parte del backlog, no todo el flujo | 5/10 |
| Planificación, colaboración y retrospectiva | 10% | Por verificar; hay responsables y HH documentadas, falta evidencia de eventos y acuerdos | 5/10 |
| **Total provisional** | **100%** | **Avance favorable con pendientes de trazabilidad y presentación** | **74/100** |

### Interpretación

El resultado provisional corresponde a un producto con avance técnico importante y reproducibilidad demostrada. La aceptación definitiva aún requiere cerrar la trazabilidad de User_02, revisar el encoding y aportar evidencia completa del GitHub Project y de los eventos Scrum.

## 6. Hallazgos

### H-01 — Reproducibilidad verificada; conservar evidencia

**Severidad:** cerrada  
**Evidencia:** el entorno virtual contiene `pandas 3.0.6`, `geopandas 1.2.0`, `jupyter 1.1.1` y `nbconvert 7.17.2`. Se ejecutó el notebook con `.\.venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute`; el proceso terminó con código 0 y generó `sprint1_match_ia_regional_validated.ipynb` en la carpeta de validación de sesión.  
**Impacto:** la reproducibilidad básica del notebook quedó demostrada en el entorno virtual del proyecto.  
**Acción de mantenimiento:** conservar el comando de validación y revisar los warnings del kernel en una futura automatización CI.

```powershell
.\.venv\Scripts\python.exe -m jupyter nbconvert --to notebook --execute notebooks\sprint1_match_ia_regional.ipynb
```

La ejecución terminó sin errores y generó nuevamente el notebook validado y sus salidas.

### H-02 — Estado inconsistente de User_02

**Severidad:** alta  
**Evidencia:** el README ya fue actualizado para reflejar 2/2 tareas, pero la captura y los artefactos locales deben contrastarse con el estado actual del GitHub Project y con los issues; anteriormente existía una discrepancia entre esas fuentes.  
**Impacto:** no existe una única fuente confiable para determinar si el Sprint 1 está cerrado.  
**Acción:** actualizar GitHub Project, issues, README y artefactos OpenSpec para que reflejen el mismo estado, o documentar explícitamente qué criterio mantiene User_02 abierta.

### H-03 — Codificación de etiquetas de cuadrante

**Severidad:** media  
**Evidencia:** al leer el dataset consolidado se observan caracteres corruptos en `Crítica` y `Transición`.  
**Impacto:** puede afectar la legibilidad del dataset, filtros del futuro dashboard y presentación a stakeholders.  
**Acción:** revisar la codificación de exportación y lectura, preferentemente UTF-8 consistente; regenerar el CSV y verificar los textos.

### H-04 — Evidencia incompleta del GitHub Project

**Severidad:** media  
**Evidencia:** la captura muestra Product Backlog, historias, Sprint 1, estimaciones y asignaciones; no demuestra PR, revisiones, historial de estados, automatizaciones, reuniones ni retrospectiva.  
**Impacto:** la dimensión de gestión ágil no puede evaluarse completamente.  
**Acción:** aportar exportación/capturas de las vistas Tasks/Sprint Kanban, issues #8–#11, PR asociadas, commits y registros de Sprint Review/Retrospective.

## 7. Definition of Done

| Criterio | Estado |
|---|---|
| Objetivo/hipótesis de negocio claro | Cumple |
| Fuentes identificadas | Cumple preliminarmente |
| Fuentes validadas | Pendiente de revisión documental |
| Limpieza reproducible | Implementada y ejecutada en `.venv` sin errores |
| Resultados respaldados por código | Cumple preliminarmente |
| Métricas y fórmulas documentadas | Cumple preliminarmente |
| Conclusiones accesibles | Cumple preliminarmente |
| Criterios de aceptación demostrados | Parcial |
| Revisión de código/PR demostrada | No verificable |
| Sprint Review demostrada | No verificable |
| Sprint Retrospective demostrada | No verificable |

## 8. Recomendación de decisión del Sprint Review

**Decisión recomendada:** aceptar el incremento como **entrega candidata con observaciones**, no como cierre definitivo, hasta resolver H-02, H-03 y H-04.

El incremento puede presentarse porque contiene:

- análisis de oferta;
- análisis de demanda y exposición;
- indicadores regionales;
- matriz Match-IA;
- visualizaciones;
- dataset consolidado;
- ficha metodológica y recomendaciones.

La aceptación definitiva debe quedar condicionada a:

1. corrección o validación del encoding;
2. sincronización de estados y trazabilidad;
3. evidencia de revisión por el Product Owner/stakeholders.

## 9. Guion de presentación

1. Objetivo del Sprint 1 y relación con User_01/User_02.
2. Fuentes, supuestos y criterios de clasificación.
3. Ejecución reproducible del notebook.
4. Indicadores de oferta y gratuidad.
5. Indicadores de demanda e IRE_IA.
6. Matriz de cuadrantes y análisis de regiones.
7. Dataset consolidado y ficha metodológica.
8. Limitaciones, hallazgos y decisiones para Sprint 2.
9. Confirmación del Product Owner sobre aceptación o devolución de observaciones.

## 10. Acciones para el Sprint 2

| Acción | Responsable sugerido | Criterio de cierre |
|---|---|---|
| Conservar validación reproducible del notebook | Equipo técnico | Comando con `.venv` documentado y log sin errores |
| Sincronizar estados de User_02 | Scrum Master/PO | README, issues, Project y tasks coinciden |
| Corregir encoding de resultados | Responsable del notebook | Cuadrantes legibles en CSV, notebook y dashboard |
| Formalizar checklist de cierre | Scrum Master | Checklist asociado a cada tarea antes de cerrarla |
| Capturar evidencia de Review/Retrospective | Equipo | Acta o comentario con acuerdos, responsables y acciones |
| Preparar integración al dashboard | Equipo Sprint 2 | Dashboard consume el dataset validado |
