# Especificación y Prompt de Agente: Tarea #8 (Marian)

## Metadatos de la Tarea
- **Responsable:** Marian
- **Rama Git:** `marian/tarea-configurar-entorno-y-estructura-del-proyecto`
- **Issue GitHub:** `#8` (`[Tarea] Configurar entorno y estructura del proyecto. Carga y estandarización de titulados`)
- **Historia de Usuario:** `[User_01] Caracterización territorial de la oferta de titulados con gratuidad (#1)`
- **Fecha Límite Sugerida:** 11/10/2026

---

## Prompt para Copiar y Pegar en el Agente de Marian (Cursor / Claude / Copilot)

```markdown
Eres un asistente de ingeniería de datos y software en Python. Estamos trabajando en el proyecto "Match-IA Regional" (repositorio TECH-MACI/2026-G03).
Tu objetivo es implementar la **Tarea #8** del Sprint 1 en la rama actual: `marian/tarea-configurar-entorno-y-estructura-del-proyecto`.

### 1. Contexto y Restricciones
- Debes entregar la estructura base del proyecto y las Secciones 0 a 3 del notebook único `notebooks/sprint1_match_ia_regional.ipynb`.
- **REGLA CRÍTICA DE GIT:** El archivo `data/oferta/Titulados-Ed-Superior-2025/20260817_Titulados_Ed_Superior_2025_WEB.csv` pesa 188 MB y NO debe subirse a GitHub (límite de 100 MB). Asegúrate de que `.gitignore` ignore `data/oferta/Titulados-Ed-Superior-2025/` y no hagas stage de ningún archivo de más de 10 MB. El archivo versionado es `data/oferta/Titulados-Ed-Superior-2025.rar` (7.6 MB).
- Toda ruta en el código debe ser relativa usando `pathlib.Path` respecto al directorio del notebook (`../data`).

### 2. Entregables Requeridos

#### A. Estructura de Directorios
Crea los siguientes directorios si no existen, con un archivo `.gitkeep` en su interior:
- `notebooks/`
- `data/processed/`
- `src/`
- `docs/`

#### B. Archivo `requirements.txt`
Crea `requirements.txt` en la raíz con las dependencias del proyecto:
```text
pandas>=2.2.0
numpy>=1.26.0
matplotlib>=3.8.0
seaborn>=0.13.0
geopandas>=0.14.0
pyogrio>=0.7.0
openpyxl>=3.1.0
jupyter>=1.0.0
nbstripout>=0.7.0
```

#### C. Datos de Instituciones Adscritas a Gratuidad 2025
Crea el archivo `data/oferta/instituciones_gratuidad_2025.csv` con codificación UTF-8 y separador `;`. 
Debe incluir las columnas: `cod_inst;nomb_inst;tipo_inst;adscrita_gratuidad;fuente`
Incluye las instituciones oficiales adscritas a gratuidad en Chile (Mineduc / beneficiosestudiantiles.cl):
- Universidades CRUCH (ej: Universidad de Chile, PUC, USACH, UdeC, UV, PUCV, UFRO, etc.)
- Universidades Privadas con Gratuidad (ej: U. Diego Portales, U. Alberto Hurtado, U. Finis Terrae, U. Silva Henríquez, etc.)
- Institutos Profesionales y CFTs con Gratuidad (ej: DUOC UC, INACAP IP, INACAP CFT, CFTs Estatales).
Coloca `adscrita_gratuidad = 1` y `fuente = "Mineduc 2025"`.

#### D. Notebook Base: `notebooks/sprint1_match_ia_regional.ipynb`
Crea un Jupyter Notebook estructurado con las siguientes secciones:

- **Sección 0: Setup y Rutas (Funcional)**
  - Configuración de `pathlib.Path`.
  - Rutas a `data/oferta/`, `data/geo/`, `data/demanda/`, `data/processed/`.
  - Mecanismo de descompresión automática: si el CSV `20260817_Titulados_Ed_Superior_2025_WEB.csv` no existe en disco, descomprimirlo desde `data/oferta/Titulados-Ed-Superior-2025.rar` (usando `tar -xf` o avisando al usuario).

- **Sección 1: Carga y Diagnóstico de Titulados (Funcional)**
  - Lectura optimizada del CSV usando `pd.read_csv` con `sep=";"`, `encoding="latin-1"`.
  - Cargar únicamente las columnas útiles para no saturar memoria: `mrun`, `gen_alu`, `fec_nac_alu`, `anio_ing_carr_ori`, `sem_ing_carr_ori`, `anio_tit`, `mes_tit`, `cod_inst`, `nomb_inst`, `tipo_inst_1`, `cod_sede`, `nomb_sede`, `cod_carrera`, `nomb_carrera`, `nivel_global`, `nivel_carrera_1`, `cine_f_13_area`, `cine_f_13_subarea`, `region_sede`.
  - Reporte de dimensiones (filas y columnas), tipos de datos y % de nulos.
  - Validación de duplicados por `mrun` + `cod_carrera` + `anio_tit`.

- **Sección 2: Limpieza, Estandarización y Gratuidad (Funcional)**
  - Limpieza de textos y espacios en nombres de instituciones y carreras.
  - Estandarización de `region_sede` a las **16 regiones oficiales de Chile** con orden geográfico Norte a Sur (1 Arica y Parinacota ... 16 Magallanes y de la Antártica Chilena).
  - Creación de variable booleana `area_afin_ia`: marcar True si `cine_f_13_area` pertenece a:
    - "Tecnología de la Información y la Comunicación (TIC)"
    - "Ingeniería, Industria y Construcción"
    - "Ciencias Naturales, Matemáticas y Estadística"
  - Cruce (Merge) con `instituciones_gratuidad_2025.csv` mediante `cod_inst` para crear la bandera `inst_gratuidad` (1 = Adscrita, 0 = No Adscrita).
  - Verificación de consistencia del cruce y reporte de instituciones sin calce.

- **Sección 3: Lectura Geográfica de Sedes (Funcional)**
  - Lectura del Shapefile directamente desde el zip `data/geo/layer_establecimientos_de_educacion_superior_20220309024111(1).zip` usando `geopandas.read_file("zip://...")`.
  - Verificación y reproyección a CRS WGS84 (`EPSG:4326`).
  - Conteo de sedes por región y validación con los datos de oferta.

- **Secciones 4 a 9 (Celdas Marcadoras / Placeholders para Tareas #9, #10 y #11)**
  - Dejar celdas Markdown claras con los encabezados:
    - `## Sección 4: Cálculo de Indicadores de Oferta (Tarea #9 - Nicolás)`
    - `## Sección 5: Visualizaciones y EDA de Oferta (Tarea #9 - Nicolás)`
    - `## Sección 6: Ingesta de Datos de Demanda y Exposición a IA (Tarea #10 - Camila)`
    - `## Sección 7: Cálculo de Indicadores de Demanda (Tarea #11 - Marcelo)`
    - `## Sección 8: Matriz y Cuadrantes Match-IA (Tarea #11 - Marcelo)`
    - `## Sección 9: Ficha Metodológica y Exportación (Tarea #11 - Marcelo)`

### 3. Criterios de Aceptación (Definition of Done)
1. El notebook se ejecuta sin errores de principio a fin en las Secciones 0 a 3.
2. `git status` no muestra el CSV de 188 MB como archivo para commit.
3. Al finalizar, hacer commit con el mensaje exacto:
   `git commit -m "feat(setup): configurar estructura del proyecto y carga estandarizada de titulados (closes #8)"`
4. Hacer push a la rama remota:
   `git push origin marian/tarea-configurar-entorno-y-estructura-del-proyecto`
```
