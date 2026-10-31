# Dashboard: datos y trazabilidad

La aplicación consume exclusivamente artefactos derivados de
`data/processed/`. No carga, descomprime ni limpia los insumos crudos de
`data/oferta/`, `data/demanda/` o `data/geo/`.

El contrato de cada artefacto está en `data/processed/dashboard_manifest.json`.
Cada entrada declara columnas, tipos, unidades, granularidad, nulos, fuente,
fecha de corte, cobertura, CRS, hash y filas. La lectura se valida antes de
renderizar y queda cacheada por firma de tamaño y modificación del archivo.

La tabla fina y la matriz LQ se materializan offline con:

```powershell
.venv\Scripts\python -m src.dashboard.prepare_offer
```

La preparación cruza `cod_inst` con la nómina
`data/oferta/instituciones_gratuidad_2025.csv`, conserva los casos sin
coincidencia y exporta la tabla fina, la matriz LQ y el reporte de auditoría.

Las fuentes principales son los indicadores de Sprint 1, los artefactos de
oferta y demanda regional y la capa de sedes validada de HU4. Las capas de red
vial, servicios en 5 km y conectividad se excluyeron del entregable porque no
cuentan con una fuente validada común.
`region_orden` usa la codificación nacional 1 a 16;
el MVP se valida con Valparaíso (6), Metropolitana de Santiago (7) y Biobío
(11). Los estados `pendiente`, `sin datos`, `excluido` y `no disponible` se
mantienen en la trazabilidad técnica, pero no se convierten en visualizaciones
del catálogo final cuando la fuente no está validada.

Para agregar una tabla, primero debe materializarse fuera de Streamlit,
registrarse en el manifest y contar con una prueba de contrato. Las vistas
futuras de la Tarea #20 pueden reutilizar `load_available` y el selector sin
modificar la entrada de la aplicación.

La correspondencia entre salidas del notebook y paneles del dashboard está
documentada en `docs/dashboard-parity.md`. La prueba automatizada se ejecuta
con `python -m src.dashboard.parity`.
