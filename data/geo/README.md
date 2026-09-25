# Datos Geográficos de Establecimientos Educacionales

## Descripción
Esta carpeta contiene información geográfica y administrativa de establecimientos educacionales chilenos, incluyendo ubicación, dependencia administrativa, niveles educativos ofrecidos y características institucionales.

## Archivos
- `geo_rbd.csv`: Base de datos geográficos de establecimientos (RBD)

---

## Diccionario de Variables

### Base Geográfica (`geo_rbd.csv`)


| Variable | Descripción | Tipo de Dato |
|----------|-------------|--------------|
| year | Año de registro de los datos | Entero |
| idrbd | Identificador único del establecimiento (RBD) | Entero |
| DGV_RBD | Dígito verificador del RBD | Entero |
| NOM_RBD | Nombre oficial del establecimiento | Texto |
| MRUN | RUN del representante legal | Decimal |
| RUT_SOSTENEDOR | RUT del sostenedor del establecimiento | Decimal |
| P_JURIDICA | Código de personalidad jurídica | Entero |
| COD_REG_RBD | Código de región | Entero |
| COD_PRO_RBD | Código de provincia | Entero |
| COD_COM_RBD | Código de comuna | Entero |
| NOM_COM_RBD | Nombre de la comuna | Texto |
| COD_DEPROV_RBD | Código de dependencia provincial | Entero |
| NOM_DEPROV_RBD | Nombre de dependencia provincial | Texto |
| COD_DEPE | Código de dependencia administrativa | Entero |
| COD_DEPE2 | Código de dependencia administrativa (2) | Entero |
| RURAL_RBD | Indicador área rural (1) o urbana (0) | Entero |
| LATITUD | Coordenada de latitud del establecimiento | Texto |
| LONGITUD | Coordenada de longitud del establecimiento | Texto |
| CONVENIO_PIE | Indicador de convenio PIE (Programa Integración Escolar). Sí (1) , No (0)| Entero |
| ENS_01 | Imparte educación preescolar | Entero |
| ENS_02 | Imparte educación básica (1° a 6° básico) | Entero |
| ENS_03 | Imparte educación básica (7° y 8° básico) | Entero |
| ENS_04 | Imparte educación media científico-humanista | Entero |
| ENS_05 | Imparte educación media técnico-profesional | Entero |
| ENS_06 | Imparte educación especial | Entero |
| ENS_07 | Imparte educación de adultos | Entero |
| ENS_08 | Imparte educación superior | Entero |
| ENS_09 | Imparte otros niveles educativos | Entero |
| MATRICULA | Matrícula total del establecimiento | Entero |
| ESTADO_ESTAB | Estado del establecimiento (activo/inactivo) | Entero |
| ORI_RELIGIOSA | Indicador de orientación religiosa. Otra (7)| Entero |
| ORI_OTRO_GLOSA | Descripción de otra orientación | Texto |
| PAGO_MATRICULA | Rango de costo de matrícula | Texto |
| PAGO_MENSUAL | Rango de costo de mensualidad | Texto |

## Códigos de Referencia

### Dependencia Administrativa (COD_DEPE)
- 1: Municipal
- 2: Particular Subvencionado  
- 3: Particular Pagado
- 4: Corporación de Administración Delegada

### Niveles Educativos (ENS_XX)
**Pendiente su significado. Números poco comunes.**

## Notas Metodológicas
- RBD: Rol Base de Datos del establecimiento educacional
- PIE: Programa de Integración Escolar para estudiantes con NEE

