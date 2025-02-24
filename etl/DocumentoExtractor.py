import re
import locale
import logging
from datetime import datetime
import pandas as pd
import os
from dateutil import parser
import dateparser
from functions.calidadparte import identificar_parte
from functions.medidaprovisional import determinar_medida
from functions import accionante
from functions import utils


class DocumentoExtractor:
    def __init__(self, ruta_csv=None,):
        self.texto = None
        self.lines = []
        self.current_year = datetime.now().year
        self.previous_year = self.current_year - 1
        self.df_juzgados = None
        self.fechacorreo = "2024-11-25 16:30:00.000"  # Fecha fija para pruebas
        self.es_empresa = False
        self.codigo_juzgado_acumulado = None
        self.numero_parcial_acumulado = None
        self.nmrs_rdcds_jdcls_list = []
        self.nmrs_idntfccn_accnnte = []
        self.nmbre_cmplto_accnnte = None
 
        # Configurar la ruta del CSV relativa al directorio del script
        ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_csv = os.path.join(ruta_base, 'tbjuzgados.csv')
        
        # Configuración del logger
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        
        # Si se proporciona la ruta del CSV, cargarlo automáticamente
        if ruta_csv:
            self.cargar_csv_juzgados(ruta_csv)
        else:
            # Inicializar df_juzgados como DataFrame vacío si no se proporciona ruta
            self.df_juzgados = pd.DataFrame()
            self.logger.warning("No se proporcionó ruta del CSV de juzgados. Algunas funcionalidades estarán limitadas.")

    def agregar_nmro_rdcdo_jdcl(self, nmro_rdcdo_jdcl):
        if nmro_rdcdo_jdcl and nmro_rdcdo_jdcl not in self.nmrs_rdcds_jdcls_list:
            self.nmrs_rdcds_jdcls_list.append(nmro_rdcdo_jdcl)

    def agregar_nmro_idntfccn_accnnte(self, nmro_idntfccn_accnnte, distancia):
        """
        Agrega un número de identificación asegurando que, si se repite, se mantenga el que tiene menor distancia.
        """
        for item in self.nmrs_idntfccn_accnnte:
            if item["numero"] == nmro_idntfccn_accnnte:
                if distancia < item["distancia"]:  # Reemplaza si la nueva distancia es menor
                    item["distancia"] = distancia
                return

        self.nmrs_idntfccn_accnnte.append({"numero": nmro_idntfccn_accnnte, "distancia": distancia})

    def set_texto(self, texto):
        """Establece el texto a procesar"""
        self.texto = texto
        self.lines = texto.split('\n')
        
    def cargar_csv_juzgados(self, ruta_csv):
        """Carga el CSV de juzgados"""
        try:
            self.logger.debug(f"Intentando cargar el CSV desde: {ruta_csv}")
            
            # Cargar el CSV usando la codificación ANSI (ISO-8859-1)
            self.df_juzgados = pd.read_csv(ruta_csv, encoding='ISO-8859-1')
            
            # Limpieza de espacios en columnas y valores
            self.df_juzgados.columns = self.df_juzgados.columns.str.strip()
            if 'dscrpcn_jzgdo' in self.df_juzgados.columns and 'dscrpcn_jzgdo_hmlgdo' in self.df_juzgados.columns:
                self.df_juzgados['dscrpcn_jzgdo'] = self.df_juzgados['dscrpcn_jzgdo'].str.strip()
                self.df_juzgados['dscrpcn_jzgdo_hmlgdo'] = self.df_juzgados['dscrpcn_jzgdo_hmlgdo'].str.strip()
                
            self.logger.info(f"CSV cargado correctamente con {len(self.df_juzgados)} registros")
            self.logger.debug(f"Primeros registros del CSV:\n{self.df_juzgados.head()}")
            return True
            
        except FileNotFoundError:
            self.logger.error(f"Archivo CSV no encontrado en la ruta: {ruta_csv}")
            self.df_juzgados = pd.DataFrame()  # Inicializar como DataFrame vacío en caso de error
            return False
        except Exception as e:
            self.logger.error(f"Error al cargar CSV de juzgados: {str(e)}")
            self.df_juzgados = pd.DataFrame()  # Inicializar como DataFrame vacío en caso de error
            return False
            
    def buscar_codigo_juzgado(self, nombre_juzgado):
        """Busca el código del juzgado basado en su nombre"""
        if self.df_juzgados.empty or nombre_juzgado is None:
            self.logger.warning("DataFrame de juzgados vacío o nombre del juzgado no disponible")
            return None
            
        try:
            # Normalizar el nombre del juzgado para comparación
            nombre_juzgado = nombre_juzgado.strip().lower()
            
            # Realizar la búsqueda flexible
            coincidencias = self.df_juzgados[
                (self.df_juzgados['dscrpcn_jzgdo'].str.lower().str.contains(nombre_juzgado, na=False)) |
                (self.df_juzgados['dscrpcn_jzgdo_hmlgdo'].str.lower().str.contains(nombre_juzgado, na=False))
            ]
            
            if not coincidencias.empty:
                self.logger.debug(f"Coincidencias encontradas:\n{coincidencias}")
                codigo = coincidencias.iloc[0]['cdgo_jzgdo']
                self.logger.info(f"Código encontrado para el juzgado '{nombre_juzgado}': {codigo}")
                return str(codigo)
            else:
                self.logger.warning(f"No se encontró coincidencia para el juzgado: {nombre_juzgado}")
                return None
                
        except Exception as e:
            self.logger.error(f"Error al buscar código de juzgado: {str(e)}")
            return None
        
    def buscar_numero_parcial(self):
        """Busca números parciales de radicado (YYYY-XXXXX)"""
        for linea in self.lines:
            linea = linea.lower().strip()
            patron_completo = r'\b(\d{4})[-–—](\d{5})[-–—](\d{2})\b'
            match = re.search(patron_completo, linea)
            if match:
                año = match.group(1)
                numero = match.group(2).strip().zfill(5)
                sufijo = match.group(3)
                completo = f"{año}{numero}{sufijo}"
                self.logger.debug(f"Encontrado número parcial completo: {completo}")
                return completo
            
        # Buscar después de "radicado" con cualquier tipo de guión o espacio
            patron_radicado = r'radicado\s+(?:No\.)?\s*(\d{4})\s*[-–—\s]+\s*(\d{1,5})(?:[-–—\s]+\d{2})?'
            match = re.search(patron_radicado, linea.lower())
            if match:
                año = match.group(1)
                numero = match.group(2).strip().zfill(5)
                self.logger.debug(f"Encontrado número parcial: {año}-{numero}")
                return f"{año}-{numero}"
            
        
        # Nuevo patrón para capturar formato YYYY-XXXXX-00
            patron_con_sufijo = r'\b(\d{4})\s*[-–—\s]+\s*(\d{1,5})\s*[-–—\s]+\s*\d{2}\b'
            match = re.search(patron_con_sufijo, linea)
            if match:
                año = match.group(1)
                numero = match.group(2).strip().zfill(5)
                self.logger.debug(f"Encontrado número parcial con sufijo: {año}-{numero}")
                return f"{año}-{numero}"
                
            
            
        
        # Mantener el patrón original como respaldo
            patron_parcial = f'\\b({self.current_year}|{self.previous_year})-\\d{{5}}\\b'
            match = re.search(patron_parcial, linea)
            if match:
                return match.group(0)
        return None

    def buscar_nmroRdcdoJdcl(self):
        """
    Busca el número de radicado en el texto.
    Si no encuentra el formato completo, intenta construirlo usando
    el código del juzgado y el número parcial.
    Si no puede construir el número completo, retorna la información parcial encontrada.
    """
        try:
            
        # Primero intentar con los patrones originales
            for linea in self.lines:
                linea = linea.lower().strip()
                sinonimos_radicacion = ['radicado', 'radicación', 'rad', 'radicacion', 'ref']
                if any(termino in linea for termino in sinonimos_radicacion):
                    #self.logger.debug(f"Analizando línea con 'radicado': {linea}")               

                    patron_nuevo_cali = r'\b(\d{5})-(\d{4})-(\d{3})-(\d{4})-(\d{5})-(\d{2})\b'
                    match_cali = re.search(patron_nuevo_cali, linea)
                    if match_cali:
                        numero = ''.join(match_cali.groups())
                        self.logger.debug(f"Encontrado número con patrón Cali: {numero}")
                        if len(numero) >= 21:
                            return numero

                    # Patrón para capturar números con espacios (como en el ejemplo: 190014009006 2024 00 346)
                    patron_espaciado_21 = r'\b(\d{12})\s+(\d{4})\s+(\d{2})\s+(\d{3})\b'
                    match_espaciado_21 = re.search(patron_espaciado_21, linea)
                    if match_espaciado_21:
                        numero = f"{match_espaciado_21.group(1)}{match_espaciado_21.group(2)}{match_espaciado_21.group(3)}{match_espaciado_21.group(4)}"
                        if len(numero) == 21:
                            numero += "00"
                        self.logger.debug(f"Encontrado número con patrón espaciado 21: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    # Nuevo patrón para formato con espacios (76001 41 05 004 2024 00613 00)
                    patron_espacios = r'\b(\d{5})\s+(\d{2})\s+(\d{2})\s+(\d{3})\s+(\d{4})\s+(\d{5})\s+(\d{2})\b'
                    match_espacios = re.search(patron_espacios, linea)
                    if match_espacios:
                        numero = ''.join(match_espacios.groups())
                        self.logger.debug(f"Encontrado número con patrón espaciado: {numero}")
                        if len(numero) >= 21:
                            return numero
                
                    # Nuevo patrón específico para el formato 76-111-3187-004-2024-00041-00
                    patron_completo_nuevo = r'\b(\d{2})-(\d{3})-(\d{4})-(\d{3})-(\d{4})-(\d{5})-(\d{2})\b'
                    match_completo_nuevo = re.search(patron_completo_nuevo, linea)
                    if match_completo_nuevo:
                        numero = ''.join(match_completo_nuevo.groups())
                        self.logger.debug(f"Encontrado número con patrón completo nuevo: {numero}")
                        if len(numero) >= 21:
                            return numero

                    # Nuevo patrón para el formato específico 
                    patron_completo = r'\b(\d{2})-(\d{3})-(\d{4})-(\d{3})-(\d{4})-(\d{5})-\d{2}\b'
                    match_completo = re.search(patron_completo, linea)
                    if match_completo:
                        numero = ''.join(match_completo.groups())
                        self.logger.debug(f"Encontrado número con patrón completo: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    # Nuevo patrón para capturar números de 21 dígitos sin guiones ni espacios
                    patron_21_digitos = r'\b(\d{21})\b'
                    match_21 = re.search(patron_21_digitos, linea)
                    if match_21:
                        numero = match_21.group(1) + "00"  # Agregar 00 al final
                        self.logger.debug(f"Encontrado número de 21 dígitos: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    # Nuevo patrón específico para Tuluá con el formato XXXXXX-XXXX-XXXXX-XX
                    patron_tulua_nuevo = r'\b(\d{12})-(\d{4})-(\d{5})-(\d{2})\b'
                    match_tulua = re.search(patron_tulua_nuevo, linea)
                    if match_tulua:
                        numero = f"{match_tulua.group(1)}{match_tulua.group(2)}{match_tulua.group(3)}{match_tulua.group(4)}"
                        self.logger.debug(f"Encontrado número con patrón Tuluá: {numero}")
                        if len(numero) >= 21:
                            return numero
                
                    patron_tulua = r'\b(\d{2})-\s*(\d{3})-(\d{2})-(\d{2})-(\d{3})-(\d{4})-(\d{5})-(\d{2})\b'
                    match_tulua = re.search(patron_tulua, linea)
                    if match_tulua:
                        numero = ''.join(match_tulua.groups())
                        self.logger.debug(f"Encontrado número con patrón Tuluá: {numero}")
                        if len(numero) >= 21:
                            return numero

                    # Patrón alternativo que maneja espacios opcionales después de los guiones
                    patron_flexible = r'\b(\d{2})-\s*(\d{3})-(\d{2})-(\d{2})-(\d{3})-(\d{4})-(\d{5})-(\d{2})\b'
                    match_flexible = re.search(patron_flexible, linea)
                    if match_flexible:
                        numero = ''.join(match_flexible.groups())
                        self.logger.debug(f"Encontrado número con patrón flexible: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    # Nuevo patrón para el formato específico encontrado
                    patron_espaciado = r'\b(\d{12})\s+(\d{4})\s+(\d{2})\s+(\d{3})\b'
                    match_espaciado = re.search(patron_espaciado, linea)
                    if match_espaciado:
                        numero = f"{match_espaciado.group(1)}{match_espaciado.group(2)}{match_espaciado.group(3)}{match_espaciado.group(4)}"
                        self.logger.debug(f"Encontrado número con patrón espaciado: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    # Nuevo patrón para formato específico (12 dígitos - 4 dígitos - 5 dígitos - 00 al final)
                    patron_nuevo = r'\b(\d{12})-(\d{4})-(\d{5})\b'
                    match_nuevo = re.search(patron_nuevo, linea)
                    if match_nuevo:
                        numero = f"{match_nuevo.group(1)}{match_nuevo.group(2)}{match_nuevo.group(3)}00"
                        self.logger.debug(f"Encontrado número con nuevo patrón: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    # Patrón específico para el caso con espacios opcionales
                    patron_espacios_opcionales = r'\b(\d{5})-\s*(\d{2})-\s*(\d{2})-\s*(\d{3})-\s*(\d{4})-\s*(\d{5})-\s*(\d{2})\b'
                    match_espacios = re.search(patron_espacios_opcionales, linea)
                    if match_espacios:
                        numero = ''.join(match_espacios.groups())
                        self.logger.debug(f"Encontrado número con espacios opcionales: {numero}")
                        if len(numero) >= 21:
                            return numero

                    # Formato de 23 dígitos continuos
                    patron_continuo = r'\b(\d{23})\b'
                    match_continuo = re.search(patron_continuo, linea)
                    if match_continuo:
                        if len(match_continuo.group(1)) >= 21:
                            return match_continuo.group(1)
                    
                    # Nuevo patrón para capturar XXXXXXXXXXXXXX XXXXX XX
                    patron_espaciado_nuevo = r'\b(\d{16})\s+(\d{5})\s+(\d{2})\b'
                    match_espaciado_nuevo = re.search(patron_espaciado_nuevo, linea)
                    if match_espaciado_nuevo:
                        numero = f"{match_espaciado_nuevo.group(1)}{match_espaciado_nuevo.group(2)}{match_espaciado_nuevo.group(3)}"
                        self.logger.debug(f"Encontrado número con patrón espaciado nuevo: {numero}")
                        if len(numero) >= 21:
                            return numero
                
                    # Formato de 20 dígitos continuos
                    patron_continuo = r'\b(\d{20})\b'
                    match_continuo = re.search(patron_continuo, linea)
                    if match_continuo:
                        if len(match_continuo.group(1)) >= 21:
                            return match_continuo.group(1)
                    
                    # Nuevo patrón para el formato XXXXXXXXXX-YYYY-XXXXX-XX
                    patron_nuevo_formato = r'\b(\d{12})-\s*(\d{4})-\s*(\d{5})-\s*(\d{2})\b'
                    match_nuevo_formato = re.search(patron_nuevo_formato, linea)
                    if match_nuevo_formato:
                        numero = ''.join(match_nuevo_formato.groups())
                        self.logger.debug(f"Encontrado número con nuevo formato: {numero}")
                        if len(numero) >= 21:
                            return numero

                    # Nuevo patrón para capturar el formato "RADICADO : XXXXXXXXXXXXXXXXXXXXXXX"
                    patron_radicado_con_label = r'(?i)radicado\s*:\s*(\d{16})-(\d{5})'
                    match_radicado = re.search(patron_radicado_con_label, linea)
                    if match_radicado:
                        numero = match_radicado.group(1) + match_radicado.group(2) + "00"
                        self.logger.debug(f"Encontrado número con patrón radicado con label: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    # Nuevo patrón para capturar el formato "RADICADO : XXXXXXXXXXXXXXXXXXXXXXX"
                    patron_radicado_con_labelv2 = r'(?i)RADICADO\s*:\s*(\d{16})-(\d{5})'
                    match_radicadov2 = re.search(patron_radicado_con_labelv2, linea)
                    if match_radicadov2:
                        numero = match_radicadov2.group(1) + match_radicadov2.group(2) + "00"
                        self.logger.debug(f"Encontrado número con patrón radicado con labelv2: {numero}")
                        if len(numero) >= 21:
                            return numero

                    patron_rad_con_formato = r'(?i)RAD\.\s*(\d{7}\s\d{3}\s\d{3}\s\d{4}\s\d{5}\s\d{2})'
                    match_rad_con_formato = re.search(patron_rad_con_formato, linea)
                    if match_rad_con_formato:
                        numero = match_rad_con_formato.group(1).replace(" ", "")
                        self.logger.debug(f"Encontrado número con patrón RAD. con formato: {numero}")
                        if len(numero) >= 21:
                            return numero

                    #RADICACIÓN No. 76-834-40-04-001-2025-00021
                    patron_radicado_23 = r'\b(\d{2})-(\d{3})-(\d{2})-(\d{2})-(\d{3})-(\d{4})-(\d{5})\b'
                    match_radicado_23 = re.search(patron_radicado_23, linea)

                    if match_radicado_23:
                        numero = ''.join(match_radicado_23.groups()) + "00"
                        self.logger.debug(f"Encontrado número con patrón radicado 23: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    #patrón de 8 segmentos
                    patron_radicado_25 = r'\b(\d{2})-(\d{3})-(\d{2})-(\d{2})-(\d{3})-(\d{4})-(\d{5})-(\d{2})\b'
                    match_radicado_25 = re.search(patron_radicado_25, linea)

                    if match_radicado_25:
                        numero = ''.join(match_radicado_25.groups())
                        self.logger.debug(f"Encontrado número con patrón radicado 25: {numero}")
                        if len(numero) >= 21:
                            return numero

                    patron_radicado_23 = r'\b(\d{6})(\d{3})(\d{2})(\d{4})(\d{6})\b'
                    match_radicado_23 = re.search(patron_radicado_23, linea)

                    if match_radicado_23:
                        numero = ''.join(match_radicado_23.groups())
                        self.logger.debug(f"Encontrado número con patrón radicado 23: {numero}")
                        if len(numero) >= 21:
                            return numero

                    patron_radicado_desacato1 = r'\b(\d{10})\s*-\s*(\d{2})\s*-\s*(\d{9})\s*-\s*(\d{2})\b'
                    match_radicado_desacato1 = re.search(patron_radicado_desacato1, linea)

                    if match_radicado_desacato1:
                        numero = ''.join(match_radicado_desacato1.groups())
                        self.logger.debug(f"Encontrado número con patrón radicado 23 desacato1: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    patron_radicado_desacato2 = r'\b(\d{10})-(\d{2})-(\d{4})-(\d{5})-(\d{2})\b'   
                    match_radicado_desacato2 = re.search(patron_radicado_desacato2, linea)

                    if match_radicado_desacato2:
                        numero_radicado_desacato2 = ''.join(match_radicado_desacato2.groups())  
                        self.logger.debug(f"Encontrado número de radicado desacato2: {numero_radicado_desacato2}")
                        if len(numero_radicado_desacato2) >= 21:
                            return numero_radicado_desacato2

                    patron_radicado_fallo1 = r'Radicaci[óo]n:?\s*(\d{12})\s*(\d{11})'
                    patron_radicado_fallo1 = re.search(patron_radicado_fallo1, linea)
                    if patron_radicado_fallo1:
                        numero_radicado = ''.join(patron_radicado_fallo1.groups())
                        self.logger.debug(f"Encontrado número de radicado: {numero_radicado}")
                        if len(numero_radicado) >= 21:
                            return numero_radicado

                    patron_radicado_admision1 = r'(?i)radicaci[óo]n:?\s*(\d+)\s*(\d+)'
                    patron_radicado_admision1 = re.search(patron_radicado_admision1, linea)
                    if patron_radicado_admision1:
                        numero_radicado = ''.join(patron_radicado_admision1.groups())
                        self.logger.debug(f"Encontrado número de radicado: {numero_radicado}")
                        if len(numero_radicado) >= 21:
                            return numero_radicado

                    patron_radicado_cuadro = r'\b(\d{12})\s+(\d{4})\s+(\d{5})\s+(\d{2})\b'
                    match_radicado = re.search(patron_radicado_cuadro, linea)
                    if match_radicado:
                        numero_radicado = ''.join(match_radicado.groups())
                        self.logger.debug(f"Encontrado número de radicado: {numero_radicado}")
                        if len(numero_radicado) >= 21:
                            return numero_radicado
                    
                    # Patrón para capturar números de radicación con el formato XXXXXXXXXXXXXXXX-XXXXX-XX
                    patron_radicacion_guion = r'(?i)RADICACI[ÓO]N:\s*(\d{14,16})-(\d{5})-(\d{2})\b'
                    match_radicacion = re.search(patron_radicacion_guion, linea)
                    if match_radicacion:
                        numero = ''.join(match_radicacion.groups())
                        self.logger.debug(f"Encontrado número con patrón radicación con guiones: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    # patrón desacato 3 XXXXXXXXXXXX-XXXX-XXXXXX-XX
                    patron_desacato_nuevo = r'(?i)RADICADO:\s*(\d{12})-(\d{4})-(\d{6})-(\d{2})\b'
                    match_desacato_nuevo = re.search(patron_desacato_nuevo, linea)
                    if match_desacato_nuevo:
                        numero = ''.join(match_desacato_nuevo.groups())
                        self.logger.debug(f"Encontrado número con patrón desacato nuevo: {numero}")
                        if len(numero) >= 21:
                            return numero
                    
                    # Patrón para capturar radicación con puntos 76.845.40.89.001.2025.00031.00
                    patron_fallopunto = r'(?i)Radicaci[oó]n\s*No\.\s*(\d{2})\.(\d{3})\.(\d{2})\.(\d{2})\.(\d{3})\.(\d{4})\.(\d{5})\.(\d{2})'
                    match_fallopunto = re.search(patron_fallopunto, linea)
                    if match_fallopunto:
                        numero = ''.join(match_fallopunto.groups()) # Une todos los grupos en una sola cadena
                        self.logger.debug(f"Encontrado número con patrón fallopunto: {numero}")
                        if len(numero) >= 21:  # Para asegurar la longitud esperada
                            return numero
                    
                    # Patrón para capturar radicación con guiones
                    patron_auto_interlocutorio = r'(?i)Radicado\s*N[°º]?\s*[:.]?\s*(\d{5})[-\s](\d{2})[-\s](\d{2})[-\s](\d{3})[-\s](\d{4})[-\s](\d{4,6})[-\s](\d{2})'
                    match_auto_interlocutorio = re.search(patron_auto_interlocutorio, linea)
                    if match_auto_interlocutorio:
                        numero = ''.join(match_auto_interlocutorio.groups())  # Une todos los grupos en una sola cadena
                        self.logger.debug(f"Encontrado número con patrón auto_interlocutorio: {numero}")
                        if len(numero) >= 21:  # Para asegurar la longitud esperada
                            return numero
                    #Patrón para RADICADO RAD
                    patron_radicado_alternativo = r'(?i)RADICADO\s+RAD\.\s*No\.\s*(\d{5})\s+(\d{2})\s+(\d{2})\s+(\d{3})[- ](\d{4})[- ](\d{5})[- ](\d{2})'
                    match_radicado_alternativo = re.search(patron_radicado_alternativo, linea)
                    if match_radicado_alternativo:
                        numero = ''.join(match_radicado_alternativo.groups())  # Une todos los grupos en una sola cadena
                        self.logger.debug(f"Encontrado número con patrón radicado_alternativo: {numero}")
                        if len(numero) >= 21:  # Para asegurar la longitud esperada
                            return numero

                    patron_radicado_fallo2 = r'(?i)Ref\.:\s*Acci[óo]n\s+de\s+Tutela\s+(\d{2})\s+(\d{10})\s*[-]\s*(\d{4})\s+(\d{5})'
                    match_radicado_fallo2 = re.search(patron_radicado_fallo2, linea)
                    if match_radicado_fallo2:
                        numero = ''.join(match_radicado_fallo2.groups())+ '00'
                        self.logger.debug(f"Encontrado número con patrón radicado_fallo2: {numero}")
                        if len(numero) >= 21:
                            return numero
                        
                    patron_radicado_nuevo = r'\b(\d{16})-?(\d{7})\b'
                    match_radicado_nuevo = re.search(patron_radicado_nuevo, linea)
                    if match_radicado_nuevo:
                        numero = ''.join(match_radicado_nuevo.groups())
                        self.logger.debug(f"Encontrado número con patrón radicado nuevo: {numero}")
                        if len(numero) >= 21:
                            return numero
                        
                    patron_desacato3 = r'(?i)Rad\.?\s*(\d{16})-(\d{5})-(\d{2})'
                    match_desacato3 = re.search(patron_desacato3, linea)
                    if match_desacato3:
                        numero = ''.join(match_desacato3.groups())
                        self.logger.debug(f"Encontrado número con patrón radicado desacato 3 {numero}")
                        if len(numero) >= 21:
                            return numero
                        
                    patron_admision2radicac = r'(?i)RADICAC\.?\s*No\.?\s*(\d{12})\s*-\s*(\d{4})\s*-\s*(\d{5})\s*-\s*(\d{2})'
                    match_admision2radicac = re.search(patron_admision2radicac, linea)
                    if match_admision2radicac:
                        numero = ''.join(match_admision2radicac.groups())
                        self.logger.debug(f"Encontrado número con patrón radicado admision 2 radic {numero}")
                        if len(numero) >= 21:
                            return numero
                        

                    patron_radicacion23 = r'(?i)Radicaci[oó]n:?\s*(\d{5})-(\d{2})-(\d{2})-(\d{3})-(\d{4})-(\d{7})'
                    match_radicacion23 = re.search(patron_radicacion23, linea)
                    if match_radicacion23:
                        numero = ''.join(match_radicacion23.groups())
                        self.logger.debug(f"Encontrado número con patrón _radicacion23: {numero}")
                        if len(numero) >= 21:
                            return numero
                        
                    patron_desacato4 = r'(?i)Rad\.?\s*No\.?\s*(\d{2})\.(\d{3})\.(\d{2})\.(\d{2})\.(\d{3})\.(\d{4})-(\d{5})-(\d{2})'
                    match_desacato4 = re.search(patron_desacato4, linea)
                    if match_desacato4:
                        numero = ''.join(match_desacato4.groups())  
                        self.logger.debug(f"Encontrado número con patrón desacato 4: {numero}")
                        if len(numero) >= 21:
                            return numero

                        

                    # # Formatos con guiones
                    # Se comentan patrones generales ya que no estan funcionando correctamente
                    # patrones = [
                    #     r'\b(\d{12})-(\d{4})-(\d{5})\b',  # Formato: 631303187002-2024-00096
                    #     r'\b(\d{5}-\d{4}-\d{3}-\d{4}-\d{5}-\d{2})\b',
                    #     r'\b(\d{2}-\d{3}-\d{2}-\d{2}-\d{3}-\d{4}-\d{5}-\d{2})\b',
                    #     r'\b(\d{5}-\d{2}-\d{2}-\d{3}-\d{4}-\d{5}-\d{2})\b',
                    #     r'\b(\d{2}-\d{3}-\d{2}-\d{2}-\d{4}-\d{5}-\d{2})\b',
                    #     r'\b(\d{12}-\d{4}-\d{5}-\d{2})\b',
                    #     r'(?i)(?:acción\s+de\s+tutela\s+No\.?\s*)?(\d{2}-\d{3}-\d{2}-\d{2}-\d{3}-\d{4}-\d{5}-\d{2})\b',
                    #     r'\b(\d{9}-\d{3}-\d{4}-\d{5}-\d{2})\b',
                    #     r'\b(\d{5}\s\d{2}\s\d{2}\s\d{3}\s\d{4}\s\d{7})\b'
                    # ]
                
                    # for patron in patrones:
                    #     match = re.search(patron, linea)
                    #     if match:
                    #         nmroRdcdoJdcl = match.group(1)
                    #         self.logger.debug(f"Encontrado número con patrón estándar: {nmroRdcdoJdcl}")
                    #         return nmroRdcdoJdcl.replace(" ", "").replace("-", "")
            
            # Si no se encontró directamente, construir el número de radicado
            codigo_juzgado = self.buscar_CdgoJzgdo()
            numero_parcial = self.buscar_numero_parcial()

            if codigo_juzgado:
                self.codigo_juzgado_acumulado = codigo_juzgado
            if numero_parcial:
                self.numero_parcial_acumulado = numero_parcial

            if codigo_juzgado and numero_parcial:
                if '-' in numero_parcial:
                    año, numero = numero_parcial.split('-')
                else:
                # Si el número parcial ya está sin guiones, extraer año y número
                    año = numero_parcial[:4]
                    numero = numero_parcial[4:]
            
            # Construir el número completo concatenando código de juzgado + año + número
                numero_completo = f"{codigo_juzgado}{año}{numero.zfill(5)}"

                        # Validar si el número completo tiene 21 dígitos y agregar "00" al final
                if len(numero_completo) == 21:
                    numero_completo += "00"

                self.logger.info(f"Número de radicado construido: {numero_completo}")
                return numero_completo
            
            elif self.codigo_juzgado_acumulado and self.numero_parcial_acumulado:
                codigo_juzgado = self.codigo_juzgado_acumulado
                numero_parcial = self.numero_parcial_acumulado

                if '-' in numero_parcial:
                    año, numero = numero_parcial.split('-')
                else:
                # Si el número parcial ya está sin guiones, extraer año y número
                    año = numero_parcial[:4]
                    numero = numero_parcial[4:]
            
                # Construir el número completo concatenando código de juzgado + año + número
                numero_completo = f"{codigo_juzgado}{año}{numero.zfill(5)}"

                        # Validar si el número completo tiene 21 dígitos y agregar "00" al final
                if len(numero_completo) == 21:
                    numero_completo += "00"

                self.logger.info(f"Número de radicado construido: {numero_completo}")
                return numero_completo
        
        # Si solo tenemos el número parcial, lo retornamos
            elif numero_parcial:
                self.logger.info(f"Retornando número parcial encontrado: {numero_parcial}")
            # Si el número parcial tiene guiones, los removemos
                return numero_parcial.replace('-', '')            

            self.logger.warning("No se encontró ningún número de radicado")
            return None

        except Exception as e:
            self.logger.error(f"Error al buscar número de radicado: {str(e)}")
            return None

    def buscar_fchaVncmnto(self):
        """
    Busca la fecha de vencimiento del auto admisorio o plazo en el texto.
    Prioriza patrones más específicos y contextuales.
    """
        patrones = [
        # Nuevo patrón para "UN (01) DÍA"
            r't[ée]rmino\s+de\s+UN\s*\(\s*0?1\s*\)\s*D[ÍI]A',
        
        # Patrones anteriores
            r'en\s+el\s+t[ée]rmino\s+m[aá]ximo\s+de\s+un\s*d[ií]a\s*\(?\s*1\s*\)?',
        
            r'(?:un\s+)?t[ée]rmino\s+no\s+superior\s+a\s*(?:cuarenta\s+y\s+ocho|48)\s*\(?\s*48\s*\)?\s*(?:horas)',
            r'(?:en|por|dentro\s+de)\s+(?:un\s+)?t[ée]rmino\s+no\s+superior\s+a\s*(?:cuarenta\s+y\s+ocho|48)\s*\(?\s*48\s*\)?\s*(?:horas)',
        
        # Patrones generales anteriores
            r'en el t[ée]rmino de\s*(un|una|uno)\s*\(?(\d+)\)?\s*(d[ií]as|horas)',
            r'por el t[ée]rmino de\s*(un|una|uno)\s*\(?(\d+)\)?\s*(d[ií]as|horas)',
            r'por el t[ée]rmino de\s*(\w+)\s*\((\d+)\)\s*(d[ií]as|horas)',
            r'dentro de\s*(\w+)\s*\((\d+)\)\s*(d[ií]as|horas)',
            r'dentro de los\s*(\w+)\s*\((\d+)\)\s*(d[ií]as|horas)',
            r't[ée]rmino perentorio de\s*(\w+)\s*\((\d+)\)\s*(d[ía]s|horas)',
            r'cuentan con el t[ée]rmino de\s*(\w+)\s*\((\d+)\)\s*(d[ía]s|horas)',
            r'en el t[ée]rmino de\s*(\w+)\s*\((\d+)\)\s*(d[ía]s|horas)',
            r'(\w+)\s*\((\d+)\)\s*(d[ía]s|horas)',
        ]

        numeros_en_palabras = {
            "uno": 1, "un": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
            "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
            "dieciséis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
            "veinte": 20, "veintiuno": 21, "veintidós": 22, "veintitrés": 23,
            "veinticuatro": 24, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
            "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90,
            "cien": 100, "cuarenta y ocho": 48
        }

    # Limpiar y unificar el texto
        texto_limpio = self.texto.replace('\n', ' ').replace('\r', ' ').strip()
    
    # Dividir en líneas
        lineas = [linea.strip() for linea in texto_limpio.split('.')]

    # Primero, buscar el patrón específico de un día (código original)
        for linea in lineas:
            match = re.search(r'en\s+el\s+t[ée]rmino\s+m[aá]ximo\s+de\s+un\s*d[ií]a\s*\(?\s*1\s*\)?', linea, re.IGNORECASE)
            if match:
                return "1 dia"

    # Luego, buscar el nuevo patrón de UN (01) DÍA
        for linea in lineas:
            match = re.search(r't[ée]rmino\s+de\s+UN\s*\(\s*0?1\s*\)\s*D[ÍI]A', linea, re.IGNORECASE)
            if match:
                return "1 dia"

    # Si no se encuentra, continuar con los patrones anteriores
        for linea in lineas:
            for patron in patrones:
                match = re.search(patron, linea, re.IGNORECASE)

                if match:
 
                # Patrón específico para 48 horas
                    if "cuarenta y ocho" in linea.lower() or "48" in linea:
                        return "48 horas"
                
                    if len(match.groups()) >= 3:
                    # Capturar datos del match
                        numero_en_palabras = match.group(1).strip().lower()
                        numero_numerico = match.group(2)
                        unidad = match.group(3)

                    # Convertir palabras a números si es necesario
                        numero = numeros_en_palabras.get(numero_en_palabras, None)
                        if numero is None:
                            numero = numero_numerico

                    # Validar que la unidad sea "días" o "horas"
                        if numero is not None:
                            numero = int(numero)  # Asegurarnos de que sea un número entero
                            if numero > 5 and unidad.lower() in ["días", "dias"]:
                                return "48 horas"
                        return f"{numero} {unidad}"
                        
                        
    
        return "48 horas"

    def buscar_fchaTtla(self):
        patron = r"\bjuzgado\b"
        # Buscar la primera aparición de "juzgado"
        match = re.search(patron, self.texto[:800], re.IGNORECASE)
        inicioEncontrado = 0
        if match:
                inicioEncontrado = match.start()
        else:
                inicioEncontrado = 0
                
        fecha_final_procesada = self.buscar_fchaTtla_procesar(inicioEncontrado,800)
        if fecha_final_procesada == None:
           fecha_final_procesada = self.buscar_fchaTtla_procesar(0,1400)
           
           
        return fecha_final_procesada

    def buscar_fchaTtla_procesar(self,inicial,final):
        print(f"p inicial: {inicial}")    
        print(f"p final: {final}")   
        texto_encabezado = self.texto[inicial:final]
        print(f"texto encabezado inicial: {texto_encabezado}")    
        """
    Busca la fecha en el texto, la convierte al formato YYYY-MM-DD y concatena la hora.
    """
        locale.setlocale(locale.LC_TIME, 'Spanish_Spain')

        meses = {
            'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
            'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
            'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
        }

        numeros_texto = {
            'veintiocho': '28', 'veintinueve': '29', 'treinta': '30', 'treintaiuno': '31',
            'uno': '1', 'dos': '2', 'tres': '3', 'cuatro': '4', 'cinco': '5',
            'seis': '6', 'siete': '7', 'ocho': '8', 'nueve': '9', 'diez': '10',
            'once': '11', 'doce': '12', 'trece': '13', 'catorce': '14', 'quince': '15',
            'dieciséis': '16', 'diecisiete': '17', 'dieciocho': '18', 'diecinueve': '19',
            'veinte': '20', 'veintiuno': '21', 'veintidós': '22', 'veintitrés': '23',
            'veinticuatro': '24', 'veinticinco': '25', 'veintiséis': '26', 'veintisiete': '27'
        }

        def convertir_fecha(fecha):
            """
        Convierte una fecha al formato YYYY-MM-DD.
        """
            def formato_YYYY_MM_DD(dia, mes, anio):
                return f"{anio}-{int(mes):02d}-{int(dia):02d}"

            def extraer_numero(texto):
            # Si el texto ya es un número, devolverlo
                if texto.isdigit():
                    return texto

                match_parentesis = re.search(r'\((\d+)\)', texto)
                if match_parentesis:
                    return match_parentesis.group(1)
                texto_limpio = texto.lower().strip()
                return numeros_texto.get(texto_limpio, texto)

            def extraer_anio(texto):
                # Patrón para años en paréntesis
                match_parentesis = re.search(r'\((\d{4})\)', texto)
                if match_parentesis:
                    return match_parentesis.group(1)

            # Manejar "dos mil" seguido de número
                if 'dos mil' in texto.lower():
                    texto_limpio = texto.lower().replace('dos mil', '').strip()
                    for texto_num, digito in numeros_texto.items():
                        if texto_limpio == texto_num:
                            return f"20{digito.zfill(2)}"

                return texto

        # Nuevo patrón para el formato específico mencionado
            patron_especifico = r'(?:.*,\s*)?([a-zA-Zé]+|\d+)\s*(?:\((\d+)\))?\s+de\s+([a-zA-Z]+)\s+(?:del\s+)?(?:año\s+)?(?:dos mil [a-zA-Zé]+)\s*\((\d{4})\)'
            match_especifico = re.search(patron_especifico, fecha, re.IGNORECASE)
            if match_especifico:
                self.logger.debug(f"prueba akn 1:{ match_especifico.start()}")
                dia = match_especifico.group(2) if match_especifico.group(2) else extraer_numero(match_especifico.group(1))
                mes = match_especifico.group(3).lower()
                anio = match_especifico.group(4)
                mes_num = meses.get(mes, None)
                if mes_num and dia and anio:
                    try:
                        return formato_YYYY_MM_DD(dia, mes_num, anio)
                    except ValueError:
                        pass

        # Patrones existentes
            patrones_complejos = [
                r'(?:.*,\s*)?([a-zA-Zé]+|\(\d+\)|\d+)\s+(?:\([^)]+\)\s+)?de\s+([a-zA-Z]+)\s+de\s+((?:dos mil [a-zA-Zé]+|\(\d{4}\)|\d{4}))',
                r'(?:.*,\s*)?([a-zA-Zé]+|\(\d+\)|\d+)\s+(?:\([^)]+\)\s+)?de\s+([a-zA-Z]+)\s+del\s+((?:dos mil [a-zA-Zé]+|\(\d{4}\)|\d{4}))',
                r'(?:.*,\s*)?([a-zA-Zé]+|\d+)\s*\((\d+)\)\s+de\s+([a-zA-Z]+)\s+(?:del\s+)?(?:año\s+)?(?:dos mil [a-zA-Zé]+)\s*\((\d{4})\)'
            ]

            for patron in patrones_complejos:
                match = re.search(patron, fecha, re.IGNORECASE)
                if match:
                    self.logger.debug(f"prueba akn 2:{  match.group(2)}")
                    if len(match.groups()) == 4:  # Para el nuevo patrón
                        dia = match.group(2)
                        mes = match.group(3).lower()
                        anio = match.group(4)
                    else:  # Para los patrones antiguos
                        dia = extraer_numero(match.group(1))
                        mes = match.group(2).lower()
                        anio = extraer_anio(match.group(3))

                    mes_num = meses.get(mes, None)
                    if mes_num and dia and anio:
                        try:
                            return formato_YYYY_MM_DD(dia, mes_num, anio)
                        except ValueError:
                            continue
            return None

        def buscar_fechas_inicio(texto):
            self.logger.debug("caso 0")
            patrones_inicio = [
                r'^Santiago de Cali,\s*([a-zA-Z]+\s+\d{1,2}\s+de\s+[a-zA-Z]+\s+de\s+\d{4})',
                r'^[A-Za-z\s]+,\s*([a-zA-Z]+\s+\d{1,2}\s+de\s+[a-zA-Z]+\s+de\s+\d{4})',
                r'(?:.*,\s*)?([a-zA-Zé]+\s+\(\d+\)\s+de\s+[a-zA-Z]+\s+de\s+(?:dos mil [a-zA-Zé]+|\(\d{4}\)|\d{4}))',
                r'(?:.*,\s*)?([a-zA-Zé]+\s*\(\d+\)\s+de\s+[a-zA-Z]+\s+de\s+dos mil [a-zA-Zé]+\s*\(\d{4}\))',
                r'(?:.*,\s*)?([a-zA-Zé]+|\d+)\s*\((\d+)\)\s+de\s+([a-zA-Z]+)\s+(?:del\s+)?(?:año\s+)?(?:dos mil [a-zA-Zé]+)\s*\((\d{4})\)'
            ]

            primeras_lineas = texto.split('\n')[:5]
            texto_primeras_lineas = ' '.join(primeras_lineas)

            for patron in patrones_inicio:
                match = re.search(patron, texto_primeras_lineas, re.IGNORECASE)
                if match:
                    self.logger.debug(f"prueba akn 3:{match.start}")
                    if len(match.groups()) == 4:  # Para el nuevo patrón específico
                        fecha_encontrada = f"{match.group(1)}({match.group(2)}) de {match.group(3)} del año dos mil veinticinco ({match.group(4)})"
                    else:
                        fecha_encontrada = match.group(1)
                    fecha_convertida = convertir_fecha(fecha_encontrada)
                    if fecha_convertida:
                        return fecha_convertida

            return None
        
        def buscar_fechas_inicio_bloque2(texto_encabezado):
            meses = {
            "ENERO": 1, "FEBRERO": 2, "MARZO": 3, "ABRIL": 4, "MAYO": 5, "JUNIO": 6,
            "JULIO": 7, "AGOSTO": 8, "SEPTIEMBRE": 9, "OCTUBRE": 10, "NOVIEMBRE": 11, "DICIEMBRE": 12,
             "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
             "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
             "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
            }
            
            numeros_escritos = {
                "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
                "cinco": 5, "seis": 6, "siete": 7, "ocho": 8,
                "nueve": 9, "diez": 10, "once": 11, "doce": 12,
                "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16, "dieciseis": 16,
                "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
                "veintiuno": 21, "veintidós": 22, "veintidos": 22, "veintitrés": 23,"veintitres": 23, "veinticuatro": 24,
                "veinticinco": 25, "veintiséis": 26,"veintiseis": 26, "veintisiete": 27,
                "veintiocho": 28, "veintinueve": 29, "treinta": 30, "treinta y uno": 31 , "Treintaiuno": 31 , "Treintauno": 31,
                "treintauno": 31
            }
            
            def convertir_a_ano(anio_texto):
                if 'mil' in anio_texto:
                    partes = anio_texto.split('mil')
                    if partes[1].strip():  # Si tiene parte del año después de "mil"
                        return 2000 + numeros_escritos.get(partes[1].strip(), 0)
                    else:  # Si solo es "dos mil"
                        return 2000
                else:
                    return int(anio_texto)
    
            print('fecha:');  
            
            print(texto_encabezado)
           
        # match_fecha = re.search(r"(?:Fecha:|fecha|FECHA:|Fecha :)\s*(.*)", texto_encabezado)
            patron_fecha_inicial = r"(?i)(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\s+(\d{1,2})\s+de\s+(\d{4})"
            match_fecha = re.search(patron_fecha_inicial, texto_encabezado)
            
           
            patron_fecha = r"\b(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre),?\s*(?:[a-z]+)?\s*(?:\(\d{1,2}\)|\d{1,2})\s*de\s*(?:dos mil|mil novecientos|mil ochocientos|mil setecientos)?\s*[a-z]+\s*\(\d{4}\)"
                                        
            
            patron_fecha1 = r"""
                                \b
                                (?:(\d{1,2}|(?:uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|dieciséis|diecisiete|dieciocho|diecinueve|veinte|veintiuno|veintidós|veintitrés|veinticuatro|veinticinco|veintiséis|veintisiete|veintiocho|veintinueve|treinta|treinta y uno))\s+de\s+)  # Día en dígitos o palabras
                                (enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)  # Mes
                                \s+(?:del\s+)?  # Manejo opcional de "del"
                                (\d{4})  # Año en formato de 4 dígitos
                            """
                            
            patron_fecha2 = r"""
                            \b
                            (?:(?:\d{1,2}|(?:uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|dieciséis|diecisiete|dieciocho|diecinueve|veinte|veintiuno|veintidós|veintitrés|veinticuatro|veinticinco|veintiséis|veintisiete|veintiocho|veintinueve|treinta|treinta y uno))\s*(?:de)?)?  # Día en dígitos o palabras
                            \s*(?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)  # Meses
                            \s*[,;]?  # Separadores opcionales
                            \s*(?:(?:\(\d{1,2}\))|\d{1,2}|(?:uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|dieciséis|diecisiete|dieciocho|diecinueve|veinte|veintiuno|veintidós|veintitrés|veinticuatro|veinticinco|veintiséis|veintisiete|veintiocho|veintinueve|treinta|treinta y uno))?  # Día en dígitos, paréntesis o palabras
                            \s*(?:de)?  # Conector opcional 'de'
                            \s*(?:dos mil|mil novecientos|mil ochocientos|mil setecientos|mil seiscientos|\d{4})  # Año en texto o dígitos
                            (?:\s*\(\d{4}\))?  # Año opcional entre paréntesis
                            """      
                            
            patron_fecha3 = r"""
                            \b
                            (?:uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|
                            dieciséis|diecisiete|dieciocho|diecinueve|veinte|veintiuno|veintidós|veintitrés|veinticuatro|
                            veinticinco|veintiséis|veintisiete|veintiocho|veintinueve|treinta|treinta y uno)  # Día en texto
                            \s*\(\d{1,2}\)  # Día en número entre paréntesis
                            \s*de
                            \s*(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)  # Mes en texto
                            \s*de
                            \s*(?:dos mil(?:\s+(uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|
                            trece|catorce|quince|dieciséis|diecisiete|dieciocho|diecinueve|veinte|veintiuno|
                            veintidós|veintitrés|veinticuatro|veinticinco|veintiséis|veintisiete|veintiocho|
                            veintinueve|treinta))?)  # Año en texto
                            \s*\(\d{4}\)  # Año en número entre paréntesis
                            """               
            patronMeses = r'\b(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)\b'    
            
                            # Regex para identificar años
            
            patronYears = r"""
                    \b(?:                # Inicio de la palabra completa
                        \d{4}            # Años en formato numérico (2024)
                        |                # O bien
                        dos\s+mil(?:     # La parte inicial 'dos mil'
                            \s+(uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|
                            once|doce|trece|catorce|quince|dieciséis|diecisiete|dieciocho|
                            diecinueve|veinte|veintiuno|veintidos|veintidós|veintitres|veintitrés|veinticuatro|
                            veinticinco|veintiséis|veintisiete|veintiocho|veintinueve|
                            treinta)
                        )?
                    )\b                # Fin de la palabra completa
                    """         
            patron_numeros = r"\b(uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|once|doce|trece|catorce|quince|dieciseis|dieciséis|diecisiete|dieciocho|diecinueve|veinte|veintiuno|veintidós|veintidos|veintitres|veintitrés|veinticuatro|veinticinco|veintiseis|veintiséis|veintisiete|veintiocho|veintinueve|treinta|treintauno|treinta y uno|treinta y una|veint[once|dós|tres|cuatro|cinco|seis|siete|ocho|nueve]|[12]?\d{1,2})\b"
    
            # Buscar la fecha
            match = re.search(patron_fecha, texto_encabezado, re.IGNORECASE)
            matche1 = re.finditer(patron_fecha1, texto_encabezado, re.IGNORECASE | re.VERBOSE)
            matche2 = re.finditer(patron_fecha2, texto_encabezado, re.IGNORECASE | re.VERBOSE)
            matche3 = re.finditer(patron_fecha3, texto_encabezado, re.IGNORECASE | re.VERBOSE)
            
            matchMeses = re.finditer(patronMeses,self.eliminar_caracteres_especiales(texto_encabezado), re.IGNORECASE)
            validacionProceso = 0
            mesEncontrado = None
            def procesamientoFechas(fragmento,fragmento2,mesEncontrado):    
                                anioEncontrado = None
                                matchesYears = re.finditer(patronYears, self.eliminar_caracteres_especiales(fragmento), re.IGNORECASE | re.VERBOSE)
                                posicionAño = 0
                                posicionDia = 0
                                for match in matchesYears:
                                    anioEncontrado = match.group()
                                    posicionAño  = match.start()
                                    print(posicionAño)
                                    print(f"Año encontrado: {match.group()}")
                                    fragmento = fragmento.replace(anioEncontrado, '')
                                    break
                                    
                                # Primero eliminamos el mes
                                texto_prefinal = fragmento.replace(mesEncontrado, '')
                                
                                    
                                print("texto prefinal:" + texto_prefinal)
                                
                                matchesNro = re.findall(patron_numeros,  self.eliminar_caracteres_especiales( texto_prefinal), re.IGNORECASE)
                                diaEncontrado = None
                                
                                
                                
                                validaNumeroSuperior = 0 
                                if matchesNro:
                                    # Mostrar los resultados
                                    
                                    
                                    for matchNumero in matchesNro:
                                        diaEncontrado = matchNumero
                                        print(f"Número encontrado1: {matchNumero}")
                                        
                                        matchesNroValida= re.finditer(diaEncontrado, fragmento)
                                        for matchNumero1 in matchesNroValida:
                                            print(f"pocision dia:{matchNumero1.start()}")
                                            print(f"pocision anio:{posicionAño}") 
                                        if matchNumero1.start() > posicionAño:
                                            validaNumeroSuperior = 1
                                        
                                        break
                                else:
                                    validaNumeroSuperior = 1
                                        
                                        
                                if  validaNumeroSuperior == 1:
                                    matchesNro = re.findall(patron_numeros, fragmento2, re.IGNORECASE)
                                    for matchNumero in matchesNro:
                                        diaEncontrado = matchNumero
                                        print(f"Número encontrado2: {matchNumero}")
                                        
                                if diaEncontrado.isdigit() and int(diaEncontrado) > 31:     
                                    matchesNro = re.findall(patron_numeros, fragmento2, re.IGNORECASE)
                                    for matchNumero in matchesNro:
                                        diaEncontrado = matchNumero
                                        print(f"Número encontrado3: {matchNumero}")   
                                                    
                        
                                if not diaEncontrado and not anioEncontrado and not mesEncontrado: # si no se encuentra los valores se devuelve vacio el valor
                                    return None    
                                else:
                                    validacionProceso = 1 
                                            
                                    
                                # Convertir el año a número
                                ano_numero = convertir_a_ano(anioEncontrado.lower())  # Convertir el año escrito a numérico

                                # Convertir el día de texto a número
                                if not diaEncontrado.isdigit():
                                    dia_numero = numeros_escritos[diaEncontrado.lower()]  # Convertir el día escrito a numérico
                                else:
                                    dia_numero =  diaEncontrado  

                                # Crear la fecha en formato yyyy-mm-dd
                                print(dia_numero)
                                print(ano_numero)
                                fecha_final_encontrada = str(dia_numero) + ' ' + mesEncontrado + ' ' + str(ano_numero)
                                print(f"prueba: {fecha_final_encontrada}")
                                
                                fecha_procesada = dateparser.parse(fecha_final_encontrada, languages=['es'])
                                if fecha_procesada:
                                
                                    print(f"fecha procesada final: {fecha_procesada}")
                                    return fecha_procesada.strftime('%Y-%m-%d')  
                        
            def obtener_fecha_mas_reciente(fechas):
                    # Convertir las fechas de string a objetos datetime
                    fechas_dt = [fecha.strip() for fecha in fechas if len(fecha.strip()) == 10]
                    print("Fechas atrapadas:", fechas_dt)
                    
                    # Ordenar las fechas en orden descendente
                    fechas_dt.sort(reverse=True)
                    
                    # Obtener la fecha actual
                    hoy = datetime.today().strftime('%Y-%m-%d')
                    
                    # Buscar la fecha más reciente que no sea superior a hoy
                    for fecha in fechas_dt:
                        if fecha <= hoy:
                            return fecha
                    
                    # Si todas las fechas son mayores a hoy, devolver la siguiente más reciente
                    return fechas_dt[-1] if fechas_dt else None           
            try:
                if matchMeses:    
                    print("caso 3")
                    fecha_lista = []
                    for match in matchMeses:
                        inicio = match.start()
                        # Extraer desde el inicio del mes hasta 40 caracteres después
                        print(inicio)
                        fragmento = texto_encabezado[inicio+2:inicio+88]
                        fragmentoAntes= inicio-15
                        fragmento2 = texto_encabezado[fragmentoAntes:inicio+10]
                        print("texto:" + fragmento)
                        print("texto2:" + fragmento2)
                        print(f"Mes encontrado: {match.group()}")
                        mesEncontrado = match.group().strip().lower() 
                        resultado = procesamientoFechas(fragmento, fragmento2, mesEncontrado)
                        if resultado is not None:
                            fecha_lista.append(resultado)
                        print(f"fecha lista:{fecha_lista}")
                        
                    return obtener_fecha_mas_reciente(fecha_lista)
                        
                        
                elif matche2 and validacionProceso == 0:
                                print("caso 4")
                                                                        
                                for match in matche1:
                                    fecha_texto = match.group()
                                    print(f"Fecha encontrada: {fecha_texto}")
                                    texto_encabezado.logger.info(fecha_texto)
                                    # Usar dateparser para analizar la fecha
                                    fecha_procesada = dateparser.parse(fecha_texto, languages=['es'])
                                    # fecha_procesada = parser.parse(fecha_texto, fuzzy=True) 
                                    if fecha_procesada:
                                        validacionProceso = 1
                                        return fecha_procesada.strftime('%Y-%m-%d')
                                    
                                for match in matche2:
                                    fecha_texto = match.group()
                                    print(f"Fecha encontrada: {fecha_texto}")
                                    # Usar dateparser para analizar la fecha
                                    fecha_procesada = dateparser.parse(fecha_texto, languages=['es'])
                                    # fecha_procesada = parser.parse(fecha_texto, fuzzy=True) 
                                    if fecha_procesada:
                                        validacionProceso = 1
                                        return fecha_procesada.strftime('%Y-%m-%d')
                                    
                                    
                                for match in matche3:
                                    fecha_texto = match.group()
                                    print(f"Fecha encontrada: {fecha_texto}")
                                    texto_encabezado.logger.info(fecha_texto)
                                    # Usar dateparser para analizar la fecha
                                    fecha_procesada = dateparser.parse(fecha_texto, languages=['es'])
                                    # fecha_procesada = parser.parse(fecha_texto, fuzzy=True) 
                                    if fecha_procesada:
                                        validacionProceso = 1
                                        return fecha_procesada.strftime('%Y-%m-%d')            
                    
                elif match:
                    print("caso 2")
                    fecha_texto = match.group()
                    print(f"Fecha encontrada: {fecha_texto}")

                    # Usar dateparser para analizar la fecha
                    fecha_procesada = parser.parse(fecha_texto, fuzzy=True)
                    if fecha_procesada:
                        return fecha_procesada.strftime('%Y-%m-%d')
                    else:
                        return None
                else:
                    return None
                
            
                            
                            
            except Exception as e:
                    self.logger.error(f"Error al generar fecha tutela: {e}", exc_info=True)
                    return None    
                        
    # Intentar extraer del encabezado con las formatos mas atipícos y estandarizados
        texto_encabezado = self.texto[inicial:final]
        fecha_inicio = buscar_fechas_inicio_bloque2(texto_encabezado)
        if fecha_inicio:
            return self.concatenar_hora(fecha_inicio) 
        
    # Primero buscar fecha al inicio del documento
        texto_encabezado = self.texto[inicial:final]
        fecha_inicio = buscar_fechas_inicio(texto_encabezado)
        if fecha_inicio:
            return self.concatenar_hora(fecha_inicio)

    # Intentar extraer del encabezado
        texto_encabezado = self.texto[inicial:final]
        fecha_convertida = convertir_fecha(texto_encabezado)
        if fecha_convertida:
            return self.concatenar_hora(fecha_convertida)    

    # Patrones adicionales para buscar fechas
        patrones_fechas = [
            r'\bFECHA\s*(\d{1,2} de [a-zA-Z]+ de \d{4})\b',
            r'(\b\d{1,2}[/-]\d{1,2}[/-]\d{4}\b)',
            r'(\b\d{1,2} de [a-zA-Z]+ de (\d{4}|dos mil \d{2})\b)',
            r'(\b\d{1,2} de [a-zA-Z]+ del (\d{4}|dos mil \d{2})\b)'
        ]

        for patron in patrones_fechas:
            match = re.search(patron, texto_encabezado, re.IGNORECASE)
            if match:
                fecha_encontrada = match.group(1)
                fecha_convertida = convertir_fecha(fecha_encontrada)
                if fecha_convertida:
                    return self.concatenar_hora(fecha_convertida)

        return None
    
    def eliminar_caracteres_especiales(self,texto):
        return utils.eliminar_caracteres_especiales(texto)

    def concatenar_hora(self, fecha):
        if self.fechacorreo == None:
          fechaCorreoFinal = '2025-01-17 10:05:00'
        else:
          fechaCorreoFinal =  self.fechacorreo  
        
        try:
            print(f"Fecha extraída: {fecha}")
            print(f"Fecha correo original: {fechaCorreoFinal}")
 
            try:
                fecha_correo = datetime.strptime(fechaCorreoFinal, "%Y-%m-%d %H:%M:%S.%f")
            except ValueError:
                fecha_correo = datetime.strptime(fechaCorreoFinal, "%Y-%m-%d %H:%M:%S")
 
            fecha_con_hora = datetime.strptime(fecha, "%Y-%m-%d").replace(
                hour=fecha_correo.hour,
                minute=fecha_correo.minute,
                second=fecha_correo.second,
                microsecond=0
            )
 
            return fecha_con_hora.strftime("%Y-%m-%d %H:%M:%S") + ".000"
 
        except Exception as e:
            self.logger.error(f"Error al concatenar hora: {e}", exc_info=True)
            return None 

    def buscar_nombre_juzgado(self):
        """
        Busca el nombre completo del juzgado en el texto, limitado a un máximo de dos líneas consecutivas.
        Excluye correos electrónicos y palabras irrelevantes, y limpia el resultado según reglas específicas.
        Se detiene después de encontrar la primera coincidencia válida completa.
        """
        try:
            nombre_juzgado = ""
            patron_juzgado = r'JUZGADO\s+([A-Za-záéíóúÁÉÍÓÚ\d\s()]+)'  # Patrón principal
    
            delimitadores_fin = [
                r'\bPALACIO\b',
                r'\bAUTO\s+N[o°]?\.*\s*\d*\b',
                r'\bDE TUTELA\s+N[o°]?\.*\s*\d*\b',
                r'\bIDENTFICACION\b',
                r'\bCRA\b',
                r'\bCarrera\b',
                r'\bRADICAC[IÓ]?[OÓ]N\s*(?:N[o°]?\.*\s*)?(?:\d+-)?\d*\b',
                r'\bRAD[.: ]+\d*\b',
                r'\bRda\b.*',  
                r'\bACCION\b',
                r'\bAuto\b',
                r'\bproceso\b',
                r'\bDireccion\b',
                r'\bno\b',
                r'\binterlocutorio\b',
                #en prueba
                r'\bJuzgado\b',
                r'\bS E C R E T A R I A\b',
                r'\bproyecto\b',
                r'\bDENTIFICACION\b',
                r'\bIDENTIFICACION\b',
                r'\bEMAIL\b',
                r'\bNoviembre\b',
                r'\bSENTENCIA\b',
                r'\bAsunto\b',
                r'\bRAD\b',
                r'\bCorreo\b',
                r'\bOctubre\b',
                r'\bCelular\b',
                r'\bINCIDENTE\b',
                r'\bSEDE\b',
                r'\b19573\b',
                r'\bcodigo\b',
                r'\bCalle\b',
            ]

            palabra_irrelevante = r'\bCARRERA\b'
            frases_excluir = [
                r'(SENTENCIA DE TUTELA No)',
                r'(\d+\s*SENTENCIA DE TUTELA Nro)',
                
            ]
            patron_correo = r'\S+@\S+\.\S+'
            patron_telefono = r'(?i)\bTelefono\b.*'
        
            for i, linea in enumerate(self.lines):
                if "Juzgado" in linea or "JUZGADO" in linea:
                    match = re.search(patron_juzgado, linea, re.IGNORECASE)
                    if match:
                        nombre_temp = match.group(1).strip()

                        # Verificar la línea siguiente solo si es necesario
                        if i + 1 < len(self.lines):
                            siguiente_linea = self.lines[i + 1].strip()
                            siguiente_linea = re.sub(palabra_irrelevante, '', siguiente_linea, flags=re.IGNORECASE).strip()

                            # Verificar delimitadores antes de agregar la siguiente línea
                            if not any(re.search(delim, siguiente_linea, re.IGNORECASE) for delim in delimitadores_fin) and \
                            not re.search(patron_juzgado, siguiente_linea, re.IGNORECASE):  # Nueva verificación
                                nombre_temp += f" {siguiente_linea}"

                        # Eliminar correos electrónicos
                        nombre_temp = re.sub(patron_correo, '', nombre_temp).strip()

                        # Eliminar todo lo que esté después de la palabra "Telefono"
                        nombre_temp = re.sub(patron_telefono, '', nombre_temp).strip()

                        # Aplicar todos los delimitadores
                        for delim in delimitadores_fin:
                            match_delim = re.search(delim, nombre_temp, re.IGNORECASE)
                            if match_delim:
                                nombre_temp = nombre_temp[:match_delim.start()].strip()

                        # Eliminar frases específicas
                        for frase_excluir in frases_excluir:
                            if re.search(frase_excluir, nombre_temp, re.IGNORECASE):
                                nombre_temp = re.split(frase_excluir, nombre_temp, maxsplit=1)[0].strip()

                        # Eliminar palabras repetidas
                        palabras = nombre_temp.split()
                        palabras_unicas = []
                        for palabra in palabras:
                            if not palabras_unicas or palabra.lower() != palabras_unicas[-1].lower():
                                palabras_unicas.append(palabra)
                        nombre_temp = " ".join(palabras_unicas)

                        # Verificar y eliminar "Santiago de Cali" si aparece más de una vez
                        ocurrencias = nombre_temp.upper().count("SANTIAGO DE CALI")

                        if ocurrencias > 1:
                            primera_pos = nombre_temp.upper().find("SANTIAGO DE CALI")
                            nombre_temp = nombre_temp[:primera_pos + len("SANTIAGO DE CALI")].strip()

                        # Eliminar "Santiago de Cali" si "DE CALI" aparece antes
                        ocurrencias = nombre_temp.upper().count("DE CALI")
                        if ocurrencias > 1 and "DE CALI" in nombre_temp.upper() and "SANTIAGO DE CALI" in nombre_temp.upper():
                            nombre_temp = nombre_temp.upper().replace("SANTIAGO DE CALI", "").strip()

                        # Eliminar "Jamundi" duplicados
                        if "JAMUNDI" in nombre_temp.upper():
                            palabras = nombre_temp.split()
                            encontrado = False
                            palabras_filtradas = []
                            for palabra in palabras:
                                if palabra.upper() == "JAMUNDI":
                                    if not encontrado:
                                        palabras_filtradas.append(palabra)
                                        encontrado = True
                                else:
                                    palabras_filtradas.append(palabra)
                            nombre_temp = " ".join(palabras_filtradas)

                        # Si encontramos un nombre válido, lo guardamos y salimos del bucle
                        if nombre_temp:
                            nombre_juzgado = nombre_temp
                            break  # Salimos después de encontrar la primera coincidencia válida

                if nombre_juzgado:  # Si ya encontramos un nombre válido, salimos del bucle principal
                    break

            return nombre_juzgado.strip() if nombre_juzgado else None

        except Exception as e:
            self.logger.error(f"Error en buscar_nombre_juzgado: {str(e)}")
            return None

    def buscar_nmbreCmpltoAccnnte(self):
        return accionante.identificar_accionante(self)

    def buscar_nmroIdntfccn(self):
        return accionante.identificar_documento_identidad(self)

    def buscar_cdgoTpoIdntfccn(self):
        return accionante.identificar_tipo_documento(self)

    def buscar_CdgoJzgdo(self):
        """
    Obtiene el código de juzgado.
    1. Si el número de radicado existe, retorna los primeros 12 dígitos.
    2. Si no, busca el código del juzgado basado en su nombre en el CSV.

    Returns:
        str: Los primeros 12 dígitos del número de radicado o el código del juzgado.
    """
        try:
        # 1. Intentar obtener los primeros 12 dígitos del número de radicado
            nmro_radicado = self.buscar_nmroRdcdoJdcl()  # Llamada a la función de búsqueda del número de radicado
            if nmro_radicado:
                self.agregar_nmro_rdcdo_jdcl(nmro_radicado)
                # Asegurar que tiene al menos 12 caracteres
                if len(nmro_radicado) >= 12:
                    codigo_radicado = nmro_radicado[:12]
                    self.logger.info(f"Número de radicado encontrado, primeros 12 dígitos: {codigo_radicado}")
                    return codigo_radicado
                else:
                    self.logger.warning(f"El número de radicado es demasiado corto: {nmro_radicado}")

        # 2. Si no existe número de radicado, buscar el código del juzgado
            nombre_juzgado = self.buscar_nombre_juzgado()
            if nombre_juzgado:
            # Buscar el código del juzgado en el CSV
                codigo_juzgado = self.buscar_codigo_juzgado(nombre_juzgado)
                if codigo_juzgado:
                    self.logger.info(f"Código de juzgado obtenido del CSV: {codigo_juzgado}")
                # Rellenar con ceros a la izquierda si es necesario para completar 12 caracteres
                    return str(codigo_juzgado).zfill(12)
        
        # 3. Si no se encuentra nada
            self.logger.warning("No se pudo determinar el código de juzgado.")
            return None

        except Exception as e:
            self.logger.error(f"Error en buscar_CdgoJzgdo: {str(e)}")
            return None

    def buscar_mddaPrvcnl(self):
        return determinar_medida(self)

    def buscar_calidad_de_parte(self):
        return identificar_parte(self)

    def buscar_ano_radicado(self, fchaTtla=None):
        """
    Busca el año de radicación en el texto a partir del número de radicado o la fecha de emisión.
    Si se proporciona una fecha, extrae directamente el año.
    """
    # Si se proporciona la fecha, extraer el año de esa fecha
        if fchaTtla:
            return fchaTtla.split('-')[0]  # Extrae el año del formato YYYY-MM-DD

    # Patrón para capturar el año del número de radicado (13 dígitos antes del año)
        patron_radicado = r'\b(?:\d{2}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}[-\s]?\d{3}[-\s]?)(\d{4})[-\s]?\d{5}[-\s]?\d{2}\b'

    # Buscar el número de radicado en el texto
        for line in self.lines:
            match = re.search(patron_radicado, line)
            if match:
                return match.group(1)  # Devuelve el año extraído del número de radicado

    # Si no se encuentra un número de radicado, buscar directamente un año en contexto
        for line in self.lines:
            if "emisión" in line.lower() or "fecha de emisión" in line.lower():
                patron = r'\b(\d{4})\b'
                match = re.search(patron, line)
                if match:
                    return match.group(0)  # Devuelve el año encontrado en la línea

    # Si no se encuentra nada, retornar None
        return None
