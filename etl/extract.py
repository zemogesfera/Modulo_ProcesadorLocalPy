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

# Configurar la ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image):
    """
    Aplica preprocesamiento avanzado a la imagen para mejorar la extracción de texto con OCR.
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
    """
    Clasifica el tipo de documento según su nombre.
    """
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

def extraer_campos_clave(texto):
    """
    Extrae los campos clave específicos del texto extraído.
    """
    def buscar_patron(patron, texto, max_length=50):
        match = re.search(patron, texto, re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1).strip()[:max_length]
        return None

    campos = {
        "ciudad_juzgado": buscar_patron(r"CIUDAD\s*:\s*(\w+(?:\s*\w+)*)", texto),
        "departamento_juzgado": buscar_patron(r"DEPARTAMENTO\s*:\s*(\w+(?:\s*\w+)*)", texto),
        "fecha_emision_auto": buscar_patron(r"FECHA\s+DE\s+EMISI[ÓO]N\s+DEL\s+AUTO\s+ADMISORIO\s*:\s*([\d\/\-]+)", texto),
        "fecha_vencimiento_auto": buscar_patron(r"FECHA\s+DE\s+VENCIMIENTO\s+DEL\s+AUTO\s+ADMISORIO\s*:\s*([\d\/\-]+)", texto),
        "nombre_juzgado": buscar_patron(r"JUZGADO\s+(?:DE\s+|DEL\s+)?(?:[\w\s]+):\s*([\w\s]+)", texto),
        "numero_radicado": buscar_patron(r"RADICACI[ÓO]N\s*(?:No\.?|N[úu]mero)?\s*([-\d]+)", texto, max_length=50),
        "ano_radicado": buscar_patron(r"RADICADO\s*:\s*([\d]{4})", texto),
        "codigo_proceso": buscar_patron(r"C[ÓO]DIGO\s+DEL\s+PROCESO\s*:\s*(\w+)", texto),
        "recurso_proceso": buscar_patron(r"RECURSO\s+DEL\s+PROCESO\s*:\s*(\w+)", texto),
        "tipo_documento_accionante": buscar_patron(r"(?:TIPO\s+DE\s+)?DOCUMENTO\s+ACCIONANTE\s*:\s*(\w+)", texto),
        "numero_documento_accionante": buscar_patron(r"NÚMERO\s+DE\s+DOCUMENTO\s+ACCIONANTE\s*:\s*(\d+)", texto),
        "clasificacion_peticion": buscar_patron(r"(ÁREAS\s+TÉCNICAS|ADMINISTRATIVAS|MEDICINA\s+DEL\s+TRABAJO|SALUD|SALUD\s+ODONTOLÓGICA)", texto)
    }

    # Formatear el número de radicado para eliminar guiones
    if campos["numero_radicado"]:
        campos["numero_radicado"] = campos["numero_radicado"].replace("-", "")

    return campos

def extract_data(ruta_archivos: str, cantidad: int = None, upscale=False):
    """
    Procesa los archivos de la ruta especificada y extrae campos clave.
    """
    resultado = []
    archivos = [f for f in os.listdir(ruta_archivos) if f.lower().endswith(('.pdf', '.jpg', '.png', '.docx'))][:cantidad]
    
    for archivo in archivos:
        full_path = os.path.join(ruta_archivos, archivo)
        print(f"Procesando archivo: {full_path}")

        # Proceso OCR según el tipo de archivo
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
            print(f"Tipo de archivo no soportado: {archivo}")
            continue

        # Extraer los campos clave
        campos_extraidos = extraer_campos_clave(texto_extraido)
        
        datos_documento = {
            "nombre_archivo": archivo,
            "ciudad_juzgado": campos_extraidos.get("ciudad_juzgado"),
            "departamento_juzgado": campos_extraidos.get("departamento_juzgado"),
            "fecha_emision_auto": campos_extraidos.get("fecha_emision_auto"),
            "fecha_vencimiento_auto": campos_extraidos.get("fecha_vencimiento_auto"),
            "nombre_juzgado": campos_extraidos.get("nombre_juzgado"),
            "numero_radicado": campos_extraidos.get("numero_radicado"),
            "ano_radicado": campos_extraidos.get("ano_radicado"),
            "codigo_proceso": campos_extraidos.get("codigo_proceso"),
            "recurso_proceso": campos_extraidos.get("recurso_proceso"),
            "tipo_documento_accionante": campos_extraidos.get("tipo_documento_accionante"),
            "numero_documento_accionante": campos_extraidos.get("numero_documento_accionante"),
            "clasificacion_peticion": campos_extraidos.get("clasificacion_peticion")
        }
        
        print(f"Campos extraídos para {archivo}: {datos_documento}")
        resultado.append(datos_documento)

    return resultado