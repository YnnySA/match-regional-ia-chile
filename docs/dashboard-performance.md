# Verificación de rendimiento del dashboard

Medición local sobre Windows, Python 3.12.9, artefactos procesados existentes
y sin descargas externas:

| Medición | Resultado | Objetivo |
|---|---:|---:|
| Carga validada de `match_regional` | 0.0622 s | <= 3 s |
| Artefactos CSV consumidos | 953,723 bytes | <= 26,214,400 bytes |
| Endpoint de salud Streamlit | `ok` | aplicación disponible |

El cambio de filtro opera sobre el `DataFrame` validado en memoria. Los
artefactos se cargan bajo demanda y la clave de caché incluye tamaño y mtime,
por lo que un rerun sin cambios no relee el archivo. La medición de interfaz
de 500 ms debe repetirse en el entorno de despliegue objetivo.
