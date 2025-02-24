PATRONES_ACCIONANTE = [
    # Nuevalista final que toma al afectado independiente de quien sea el agente oficio
    r'Accionante:\s*.+?,\s*en representacion de\s+(?:el sr|sra|señor|señora|senor|senora|su hija menor|su hijo menor)\s+([A-ZÁÉÍÓÚÑa-záéíóúñ ]+?)\s+Accionado',
    r'Accionante:\s*.+?\s+en calidad de Representante Legal de\s+([A-ZÁÉÍÓÚÑa-záéíóúñ ]+?)\s+Accionado',
    r"(?i)ACCIONANTE:?.*?\bAGENCIADA:?\s+([A-ZÁÉÍÓÚÑ]+(?:\s+[A-ZÁÉÍÓÚÑ]+)*)\s+INCIDENTADO:?",
    r'(?i)agente\s+oficios[oa]\s+de(?:\s+mi\s+(madre|padre|herman[oa]))?\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+con\s+cedula|\s+identificad[oa]|$)',
    r'(?i)agente\s+oficios[oa]\s+de\s+la\s+menor\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s*,|\s+domiciliad[oa]|$)',
    r'(?i)se\s+tutel[oó]\s+los\s+derechos\s+fundamentales\s+a\s+la\s+salud\s+y\s+a\s+la\s+vida\s+de\s+la\s+(?:señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)(?=\s*,|\s+ordenando)',
    r'(?i)Agenciado\s*:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)(?=\s*Accionada|$)',
    r'(?i)agente\s+oficios[oa]\s+de\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+en\s+contra|,|\s+contra|\s+identificad[oa]|$)',
    r'(?i)de\s+su\s+menor\s+hijo\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s*,|\s+identificad[oa]|$)',
    r'(?i)(?:ACTE\.?:\s*[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)\s+en\s+calidad\s+de\s+agente\s+oficios[oa]\s+de\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)',

    r'(?i)Afectada?\s*:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)(?=\s|$)',

    r'(?i)ACCIONANTE:\s*[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?\s+C\.?C\.?\s*\d+[\d\.,]*\s+actuando\s+como\s+apoderado\s+judicial\s+de\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+C\.?C\.?)',

    r'(?i)ACCIONANTE:\s*[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?\s+actuando\s+en\s+nombre\s+y\s+representaci[óo]n\s+del\s+menor\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+ACCIONADA?:|\s*$)',
    r'(?i)ACCI[OÓ]N\s+DE\s+TUTELA\s+A[CCS]IONANTE:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s*\.|\s+ACCIONADO)',

    r'(?i)ACCI[ÓO]N\s+DE\s+TUTELA\s+instaurada\s+por\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+y\s+coadyuvada)',

    r'(?i)acci[óo]n\s+de\s+tutela\s+instaurada\s+por\s+(?:el\s+)?(?:ciudadano|ciudadana|señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=,?\s+en\s+contra\s+de)',
    r'(?i)tutela\s+interpuesta\s+por\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)\s+contra',
    r'(?i)en\s+nombre\s+y\s+representaci[óo]n\s+de\s+la\s+menor\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)(?=\s+RC\.|\s+eleva|\s*$)',
    r'(?i)quien actúa como agente oficioso\s+de\s+su\s+hij[oa]\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)(?=,|\s+en\s+contra\s+de|\s+\()',
    r'(?i)Accionante:\s+[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?\s+como\s+agente\s+oficioso\s+de\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)',
    r'(?i)Beneficiaria:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)',
    r'dignidad humana del\s+(?:sr|senor|sra|senora|señor|señora)\s+([A-ZÁÉÍÓÚÑa-záéíóúñ ]+?)\s+y\s+se\s+ordeno',
    r"como agente oficiosa de ([A-Z\s]+?)\s+(?:por|para|en contra de|contra de|contra)",

    #Patrones existentes
    r'(?i)tutela\s+instaurada\s+por\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+quien\s+act[úu]a\s+(?:a\s+trav[ée]s\s+de\s+)?agente\s+oficios[oa])',

    r'(?i)instaurada\s+por\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)\s+(?:como\s+)?agente\s+oficios[oa]\s+de\s+[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+',
    
    # Nuevo patrón específico para agente oficioso
    r'(?i)instaurada\s+por\s+(?:el|la)\s+(?:ciudadano|ciudadana|señor|señora)\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s*,\s*quien\s+act[úu]a\s+como\s+agente\s+oficios[oa])',
    
    # Nuevo patrón específico para informes secretariales
    r"(?i)ACCIONANTE:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+)(?=\s+APODERADA|$)",
    r'(?i)La\s+accionante\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+subsano\s+la\s+tutela)',

    r'(?i)se\s+dispone\s+a\s+avocar,\s+estudiar\s+y\s+decidir\s+respecto\s+de\s+la\s+(?:acción|accion)\s+de\s+tutela\s+instaurada\s+por\s+([A-ZÁÉÍÓÚÑ]+(?:\s+[A-ZÁÉÍÓÚÑ]+){1,3})\s+en\s+contra\s+de',
    r'(?i)acci[óo]n\s+de\s+tutela\s+instaurada\s+por\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+contra\b|\s+en\s+contra\s+de\b)',

    r'(?i)acci[óo]n\s+de\s+tutela\s+(?:interpuesta|que\s+ha\s+sido\s+interpuesta)\s+por\s+(?:la\s+)?señora\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?),?\s*(?:-?CC\s*\d+\.\d+\.\d+)?(?=\s*,?\s*en\s+contra\s+de)',
    r'(?i)ACCIONANTE\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+)(?=\s+ACCIONADA|$)',
    r'(?i)incoada\s+por\s+(?:el\s+|la\s+)?(?:ciudadano|ciudadana|señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=,|\s+dirigida\s+en\s+contra)',

    r'(?i)Como\s+quiera\s+que\s+la\s+Acci[óo]n\s+de\s+Tutela\s+presentada\s+por\s+(?:el\s+|la\s+)?(?:señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=,\s*quien\s+act[úu]a)',
    r'(?i)(?:actuando\s+en\s+calidad\s+de|quien\s+actúa\s+en\s+calidad\s+de)\s+agente\s+ofici[oa]s[oa]\s+del\s+(?:señor|señora)?\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s*,|\s*dentro|\s*$)',
    r'(?i)\bACCIONANTE\s*:\s*([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?:\s+[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+){1,3})(?=\s|$)',
    r'(?i)\bACCIONANTE\s*:\s*([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+\s+[A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)\b',
    r'(?i)acci[óo]n\s+de\s+tutela\s+instaurada\s+por\s+(?:el\s+)?(?:señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s*,\s*identificad[oa]?\s+con)',
    r'(?i)asunto\s*:\s*acci[óo]n\s+de\s+tutela\s+([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)\s+identificad[oa]\s+con\b',
    r'(?i)accionante\s*:\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)\.',
    r'(?i)accionante\s*:\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s*ACCIONADO|ACCIONADA|$)',
    r'(?i)ACCIONANTE\s+([A-ZÁÉÍÓÚÑa-záéíóúñ]+(?:\s+[A-ZÁÉÍÓÚÑa-záéíóúñ]+)+)(?=\s*ACCIONADO|ACCIONADA|$)',
    r'(?i)impetrada\s+por\s+el\s+(?:señor|señora|sr|sra)?\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s*en\s+contra|,|$)',
    r'(?i)accionante\s{1,}\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)(?=\s*ACCIONADO|ACCIONADA|$)',
    r'(?i)accionante\s*:\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?),\s*identificada?\s+con\b',
    r'(?i)yo,\s+([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+),\s+mayor\s+de\s+edad,\s*identificada?\s+con\b',
    r'(?i)yo,\s+([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+),\s+mayor\s+de\s+edad,\s*identificada?\s+con\b.*?presento\s+esta\s+acción\s+de\s+tutela',
    r'(?i)acci[óo]n\s+de\s+tutela\s+por\s+el\s+(?:señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)\s+identificad[oa]\s+con\b',
    r'(?i)(?:primero|primero\s*:\s*)?avocar\s+(?:el\s+)?conocimiento\s+de\s+la\s+acci[óo]n\s+de\s+tutela\s+por\s+el\s+(?:señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)\s+identificad[oa]\s+con\b',
    r'(?i)accionante\s*:\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)\s+identificado\b',
    
    # Nuevo patrón para capturar nombres en informes secretariales
    # Patrón adicional más específico para el formato de informe secretarial
    r'(?i)INFORME\s+SECRETARIAL:.*?tutela\s+instaurada\s+por\s+(?:el\s+)?(?:ciudadano|ciudadana|señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=,?\s+en\s+contra)',
    r'(?i)acci[óo]n\s+de\s+tutela\s+No\.\s+\d+-\d+\s+promovida\s+por\s+la\s+(?:señora|señor|ciudadana|ciudadano)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?),\s+identificada?\s+con\s+c[ée]dula\s+de\s+ciudadan[íi]a\s+No\.\s+\d+',
    r'(?i)yo,\s+([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+),\s+mayor\s+de\s+edad,\s*identificada?\s+con\b.*?presento\s+esta\s+acción\s+de\s+tutela',
    r'(?i)(?:primero|primero\s*:\s*)?avocar\s+(?:el\s+)?conocimiento\s+de\s+la\s+acci[óo]n\s+de\s+tutela\s+por\s+el\s+(?:señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)\s+identificad[oa]\s+con\b',
    # r'(?i)(?:el\s+)?(?:señor|señora|sr\.?|sra\.?)?\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=,\s*identificad[oa]?\s+con\s+c[ée]dula)',
    r'(?i)acci[óo]n\s+de\s+tutela\s+instaurada\s+por\s+(?:el\s+|la\s+)?(?:señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+en\s+representaci[óo]n\s+de)',
    r'(?i)donde\s+(?:el|la)\s+(?:ciudadano|ciudadana)\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?),\s+identificad[oa]\s+con\s+(?:la\s+)?[Cc]\.?[Cc]\.?\s+No\.',
    r'(?i)Tr[áa]mite\s+Acci[óo]n\s+de\s+Tutela\.\s+Accionante\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\.\s+Accionados?|$)',
        
    # Nuevo patrón específico para capturar nombre con C.C.
    r'(?i)Accionante\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)\s+C\.?C\.?\s+[\d\.,]+\b',
    r'(?i)instaurada\s+por\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+?),?\s*[Cc]\.?[Cc]\.?\s*[\d\.]+',
    
    
    # Patrón para "en calidad de agente oficiosa de su hija"
    r'(?i)en\s+calidad\s+de\s+agente\s+oficios[oa]\s+de\s+su\s+(?:hija|hijo)\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=,|\.|$)',

    # Patrón para "de su agenciada"
    r'(?i)de\s+su\s+agenciada\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=,|\.|$)',

    r'(?i)interpuesta\s+por\s+(?:el\s+|la\s+)?(?:señor|señora|ciudadano|ciudadana)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)\s+CC\.\s+\d+',
    r'(?i)AGENCIADA\s*:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+AGENTE\s+OFICIOSO)',
    r'(?i)se\s+concedi[oó]\s+el\s+amparo\s+constitucional\s+invocado\s+por\s+(?:el\s+|la\s+)?(?:señor|señora|ciudadano|ciudadana)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=,|\.|\s+en\s+garantía)',
    r'(?i)Agenciado\s*:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+Accionado:)',
    r'(?i)Incidentalista\s*:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)(?=\s*Incidentado)',

    r'(?i)acci[óo]n\s+de\s+tutela\s+promovida\s+por\s+(?:el\s+|la\s+)?(?:señor|señora|sr\.?|sra\.?)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=,?\s+contra)',
    
    #nuevo patrón más flexible:
    r'(?i)acci[óo]n\s+de\s+tutela\s+promovida\s+por\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=,|\s+por|\s+contra|\.|$)',

    r'(?i)incidentante:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)(?=\s*\n|\s*incidentado:)',

    r'(?i)\bPac(?:iente|lonte|lente|iente)[:\s]*([A-ZÁÉÍÓÚÑ]+(?:\s+[A-ZÁÉÍÓÚÑ]+){1,3})\b',
    r'(?i)INCIDENTANTE\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s*\.\s*-?\s*C\.C\.|\s*$)',
    
    # Versión más flexible que maneja variaciones en los separadores                
    r'(?i)INCIDENTALISTA:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s*[–-]\s*C\.C\.|\s+C\.C\.|\s*$)',
    r'(?i)INCIDENTANTE:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+DE\s+[A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)(?=\s*$|\n|ACCIONADO:)',
    r'(?i)INCIDENTALISTA:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?=\s+ACCIONADO:)',
    r'(?i)INCIDENTANTE\s*:\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+)(?=\s*\n|\s*INCIDENTADOS?:)',
    r'(?i)INCIDENT(?:ANTE|ALISTA|ISTA)[:\s]*([A-ZÁÉÍÓÚÑ]+(?:\s+[A-ZÁÉÍÓÚÑ]+){1,3})\b',
    r"promovido por\s+.*?\s+([A-ZÁÉÍÓÚÑ]{2,}(?:\s+[A-ZÁÉÍÓÚÑ]{2,})+)\s+.*?\s+contra",
    r"(?i)\b(?:la|el)\s+(?:señor|senor|señora|senora|sr|sra)?\s*([A-ZÁÉÍÓÚÑ]+(?:\s+[A-ZÁÉÍÓÚÑ]+){1,4})\s+identificad[oa]?\s+con\s+cedula.*?\bpresent[oó]?\s+accion de tutela",

    r'(?i)accion de tutela instaurada por(?:\s+el)?(?:\s+menor)?\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+?)(?:\s+a traves de|\s+a través de)',
    r'(?i)el incidente de desacato.*?propuesto por (?:el|la|los|las)?\s*(?:señor|señora|sr|sra)?\.?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+)\s+en contra',
    r"(?i)incidente de desacato.*?interpuesto por (?:el|la|los|las)?\s*(?:señor|señora|sr|sra)?\.?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+),\s+contra",
    r"(?i)accion de tutela.*?iniciada por (?:el|la|los|las)?\s*(?:señor|señora|sr|sra)?\.?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+?),\s+a trav[eé]s de",
    r'(?i)ACCIONANTES?\s*(?::|=>)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s-]+?)(?:\s*,?\s*(?:CC|C\.C\.)\s+[\d\.,]+|\s*$)',
    r'(?i)escrito presentado por\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+)(?=,\s+por medio del cual|,)',
    r'(?i)incidente de desacato propuesto por (?:el|la)?\s*ciudadano\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+)\s+contra',
    r'(?i)Accionante:\s*(?:Sra\.?|Sr\.?)?\s*([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+)\b',
    r'(?i)ADMITASE\s+la\s+presente\s+ACCION\s+DE\s+TUTELA\s+presentada\s+por\s+la\s+se[ñn]ora\s+([A-Z\s]+)\s+identificada\s+con',
    r'(?i)La\s+acci[óo]n\s+de\s+tutela\s+formulada\s+por\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+),\s+contra',
    r'(?i)(?:presente|promovida|instaurada)\s+acci[oó]n\s+de\s+tutela\s+(?:interpuesta|presentada)\s+por\s+(?:el|la)\s+s(?:e[ñn]or[a]?)?\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+?)(?:,|\s+(?:identificad[oa]|en contra|contra|con ced))',
    r'(?i)TRAMITAR\s+como\s+Incidente\s+(?:la\s+solicitud\s+de\s+)?DESACATO\s+formulad[oa]\s+por\s+(?:el|la)\s+s(?:e[ñn]or[a]?)?\s+([A-ZÁÉÍÓÚÑ][A-ZÁÉÍÓÚÑa-záéíóúñ\s]+?)(?:,|\s+(?:para|identificad[oa]|en contra|contra|con ced))',
]
