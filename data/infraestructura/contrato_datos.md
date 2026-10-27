# Contrato de datos de infraestructura territorial

El contrato distingue la granularidad real de cada fuente y no permite
desagregaciones sintéticas. Todos los textos deben estar en UTF-8. Las capas
geoespaciales deben conservar geometría válida y declarar `crs_input`,
`crs_metric` y `crs_display`.

## Capas procesadas

| Artefacto | Granularidad | Columnas mínimas y tipos | Unidades | Nulos críticos | Identificador estable | Reglas de validez |
|---|---|---|---|---|---|---|
| `red_vial_4326` | Segmento vial de la fuente | `source_id:string`, `segment_id:string`, `road_class:string`, `name:string?`, `region_code:string?`, `geometry:LineString/MultiLineString` | Longitud en unidad de la fuente; no calcular distancias aquí | `source_id`, `segment_id`, `geometry` | `source_id:segment_id` | Geometría válida, clave única, CRS EPSG:4326 |
| `red_vial_metric` | Segmento vial de la fuente | Igual a `red_vial_4326` | Metros para cálculos posteriores | `source_id`, `segment_id`, `geometry` | `source_id:segment_id` | Misma geometría transformada; CRS métrico documentado |
| `servicios_4326` | Punto o polígono según fuente | `source_id:string`, `service_id:string`, `category:string`, `name:string?`, `region_code:string?`, `comuna_code:string?`, `geometry:Point/Polygon/MultiPolygon` | Unidad espacial original | `source_id`, `service_id`, `category`, `geometry` | `source_id:service_id` | Geometría válida, clave única, sin inventar nivel territorial |
| `servicios_metric` | Punto o polígono de la fuente | Igual a `servicios_4326` | Metros para cálculos posteriores | `source_id`, `service_id`, `category`, `geometry` | `source_id:service_id` | Misma granularidad; CRS métrico documentado |
| `conectividad_4326` | Unidad territorial o punto de la fuente | `source_id:string`, `location_id:string`, `technology:string?`, `availability_status:string`, `region_code:string?`, `geometry:Point/Polygon?` | Unidad publicada por la fuente | `source_id`, `location_id`, `availability_status` | `source_id:location_id` | No imputar métricas ausentes; estado `pendiente` si falta fuente |

## Estados y calidad

`status` solo puede ser `disponible`, `pendiente` o `error`. Un artefacto con
geometrías inválidas, claves duplicadas, nulos críticos, codificación
incompatible o señales de mojibake no puede quedar como `disponible`.

EPSG:4326 es la salida de intercambio/visualización. El CRS métrico queda
`pendiente` hasta confirmar la cobertura espacial de las fuentes; no se deben
calcular radios o distancias antes de esa decisión.

