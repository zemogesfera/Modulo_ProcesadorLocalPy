import re

def identificar_parte(objeto):
        """
    Determina si una entidad es "Accionado" o "Vinculado" según el texto.
    Retorna "1" si identifica a SOS como la entidad directamente accionada,
    y "2" si SOS aparece en los vinculados.
    """
        try:
        # Lista de términos que identifican a SOS
            terminos_sos = [
                r"SOS",
                r"S\.O\.S\.",
                r"SERVICIO\s+OCCIDENTAL\s+DE\s+SALUD",
                r"SERVICIO\s+OCCIDENTAL\s+DE\s+SALUD\s*-?\s*SOS\s*EPS",
                r"ENTIDAD\s+PROMOTORA\s+DE\s+SALUD\s+DE\s+OCCIDENTE",
                r"5\.0\.5\s*E\.?P\.?S\.?",
                r"E\.?P\.?S\.?\s*SERVICIO\s+OCCIDENTAL\s+DE\s+SALUD",
                r"E\.?P\.?S\.?\s*S\.?O\.?S\.?"
            ]

        # Patrones para identificar explícitamente al accionado o términos equivalentes
            patrones_accionado_equivalentes = [
                r"(?i)\bACCIONAD[AO]S?:?\s*([^\n,]+)",
                r"(?i)\bINCIDENTAD[AO]S?:?\s*([^\n,]+)",  # Nuevo patrón para "incidentado"
                r"(?i)vulnerados\s+por\s+([^\n,]+)",  # Detecta entidades vulneradoras
                r"(?i)ordenar\s+a\s+([^\n,]+)",      # Detecta órdenes directas a entidades
            ]

        # Patrón para identificar vinculados
            patron_vinculado = r"(?i)\bVINCULAD[AO]S?:?\s*([^\n]+)"

                # Patrón adicional para "en contra de"
            patron_contra = r"(?i)(?<=contra\s)([^\n,]+)"

        # Normalizar texto para búsqueda
            texto_completo = ' '.join(objeto.texto.split())

        # Intentar encontrar el accionado explícito o términos equivalentes
            for patron in patrones_accionado_equivalentes:
                match = re.search(patron, texto_completo)
                if match:
                    entidad_identificada = match.group(1).strip()
                    objeto.logger.info(f"Entidad identificada como accionado o equivalente: {entidad_identificada}")

                # Verificar si la entidad coincide con los términos relacionados a SOS
                    for termino in terminos_sos:
                        if re.search(termino, entidad_identificada, re.IGNORECASE):
                            objeto.logger.info("La entidad coincide con SOS.")
                            return "1"

            # Búsqueda adicional para "en contra de"
            match_contra = re.search(patron_contra, texto_completo)
            if match_contra:
                entidad_contra = match_contra.group(1).strip()
                objeto.logger.info(f"Entidad identificada en contra de: {entidad_contra}")

                for termino in terminos_sos:
                    if re.search(termino, entidad_contra, re.IGNORECASE):
                        objeto.logger.info("SOS aparece en el contexto de 'en contra de'.")
                        return "1"

        # Búsqueda secundaria: Verificar si SOS aparece en la lista de vinculados
            match_vinculados = re.search(patron_vinculado, texto_completo)
            if match_vinculados:
                vinculados_identificados = match_vinculados.group(1).strip()
                objeto.logger.info(f"Entidades identificadas como vinculados: {vinculados_identificados}")

            # Verificar si alguno de los términos de SOS está en los vinculados
                for termino in terminos_sos:
                    if re.search(termino, vinculados_identificados, re.IGNORECASE):
                        objeto.logger.info("SOS aparece en la lista de vinculados.")
                        return "2"

        # Si no se puede determinar explícitamente el accionado o vinculado
            objeto.logger.warning("No se pudo determinar explícitamente la entidad accionada o vinculada.")
            return "2"

        except Exception as e:
            objeto.logger.error(f"Error en buscar_calidad_de_parte: {e}")
            return None