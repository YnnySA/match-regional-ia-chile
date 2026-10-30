# Síntesis exploratoria de brechas de infraestructura

Generación: 2026-10-30T03:48:04+00:00

Esta síntesis es descriptiva y exploratoria; no constituye una recomendación
definitiva de subsidios, inversión ni priorización de política pública.

1. La cobertura de sedes válidas varía entre 97.73% y
   100.00% entre las 16 regiones. La comparación se sustenta en
   `comparativa_brechas_regional.csv` y conserva sedes brutas, válidas y
   excluidas. Limitación: la cobertura depende de la fuente de sedes con corte
   2022-03-09 y no equivale a cobertura de matrícula o población.
2. La región con más exclusiones registradas es
   Metropolitana de Santiago (4
   sedes). Esto describe control de calidad de la fuente y no una brecha de
   infraestructura. Limitación: las exclusiones corresponden a reglas de
   unicidad y geometría del artefacto validado.
3. La distancia a la red vial principal permanece con estado `pendiente`
   para las sedes, por lo que no existe una comparación regional de distancia
   de viaje. Limitación: el contrato distingue distancia euclidiana de tiempo
   o distancia de viaje y el CRS métrico de #16 está pendiente.
4. La disponibilidad de servicios en radio de 5 km permanece con estado
   `pendiente` y conectividad digital con estado
   `sin datos`. Estos estados no se interpretan como ausencia
   geográfica ni como disponibilidad nula. Limitación: las fuentes de servicios
   y conectividad no tienen cobertura validada para esta entrega.
