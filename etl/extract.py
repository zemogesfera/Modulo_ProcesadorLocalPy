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
from docx import Document
from .ml_correction import aplicar_correcciones

# Configurar logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Configurar la ruta de Tesseract (ajusta según tu instalación)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image):
    """
    Aplica preprocesamientos avanzados a la imagen para mejorar la extracción de texto con OCR.
    """
    if isinstance(image, np.ndarray):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray)
    thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return Image.fromarray(img)

def upscale_image(image, scale_percent=150):
    """
    Opción para aumentar la resolución de la imagen.
    """
    width = int(image.width * scale_percent / 100)
    height = int(image.height * scale_percent / 100)
    return image.resize((width, height), Image.LANCZOS)

def extract_text_from_pdf(pdf_file: str, upscale=False) -> str:
    """
    Extrae texto de un archivo PDF. Primero intenta con texto directo, luego con OCR mejorado si es necesario.
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
    
    # Siempre aplicar OCR a la primera página para capturar el número de radicación
    try:
        images = convert_from_path(pdf_file, first_page=1, last_page=1, dpi=300)
        for image in images:
            if upscale:
                image = upscale_image(image)
            preprocessed_image = preprocess_image(image)
            text = pytesseract.image_to_string(preprocessed_image, lang='spa', config='--psm 6 --oem 3')
            extracted_text = text + "\n" + extracted_text  # Agregar al principio
    except Exception as e:
        logger.error(f"Error aplicando OCR a la primera página: {e}", exc_info=True)
    
    # Si aún no hay suficiente texto, aplicar OCR a todas las páginas
    if len(extracted_text.strip()) < 100:
        logger.info(f"Texto insuficiente extraído directamente. Aplicando OCR a todas las páginas.")
        try:
            images = convert_from_path(pdf_file, dpi=300)
            for i, image in enumerate(images):
                if upscale:
                    image = upscale_image(image)
                preprocessed_image = preprocess_image(image)
                text = pytesseract.image_to_string(preprocessed_image, lang='spa', config='--psm 6 --oem 3')
                extracted_text += text + "\n"
                logger.debug(f"Página {i + 1}: OCR mejorado completado. Extraídos {len(text)} caracteres")
        except Exception as e:
            logger.error(f"Error extrayendo texto de imágenes: {e}", exc_info=True)
    
    extracted_text = post_process_text(extracted_text)
    
    logger.info(f"Extracción de texto completada. Total de caracteres: {len(extracted_text)}")
    
    return extracted_text.strip()

def post_process_text(text):
    """
    Aplica correcciones específicas y limpieza al texto extraído.
    """
    text = re.sub(r'\s+', ' ', text)
    text = unicodedata.normalize('NFKD', text)
    text = re.sub(r'[^\w\s.,;:!¡?¿()áéíóúÁÉÍÓÚñÑüÜ@-]', '', text)
    text = aplicar_correcciones(text)
    return text.strip()

def extract_text_from_docx(docx_file: str) -> str:
    """
    Extrae texto de un archivo .docx (Word).
    """
    extracted_text = ""
    logger.info(f"Iniciando extracción de texto para {docx_file}")

    try:
        doc = Document(docx_file)
        for para in doc.paragraphs:
            extracted_text += para.text + "\n"
        logger.debug(f"Extraídos {len(extracted_text)} caracteres del archivo Word")
    except Exception as e:
        logger.error(f"Error extrayendo texto de Word: {e}", exc_info=True)
    
    extracted_text = unicodedata.normalize('NFKD', extracted_text)
    extracted_text = re.sub(r'[^\w\s.,;:!¡?¿()áéíóúÁÉÍÓÚñÑüÜ@-]', '', extracted_text)
    extracted_text = ' '.join(extracted_text.split())
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
    
    providencia = nombre.replace(".PDF", "").replace(".DOCX", "")
    
    try:
        ano = int(nombre.split("-")[-1][:2]) + 2000
    except ValueError:
        ano = None
    
    return tipo, providencia, ano

def extract_data(ruta_archivos: str, cantidad: int = None, upscale=False):
    """
    Procesa los archivos de la ruta especificada y extrae campos clave.
    """
    resultado = []
    archivos = [f for f in os.listdir(ruta_archivos) if f.lower().endswith(('.pdf', '.jpg', '.png', '.docx'))][:cantidad]
    
    for archivo in archivos:
        full_path = os.path.join(ruta_archivos, archivo)
        logger.info(f"Procesando archivo: {full_path}")

        if archivo.lower().endswith('.pdf'):
            texto_extraido = extract_text_from_pdf(full_path, upscale)
        elif archivo.lower().endswith(('.jpg', '.png')):
            image = Image.open(full_path)
            if upscale:
                image = upscale_image(image)
            preprocessed_image = preprocess_image(image)
            texto_extraido = pytesseract.image_to_string(preprocessed_image, lang='spa', config='--psm 6 --oem 3')
        elif archivo.lower().endswith('.docx'):
            texto_extraido = extract_text_from_docx(full_path)
        else:
            texto_extraido = ""

        # Extraer los campos clave
        campos_clave = extraer_campos_clave(texto_extraido)
        
        tipo_documento, providencia, ano = clasificar_documento(archivo)
        
        resultado.append({
            "nombre_archivo": archivo,
            "juzgado": campos_clave.get("juzgado"),
            "tipo_documento": tipo_documento,
            "tiempo_respuesta": campos_clave.get("tiempo_respuesta"),
            "ciudad_juzgado": campos_clave.get("ciudad"),
            "departamento_juzgado": campos_clave.get("departamento"),
            "numero_radicado": campos_clave.get("numero_radicado"),
            "ano": ano
        })
        
        logger.info(f"Archivo procesado: {archivo}")
    
    return resultado

def buscar_patron(patron, texto):
    """
    Busca un patrón regex en el texto y devuelve el resultado si lo encuentra.
    """
    match = re.search(patron, texto, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extraer_campos_clave(texto):
    """
    Extrae los campos clave específicos del texto extraído, limitando la longitud de los resultados.
    """
    def buscar_patron(patron, texto, max_length=30):
        match = re.search(patron, texto, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()[:max_length]
        return None

    campos = {
        "juzgado": buscar_patron(r"JUZGADO\s+(\w+(?:\s+\w+)?)", texto),
        "tiempo_respuesta": buscar_patron(r"(dentro\s*de\s*(\d+)\s*(horas|días|meses))", texto),
        "ciudad_juzgado": buscar_patron(r"SECCIONAL\s+(\w+)", texto) or buscar_patron(r"(\w+),\s*Valle", texto),
        "departamento_juzgado": buscar_patron(r"DEPARTAMENTO:\s*(\d+)", texto),
        "numero_radicado": buscar_patron(r"RADICACI[OÓ]N\s*(?:No\.?|N[úu]mero)?\s*([-\d]+)", texto, max_length=50)
    }
    
    # Si se encuentra el radicado con guiones, lo reformateamos sin guiones
    if campos["numero_radicado"]:
        campos["numero_radicado"] = campos["numero_radicado"].replace("-", "")
    
    return campos

def clasificar_documento(nombre_archivo):
    nombre = nombre_archivo.upper()
    if "DEMANDA" in nombre or "ANEXOS" in nombre:
        tipo = "Auto"
    elif "T" in nombre:
        tipo = "Tutela"
    elif "C" in nombre:
        tipo = "Constitucionalidad"
    elif "A" in nombre:
        tipo = "Auto"
    else:
        tipo = "Sin identificar"
    
    try:
        ano = int(re.search(r'(\d{2})(?:Demanda|Anexos)', nombre).group(1)) + 2000
    except AttributeError:
        ano = None
    
    return tipo, None, ano

def extract_data(ruta_archivos: str, cantidad: int = None, upscale=False):
    """
    Procesa los archivos de la ruta especificada y extrae campos clave.
    """
    resultado = []
    archivos = [f for f in os.listdir(ruta_archivos) if f.lower().endswith(('.pdf', '.jpg', '.png', '.docx'))][:cantidad]
    
    for archivo in archivos:
        full_path = os.path.join(ruta_archivos, archivo)
        logger.info(f"Procesando archivo: {full_path}")

        if archivo.lower().endswith('.pdf'):
            texto_extraido = extract_text_from_pdf(full_path, upscale)
        elif archivo.lower().endswith(('.jpg', '.png')):
            image = Image.open(full_path)
            if upscale:
                image = upscale_image(image)
            preprocessed_image = preprocess_image(image)
            texto_extraido = pytesseract.image_to_string(preprocessed_image, lang='spa', config='--psm 6 --oem 3')
        elif archivo.lower().endswith('.docx'):
            texto_extraido = extract_text_from_docx(full_path)
        else:
            texto_extraido = ""

        # Extraer los campos clave
        campos_clave = extraer_campos_clave(texto_extraido)
        
        tipo_documento, _, ano = clasificar_documento(archivo)
        
        resultado.append({
            "nombre_archivo": archivo,
            "juzgado": campos_clave.get("juzgado"),
            "tipo_documento": tipo_documento,
            "tiempo_respuesta": campos_clave.get("tiempo_respuesta"),
            "ciudad_juzgado": campos_clave.get("ciudad_juzgado"),
            "departamento_juzgado": campos_clave.get("departamento_juzgado"),
            "numero_radicado": campos_clave.get("numero_radicado"),
            "ano": ano
        })
        
        logger.info(f"Archivo procesado: {archivo}")
    
    return resultado