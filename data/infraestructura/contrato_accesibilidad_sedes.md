# Contrato de salidas de accesibilidad y disponibilidad de servicios (Tarea #17)

Este documento especifica las tablas y reportes producidos por la Sección 11 de
`notebooks/sprint1_match_ia_regional.ipynb` para su consumo en la Tarea #18
(Sección 12: mapas y hallazgos exploratorios de brechas de infraestructura).

## 1. Reglas generales y trazabilidad

- **Dependencia de entrada:** Consume `data/infraestructura/manifest.csv`,
  `data/infraestructura/fuentes.csv`, `data/infraestructura/contrato_datos.md`,
  `data/processed/infraestructura/manifest_validado.csv` y la capa de sedes
  de educación superior (`data/geo/layer_establecimientos_de_educacion_superior_20220309024111(1).zip`).
- **Separación de niveles territoriales:** Los indicadores se calculan a nivel de
  `cod_sede` y se agregan a nivel regional mediante `region_orden` y
  `region_nombre`. Los agregados productivos del SII no se reparten ni imputan a
  sedes, comunas ni radios de 5 km.
- **Estados explícitos permitidos:** `disponible`, `pendiente`, `sin datos` y
  `excluido`. Ninguna entrada `pendiente` o `sin datos` puede transformarse en
  valor `0` implícito.

## 2. Artefactos exportados por la Sección 11

| Artefacto | Ruta de exportación | Granularidad | Clave primaria | Consumidor |
|---|---|---|---|---|
| Tabla de indicadores por sede | `data/processed/indicadores_accesibilidad_sedes.csv` y `data/processed/infraestructura/indicadores_accesibilidad_sedes.csv` | 1 fila por registro de sede en la fuente (`cod_sede`, `sede_row_id`) | `sede_row_id` (`cod_sede` único entre sedes válidas) | Tarea #18 |
| Resumen regional de accesibilidad | `data/processed/resumen_accesibilidad_regional.csv` y `data/processed/infraestructura/resumen_accesibilidad_regional.csv` | 16 regiones oficiales de Chile | `region_orden` | Tarea #18 |
| Diccionario metodológico | `data/infraestructura/diccionario_indicadores_accesibilidad.csv` y `data/processed/diccionario_indicadores_accesibilidad.csv` | 1 fila por indicador documentado | `indicador_id` | Tarea #18 |
| Reporte de validación | `data/processed/reporte_validacion_accesibilidad.csv` y `data/processed/infraestructura/reporte_validacion_accesibilidad.csv` | 1 fila por regla de validación ejecutada | `check_id` | Tarea #18 |

## 3. Esquema de `indicadores_accesibilidad_sedes.csv`

| Columna | Tipo | Unidad | Nulos permitidos | Descripción |
|---|---|---|---|---|
| `sede_row_id` | `int` | índice | No | Identificador secuencial de fila en la fuente original (`1..1297`) |
| `cod_sede` | `string` | código | No | Clave natural determinística de sede (`SEDE_{COD_INST}_{COD_COMUNA}_{HASH8}`) |
| `cod_inst` | `int` | código | No | Código institucional Mineduc (`COD_INST`) |
| `nombre_inst` | `string` | texto | No | Nombre de la institución (`NOMBRE_INS`) |
| `nombre_sede` | `string` | texto | No | Nombre de la sede o inmueble (`NOMBRE_INM`) |
| `region_orden` | `int` | orden 1..16 | No (en válidas) | Orden geográfico norte a sur del Sprint 1 |
| `region_nombre` | `string` | texto | No (en válidas) | Nombre regional estandarizado del Sprint 1 |
| `es_region_mvp` | `bool` | booleano | No | `True` para Valparaíso (6), Metropolitana de Santiago (7) y Biobío (11) |
| `comuna_nombre` | `string` | texto | No | Comuna registrada en la fuente geográfica |
| `latitud` | `float` | grados (`EPSG:4326`) | No (en válidas) | Latitud WGS84 de la sede |
| `longitud` | `float` | grados (`EPSG:4326`) | No (en válidas) | Longitud WGS84 de la sede |
| `geometria_valida` | `bool` | booleano | No | Resultado de validación de geometría puntual no nula y válida |
| `cod_sede_unico` | `bool` | booleano | No | `True` en la primera aparición de `cod_sede`; `False` en duplicados |
| `estado_sede` | `string` | estado | No | `disponible` o `excluido` |
| `causa_exclusion` | `string` | texto | No | `ninguna` para sedes válidas o causa explícita de exclusión |
| `fuente_sedes` | `string` | referencia | No | Archivo e identificador de fuente de sedes |
| `fecha_corte_sedes` | `string` | fecha | No | Fecha de corte/versión del archivo de sedes (`2022-03-09`) |
| `crs_sedes` | `string` | CRS | No | `EPSG:4326` |
| `crs_metrico` | `string` | CRS | No | CRS métrico reportado por el manifest de #16 (`pendiente` si no está confirmado) |
| `radio_m` | `int` | metros | No | Radio fijo de evaluación de servicios (`5000`) |
| `fuente_red_vial` | `string` | referencia | No | `source_id` de `red_vial_metric` en el manifest de #16 |
| `regla_via_principal` | `string` | texto | No | Regla contractual de selección de vías principales |
| `d_via_m` | `float` | metros | Sí (`pendiente`/`sin datos`/`excluido`) | Distancia euclidiana mínima a la vía principal más cercana |
| `estado_d_via` | `string` | estado | No | `disponible`, `pendiente`, `sin datos` o `excluido` |
| `causa_d_via` | `string` | texto | No | Detalle de disponibilidad o causa de no cálculo |
| `categoria_servicio` | `string` | categoría | No | Categoría evaluada o `todas_categorias_contrato` cuando la fuente está pendiente |
| `fuente_servicios` | `string` | referencia | No | `source_id` de `servicios_metric` en el manifest de #16 |
| `n_servicios_5km` | `Int64` | conteo | Sí (`pendiente`/`sin datos`/`excluido`) | Conteo entero de servicios a distancia `<= 5000 m` |
| `disp_servicios_5km` | `Int64` | binario (`0`/`1`) | Sí (`pendiente`/`sin datos`/`excluido`) | Indicador binario `I(n_c(s) > 0)` |
| `estado_servicios` | `string` | estado | No | `disponible`, `pendiente`, `sin datos` o `excluido` |
| `causa_servicios` | `string` | texto | No | Detalle de disponibilidad o causa de no cálculo |
| `fuente_conectividad` | `string` | referencia | No | `source_id` de `conectividad_4326` en el manifest de #16 |
| `conectividad_valor` | `float` | según fuente | Sí | Valor de conectividad cuando exista fuente asociable |
| `conectividad_unidad` | `string` | texto | No | Unidad original de la fuente o `sin_datos` |
| `estado_conectividad` | `string` | estado | No | `disponible`, `pendiente`, `sin datos` o `excluido` |
| `causa_conectividad` | `string` | texto | No | Explicación explícita de disponibilidad o ausencia de fuente |

## 4. Esquema de `resumen_accesibilidad_regional.csv`

Incluye una fila por cada una de las 16 regiones (`region_orden`, `region_nombre`,
`es_region_mvp`) con:
- `n_sedes_brutas`, `n_sedes_validas`, `n_sedes_excluidas`,
  `cobertura_sedes_validas_pct` y `causas_exclusion`.
- Medidas regionales de distancia vial (`d_via_media_m`, `d_via_mediana_m`,
  `n_sedes_con_d_via`, `estado_d_via_regional`) y de servicios en radio de 5 km
  (`n_servicios_5km_medio`, `pct_sedes_con_servicios_5km`,
  `n_sedes_con_servicios`, `radio_m`, `estado_servicios_regional`), además de
  `estado_conectividad_regional`, `crs_metrico`, `fuente_sedes` y
  `nota_no_desagregacion_sii`.
