import re

def determinar_medida(objeto):
        """
    Busca si la tutela tiene Medida Provisional (SI o NO) en el texto.
    Considera múltiples formas de expresar la concesión o negación de medidas provisionales.
    """
        try:
        # Primero, buscamos "Medida Provisional:" seguido de "SI" o "NO"
            patron = r'(?i)medida\s*provisional:\s*(SI|NO)\b'
            match = re.search(patron, objeto.texto)
            if match:
                resultado = match.group(1).upper()
                objeto.logger.debug(f"Se detectó 'Medida Provisional' directamente como: {resultado}")
                return resultado

        # Patrones que indican NEGACIÓN de medida provisional
            patrones_negacion = [
                r'(?i)negar.*medida\s*provisional',
                r'(?i)no\s*se\s*concede.*medida\s*provisional',
                r'(?i)rechaza.*medida\s*provisional',
                r'(?i)sin\s*lugar.*medida\s*provisional',
                r'(?i)denegar.*medida\s*provisional',
                r'(?i)no\s*ha\s*lugar.*medida\s*provisional',
                r'(?i)admite\s*tutela,?\s*niega\s*medida\s*provisional',
                r'(?i)tercero:\s*abstenerse\s*de\s*decretar\s*la\s*medida\s*provisional',
            ]

        # Patrones que indican CONCESIÓN de medida provisional
            patrones_concesion = [
                r'(?i)(decreta|dispone|concede).*?medida\s*provisional',
                r'(?i)se\s*(decreta|dispone|concede).*?la\s*medida\s*provisional',
                r'(?i)conceder\s*la\s*medida\s*provisional',
                r'(?i)procede.*?medida\s*provisional',
                r'(?i)otorgar.*?medida\s*provisional',
                r'(?i)conceder.*?la.*?medida.*?provisional',
                r'(?i)(decretar|ordenar).*?medida.*?provisional',
            # Patrón específico para capturar casos donde hay varios párrafos entre "CONCEDER" y "MEDIDA PROVISIONAL"
                r'(?i)(?:TERCERO|SEGUNDO|PRIMERO)?:?\s*CONCEDER\b(?:.*?\n)*?.*?\bMEDIDA\s+PROVISIONAL\b',

            ]

        # Buscar contexto más amplio alrededor de "medida provisional"
            contexto = r'(?i)(?:[^\n]*?medida\s+provisional[^\n]*)'
            matches_contexto = re.finditer(contexto, objeto.texto)
            for match in matches_contexto:
                contexto_texto = match.group(0)
                objeto.logger.debug(f"Analizando contexto: {contexto_texto}")

            # Verificar primero los patrones de negación
                for patron in patrones_negacion:
                    if re.search(patron, contexto_texto):
                        objeto.logger.debug(f"Patrón de negación detectado en contexto: {patron}")
                        return 'NO'

            # Si no hay negación, verificar concesión en el contexto
                for patron in patrones_concesion:
                    if re.search(patron, contexto_texto):
                        objeto.logger.debug(f"Patrón de concesión detectado en contexto: {patron}")
                        return 'SI'

        # Búsqueda en todo el texto para patrones de concesión
            for patron in patrones_concesion:
                if re.search(patron, objeto.texto):
                    objeto.logger.debug(f"Patrón de concesión detectado en texto completo: {patron}")
                    return 'SI'

        # Si no se encontró ninguna coincidencia, devolvemos 'NO'
            objeto.logger.debug("No se detectó ningún patrón. Resultado por defecto: NO")
            return 'NO'

        except Exception as e:
            objeto.logger.error(f"Error en buscar_mddaPrvcnl: {e}")
            return 'NO'
