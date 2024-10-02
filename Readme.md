Proyecto de Extracción de Texto y Corrección con Machine Learning
Este proyecto es una API que permite extraer texto de archivos PDF utilizando OCR y luego aplicar técnicas de machine learning para corregir automáticamente errores comunes en el texto extraído. El objetivo principal es procesar grandes cantidades de documentos y generar un JSON estructurado con la información extraída y corregida.

Tabla de Contenidos
Características
Tecnologías Utilizadas
Requisitos Previos
Instalación
Estructura del Proyecto
Uso
Configuraciones Adicionales
Despliegue
Contribución
Licencia
Características
Extracción de texto de PDFs: Usa PyMuPDF (fitz) para extraer texto directamente de documentos PDF. En caso de que la extracción no sea suficiente, se utiliza OCR con Tesseract.

Corrección automática: Aplica técnicas de NLP y machine learning para corregir errores comunes en las palabras extraídas, como faltas de tildes, errores ortográficos o caracteres mal interpretados.

Clasificación de documentos: Clasifica los documentos PDF basándose en el nombre del archivo.
Generación de JSON: Al final del proceso, se genera un archivo JSON estructurado que contiene el texto corregido y los metadatos de los documentos procesados.

Tecnologías Utilizadas
Python 3.8+
Flask: Para la API.
Tesseract OCR: Para reconocimiento óptico de caracteres en imágenes.
PyMuPDF (fitz): Para la extracción de texto de PDFs.
OpenCV: Para el preprocesamiento de imágenes.
spaCy: Para el procesamiento del lenguaje natural (NLP).
pdf2image: Para la conversión de PDFs a imágenes.
Pillow (PIL): Para el manejo de imágenes.
Typer: Para la CLI (opcional si en el futuro el proyecto tiene una CLI).
Requisitos Previos
Tener lo siguiente instalado:

Python 3.8+
Tesseract OCR:
configurar la variable de entorno TESSERACT_CMD.
Poppler (para pdf2image):



para instalar el proyecto:

Clona el repositorio:


git clone https://github.com/ (Pendiente versionar)
cd (donde se va a copiar)
Instala las dependencias:


pip install -r requirements.txt
Configura Tesseract:

configura la variable TESSERACT_CMD con la ruta de instalación de Tesseract. Ejemplo:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
Instala el modelo de idioma español de spaCy:

python -m spacy download es_core_news_md
Estructura del Proyecto base

├── app.py                     # Archivo principal de Flask para la API
├── ml_correction.py           # Módulo que aplica correcciones basadas en NLP
├── extract.py                 # Módulo para extraer texto y procesar PDFs
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Documentación del proyecto
Detalles Clave:
app.py: El archivo principal que ejecuta la API con Flask.
ml_correction.py: Contiene las funciones de corrección automática usando técnicas de NLP, como la similaridad entre palabras.
extract.py: Maneja la extracción de texto de PDFs, utilizando OCR si es necesario, y llama a las funciones de corrección.
config.py: Archivo opcional para configurar rutas, ajustes de OCR, etc.
Uso
1. Ejecutar el servidor Flask
Para iniciar la API,se ejecuta el siguiente comando:

python app.py
Esto ejecutará el servidor de Flask, que estará disponible en la ruta http://localhost:5000.

2. Solicitudes a la API
Endpoint para Procesar PDFs
URL: /process
Método: POST
Descripción: Envía la ruta de un directorio local con los PDFs a procesar.
Body: Un JSON con la ruta del directorio y la cantidad de archivos a procesar.
json

{
  "ruta": "C:/ruta/a/los/archivos",

}
Respuesta: Un JSON con los datos extraídos y corregidos de los archivos PDF procesados.
Ejemplo de Respuesta
json

[
  {
    "nombre_archivo": "Documento1.pdf",
    "texto_extraido": "Este es el texto extraído y corregido del PDF.",
    "tipo_documento": "Tutela",
    "providencia": "T-123456",
    "ano": 2023
  },
  ...
]
3. Preprocesamiento de Imágenes
El preprocesamiento de las imágenes de los PDF incluye:

Conversión a escala de grises.
Aplicación de umbral adaptativo.
Dilatación y erosión para mejorar la calidad del texto extraído con OCR.
4. Correcciones Automáticas
El sistema aplica técnicas de machine learning para corregir errores de tildes, palabras mal escritas, y otros problemas comunes en textos extraídos de PDFs.

Configuraciones Adicionales
Ajustar el Umbral de OCR
Se puede modificar los parámetros de OCR para mejorar la precisión en ciertos tipos de documentos modificando la línea:

python
text = pytesseract.image_to_string(preprocessed_image, lang='spa', config='--psm 6 --oem 3')
Cambia el valor de --psm para ajustar el modo de segmentación de la página de Tesseract.

Añadir Nuevas Palabras para Corrección
En el archivo ml_correction.py, se pueden añadir más palabras clave comunes a la lista palabras_comunes para mejorar las correcciones automáticas.

