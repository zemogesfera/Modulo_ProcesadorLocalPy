import re

from palabras_prohibidas import palabras_prohibidas
from patrones import PATRONES_ACCIONANTE

def identificar_accionante(objeto):

    try:
        if objeto.es_empresa:
            return None
    
        patrones = PATRONES_ACCIONANTE

        def limpiar_nombre(nombre):
            prefijos = ['senora','señor ', 'señora ', 'sr ', 'sra ', 'dr ', 'dra ', 'ciudadano ', 'ciudadana ','senor']
            nombre_lower = nombre.lower()
            for prefijo in prefijos:
                if nombre_lower.startswith(prefijo):
                    nombre = nombre[len(prefijo):].strip()
                    break#solo elimina un prefijo (cambio)
        
            palabras = nombre.split()
            palabras_limpias = [palabra for palabra in palabras if palabra.lower() not in palabras_prohibidas]
            return ' '.join(palabras_limpias).strip()
        
        def limpiar_representante(texto):
            """
            Busca en el texto utilizando una lista de patrones predefinidos y retorna
            el texto después del primer patrón que coincida.
            
            Args:
                texto (str): El texto en el que se buscarán los patrones.
            
            Returns:
                str: El texto después del patrón encontrado, o None si no se encuentra ningún patrón.
            """
            # Lista de patrones predefinidos
            patrones_representante = [
                r"quien\s+actua.*?representacion\s+del\s+menor",
                r"quien\s+actua.*?como\s+representante\s+legal\s+del\s+menor",
                r"quien\s+actua.*?en\s+nombre\s+del\s+menor",
                r"quien\s+actua.*?en\s+representacion\s+de",
                r"quien\s+actua.*?como\s+representante\s+legal\s+de",
                r"quien\s+actua.*?como\s+representante\s+de",
            ]
            
            for patron_representante in patrones_representante:
                # Usamos una expresión regular para buscar el patrón y capturar el texto después de él
                regex = re.compile(f"{patron_representante}(.+)", re.IGNORECASE | re.DOTALL)
                match = regex.search(texto)
                if match:
                    # Retornamos el texto después del patrón coincidente
                    return match.group(1).strip()
                else:
                    # Si no se encuentra el patrón, retornamos el texto completo
                    return texto

        nombre_encontrado = None
        for patron in patrones:
            match = re.search(patron, objeto.texto, re.MULTILINE)
            if match:
                nombre_temp = match.group(1).strip()
                nombre_limpio = limpiar_nombre(nombre_temp)
                nombre_limpio = limpiar_representante(nombre_limpio)

                objeto.logger.info(f"Nombre encontrado antes de validar: {nombre_limpio}")


                palabras_nombre = nombre_limpio.split()
                if palabras_nombre and not any(palabra.lower() in palabras_prohibidas for palabra in palabras_nombre):
                    nombre_encontrado = nombre_limpio
                    break
        
        if nombre_encontrado:
        # Verificar si es representante legal después de encontrar el nombre
            patron_representante = rf'(?i)(?:representada?\s+legalmente\s+por|en\s+calidad\s+de\s+representante\s+legal|obrando\s+como\s+representante\s+legal)\s+{re.escape(nombre_encontrado)}'
            if re.search(patron_representante, objeto.texto):
                return None

        # Verificar si es entidad después de encontrar el nombre
            patron_entidad = r'\b[A-ZÁÉÍÓÚÑ]+(?:\s+[A-ZÁÉÍÓÚÑ]+)*\s+(?:S\.?A\.?|S\.?A\.?S\.?|LTDA\.?|S\.?L\.?|INC\.?|LLC\.?)\b(?=[\s.,;]|$)'
            if re.search(patron_entidad, nombre_encontrado):
                objeto.es_empresa = True
                return None

            patron_empresa = r'(?i)\b(?:BANCO|FONDO|CORPORACI[OÓ]N|COOPERATIVA|CAJA|TELEMARK|COLPENSIONES|PORVENIR|PROTECCION|COLFONDOS|SKANDIA|ING|BBVA|BANCOLOMBIA|DAVIVIENDA|EPM|EMPRESA|COMPAÑ[IÍ]A|ASEGURADORA|POSITIVA|MAPFRE|LIBERTY|ALLIANZ|SEGUROS|FIDEICOMISO|PATRIMONIO|AFP)\b\s*(?:DE\s+COLOMBIA|S\.?A\.?|S\.?A\.?S\.?|LTDA\.?|E\.?S\.?P\.?|S\.?C\.?|S\.?C\.?A\.?)?'
            if re.search(patron_empresa, nombre_encontrado):
                objeto.es_empresa = True
                return None
        
        return nombre_encontrado

    except Exception as e:
        objeto.logger.error(f"Error en buscar_nmbreCmpltoAccnnte: {e}")
        return None

def identificar_documento_identidad(objeto):
    """
    Busca el número de documento del accionante con mayor precisión.
    Prioriza la autoidentificación directa del accionante.
    """
    try:

        # nmbreCmpltoAccnnte = objeto.buscar_nmbreCmpltoAccnnte()
        # if not nmbreCmpltoAccnnte:
        #     return None
        
        # Si no tengo nada en objeto.nmbre_cmplto_accnnte busco con buscar_nmbreCmpltoAccnnte
            # Si buscar_nmbreCmpltoAccnnte devuelve el nombre, se lo asigno a objeto.nmbre_cmplto_accnnte
            # Si buscar_nmbreCmpltoAccnnte no devuelve el nombre, se retorna None
        # Si tengo algo en objeto.nmbre_cmplto_accnnte, se lo asigno a nmbreCmpltoAccnnte
        if not objeto.nmbre_cmplto_accnnte:
            nmbreCmpltoAccnnte = objeto.buscar_nmbreCmpltoAccnnte()
            if nmbreCmpltoAccnnte:
                objeto.nmbre_cmplto_accnnte = nmbreCmpltoAccnnte
            else:
                return None
        else:
            nmbreCmpltoAccnnte = objeto.nmbre_cmplto_accnnte
        

        def limpiar_y_validar_numero(numero):
            """
            Limpia puntos, espacios, guiones, comas, y reemplaza cualquier letra 'i', 'í', 'I', 'Í' con '1'.
            Valida la longitud del número.
            """
            # Reemplazar letras 'i', 'í', 'I', 'Í' por '1'
            numero = re.sub(r'[iíIÍ]', '1', numero)
            # Limpiar puntos, espacios, guiones y comas
            numero_limpio = re.sub(r'[.,\s-]', '', numero)
            # Validar que el número tenga entre 7 y 11 dígitos
            if re.match(r'^\d{7,11}$', numero_limpio):
                return numero_limpio
            
        patrones = []

        def crear_patrones(nombre_completo_accionante):
            return [
                rf"Yo,\s*{re.escape(nombre_completo_accionante)}.*?(?:identificad[oa]\s+con\s+(?:c[eé]dula\s+de\s+ciudadan[íi]a|C\.?C\.?)\s*(?:No\.?)?\s*[:.]?\s*)([\d.,\s-]+)(?=\s*,|\s*domiciliada|\s*$)",
                rf"Yo,\s*{re.escape(nombre_completo_accionante)}.*?(?:identificad[oa]\s+con\s+(?:c[eé]dula\s+de\s+ciudadan[íi]a|C\.?C\.?)\s*(?:No\.?)?\s*[:.]?\s*)([\d.,\s-]+)",
                rf"{re.escape(nombre_completo_accionante)}.*?(?:identificad[oa]\s+con\s+(?:c[eé]dula\s+de\s+ciudadan[íi]a|C\.?C\.?)\s*(?:No\.?)?\s*[:.]?\s*)([\d.,\s-]+)",
                rf"{re.escape(nombre_completo_accionante)}(?:\s+\w+)?\s+identificad[oa]\s+con\s+c[eé]dula\s+de\s+ciudadan[íi]a\s+(?:No\.?\s*)?(\d{7,11})\b",
                rf"{re.escape(nombre_completo_accionante)}\s*C\.?C\.?\s*\.?\s*:?(\d{7,11})",
                rf"{re.escape(nombre_completo_accionante)},?\s*identificad[oa]\s+con\s*la?\s*c[eé]dula\s+de\s+ciudadan[ií]a\s*(?:No\.?)?\s*([\d\.,\s]+)",
                rf"{re.escape(nombre_completo_accionante)}.*?(?:identificad[oa]\s+con\s+(?:la\s+)?c[eé]dula\s+de\s+ciudadan[íi]a\s+(?:n[úu]mero)?\s*)([\d.,\s-]+)",
                rf"{re.escape(nombre_completo_accionante)}.*?(?:identificad[oa]\s+con\s+(?:la\s+)?c[eé]dula\s+de\s+ciudadan[íi]a\s+(?:n[úu]mero)?\s*)([\d.,\s-]+)",
                rf"{re.escape(nombre_completo_accionante)}\s*C\.C\.\s*([\d.,\s-]+)",
                rf"{re.escape(nombre_completo_accionante)}\s*C\.C\.\s*([\d.,\s-]+)",
                rf"{re.escape(nombre_completo_accionante)},\s*mayor\s+de\s+edad,\s*identificada\s+con\s+la\s+c[ée]dula\s+de\s+ciudadan[íi]a\s+n[úu]mero\s*([\d\.,\s]+)\s*expedida",
                rf"{re.escape(nombre_completo_accionante)}\s+C\.C\.\s*([\d\.,\s]+)\s+de\s+Bol[ií]var",
                rf"{re.escape(nombre_completo_accionante)},\s*mayor\s+de\s+edad,\s*identificada\s+con\s*la?\s*c[eé]dula\s+de\s+ciudadan[ií]a\s+n[uú]mero\s*([\d\.,\s]+)\s*expedida",
                rf"{re.escape(nombre_completo_accionante)}.*?(?:portador[oa]?\s+de\s+(?:c[eé]dula|C\.?C\.?)\s*(?:n[úu]mero|No\.?)?\s*)(\d{7,11})\b",
                rf"{re.escape(nombre_completo_accionante)}.*?(?:identificad[oa]\s+con\s+(?:c[eé]dula\s+de\s+ciudadan[íi]a|C\.?C\.?)\s*(?:No\.?)?\s*[:.]?\s*)(\d{7,11})\b",
                rf"{re.escape(nombre_completo_accionante)}.*?RC\.\s*([\d.,\s-]+)",
                rf"{re.escape(nombre_completo_accionante)}.*?(?:identificado\s+con\s+documento\s+(?:n[úu]mero|No\.?)?\s*)(\d{7,11})\b"
                rf"{re.escape(nombre_completo_accionante)}\s+([\d.,\s-]+)\s+de\s+[A-Z][a-z]+",
                rf"Yo,\s*{re.escape(nombre_completo_accionante)}.*?(?:identificad[oa]\s+con\s+(?:c[eé]dula\s+de\s+ciudadan[íi]a|C\.?C\.?)\s*(?:No\.?)?\s*[:.]?\s*)(\d{7,11})\b",
                rf"{re.escape(nombre_completo_accionante)}.*?(?:identificad[oa]\s+con\s+(?:c[eé]dula\s+de\s+ciudadan[íi]a|C\.?C\.?)\s*(?:No\.?)?\s*[:.]?\s*)(\d{7,11})\b",
                rf"{re.escape(nombre_completo_accionante)}.*?(?:portador[oa]?\s+de\s+(?:c[eé]dula|C\.?C\.?)\s*(?:n[úu]mero|No\.?)?\s*)(\d{7,11})\b",
                rf"{re.escape(nombre_completo_accionante)}\s*CC\s*No\.?\s*([\d.,\s-]+)",
                rf"{re.escape(nombre_completo_accionante)}.*?ciudadan[íi]a\s+No\.?\s*(\d{6,11}(?:\.\d{3})*)",
                rf"{re.escape(nombre_completo_accionante)}.*?(?:identificado\s+con\s+documento\s+(?:n[úu]mero|No\.?)?\s*)(\d{7,11})\b",
                rf"{re.escape(nombre_completo_accionante)}, identificado con la CC Nro\. (\d+)",
                rf"{re.escape(nombre_completo_accionante)}, identificada con cédula de ciudadanía Núm\. ([\d\.]+)",
                rf"{re.escape(nombre_completo_accionante)}\s*C\.C\.\s*([\d.]+)",
                rf"{re.escape(nombre_completo_accionante)}\s*(?:,|\s+identificado\s+con\s+la?)?\s*(?:c\.?c\.?|cc|cédula\s+de\s+ciudadanía)\s*(?:nro\.?|n°|no\.?|num(?:ero|ro)?)?\s*[:.]?\s*([\d.]+)",
                rf"(?i){re.escape(nombre_completo_accionante)}\s+identificad[oa]?\s+con\s+(?:cedula\s+de\s+ciudadania|n[uú]mero|num|n°|c\.c\.|cc)\s*[:\-]?\s*([\d\.]+)",
                rf"(?i){re.escape(nombre_completo_accionante)}\s*,\s*identificad[oa]\s+con\s+c[ée]dula\s+de\s+ciudadan[ií]a\s+N[úu]m\.?\s*([\d\.]+)",
                rf"(?i){re.escape(nombre_completo_accionante)}\s+T\.?I\.?\s*([\d\.]+)",
                rf"(?i){re.escape(nombre_completo_accionante)}\.\s*[Cc]\.?[Cc]\.?\s*([\d\.]+)",
                rf"{re.escape(nombre_completo_accionante)}\s+con\s+([\d\.]+)",
                rf"(?i){re.escape(nmbreCmpltoAccnnte)}\s*,?\s*identificado\s+con\s+la\s+c[eé]dula\s+de\s+ciudadan[íi]a\s+n[°º]?\s*([\d\.]+)",
                rf"{re.escape(nombre_completo_accionante)}\s{{1,20}}(?i)DOCUMENTO\s*:? *(\d+)",
                rf"{re.escape(nombre_completo_accionante)}\s+Pagina\s+No\.\s+1\s+(?i)DOCUMENTO\s*:? *(\d+)",
                
            ]


        # Patrones ordenados por especificidad
        patrones.extend([

                
            #patrones de autoidentifación

            # Patrones en pruenbas 
            
            
            # Patrón para captura directa con C.C.
            
            #se comentan ya que son generales
            r"[Ii]dentificado\s+con\s+documento\s*:\s*([\d.,\s-]+)",
            r"[Ii]dentificado\s+con\s+documento\s+[Nn]o\.\s*:\s*([\d.,\s-]+)",
            r"[Ii]dentificada?\s+con\s+documento\s*:\s*([\d.,\s-]+)",
            #patrones de reformación de los 3 anteriores 
            #pendiente los 3 de reformación

            # Nuevo patrón para capturar el formato específico del caso mencionado, se comenta ya que captura cualquier número de cc y se asigna el nuevo
            #r"identificado\s+con\s+c[eé]dula\s+de\s+ciudadan[íi]a\s+(?:n[úu]mero|No\.?)?\s*([\d.,\s]+)(?:\s*[,\.]|$)",
            # Patrón para el formato específico "C.C N.° 1.005.944.947 de [ciudad]"
            r"C\.?C\.?\s*N\.?°?\s*([\d.,\s]+)\s+de\b",
                
            # Patrón específico para capturar casos como "C.C No. 1.107.978.306" se comenta ya que es un proceso generalizado. y se agrega una nueva versión en pruebas 
            #r"(?:C\.?C\.?|c[eé]dula\s+de\s+ciudadan[íi]a)\s+(?:n[úu]mero|No\.?)?\s*([\d.,\s]+)",

            # Otros patrones
            r"identificada?\s+con\s+c[eé]dula\s+de\s+ciudadan[íi]a\s+(?:n[úu]mero|No\.?\s+)?([\d.,\s]+)\b",
            r"identificad[oa]\s+con\s+(?:c\.?c\.?|c[eé]dula)(?:\s+de\s+ciudadan[íi]a)?\s+(?:n[úu]mero|No\.?\s+)?([\d.,\s]+)\b",
            r"(?:c\.?c\.?|c[eé]dula)(?:\s+de\s+ciudadan[íi]a)?\s+(?:n[úu]mero|No\.?\s+)?([\d.,\s]+)\b",
            r"portador[oa]?\s+de\s+(?:c[eé]dula|C\.?C\.?)\s*(?:n[úu]mero|No\.?)?\s*([\d.,\s]+)\b",

            # Patrón más general para capturas simples
            r"(?:n[úu]mero|No\.?\s+)?([\d.,\s]+)(?:\s+expedida)?",
            
            # Patrón específico para casos donde el número está entre comas
            r",\s*(?:n[úu]mero|No\.?\s+)?([\d.,\s]+)\s*[,\.]",

                            # Nuevo patrón para capturar "C.C. No. 16.278.340 y portador"
            r"C\.?C\.?\s*No\.?\s*([\d.,\s]+)\s+y\s+portador\b",
            
            # Patrón general para "C.C No. 16.278.340" se comenta ya que no incluye el accionante se incluye uno nuevo en pruebas
            #r"C\.?C\.?\s*(?:n[úu]mero|No\.?)?\s*([\d.,\s]+)\b",
            
            r"(?:N°|No\.?\s+)([\d.,\s]+)",
            r"[Cc]edula\s+de\s+[Cc]iudadan[ií]a\s+(?:Nro\.?|[Nn][úu]mero\.?)\s*([\d.,\s-]+)",
            
            # Patrón directo con "Yo, {Nombre} identificado con..."

            #  Patrón general con el nombre antes de la identificación

            # Variación con "portador de cédula"

            #nuevo contexto:EGIDIO QUINTERO VEGA  
            #CC No. 16214057
            r"(?:C\.?C\.?|c[eé]dula\s+de\s+ciudadan[íi]a)\s+(?:n[úu]mero|No\.?)?\s*([\d.,\s]+)",
            r"identificad[oa]\s+con\s+numero\s+de\s+C\.?C\.?\s*[:.]?\s*([\d.,-]+)",
            r"identificad[oa]\s+con\s+c[eé]dula\s+de\s+ciudadan[íi]a\s+No\.?\s*([\d.,\s-]+)",
            r"identificad[oa]\s+con\s+C[eé]dula\s+de\s+Ciudadan[íi]a\s+n[úu]mero\.?\s*([\d.,\s-]+)",
            r"identificado con la CC Nro\. (\d+)",
            r"identificada con cédula de ciudadanía Núm\. ([\d\.]+)"
            
        ])

        texto_original = objeto.texto
        texto = texto_original.lower()
        nombre_accionante_orginal = objeto.nmbre_cmplto_accnnte
        nombre_accionante = nombre_accionante_orginal.lower()

        nombres_validar = []
        nombres_validar.append(nombre_accionante)
        partes_nombre = nombre_accionante.split()
        primera_parte_nombre = " ".join(partes_nombre[:2])
        nombres_validar.append(primera_parte_nombre)

        primer_nombre = partes_nombre[0]
        segundo_nombre = partes_nombre[1] if len(partes_nombre) > 1 else ""
        if segundo_nombre:
            nombres_validar.append(f"{primer_nombre} de {segundo_nombre}")
            nombres_validar.append(f"{primer_nombre} del {segundo_nombre}")

        apellidos = partes_nombre[2:]
        primer_apellido = apellidos[0] if apellidos else ""
        segundo_apellido = apellidos[1] if len(apellidos) > 1 else ""

        if primer_apellido:
            nombres_validar.append(f"{primer_nombre} {segundo_nombre} de {primer_apellido}")
            nombres_validar.append(f"{primer_nombre} {segundo_nombre} del {primer_apellido}")

        if segundo_apellido:
            nombres_validar.append(f"{primer_apellido} de {segundo_apellido}")
            nombres_validar.append(f"{primer_apellido} del {segundo_apellido}")
        
        posiciones_nombre = []
        for nombre in nombres_validar:
            patrones_creados = crear_patrones(nombre)
            if patrones_creados:
                patrones.extend(patrones_creados)

            # Encuentra todas las posiciones del nombre del accionante en el texto
            posiciones_nombre.extend([m.start() for m in re.finditer(re.escape(nombre), texto)])
            posiciones_nombre = list(set(posiciones_nombre))
            
        # Para cada aparición del nombre, busca el número de documento en el contexto siguiente
        for pos in posiciones_nombre:
            # Toma el texto después de esta aparición del nombre (limitado a 70 caracteres)
            contexto_relevante = texto[pos:pos + 500]
            # Intenta cada patrón en el contexto relevante
            for patron in patrones:
                match = re.search(patron, contexto_relevante, re.IGNORECASE)

                if match and len(match.group(1).strip()) >= 7:
                    numero = match.group(1).strip()
                    numero_limpio = limpiar_y_validar_numero(numero)
                    if numero_limpio:
                        for nombre in nombres_validar:
                            distancia = contexto_relevante.find(numero) - contexto_relevante.find(nombre)  # Calcula la distancia
                            if distancia > 1 and distancia <= 100:  # Asegurar que la distancia sea válida
                                objeto.logger.debug(f"Encontrado número de identificación: {numero_limpio} con distancia: {distancia} al nombre '{nombre}'")
                                objeto.agregar_nmro_idntfccn_accnnte(numero_limpio, distancia)

        if not objeto.nmrs_idntfccn_accnnte:
            objeto.logger.error(f"No se encontraron números de identificación del accionante en el texto")
            return None

        return min(objeto.nmrs_idntfccn_accnnte, key=lambda x: x["distancia"])["numero"]

    except Exception as e:
        objeto.logger.error(f"Error al buscar número de identificación: {str(e)}")
        return None

def identificar_tipo_documento(objeto):
    """
    Busca el tipo de documento del accionante en el texto.
    Retorna CC, RC, o TI según el tipo de documento identificado.
    """
    try:
        # Verificar primero si existe número de identificación
        if not objeto.buscar_nmroIdntfccn():
            objeto.logger.error(f"No hay número de identificación")

            return None

        # Obtener el nombre completo del accionante
        if not objeto.nmbre_cmplto_accnnte:
            nmbreCmpltoAccnnte = objeto.buscar_nmbreCmpltoAccnnte()
            if nmbreCmpltoAccnnte:
                objeto.nmbre_cmplto_accnnte = nmbreCmpltoAccnnte
        else:
            nmbreCmpltoAccnnte = objeto.nmbre_cmplto_accnnte

        patrones = []
        if nmbreCmpltoAccnnte:
            patrones.extend(
                [
                    
                    rf"{re.escape(nmbreCmpltoAccnnte)}.*?(RC|C\.?C\.?|T\.?I\.?)\.",
                ]
            )

        # Patrones originales
        patrones.extend([
            r'(?:accionante|paciente).*?identificad[oa] con (?:la |el )?(\w+(?:\s+\w+){0,4})\s+No\.',
            #este no es, este identifica el agente oficioso, debe identificar el en representacion
            r'agente oficios[oa] de .*?identificad[oa] con (?:la |el )?(\w+(?:\s+\w+){0,4})\s+No\.',
            r'(?:accionante|paciente|señor[a]?)\s.*?portador[a]? de (?:la |el )?(\w+(?:\s+\w+){0,4})\s+No\.',
            r'con\s+(C\.?C\.?|T\.?I\.?|RC|CE|P\.?P\.?)\s+(?:No\.?\s+)?[\d\.,]+[A-Za-z]*',
            r'identificad[oa] con\s+(C[eé]dula\s+de\s+Ciudadan[ií]a|Tarjeta\s+de\s+Identidad|Registro\s+Civil|C[eé]dula\s+de\s+Extranjer[ií]a|Pasaporte)',
            r'portador[a]? de la\s+(C\.?C\.?|T\.?I\.?|RC|CE|P\.?P\.?)\s+No\.',
            r'cédula\s+de\s+ciudadan[ií]a\s+No\.\s*(\d{1,2}(\.\d{1,3}){2,3})',
            r'cédula\s+de\s+ciudadan[ií]a\s+No\.\s*([\d\.\-]+)',
            r'ACCIONANTE:.*?\s(C\.?C\.?|T\.?I\.?|RC|CE|P\.?P\.?)\b',
            
        ])

        # Mapeo para normalizar y clasificar los tipos de documentos
        mapping_documentos = {
            'cédula de ciudadanía': 'CC',
            'cedula de ciudadania': 'CC',
            'cedula de ciudadanía' : 'CC',
            'C.C.': 'CC',
            'CC': 'CC',
            'registro civil': 'RC',
            'RC': 'RC',
            'RC.': 'RC',

            'tarjeta de identidad': 'TI',
            'T.I': 'TI',
            'T.I.': 'TI',
            'TI': 'TI',
        }

        # Primero buscar con los patrones originales
        for patron in patrones:
            match = re.search(patron, objeto.texto, re.IGNORECASE | re.DOTALL)
            if match:
                # Obtener el tipo de documento y normalizarlo
                tipo_documento = match.group(1).strip()

                # Verificar si está en el mapeo
                tipo_documento_normalizado = mapping_documentos.get(tipo_documento.upper(), None)
                if tipo_documento_normalizado:
                    return tipo_documento_normalizado

                # Normalización adicional basada en palabras clave
                tipo_documento_lower = tipo_documento.lower()
                if 'cédula' in tipo_documento_lower or 'cedula' in tipo_documento_lower:
                    return 'CC'
                elif 'registro civil' in tipo_documento_lower:
                    return 'RC'
                elif 'tarjeta' in tipo_documento_lower:
                    return 'TI'

        # Si no se encuentra con los patrones originales y tenemos un nombre
        if nmbreCmpltoAccnnte:
        # Obtener las primeras dos palabras del nombre
            palabras_nombre = nmbreCmpltoAccnnte.split()
            if len(palabras_nombre) >= 2:
                # Crear patrón de búsqueda basado en las primeras dos palabras del nombre
                primer_palabra = re.escape(palabras_nombre[0])
                segunda_palabra = re.escape(palabras_nombre[1])

                # Patrones de búsqueda específicos para el nombre
                patrones_nombre = [
                # Patrón para CC. inmediatamente después o cerca del nombre
                    fr'{primer_palabra}\s+{segunda_palabra}.*?CC\.?\s*\d',

                # Patrón para CC. en líneas cercanas al nombre
                    fr'{primer_palabra}\s+{segunda_palabra}.*\n.*?CC\.?',

                # Patrón más flexible
                    fr'(?:{primer_palabra}\s+{segunda_palabra}).*?CC\.?',

                    
                ]

                # Buscar con los nuevos patrones
                for patron in patrones_nombre:
                    match_nombre = re.search(patron, objeto.texto, re.IGNORECASE | re.MULTILINE | re.DOTALL)
                    if match_nombre:
                        return 'CC'

        # Si no se encontró ningún tipo de documento pero hay número de identificación, retornar CC por defecto
        return 'CC'
    
    except Exception as e:
        objeto.logger.error(f"Error en buscar_cdgoTpoIdntfccn: {e}")
        return None
