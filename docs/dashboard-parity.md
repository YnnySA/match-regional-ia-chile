# Matriz de paridad notebook-dashboard

El notebook es la referencia técnica y Streamlit la representación visual. La
paridad se valida sobre artefactos procesados, no sobre imágenes.

| Resultado del notebook | Artefacto compartido | Vista del dashboard | Unidad/corte | Estado |
|---|---|---|---|---|
| Oferta regional y % afín | `dataset_match_ia_regional_sprint1.csv` | Ranking y tabla de oferta | conteos, %, 2025 | disponible |
| Composición por área y nivel | `oferta_fina_region_cine_nivel_gratuidad.csv` | Composición de titulados | titulados, 2025 | disponible |
| Gratuidad institucional | `oferta_fina_region_cine_nivel_gratuidad.csv` | Gratuidad institucional | titulados, 2025 | disponible |
| LQ por área CINE | `matriz_lq_cine_regional.csv` | Especialización territorial | índice LQ, 2025 | disponible/estado declarado |
| Demanda e IRE-IA | `indicadores_demanda_regional.csv` | Estructura productiva | región, 2025 | disponible |
| Cuadrantes Match-IA | `dataset_match_ia_regional_sprint1.csv` | Matriz Match-IA | IRE-IA y %, 2025 | disponible |
| Sedes válidas y excluidas | `resumen_accesibilidad_regional.csv` | Distribución regional de sedes | sedes y %, 2022-03-09 | disponible |
| Red vial | — | — | — | excluido por falta de fuente validada |
| Servicios en 5 km | — | — | — | excluido por falta de fuente validada |
| Conectividad | — | — | — | excluido por falta de fuente validada |

Para ejecutar la validación de valores y estados de las regiones MVP:

```powershell
.venv\Scripts\python -m src.dashboard.parity
```

La validación cubre Valparaíso (6), Metropolitana de Santiago (7) y Biobío
(11), y no convierte estados pendientes o sin datos en ceros. Las capas de red
vial, servicios y conectividad no forman parte del catálogo visual final.
