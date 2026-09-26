Detección de Sitios Web de Phishing con Machine Learning

Este proyecto utiliza técnicas de Machine Learning y Web Scraping para detectar sitios web de phishing basándose únicamente en el contenido HTML (características binarias y cuantitativas), sin analizar la URL. Incluye una interfaz gráfica interactiva construida con Streamlit.

Requisitos Previos

Python 3.8 o superior.

Conexión a internet para la descarga de datasets y evaluación de URLs en tiempo real.

1. Instalación y Configuración

Sigue estos pasos en tu terminal para preparar el entorno de desarrollo:

Clona o descarga el proyecto y navega hasta la carpeta raíz:

cd tu-carpeta-del-proyecto


Crea un entorno virtual:

En Windows: python -m venv venv

En Linux/Mac: python3 -m venv venv

Activa el entorno virtual:

En Windows: venv\Scripts\activate

En Linux/Mac: source venv/bin/activate

Instala las dependencias usando el archivo de requerimientos:

pip install -r requirements.txt


2. Preparación de los Datos (Datasets)

Antes de ejecutar los scripts, necesitas descargar las listas de URLs que alimentarán el modelo:

URLs Legítimas: Descarga la lista desde Tranco List. Descomprime el archivo, renómbralo como top-1m.csv y colócalo en la raíz del proyecto. Nota: Abre el archivo y añade la palabra url en la primera línea como cabecera.

URLs de Phishing: Descarga la lista de URLs maliciosas desde el portal de desarrolladores de Phishtank. Guarda el archivo CSV como verified_online.csv en la raíz del proyecto.

3. Flujo de Ejecución

Una vez que tengas el entorno activo y los datos en la carpeta, sigue este orden estricto:

Paso A: Recolección de Datos

Extrae las características HTML de las URLs para generar los datasets estructurados.

Procesar sitios legítimos: Ejecuta el recolector con la configuración por defecto para sitios legítimos.

python data_collector.py


(Esto generará el archivo structured_data_legitimate.csv)

Procesar sitios de phishing: Abre el archivo data_collector.py, comenta las variables bajo "SITIOS LEGÍTIMOS" y descomenta las variables bajo "SITIOS PHISHING". Luego, vuelve a ejecutar el script:

python data_collector.py


(Esto generará el archivo structured_data_phishing.csv)

Paso B: (Opcional) Entrenamiento y Evaluación de Modelos

Si deseas ver el rendimiento (Exactitud, Precisión, Recall) de los 7 modelos de Machine Learning mediante validación cruzada directamente en la consola, ejecuta:

python machine_learning.py


Paso C: Lanzamiento de la Interfaz Web

Para probar la aplicación final de manera visual e interactiva con URLs en tiempo real, lanza Streamlit:

streamlit run app.py


Tu navegador se abrirá automáticamente en http://localhost:8501.

Estructura del Proyecto

features.py: Funciones base para extracción de características del HTML.

feature_extraction.py: Módulo para vectorizar el HTML en base a las características.

data_collector.py: Script para hacer scraping y generar los datasets estructurados.

machine_learning.py: Lógica de entrenamiento y evaluación de modelos.

app.py: Interfaz de usuario construida con Streamlit.

requirements.txt: Lista de dependencias del proyecto.