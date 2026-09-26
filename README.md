# Detección de Sitios Web de Phishing con Machine Learning

Este proyecto utiliza técnicas de **Machine Learning** y **Web Scraping** para detectar sitios web de phishing basándose exclusivamente en su contenido HTML (características binarias y cuantitativas), sin analizar la URL. Incluye una interfaz gráfica interactiva construida con **Streamlit**.

**Demo en vivo:** [https://phishing-detection-ml-jdcxureaduuvko7fhd6cky.streamlit.app/](https://phishing-detection-ml-jdcxureaduuvko7fhd6cky.streamlit.app/)

---

## Requisitos Previos

* **Python:** 3.8 o superior.
* **Conexión a internet:** Necesaria para la descarga de datasets y la evaluación de URLs en tiempo real.

---

## 1. Instalación y Configuración

Sigue estos pasos en tu terminal para preparar el entorno de desarrollo:

1. **Clonar o descargar el proyecto:**
   ```bash
   cd tu-carpeta-del-proyecto
   ```

2. **Crear el entorno virtual:**
   * **Windows:**
     ```cmd
     python -m venv venv
     ```
   * **Linux / Mac:**
     ```bash
     python3 -m venv venv
     ```

3. **Activar el entorno virtual:**
   * **Windows:**
     ```cmd
     venv\Scripts\activate
     ```
   * **Linux / Mac:**
     ```bash
     source venv/bin/activate
     ```

4. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 2. Preparación de los Datos (Datasets)

Antes de ejecutar los scripts, necesitas descargar las listas de URLs que alimentarán los modelos:

* **URLs Legítimas:** 
  1. Descarga la lista desde [Tranco List](https://tranco-list.eu).
  2. Descomprime el archivo, renómbralo a `top-1m.csv` y colócalo en la raíz del proyecto.
  3. **Nota importante:** Abre el archivo y añade la palabra `url` en la primera línea como encabezado.
* **URLs de Phishing:** 
  1. Descarga la lista desde el portal de desarrolladores de [Phishtank](https://phishtank.org/phisharchive.php).
  2. Guarda el archivo CSV como `verified_online.csv` en la raíz del proyecto.

---

## 3. Flujo de Ejecución

Una vez que tengas el entorno activo y los datos en la carpeta, sigue este orden de ejecución:

### Paso A: Recolección de Datos (`data_collector.py`)
Extrae las características HTML de las URLs para generar los datasets estructurados.

1. **Procesar sitios legítimos:** Ejecuta el recolector con la configuración por defecto para sitios legítimos:
   ```bash
   python data_collector.py
   ```
   > Esto generará el archivo `structured_data_legitimate.csv`.

2. **Procesar sitios de phishing:** Abre el archivo `data_collector.py`, comenta las variables bajo `"SITIOS LEGÍTIMOS"` y descomenta las variables bajo `"SITIOS PHISHING"`. Luego, vuelve a ejecutar el script:
   ```bash
   python data_collector.py
   ```
   > Esto generará el archivo `structured_data_phishing.csv`.

### Paso B: Entrenamiento y Evaluación (`machine_learning.py`)
*(Opcional)* Si deseas ver el rendimiento (**Exactitud**, **Precisión**, **Recall**) de los 7 modelos de Machine Learning mediante validación cruzada directamente en la consola, ejecuta:
```bash
python machine_learning.py
```

### Paso C: Lanzamiento de la Interfaz Web Local (`app.py`)
Para probar la aplicación final de manera visual e interactiva con URLs en tiempo real:
```bash
streamlit run app.py
```
Tu navegador se abrirá automáticamente en `http://localhost:8501`.

---

## 4. Despliegue

La aplicación se encuentra desplegada en la nube y se puede consultar en tiempo real sin necesidad de ejecutar el código localmente:

* **URL del Despliegue:** [https://phishing-detection-ml-jdcxureaduuvko7fhd6cky.streamlit.app/](https://phishing-detection-ml-jdcxureaduuvko7fhd6cky.streamlit.app/)

---

## Estructura del Proyecto

* **`features.py`**: Funciones base para extracción de características del HTML.
* **`feature_extraction.py`**: Módulo para vectorizar el HTML en base a las características extraídas.
* **`data_collector.py`**: Script para hacer scraping y generar los datasets estructurados (`.csv`).
* **`machine_learning.py`**: Lógica de entrenamiento, validación cruzada y evaluación de los 7 modelos.
* **`app.py`**: Interfaz de usuario interactiva construida con Streamlit.
* **`requirements.txt`**: Lista con todas las librerías necesarias para el proyecto.
