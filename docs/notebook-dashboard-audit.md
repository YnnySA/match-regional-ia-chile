# Auditoría de paridad notebook-dashboard

## Hallazgos corregidos

- El dashboard resumía la tabla fina para KPI y reutilizaba ese resumen en
  Match-IA, perdiendo `ire_ia`, `cuadrante_codigo` y `cuadrante_match_ia`.
  Ahora Match-IA conserva el artefacto maestro regional y los KPI usan una
  tabla filtrada separada.
- La matriz LQ tenía una altura dependiente del número de filas y se mostraba
  comprimida. Ahora usa un contenedor amplio, etiquetas legibles y una matriz
  numérica colapsable.
- La selección inicial estaba limitada a Valparaíso y sin áreas. Ahora inicia
  con las 16 regiones y las 10 áreas CINE-F-13.
- El notebook y el dashboard mostraban capas de red vial, servicios y
  conectividad sin fuente validada común. Esas visualizaciones fueron retiradas
  del producto entregable; se conserva únicamente la capa de sedes validada.

## Catálogo final común

| Resultado | Artefacto | Notebook | Dashboard |
|---|---|---|---|
| Ranking de oferta afín a IA | `dataset_match_ia_regional_sprint1.csv` | Sí | Sí |
| Gratuidad institucional | `oferta_fina_region_cine_nivel_gratuidad.csv` | Sí | Sí |
| Heatmap LQ | `matriz_lq_cine_regional.csv` | Sí | Sí |
| Sedes regionales | `indicadores_accesibilidad_sedes.csv` | Sí | Sí |
| Match-IA | `dataset_match_ia_regional_sprint1.csv` | Sí | Sí |
| Red vial, servicios y conectividad | — | Excluido | Excluido |

Las diferencias entre Matplotlib/Seaborn y Altair son únicamente de
presentación. Los valores, fórmulas, denominadores, unidades, corte 2025 y
granularidad regional deben provenir de los mismos artefactos procesados.
