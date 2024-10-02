import fitz  # PyMuPDF
import unicodedata
import re
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import cv2
import numpy as np
import os
import logging
from .ml_correction import aplicar_correcciones

# Configurar logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configurar la ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image):
    """
    Aplica preprocesamiento a la imagen para mejorar la extracción de texto con OCR.
    """
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 2)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(thresh, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    return Image.fromarray(img)

def extract_text(pdf_file: str) -> str:
    """
    Extrae texto de un archivo PDF, primero intenta con texto directo luego con OCR.
    """
    extracted_text = ""
    logger.info(f"Iniciando extracción de texto para {pdf_file}")
    
    try:
        with fitz.open(pdf_file) as pdf_document:
            for page_num, page in enumerate(pdf_document):
                page_text = page.get_text()
                extracted_text += page_text
                logger.debug(f"Página {page_num + 1}: Extraídos {len(page_text)} caracteres")
    except Exception as e:
        logger.error(f"Error extrayendo texto del PDF: {e}", exc_info=True)
    
    # Si el texto extraído es insuficiente, usar OCR
    if len(extracted_text.strip()) < 100:
        logger.info(f"Texto insuficiente extraído directamente. Intentando OCR.")
        try:
            images = convert_from_path(pdf_file, dpi=400)
            logger.info(f"Convertidas {len(images)} páginas a imágenes")
            for i, image in enumerate(images):
                preprocessed_image = preprocess_image(image)
                text = pytesseract.image_to_string(preprocessed_image, lang='spa', config='--psm 6 --oem 3')
                extracted_text += text + "\n"
                logger.debug(f"Página {i + 1}: OCR completado. Extraídos {len(text)} caracteres")
        except Exception as e:
            logger.error(f"Error extrayendo texto de imágenes: {e}", exc_info=True)
    
    # Normalizar y limpiar el texto
    extracted_text = unicodedata.normalize('NFKD', extracted_text)
    extracted_text = re.sub(r'[^\w\s.,;:!¡?¿()áéíóúÁÉÍÓÚñÑüÜ@-]', '', extracted_text)
    extracted_text = ' '.join(extracted_text.split())
    
    logger.info(f"Extracción de texto completada. Total de caracteres: {len(extracted_text)}")

    # Aplicar correcciones con el modelo de machine learning
    extracted_text = aplicar_correcciones(extracted_text)
    
    return extracted_text.strip()

def clasificar_documento(nombre_archivo):
    nombre = nombre_archivo.upper()
    if "T" in nombre:
        tipo = "Tutela"
    elif "C" in nombre:
        tipo = "Constitucionalidad"
    elif "A" in nombre:
        tipo = "Auto"
    else:
        tipo = "Sin identificar"
    
    providencia = nombre.replace(".PDF", "")
    
    try:
        ano = int(nombre.split("-")[-1][:2]) + 2000
    except ValueError:
        ano = None
    
    return tipo, providencia, ano

def extract_data(ruta_pdf: str, cantidad: int):
    resultado = []
    pdf_files = [f for f in os.listdir(ruta_pdf) if f.lower().endswith('.pdf')][:cantidad]
    
    for pdf_file in pdf_files:
        full_path = os.path.join(ruta_pdf, pdf_file)
        logger.info(f"Procesando archivo: {full_path}")
        texto_extraido = extract_text(full_path)
        
        tipo_documento, providencia, ano = clasificar_documento(pdf_file)
        
        resultado.append({
            "nombre_archivo": pdf_file,
            "texto_extraido": texto_extraido,
            "tipo_documento": tipo_documento,
            "providencia": providencia,
            "ano": ano
        })
        
        logger.info(f"Archivo procesado: {pdf_file}")
    
    return resultado
