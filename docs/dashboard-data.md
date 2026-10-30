# Dashboard: datos y trazabilidad

La aplicación consume exclusivamente artefactos derivados de
`data/processed/`. No carga, descomprime ni limpia los insumos crudos de
`data/oferta/`, `data/demanda/` o `data/geo/`.

El contrato de cada artefacto está en `data/processed/dashboard_manifest.json`.
Cada entrada declara columnas, tipos, unidades, granularidad, nulos, fuente,
fecha de corte, cobertura, CRS, hash y filas. La lectura se valida antes de
renderizar y queda cacheada por firma de tamaño y modificación del archivo.

Las fuentes principales son los indicadores de Sprint 1 y los resultados de
infraestructura de HU4. `region_orden` usa la codificación nacional 1 a 16;
el MVP se valida con Valparaíso (6), Metropolitana de Santiago (7) y Biobío
(11). Los estados `pendiente`, `sin datos`, `excluido` y `no disponible` se
mantienen visibles cuando un artefacto no puede presentarse como válido.

Para agregar una tabla, primero debe materializarse fuera de Streamlit,
registrarse en el manifest y contar con una prueba de contrato. Las vistas
futuras de la Tarea #20 pueden reutilizar `load_available` y el selector sin
modificar la entrada de la aplicación.
