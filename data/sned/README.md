# Datos SNED (Sistema Nacional de Evaluación del Desempeño)

## Descripción
Esta carpeta contiene datos del Sistema Nacional de Evaluación del Desempeño de establecimientos educacionales subvencionados en Chile. El SNED es un sistema que evalúa y premia el desempeño de establecimientos educacionales a través de diversos indicadores de calidad educativa.

## Archivos
- `sned.csv`: Base de datos con indicadores SNED por establecimiento

---

## Diccionario de Variables

### Base SNED (`sned.csv`)

#### Identificación del Establecimiento
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| idrbd | Identificador único del establecimiento (RBD) | Entero |
| nom_rbd | Nombre oficial del establecimiento | Texto |

#### Ubicación Geográfica
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| cod_reg_rbd | Código de región del establecimiento | Entero |
| cod_pro_rbd | Código de provincia del establecimiento | Entero |
| cod_com_rbd | Código de comuna del establecimiento | Entero |
| nom_com_rbd | Nombre de la comuna | Texto |
| cod_deprov_rbd | Código de dependencia provincial | Entero |
| nom_deprov_rbd | Nombre de la dependencia provincial | Texto |
| rural_rbd | Indicador de ruralidad (1=Urbano, 2=Rural) | Entero |

#### Indicadores de Desempeño SNED
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| efectivr | Factor Efectividad: logro de objetivos educacionales | Decimal |
| superar | Factor Superación: progreso educativo del establecimiento | Decimal |
| iniciar | Factor Iniciativa: capacidad innovadora y compromiso docente | Decimal |
| mejorar | Factor Mejoramiento: capacidad de perfeccionamiento | Decimal |
| integrar | Factor Integración: trabajo en equipo y participación | Decimal |
| igualdr | Factor Igualdad de Oportunidades: integración de grupos vulnerables | Decimal |

#### Clasificación y Selección
| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| cluster | indicador de grupo por puntaje SNED | Entero |
| indicer | Índice general SNED (puntaje final ponderado) | Decimal |
| sel2016_25 | El establecimiento es seleccionado por SNED (25% superior).| Entero |
| sel2016_35 | El establecimiento es seleccionado por SNED (35% superior).| Entero |
| **sel** | Indicador final de selección SNED | Entero |

## Metodología SNED

### Los 6 Factores de Evaluación

1. **Efectividad (efectivr)**: 
   - Mide el logro de los objetivos educacionales del establecimiento
   - Basado en resultados SIMCE y otros indicadores académicos

2. **Superación (superar)**:
   - Evalúa el progreso educativo y las tendencias de mejoramiento
   - Compara el desempeño actual con períodos anteriores

3. **Iniciativa (iniciar)**:
   - Mide la capacidad de innovación y el compromiso de los docentes
   - Incluye proyectos educativos y actividades extracurriculares

4. **Mejoramiento (mejorar)**:
   - Evalúa la capacidad de perfeccionamiento del equipo docente
   - Considera la formación continua y actualización pedagógica

5. **Integración (integrar)**:
   - Mide el trabajo en equipo y la participación de la comunidad
   - Incluye participación de padres y integración comunitaria

6. **Igualdad de Oportunidades (igualdr)**:
   - Evalúa la integración y atención de grupos vulnerables
   - Considera políticas de inclusión y equidad

### Sistema de Agrupación
- **Clusters**: Los establecimientos se agrupan por características similares (matrícula, ruralidad, dependencia) para una comparación justa
- **Selección 1**: A los establecimientos con mayores puntajes en
el Índice SNED, y que representen **hasta el 25%**
de la matrícula regional, les corresponde recibir el 100% del valor de la Subvención por Desempeño
de Excelencia.
- **Selección 2**: A los establecimientos que representen hasta el
35% de la matrícula regional, y que no alcanzaron a
estar incluidos en el tramo anterior, les corresponde
percibir el 60% del valor de dicha subvención.

### Códigos de Selección
- **1**: No seleccionado para incentivo SNED
- **2**: Seleccionado para incentivo SNED

## Notas Metodológicas

- Los datos corresponden al período de evaluación 2016-2017
- Todos los indicadores están normalizados para permitir comparación entre establecimientos
- Solo establecimientos subvencionados participan en el SNED
- El incentivo SNED corresponde a una asignación monetaria para los docentes del establecimiento

Para mayor información, visitar: https://sned.mineduc.cl/