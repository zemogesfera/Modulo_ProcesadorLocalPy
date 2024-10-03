import spacy
from difflib import SequenceMatcher
import re

# Cargar el modelo de idioma español de spaCy
nlp = spacy.load("es_core_news_md")

# Lista de palabras clave que suelen tener errores, ir ampliando con el contexto de los documentos
palabras_comunes = ["circuito","documentacion", "aseguradora", "paciente",
    "sentencia", "razones", "referencia", "conductas", "punibles", "republica",
    "Python", "expediente", "medicamento", "recobro", "procedimiento",
    "tutela", "afiliado", "informe", "clinico", "prescripcion",
    "prestacion", "facturacion", "especialidad", "recuperacion", "hospital",
    "institucion", "medico", "diagnóstico", "historia", "evolucion", 
    "comite", "autorizacion", "ministerio", "salud", 
    "servicio", "atencion", "dosis", "receta", "validacion", "proceso",
    "glosa", "detalle", "suministro", "pacientes", "reporte", "reclamacion", 
    "subsidio", "solicitud", "acuerdo", "declaracion", "registro", "certificado",
    "intervencion", "terapia", "tratamiento", "diagnóstico", "especialista",
    "urgencias", "farmacia", "medicacion", "prueba", "laboratorio",
    "radiografía", "ultrasonido", "quimioterapia", "procedimientos", "cobertura",
    "exclusiones", "incapacidad", "derecho", "demanda", "responsabilidad",
    "delito", "apelacion", "legislacion", "consulta",
    "sancion", "jurisprudencia", "constitucional", "audiencia", "acta",
    "peritaje", "dictamen", "competencia", "testimonio",
    "providencia", "reglamento", "orden judicial", "mandato", "juridico"]


def similaridad(palabra1, palabra2):
    """
    Calcula la similaridad entre dos palabras usando SequenceMatcher para detectar errores menores.
    """
    return SequenceMatcher(None, palabra1.lower(), palabra2.lower()).ratio()

def corregir_palabra(palabra, texto):
    """
    Intenta corregir una palabra en el texto en función de la similaridad con palabras comunes.
    """
    palabras = texto.split()
    for i, palabra_texto in enumerate(palabras):
        if similaridad(palabra_texto, palabra) > 0.8:  # Similaridad mayor al 80%
            palabras[i] = palabra  # Reemplazar con la palabra correcta
    return ' '.join(palabras)

def corregir_texto(texto):
    """
    Aplica técnicas de NLP para corregir errores de palabras basados en contexto y tildes.
    """
    # Pasar el texto por el modelo NLP de spaCy para análisis gramatical
    doc = nlp(texto)

    # Corregir las palabras clave comunes
    for palabra in palabras_comunes:
        texto = corregir_palabra(palabra, texto)

    # Corregir posibles errores de espacios extra
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

def aplicar_correcciones(texto_extraido):
    """
    Función principal para aplicar correcciones automáticas con machine learning.
    """
    texto_corregido = corregir_texto(texto_extraido)
    return texto_corregido
