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
from datetime import datetime
import locale
from etl.DocumentoExtractor import DocumentoExtractor
import shutil
from typing import Dict, List, Tuple

# Configurar el registro
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
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
    Extrae texto de un archivo PDF. Primero intenta con texto directo, 
    luego con OCR mejorado si es necesario.
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
        logger.info("Texto insuficiente extraído directamente. Aplicando OCR a todas las páginas.")
        try:
            images = convert_from_path(pdf_file, dpi=300)
            for i, image in enumerate(images):
                if upscale:
                    image = upscale_image(image)
                preprocessed_image = preprocess_image(image)
                text = pytesseract.image_to_string(
                    preprocessed_image,
                    lang='spa',
                    config='--psm 6 --oem 3'
                )
                extracted_text += text + "\n"
                logger.debug(f"Página {i + 1}: OCR mejorado completado. Extraídos {len(text)} caracteres")
        except Exception as e:
            logger.error(f"Error extrayendo texto de imágenes: {e}", exc_info=True)
    
    extracted_text = post_process_text(extracted_text)
    logger.info(f"Extracción de texto completada. Total de caracteres: {len(extracted_text)}")
    return extracted_text.strip()

def post_process_text(text):
    """
    Aplicación de correcciones específicas y limpieza al texto extraído
    """
    text = re.sub(r'\s+', ' ', text)
    text = unicodedata.normalize('NFKD', text)
    text = re.sub(r'[^\w\s.,;:!¡?¿()áéíóúÁÉÍÓÚñÑüÜ@-]', '', text)
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
    return extracted_text.strip()

from typing import List, Tuple, Dict

# Mantener un registro global de etiquetas asignadas
etiquetas_asignadas = {
    'auto_tutela': False,  # Representa '01'
    'juzgado': set(),      # Conjunto para '02', '03', '04'
    'anexos': set()        # Conjunto para '05', '06', '07'
}

def classify_document(campos_extraidos: Dict, texto_extraido: str) -> Tuple[str, str]:
    """
    Clasifica documentos asegurando que cada etiqueta se use solo una vez por caso.
    """
    texto_lower = texto_extraido.lower()
    texto_sin_tildes = normalize_text(texto_lower)
    
    # Patrones de búsqueda según la clasificación requerida
    patrones = {
        'auto_tutela': {
            'principales': [
                'auto omisorio', 'auto admisorio', 'admision tutela', 
                'admitir la accion', 'accion de tutela', 'auto de sustanciacion',
                'admitese la presente accion', 'resuelve admitir'
            ],
            'secundarios': ['tutela', 'amparo constitucional', 'derecho fundamental', 'accionante', 'accionado']
        },
        'juzgado': {
            'principales': [
                'juzgado', 'despacho judicial', 'tribunal', 
                'rama judicial', 'secretaria del juzgado'
            ],
            'secundarios': ['expediente', 'radicado', 'proceso', 'magistrado']
        },
        'anexos': {
            'principales': ['anexo', 'demanda', 'fotocopia cedula', 'historia clinica', 'documento anexo'],
            'secundarios': ['soporte', 'certificado', 'constancia', 'comprobante']
        }
    }

    def calcular_score_tipo(texto: str, patrones_tipo: dict) -> int:
        score = 0
        for patron in patrones_tipo['principales']:
            if patron in texto:
                score += 2
        for patron in patrones_tipo['secundarios']:
            if patron in texto:
                score += 1
        return score

    # Calcular scores para cada tipo
    scores = {
        'auto_tutela': calcular_score_tipo(texto_sin_tildes, patrones['auto_tutela']),
        'juzgado': calcular_score_tipo(texto_sin_tildes, patrones['juzgado']),
        'anexos': calcular_score_tipo(texto_sin_tildes, patrones['anexos'])
    }

    # Determinar tipo de documento basado en el mayor score
    tipo_documento = max(scores.items(), key=lambda x: x[1])[0]
    
    # Asignar prioridades en formato de dos dígitos, asegurando uso único
    if tipo_documento == 'auto_tutela' and scores['auto_tutela'] > 0:
        if not etiquetas_asignadas['auto_tutela']:
            prioridad = '01'
            etiquetas_asignadas['auto_tutela'] = True
        else:
            tipo_documento = 'juzgado'  # Si ya se asignó 01, recategorizamos
            prioridad = asignar_prioridad('juzgado', scores['juzgado'])
    elif tipo_documento == 'juzgado':
        prioridad = asignar_prioridad('juzgado', scores['juzgado'])
    elif tipo_documento == 'anexos':
        prioridad = asignar_prioridad('anexos', scores['anexos'])
    else:
        prioridad = '08'

    return prioridad, tipo_documento

def asignar_prioridad(tipo: str, score: int) -> str:
    """
    Asigna la prioridad más baja disponible para un tipo de documento.
    """
    if tipo == 'juzgado':
        opciones = ['02', '03', '04']
    elif tipo == 'anexos':
        opciones = ['05', '06', '07']
    else:
        return '08'

    for opcion in opciones:
        if opcion not in etiquetas_asignadas[tipo]:
            etiquetas_asignadas[tipo].add(opcion)
            return opcion

    return '08'  # Por defecto, si no hay más opciones disponibles




def normalize_text(text: str) -> str:
    """
    Normaliza el texto removiendo tildes y caracteres especiales.
    """
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                  if unicodedata.category(c) != 'Mn')

def extract_data(ruta_archivos: str, cantidad: int = None, upscale=False, tpoDcmnto: str = None, asntoCrro: str = None):
    resultado_procesamiento = []

    # Obtener la lista de archivos válidos
    archivos = [
        f for f in os.listdir(ruta_archivos)
        if f.lower().endswith(('.pdf', '.jpg', '.png', '.docx'))
    ]

    # Priorizar archivos por palabras clave en el nombre
    archivos_prioritarios_autoadmite = [
        f for f in archivos 
        if any(keyword in f.lower() for keyword in ('admision','autoadmite', 'autoadmision', 'admite tutela', 'acciontutela', 'autoadmisorio', 'autorequiereincidente', 'auto','autoadmitir','autoadmite','admite',
                                                    'sentencia','oficio','Oficiofallo','fallo',
                                                    'EscritoIncidente','AutoApertura','PrimerRequerimiento'
                                                    ))
    ]
    archivos_prioritarios_autoavoca = [
        f for f in archivos 
        if any(keyword in f.lower() for keyword in ('autoavoca', 'auto avocamiento', 'autodeavocamiento')) and f not in archivos_prioritarios_autoadmite
    ]
    archivos_restantes = [
        f for f in archivos 
        if f not in archivos_prioritarios_autoadmite and f not in archivos_prioritarios_autoavoca
    ]

    # Combinar los archivos en orden de prioridad
    archivos = archivos_prioritarios_autoadmite + archivos_prioritarios_autoavoca + archivos_restantes

    if not archivos:
        logger.warning("No se encontraron archivos en la ruta especificada.")
        return resultado_procesamiento

    extractor = DocumentoExtractor()

    campos_encontrados = {
        'nmroRdcdoJdcl': None,
        'nmbreCmpltoAccnnte': None,
        'nmroIdntfccn': None,
        'nombre_juzgado': None,
        'CdgoJzgdo': None,
        'fchaVncmnto': None,
        'fchaTtla': None,
        'cdgoTpoIdntfccn': None,
        'mddaPrvcnl': None,
        'calidad_de_parte': None
    }

    for archivo in archivos:
        full_path = os.path.join(ruta_archivos, archivo)
        logger.info(f"Procesando archivo: {full_path}")

        try:
            if archivo.lower().endswith('.pdf'):
                texto_extraido = extract_text_from_pdf(full_path, upscale)
            elif archivo.lower().endswith(('.jpg', '.png')):
                imagen = Image.open(full_path)
                if upscale:
                    imagen = upscale_image(imagen)
                imagen_preprocesada = preprocess_image(imagen)
                texto_extraido = pytesseract.image_to_string(
                    imagen_preprocesada,
                    lang='spa',
                    config='--psm 6 --oem 3'
                )
            elif archivo.lower().endswith('.docx'):
                texto_extraido = extract_text_from_docx(full_path)
            else:
                continue

            extractor.set_texto(texto_extraido)
            campos_extraidos = {}

            for campo in campos_encontrados.keys():
                if campos_encontrados[campo] is not None:
                    campos_extraidos[campo] = campos_encontrados[campo]
                else:
                    metodo_busqueda = f'buscar_{campo}'
                    if hasattr(extractor, metodo_busqueda):
                        valor = getattr(extractor, metodo_busqueda)()
                        if valor:
                            campos_encontrados[campo] = valor
                        campos_extraidos[campo] = valor if valor else None

            if campos_extraidos['nmroRdcdoJdcl']:
                campos_adicionales = {
                    'ano_radicado': extractor.buscar_ano_radicado(campos_extraidos['fchaTtla']),
                }
                for k, v in campos_adicionales.items():
                    if v:
                        campos_encontrados[k] = v
                    campos_extraidos[k] = v if v else None

            prioridad, _ = classify_document(campos_extraidos, texto_extraido)
            nuevo_nombre = f"{prioridad}_{archivo}"
            nuevo_path = os.path.join(ruta_archivos, nuevo_nombre)

            if os.path.exists(full_path):
                shutil.move(full_path, nuevo_path)
                logger.info(f"Archivo renombrado: {nuevo_nombre}")

            resultado_procesamiento.append({
                "tpoDcmnto": tpoDcmnto,
                "asntoCrro": asntoCrro,
                **campos_extraidos
            })

        except Exception as e:
            logger.error(f"Error procesando el archivo {archivo}: {e}", exc_info=True)

    for resultado in resultado_procesamiento:
        for campo, valor in campos_encontrados.items():
            if campo == 'nmroRdcdoJdcl':
                if len(valor) < 23:
                    for nmro_rdcdo_jdcl in extractor.nmrs_rdcds_jdcls_list:
                        if len(nmro_rdcdo_jdcl) > len(valor):
                            valor = nmro_rdcdo_jdcl
                    
                    if resultado[campo]:
                        resultado[campo] = valor
            resultado[campo] = valor if resultado.get(campo) is None else resultado[campo]

    return resultado_procesamiento

