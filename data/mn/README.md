# Datos de Desarrollo Infantil Temprano

## Descripción
Esta carpeta contiene datos del estudio longitudinal de desarrollo infantil temprano, incluyendo información sobre estado nutricional por niveles educativos iniciales y seguimiento longitudinal de niños desde educación preescolar.

## Archivos
- `1m2017.csv`: Estado nutricional en primero basico por género (2017)
- `mn_5p_2017b.csv`: Panel longitudinal de desarrollo infantil (Rrondas 0, 1, 2)

---

## Diccionario de Variables

### Matrícula por Nivel (`1m2017.csv`)

| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| idrbd | Identificador único del establecimiento (RBD) | Decimal |
| dnino | desnutricion - niños | Entero |
| dnina | desnutricion - niñas | Entero |
| bpnino | bajo peso - niños | Entero |
| bpnina | bajo peso - niñas | Entero |
| nnino | peso normal - niños | Entero |
| nnina | peso normal - niñas | Entero |
| snino | sobrepeso - niños | Entero |
| snina | sobrepeso - niñas | Entero |
| onino | obesidad - niños | Entero |
| onina | obesidad - niñas | Entero |
| rtnino | retraso talla - niños | Entero |
| rtnina | retraso talla - niñas | Entero |
| tnino | Total matrícula - niños | Entero |
| tnina | Total matrícula - niñas | Entero |
| total | Total general de matrícula | Entero |

### Panel Longitudinal Desarrollo Infantil (`mn_5p_2017b.csv`)


#### Variables Demográficas Base
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| sexo_0 | Sexo del niño/a (ronda 0) | Entero |
| rbd_0 | ID establecimiento educacional (ronda 0) | Entero |
| te_0 | talla estandarizada (ronda 0) | Decimal |
| imce_0 | Índice de masa corporal estandarizado (ronda 0) | Decimal |
| area_0 | Área geográfica: urbana/rural (ronda 0) | Entero |

#### Composición del Hogar (ronda 0)
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| vive_padre_0 | Vive con padre en el hogar | Entero |
| vive_madre_0 | Vive con madre en el hogar | Entero |
| vive_abuelo_0 | Vive con abuelo en el hogar | Entero |
| vive_abuela_0 | Vive con abuela en el hogar | Entero |
| vive_hermano_0 | Vive con hermanos en el hogar | Entero |
| vive_tioa_0 | Vive con tíos/as en el hogar | Entero |
| vive_otro_familiar_0 | Vive con otros familiares | Entero |
| vive_otro_no_familiar_0 | Vive con personas no familiares | Entero |
| vive_hogar_menores_0 | Vive en hogar de menores | Entero |
| vive_acogida_0 | Vive en familia de acogida | Entero |
| vive_no_sabe_0 | No se sabe composición del hogar | Entero |

#### Cuidado del Niño/a (ronda 0)
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| cuida_padre_0 | Cuidado principal: padre | Entero |
| cuida_madre_0 | Cuidado principal: madre | Entero |
| cuida_abuelo_0 | Cuidado principal: abuelo | Entero |
| cuida_abuela_0 | Cuidado principal: abuela | Entero |
| cuida_hermano_0 | Cuidado principal: hermanos | Entero |
| cuida_tioa_0 | Cuidado principal: tíos/as | Entero |
| cuida_otro_familiar_0 | Cuidado principal: otros familiares | Entero |
| cuida_otro_no_familiar_0 | Cuidado principal: no familiares | Entero |
| cuida_acogida_0 | Cuidado en familia de acogida | Entero |
| cuida_no_aplica_0 | No aplica cuidado | Decimal |
| cuida_no_sabe_0 | No se sabe quién cuida | Entero |

#### Características Socioeconómicas (ronda 0)
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| n_personas_0 | Número de personas en el hogar | Decimal |
| ocu_madre_0 | Ocupación/trabajo de la madre | Decimal |
| ocu_padre_0 | Ocupación/trabajo del padre | Decimal |
| ocu_jf_0 | Ocupación del jefe de hogar | Decimal |
| educm_0 | Nivel educacional de la madre | Entero |
| educp_0 | Nivel educacional del padre | Entero |
| n_habitaciones_0 | Número de habitaciones en el hogar | Decimal |
| pieza_nino_0 | El menor tiene pieza independiente | Decimal |
| espacio_tareas_0 | Cantidad de espacios adecuados para hacer tareas | Decimal |

#### Características del Entorno (ronda 0)
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| cercania_juegos_0 | Cercanía a espacios de juego/recreación. Muy cerca (1)-Muy lejos (4) | Decimal |
| cercania_servicios_0 | Cercanía a servicios básicos. Muy cerca (1)-Muy lejos (4) | Decimal |

#### Características del Nacimiento (ronda 0)
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| edad_parto_0 | Edad de la madre al parto | Decimal |
| edad_primer_parto_0 | Edad de la madre al primer parto | Decimal |
| p_nacer_0 | Peso al nacer del niño/a | Decimal |
| prematuro_0 | Indicador de parto prematuro. Sí (1), No (2). | Decimal |

#### Figuras Paternas (ronda 0)
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| fig_pat_crianza_0 | Figura paterna esta en la crianza | Entero |
| fig_pat_recursos_0 | Figura paterna aporta recursos económicos | Entero |

#### Difficultades de aprendizaje (ronda 0)
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| diff0_0 | dificultad para realizar tarea | Decimal |
| diff1_0 | dificultad visual | Decimal |
| diff2_0 | dificultad auditiva | Decimal |
| diff3_0 | dificultad control de comportamiento | Decimal |
| diff4_0 | difucultad para entender | Decimal |
| diff5_0 | dificultad para aprender | Decimal |
| diff6_0 | dificultad para caminar | Decimal |
| diff7_0 | dificultad social | Decimal |
| diff8_0 | el colegio apoya con las dificultades | Decimal |

#### Indicadores de inversion parental (I) y desarrollo socioemocional (S)
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| I1 | Indicador de desarrollo 1 | Decimal |
| I2 | Indicador de desarrollo 2 | Decimal |
| S0 | Score/puntaje ronda 0 | Decimal |
| S1 | Score/puntaje ronda 1 | Decimal |
| S2 | Score/puntaje ronda 2 | Decimal |

## Estructura panel de datos
- **ronda 0**: Variables con sufijo `_0` (línea base)
- **ronda 1**: Variables con sufijo `_1` (primer seguimiento)  
- **ronda 2**: Variables con sufijo `_2` (segundo seguimiento)

## Notas Metodológicas
- Datos de panel: mismo grupo de niños seguido en 3 momentos temporales
- Variables binarias: 0 = No, 1 = Sí
- Algunas variables pueden tener valores perdidos (NaN)
- IMCE: Índice de Masa Corporal Estandarizado
- Los puntajes finales (S0, S1, S2) representan indices de desarrollo socioemocional