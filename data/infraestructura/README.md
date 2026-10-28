# Datos territoriales de infraestructura y servicios

Este directorio contiene el inventario, contrato y manifest de los insumos
previstos para HU4. La disponibilidad se expresa de forma explícita:
`disponible` solo se usa cuando la fuente, licencia, cobertura y formato han
sido verificados; en otro caso el estado es `pendiente`.

## Decisiones aún pendientes

| Decisión | Estado | Regla de uso |
|---|---|---|
| Tres regiones del MVP | `pendiente` | Se conserva la cobertura territorial declarada por cada fuente; no se filtran ni inventan regiones. |
| Fuente de red vial | `pendiente` | No se genera una capa de red hasta verificar origen, licencia, fecha de corte y CRS. |
| Fuente de servicios territoriales | `pendiente` | Las referencias candidatas se mantienen en el inventario, sin declararlas disponibles. |
| Fuente de conectividad digital | `pendiente` | No se imputan velocidades, cobertura ni puntos de conectividad. |
| Radio y unidad para la tarea #17 | `pendiente` | El contrato deja el campo preparado, pero no calcula distancias ni accesibilidad. |

## Fuentes candidatas

Las referencias de `fuentes.csv` son puntos de partida documentales. No son
entradas utilizables mientras permanezcan con estado `pendiente`.

- Instalaciones y edificaciones públicas: catálogo de datos.gob.cl.
- Descargas geoespaciales del Ministerio de Obras Públicas: portal Geomop.
- Conectividad: portal institucional de SUBTEL, pendiente de identificar el
  conjunto de datos y su licencia aplicable.

## Obtención reproducible

1. Registrar en `fuentes.csv` la URL exacta del recurso, licencia, fecha de
   consulta, fecha de corte, cobertura, nivel territorial, formato, CRS y
   tamaño observado o `pendiente`.
2. Descargar el recurso fuera de Git en `data/infraestructura/raw/` usando la
   URL registrada. No modificar el archivo crudo.
3. Calcular un SHA-256 y registrar el valor esperado en `manifest.csv`.
4. Ejecutar el notebook desde la raíz del repositorio. La Sección 10 solo
   materializa resultados con estado `disponible` y conserva los demás como
   `pendiente`.
5. Si cambia el recurso, fecha o hash, crear una nueva entrada de manifest;
   no sobrescribir la trazabilidad anterior.

Los archivos crudos pesados o no redistribuibles permanecen fuera del índice
de Git. Los artefactos derivados livianos y documentales sí pueden versionarse.

