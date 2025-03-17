palabras_prohibidas = {'que', 'la', 'el', 'entidad', 'de', 'y', 'a', 'no',
'señor', 'señora', 'sr', 'sra', 'sres', 'sras','senor','senora',
'ciudadano', 'ciudadana', 'agente', 'oficioso', 'representante',
'teniendo', 'cuenta', 'accion', 'tutela', 'formulada', 'por',
'considerando', 'vista', 'presente', 'en', 'accionados','admitir','interpuesta','afectada',
'usted','oficiosa','como','identificado','traves','apoderado', 'accionante','parte', 'accionada',
'ha','recibido','respuesta','producto','conducta','informa','acudio', 'ante','medico','particular',
'posteriormente','ael','para', 'eps','calidad', 'tutelar', 'derecho', 'fundamental', 'seguridad', 'social',
'acuerdo','al','informe','secretarial', 'donde','indico','haber','llamada', 'del', 'cual', 'es', 'titular',
'social', 'del','quien','actua','informo','residente','esta','ciudad','deba','acudir','otras','acciones',
'constitucionales','pro','su','salud','pueda','verse','afectado','las','trabas','administrativas',
'admision','fallo','desacato','edad','anos','medida','provisional','solicito','ordene','despacho',
'correspondio','referencia','dentro','termino','proferira','decision','fondo','le','comunicara',
'oportunamente','cumplase','mi','tia','tenga','relacion','subordinacion','indefension','frente','o',
'esposa','suministro','medicamentos','prescritos','tratante','forma','oportuna','terapias','fundacion',
'fin','preste','valle','lili','nina','interpone','siendo','incumplida','ya','puede','procede',
'tramite','acdo','diagnosticada','cistitis','incidentista','te','ayeliido','nueva','sa',
'negar','favor','cumplimiento','requerimientos','occidental','sos','cedula','estado',
'yo','impetrado','amparen','derechos','fundamentales','vida','progenitora','tiene','recibir',
'radicacion','abrigar','esperanzas','representada','agt','incidentado','presento','informando',
'criterios','completos','promovida','torno','articulo','cumpliendo','niegue','prestacion',
'garantice','debida','atencion','equivocadamente','sido','interpretado','aguja','tutela','scanned','with',
'misma','tutelada','hace','sos-','aporta','rechrso','impugnacion','presentado',
'incidental','quiera','contusion','esposo','conceder','insumo','documentos','anexos',
'corrase','traslado','guardo','silencio','respecto','correspondiente','era','atendido',
'comfandi','comunicacion','femenina','masculino','genero','mujer','hombre','inscrito',
'inscrita','probado','aportados','informes','entidades','persistia','indicando','indicado',
'indicaba','indica','pretenda','proteja','protejer','concalculados','pretende','conculcados',
'diagnosticado','linfoma','hodgkin','basico','condiagnosticodeLinfomaHodgkinclasicoenfase',
'avanzada','avanzando','actuando','dirigida','aparece','reportada','beneficiaria','regimen',
'contributivo','afiliada','afiliado','aqui','debe','debiendo','deber','debo',
'rep','representando','representante','representacion','identidad','identificado',
'medio','dia','noche','numero','autorizacion','autorizo','autorizare','autorizara',
'senores','senoras','autorizado','autorizada','red','redes','servicio','servicios',
'vigente','prestador','prestadores','alto','alta','enano','enana','pequeño','grande',
'infeccion','reaccion','suministrar','suministro','suministracion','suministrando',
'requeridos','requeridas','previo','previa','finalidad','indique','exactitud','medicos',
'pretendidos','incumplidos','otra','otro','otras','otros','pertenece','pertenecio',
'pertenecera','cohorte','importante','aparte','resuelve','conducto','apodera',
'recibire','notificaciones','notificacion','notifica','preferiblemente','preferible',
'direccion','direcciones','directo','nucleo','diagnostico','diagnostica','tambien',
'discapacidad','huerfana','rara','raro','exija','pronta','identificada','identificado',
'identificandose','tanto','dispensario','ramedicas','telefono','telefonica',
'instauro','instaurada','aporto','aporte','aportando','siguiente','documentos',
'documentacion','efectivo','estan','pendiente','sujecion','torax','identificacion',
'mitigar','actora','actor','ninguno','acredita','acredita','realizacion','pasado',
'encontraba','sea','atendida','intrahospitalariamente','ARL','amparada','especial',
'cama','habitacion','acompanante','ninguna','ningun','acredite','incidentalista',
'allegaron','inaplicacion','razon','cumplido','aluminio','senalo','haya','solicitud',
'solicitado','agendamiento','defecto','brindando','confirmando','afirmacion',
'tendiente','orden','ordenarle','pacientes','pudiendo','obtener','ingresos',
'a','b','c','d','e','f','g','h','i','l','m','n','k','z','j','w','s','q','x','r','t',
'u','p','allego','origen','solicitando','declare','mediante','sufrio','sufre',
'accidente','accidentalmente','transito','conmine','argumento','argumentando',
'comparte','valoro','pruebas','trata','pago','luego','trabajo','tampoco','tuvo',
'vulnerable','vulnerabilidad','pues','tres','hijos','les','alimentos','ademas',
'usuaria','cateter','jj','remitido','porque','para','dispuso','dele','desele',
'valor','tienen','son','derivadas','labora','laboral','supuesta','incurrido',
'menores','ordena','manera','inmediata','autorice','realice','condicion',
'fumadora','me','sean','son','suministra','suministrados','extremo','octava',
'activa','activo','legitima','legitimada','presunta','actuacion',
'diabetica','diabeticos','insulina','dependiente','independiente','judicial',
'lleva','mucho','tiempo','espera','ante','ente','vulnera','consecuencia',
'emitida','sefior',
#pendiente incluir enfermades, quizas ciudades
#los de arriba son los encontrados en diferentes casos de analisis.


    # Términos generales
    'que', 'la', 'el', 'entidad', 'de', 'y', 'a', 'no', 'con', 'para', 'por', 'en', 'es', 'al', 'del', 'cual', 'cuales',
    'se', 'su', 'sus', 'este', 'esta', 'estos', 'estas', 'lo', 'los', 'las', 'un', 'una', 'unos', 'unas',
    
# Identificadores y tratamientos
'señor', 'señora', 'sr', 'sra', 'sres', 'sras', 'senor', 'senora',
'ciudadano', 'ciudadana', 'dr', 'dra', 'abogado', 'abogada',
'don', 'doña', 'sr.', 'sra.', 'lic.', 'ing.', 'prof.', 

# Ampliación de identificadores
'ciudadano', 'ciudadana', 'vecino', 'vecina', 'residente',
'habitante', 'persona', 'individuo', 'sujeto', 'representante',
'beneficiario', 'afectado', 'interesado', 'demandante', 'demandado',

# Títulos académicos y profesionales
'dr', 'dra', 'doctor', 'doctora', 'prof', 'profesor', 'profesora',
'lic', 'licenciado', 'licenciada', 'ing', 'ingeniero', 'ingeniera',
'arq', 'arquitecto', 'arquitecta', 'abg', 'abogado', 'abogada',
'med', 'medico', 'medica', 'enfermero', 'enfermera', 
'psic', 'psicologo', 'psicologa', 'economista', 'contador', 'contadora',
'odontologo', 'odontologa', 'fisioterapeuta', 'nutricionista', 
'quimico', 'quimica', 'abogado', 'abogada', 'administrador', 'administradora',

# Títulos religiosos
'padre', 'madre', 'pastor', 'sacerdote', 'monje', 'monja',
'hermano', 'hermana', 'cura', 'rabino', 'imán', 'sacerdotisa',

# Títulos nobiliarios y honoríficos
'sir', 'lady', 'lord', 'honorable', 'excelentisimo', 'excelentisima',
'ilustrisimo', 'ilustrisima', 'reverendisimo', 'reverendisima',
'duquesa', 'marques', 'marquesa', 'conde', 'condesa',

# Tratamientos formales en diferentes contextos
'sr', 'sra', 'srta', 'don', 'doña', 'señorita', 
'mister', 'miss', 'ms', 'mrs', 'mr', 'madame', 'monsieur',

# Tratamientos en contextos específicos
'apoderado', 'representante', 'tutor', 'tutora', 
'curador', 'curadora', 'defensor', 'defensora',
'gestor', 'interventor', 'mediador', 'arbitro', 'procurador',

# Identificadores en contextos legales
'demandante', 'demandado', 'accionante', 'accionado',
'querellante', 'querellado', 'recurrente', 'recurrido',
'parte', 'parte demandante', 'parte demandada', 'parte querellante',

# Títulos académicos adicionales
'licenciado', 'licenciada', 'maestro', 'maestra', 'técnico', 'técnica',
'profesor asociado', 'profesor adjunto', 'profesor titular', 'profesor emérito',

# Títulos en el ámbito médico
'cirujano', 'cirujana', 'pediatra', 'ginecólogo', 'ginecóloga',
'dermatólogo', 'dermatóloga', 'cardiólogo', 'cardióloga',
'neurólogo', 'neuróloga', 'oncólogo', 'oncóloga',

# Títulos en el ámbito educativo
'rector', 'rectora', 'decano', 'decana', 'coordinador', 'coordinadora',
'orientador', 'orientadora', 'profesor visitante', 'profesor invitado',

# Títulos en el ámbito empresarial
'gerente', 'directora', 'director', 'administrador', 'administradora',
'ejecutivo', 'ejecutiva', 'consultor', 'consultora', 'analista',

# Títulos en el ámbito político
'presidente', 'presidenta', 'senador', 'senadora', 'diputado', 'diputada',
'alcalde', 'alcaldesa', 'gobernador', 'gobernadora', 'ministro', 'ministra',

# Títulos en el ámbito social
'voluntario', 'voluntaria', 'activista', 'líder', 'lideresa',
'coordinador social', 'coordinadora social',

# Títulos en el ámbito cultural
'artista', 'escritor', 'escritora', 'poeta', 'poetisa',
'músico', 'música', 'actor', 'actriz', 'director de cine', 'directora de cine',

# Títulos en el ámbito deportivo
'atleta', 'deportista', 'entrenador', 'entrenadora', 'jugador', 'jugadora',

# Títulos en el ámbito tecnológico
'programador', 'programadora', 'ingeniero de software', 'ingeniera de software',
'analista de sistemas', 'especialista en IT', 'desarrollador', 'desarrolladora',

# Títulos en el ámbito científico
'investigador', 'investigadora', 'científico', 'científica',
'biologo', 'biologa', 'quimico', 'quimica', 'físico', 'física',

# Títulos en el ámbito legal
'juez', 'jueza', 'fiscal', 'fiscalía', 'abogado defensor', 'abogada defensora',
'notario', 'notaria', 'escribano', 'escribana',

# Títulos en el ámbito financiero
'inversionista', 'financiero', 'financiera', 'analista financiero',
'asesor', 'asesora', 'consultor financiero', 'consultora financiera',

# Títulos en el ámbito ambiental
'ecólogo', 'ecóloga', 'ambientalista', 'conservacionista',

# Títulos en el ámbito de la comunicación
'periodista', 'reportero', 'reportera', 'editor', 'editora',
'locutor', 'locutora', 'presentador', 'presentadora',

# Títulos en el ámbito de la seguridad
'policía', 'policía nacional', 'guardia', 'vigilante', 'seguridad',

# Títulos en el ámbito de la justicia
'juez', 'jueza', 'fiscal', 'defensor público', 'defensora pública',

# Títulos en el ámbito de la educación
'educador', 'educadora', 'maestro', 'maestra', 'tutor', 'tutora',

# Títulos en el ámbito de la salud
'terapeuta', 'fisioterapeuta', 'psicólogo', 'psicóloga', 'nutricionista',

# Títulos en el ámbito de la investigación
'investigador', 'investigadora', 'científico', 'científica',

# Títulos en el ámbito de la administración pública
'funcionario', 'funcionaria', 'empleado', 'empleada', 'servidor', 'servidora',

# Títulos en el ámbito de la comunidad
'miembro', 'miembra', 'voluntario', 'voluntaria', 'activista',

# Títulos en el ámbito de la familia
'padre', 'madre', 'hermano', 'hermana', 'hijo', 'hija', 'abuelo', 'abuela',

# Títulos en el ámbito de la política
'presidente', 'presidenta', 'senador', 'senadora', 'diputado', 'diputada',

# Títulos en el ámbito de la cultura
'artista', 'escritor', 'escritora', 'músico', 'música',

# Títulos en el ámbito de la religión
'padre', 'madre', 'pastor', 'sacerdote', 'rabino', 'imán',

# Títulos en el ámbito de la familia
'padre', 'madre', 'hermano', 'hermana', 'hijo', 'hija', 'abuelo', 'abuela',

# Títulos en el ámbito de la comunidad
'miembro', 'miembra', 'voluntario', 'voluntaria', 'activista',

# Títulos en el ámbito de la educación
'educador', 'educadora', 'maestro', 'maestra', 'tutor', 'tutora',

# Títulos en el ámbito de la salud (continuación)
'psicoterapeuta', 'psicoanalista', 'psiquiatra', 'psiquiatra',
'neurólogo', 'neuróloga', 'cardiólogo', 'cardióloga',
'neumólogo', 'neumóloga', 'endocrinólogo', 'endocrinóloga',
'genetista', 'epidemiólogo', 'epidemióloga', 'forense',

# Títulos en el ámbito tecnológico (continuación)
'cibernetico', 'cibernetica', 'robotista', 'nanotecnologo', 'nanotecnologa',
'especialista en inteligencia artificial', 'experto en ciberseguridad',
'arquitecto de sistemas', 'arquitecta de sistemas',

# Títulos en el ámbito científico (continuación)
'astrofísico', 'astrofísica', 'geólogo', 'geóloga', 'oceanógrafo', 'oceanógrafa',
'paleontólogo', 'paleontóloga', 'antropólogo', 'antropóloga',
'arqueólogo', 'arqueóloga', 'sismólogo', 'sismóloga',

# Títulos en el ámbito ambiental (continuación)
'climatólogo', 'climatóloga', 'geógrafo', 'geógrafa',
'especialista en recursos naturales', 'experto en sostenibilidad',

# Títulos en el ámbito deportivo (continuación)
'entrenador personal', 'preparador físico', 'nutricionista deportivo',
'fisioterapeuta deportivo', 'psicólogo deportivo',

# Títulos en contextos internacionales
'embajador', 'embajadora', 'cónsul', 'agregado', 'agregada',
'diplomático', 'diplomática', 'representante internacional',

# Títulos en el ámbito artístico
'compositor', 'compositora', 'pintor', 'pintora', 'escultor', 'escultora',
'bailarín', 'bailarina', 'coreógrafo', 'coreógrafa',

# Títulos en el ámbito de la investigación social
'sociólogo', 'socióloga', 'antropólogo', 'antropóloga',
'politólogo', 'politóloga', 'historiador', 'historiadora',

# Títulos en el ámbito de la comunicación
'comunicólogo', 'comunicóloga', 'relacionista público',
'especialista en comunicación digital', 'community manager',

# Títulos en el ámbito de la seguridad
'investigador privado', 'especialista en seguridad', 'analista de seguridad',
'consultor en prevención de riesgos', 'experto en ciberseguridad',

# Títulos honoríficos y académicos adicionales
'emérito', 'emerita', 'distinguido', 'distinguida', 'honorario', 'honoraria',
'profesor invitado', 'profesor visitante', 'investigador asociado',

# Términos de género y edad
'menor', 'adulto', 'anciano', 'joven', 'niño', 'niña',
'adolescente', 'infante', 'mayor', 'menor de edad', 'tercera edad',

# Tratamientos en diferentes idiomas y culturas
'monsieur', 'madame', 'senhor', 'senhora', 'herr', 'frau',
'señor', 'señora', 'san', 'santa', 'maestro', 'maestra',

# Identificadores en contextos específicos
'requirente', 'solicitante', 'peticionario', 'interesado',
'afectado', 'beneficiario', 'destinatario', 'usuario',

# Términos de representación legal
'representante legal', 'apoderado', 'mandatario', 'gestor',
'interventor', 'mediador', 'árbitro', 'procurador',

# Términos adicionales de identificación
'requirente', 'solicitante', 'peticionario', 'interesado',
'afectado', 'beneficiario', 'destinatario', 'usuario',
'parte interesada', 'compareciente', 'recurrente',

# Títulos en ámbitos emergentes y tecnológicos
'especialista en blockchain', 'experto en criptomonedas', 'analista de datos',
'científico de datos', 'ingeniero de machine learning', 
'especialista en transformación digital', 'arquitecto cloud',
'experto en sostenibilidad tecnológica', 'especialista en IoT',
'ingeniero de realidad virtual', 'desarrollador de inteligencia artificial',

# Títulos en ámbitos sociales y humanitarios
'trabajador social', 'trabajadora social', 'antropólogo social',
'mediador comunitario', 'promotor de derechos humanos',
'activista social', 'defensor de derechos', 'gestor de paz',
'especialista en inclusión', 'consultor de diversidad',

# Títulos en ámbitos emergentes de sostenibilidad
'consultor ambiental', 'especialista en economía circular',
'experto en energías renovables', 'ingeniero de sostenibilidad',
'analista de impacto ambiental', 'gestor de residuos',
'consultor en cambio climático', 'especialista en biodiversidad',

# Títulos en ámbitos de innovación y emprendimiento
'emprendedor', 'innovador', 'consultor de startups',
'gestor de innovación', 'especialista en transformación empresarial',
'coach de innovación', 'diseñador de experiencia de usuario',
'estratega de innovación', 'facilitador de innovación',

# Títulos en ámbitos de salud mental y bienestar
'psicoterapeuta', 'consejero', 'consejera', 'coach de bienestar',
'especialista en salud mental', 'terapeuta holístico',
'constelador familiar', 'mediador emocional',
'especialista en mindfulness', 'coach de resiliencia',

# Títulos en ámbitos de educación alternativa
'facilitador de aprendizaje', 'diseñador instruccional',
'especialista en educación inclusiva', 'coach educativo',
'mentor', 'tutor online', 'especialista en aprendizaje digital',
'desarrollador de contenidos educativos',

# Títulos en ámbitos de gestión del conocimiento
'gestor de conocimiento', 'especialista en gestión del talento',
'consultor de recursos humanos', 'analista de capital humano',
'desarrollador de cultura organizacional',
'especialista en transformación cultural',

# Títulos en ámbitos de economía colaborativa
'especialista en economía colaborativa', 'consultor de sharing economy',
'gestor de plataformas colaborativas', 'analista de modelos de negocio',
'experto en comunidades digitales',

# Títulos en ámbitos de seguridad digital
'especialista en ciberseguridad', 'analista forense digital',
'experto en seguridad de la información', 'consultor de riesgos digitales',
'especialista en protección de datos', 'arquitecto de seguridad',

# Títulos en ámbitos de comunicación digital
'estratega de contenidos', 'especialista en marketing digital',
'gestor de comunidades online', 'analista de redes sociales',
'consultor de comunicación digital', 'experto en branded content',

# Títulos en ámbitos de responsabilidad social
'consultor de responsabilidad social', 'gestor de impacto social',
'especialista en desarrollo sostenible', 'analista de impacto',
'coordinador de proyectos sociales',

# Identificadores de roles emergentes
'agente de cambio', 'facilitador', 'catalizador',
'estratega', 'visionario', 'transformador',
'conector', 'integrador', 'mediador',

# Títulos en ámbitos de diversidad e inclusión
'especialista en diversidad', 'consultor de inclusión',
'gestor de equidad', 'analista de inclusión laboral',
'promotor de diversidad', 'especialista en equidad de género',

# Términos de representación y participación
'representante', 'delegado', 'comisionado', 'enlace',
'intermediario', 'vocero', 'portavoz', 'interlocutor',








    
# Roles legales
'agente', 'oficioso', 'representante', 'apoderado', 'accionante', 'parte', 'accionada', 
'tutor', 'tutora', 'curador', 'curadora', 'defensor', 'defensora',
'mandatario', 'procurador', 'gestor', 'interventor', 'mediador', 'arbitro',

# Roles adicionales en el ámbito legal
'litigante', 'demandante', 'demandado', 'querellante', 'querellado',
'parte demandante', 'parte demandada', 'recurrente', 'recurrido',
'coadyuvante', 'coadyuvante', 'interesado', 'afectado', 'beneficiario',

# Títulos en el ámbito judicial
'juez', 'jueza', 'magistrado', 'magistrada', 'fiscal', 'fiscalía',
'notario', 'notaria', 'escribano', 'escribana', 'secretario judicial',
'auxiliar judicial', 'relator', 'relatora', 'perito', 'perita',

# Roles en el ámbito de la defensa
'abogado defensor', 'abogada defensora', 'defensor público', 'defensora pública',
'asesor legal', 'consultor jurídico', 'abogado litigante', 'abogada litigante',

# Roles en el ámbito de la mediación y arbitraje
'mediador', 'mediadora', 'árbitro', 'árbitra', 'conciliador', 'conciliadora',
'facilitador', 'facilitadora', 'negociador', 'negociadora',

# Roles en el ámbito administrativo
'funcionario', 'funcionaria', 'empleado público', 'empleada pública',
'servidor público', 'servidora pública', 'gestor administrativo',
'coordinador', 'coordinadora', 'director', 'directora',

# Roles en el ámbito de la investigación
'investigador', 'investigadora', 'analista', 'analista legal',
'consultor', 'consultora', 'especialista en derecho',

# Roles en el ámbito de derechos humanos
'defensor de derechos humanos', 'activista', 'promotor de derechos',
'coordinador de derechos humanos', 'especialista en derechos humanos',

# Roles en el ámbito de la justicia restaurativa
'facilitador de justicia restaurativa', 'mediador comunitario',
'coordinador de programas de justicia restaurativa',

# Roles en el ámbito de la protección de menores
'defensor de menores', 'abogado de menores', 'tutor legal',
'curador de menores', 'interventor de menores',

# Roles en el ámbito de la propiedad intelectual
'asesor de propiedad intelectual', 'abogado de propiedad intelectual',
'consultor de patentes', 'especialista en derechos de autor',

# Roles en el ámbito de la propiedad y bienes
'gestor de bienes', 'administrador de propiedades', 'abogado inmobiliario',
'consultor inmobiliario', 'especialista en bienes raíces',

# Roles en el ámbito de la familia
'abogado de familia', 'mediador familiar', 'tutor de familia',
'curador familiar', 'defensor de la familia',

# Roles en el ámbito de la salud
'defensor de pacientes', 'abogado de salud', 'consultor de salud',
'asesor legal en salud', 'especialista en derecho sanitario',

# Roles en el ámbito de la educación
'defensor de derechos educativos', 'abogado educativo', 'consultor educativo',
'mediador educativo', 'especialista en derecho educativo',

# Roles en el ámbito de la seguridad social
'defensor de derechos laborales', 'abogado laboral', 'consultor laboral',
'asesor en seguridad social', 'especialista en derecho laboral',

# Roles en el ámbito de la administración pública
'gestor público', 'administrador público', 'consultor en políticas públicas',
'analista de políticas públicas', 'especialista en gestión pública',

# Roles en el ámbito de la ética y la responsabilidad
'comisionado de ética', 'defensor del pueblo', 'ombudsman',
'procurador de derechos humanos', 'defensor del consumidor',

# Roles en el ámbito de la justicia penal
'abogado penalista', 'defensor penal', 'fiscal penal', 'juez penal',
'consultor en derecho penal', 'especialista en derecho penal',

# Roles en el ámbito de la justicia civil
'abogado civil', 'defensor civil', 'juez civil', 'consultor en derecho civil',
'especialista en derecho civil',

# Roles en el ámbito de la justicia administrativa (continuación)
'juez administrativo', 'magistrado administrativo', 'fiscal administrativo',
'consultor en derecho administrativo', 'especialista en contratación estatal',
'asesor de entidades públicas', 'interventor de contratos',

# Roles en el ámbito de la justicia constitucional
'defensor constitucional', 'abogado constitucionalista', 'juez constitucional',
'magistrado constitucional', 'consultor en derecho constitucional',
'especialista en garantías constitucionales', 'protector de derechos fundamentales',

# Roles en el ámbito internacional
'diplomático', 'diplomática', 'asesor internacional', 'consultor de derecho internacional',
'abogado internacional', 'especialista en derecho transnacional',
'mediador internacional', 'árbitro internacional', 'juez internacional',

# Roles en el ámbito de resolución de conflictos
'negociador', 'facilitador de conflictos', 'mediador especializado',
'conciliador extrajudicial', 'árbitro de controversias',
'especialista en resolución alternativa de conflictos',

# Roles en el ámbito de protección especial
'defensor de víctimas', 'asesor de víctimas', 'acompañante legal',
'protector de testigos', 'representante de grupos vulnerables',
'especialista en protección de derechos de minorías',

# Roles en el ámbito de la justicia restaurativa
'facilitador de justicia restaurativa', 'mediador comunitario',
'coordinador de programas de reparación', 'especialista en reconciliación',

# Roles en el ámbito de la justicia juvenil
'defensor de menores', 'juez de menores', 'fiscal de menores',
'mediador juvenil', 'especialista en derecho de la infancia',
'tutor de menores infractores', 'coordinador de programas juveniles',

# Roles en el ámbito de la protección ambiental
'defensor ambiental', 'abogado ambientalista', 'consultor en derecho ambiental',
'especialista en legislación ecológica', 'procurador ambiental',
'mediador de conflictos ambientales',

# Roles en el ámbito de la protección de datos
'defensor de datos personales', 'consultor en privacidad',
'especialista en protección de información', 'auditor de seguridad digital',
'asesor de cumplimiento de datos', 'protector de información sensible',

# Roles en el ámbito de la transparencia
'defensor de la transparencia', 'auditor', 'interventor',
'veedor', 'supervisor', 'monitor', 'fiscal de transparencia',
'especialista en gobierno abierto', 'consultor de integridad',

# Roles en el ámbito de la gestión de riesgos
'gestor de riesgos legales', 'consultor de cumplimiento',
'especialista en prevención de conflictos', 'asesor de riesgos',
'analista de mitigación legal', 'consultor de estrategia legal',

# Roles en el ámbito de la innovación legal
'innovador legal', 'consultor de transformación jurídica',
'especialista en derecho tecnológico', 'estratega legal',
'diseñador de soluciones jurídicas', 'consultor de modernización legal',

# Roles en el ámbito de la ética profesional
'consejero ético', 'comité de ética', 'defensor de la ética profesional',
'supervisor de conducta', 'auditor ético', 'consultor de integridad',

# Roles en el ámbito de la inclusión y diversidad
'defensor de la inclusión', 'especialista en equidad',
'mediador de diversidad', 'consultor de derechos humanos',
'promotor de políticas inclusivas', 'garante de derechos',

# Roles emergentes en el ámbito legal
'abogado de innovación', 'especialista en derecho digital',
'consultor de transformación legal', 'estratega de justicia tecnológica',
'mediador de conflictos digitales', 'especialista en derecho de nuevas tecnologías',

# Roles de representación y participación
'representante', 'delegado', 'comisionado', 'enlace',
'intermediario', 'vocero', 'portavoz', 'interlocutor',
'gestor de representación', 'coordinador de participación',

# Roles en el ámbito de la justicia digital y tecnológica
'especialista en derecho digital', 'abogado de tecnología', 
'consultor de transformación digital', 'experto en ciberderecho',
'asesor legal de inteligencia artificial', 'especialista en blockchain legal',
'consultor de regulación tecnológica', 'defensor de derechos digitales',
'mediador de conflictos tecnológicos', 'árbitro de disputas digitales',

# Roles en el ámbito de la inteligencia legal
'analista legal predictivo', 'estratega de litigio',
'consultor de big data jurídico', 'especialista en analítica legal',
'investigador de jurimetría', 'consultor de inteligencia legal',
'experto en machine learning jurídico', 'analista de riesgos legales',

# Roles en el ámbito de la justicia social
'defensor de justicia social', 'promotor de equidad',
'especialista en derechos de comunidades marginadas',
'consultor de políticas de inclusión', 'mediador de justicia comunitaria',
'coordinador de reparación histórica', 'defensor de memoria histórica',

# Roles en el ámbito de la justicia transicional
'especialista en justicia transicional', 'mediador de reconciliación',
'consultor de paz', 'facilitador de memoria histórica',
'asesor de procesos de reparación', 'coordinador de verdad y reparación',

# Roles en el ámbito de la justicia restaurativa avanzada
'facilitador de círculos restaurativos', 'mediador transformativo',
'especialista en diálogo reconstructivo', 'coordinador de encuentros restaurativos',
'asesor de procesos de sanación', 'facilitador de justicia comunitaria',

# Roles en el ámbito de la bioética y derecho
'bioeticista', 'consultor de ética médica', 'especialista en derecho biomédico',
'asesor de comités de ética', 'mediador de dilemas bioéticos',
'defensor de derechos reproductivos', 'especialista en ética de la investigación',

# Roles en el ámbito de la justicia climática
'defensor de justicia climática', 'especialista en derecho ambiental',
'consultor de políticas de sostenibilidad', 'mediador de conflictos ecológicos',
'asesor de derechos de la naturaleza', 'coordinador de litigio climático',

# Roles en el ámbito de la inteligencia emocional legal
'mediador empático', 'facilitador de diálogo emocional',
'consultor de comunicación legal', 'especialista en negociación transformadora',
'coach de resolución de conflictos', 'asesor de inteligencia emocional jurídica',

# Roles en el ámbito de la prospectiva legal
'futurista legal', 'estratega de escenarios jurídicos',
'consultor de tendencias legales', 'especialista en derecho prospectivo',
'investigador de innovación jurídica', 'analista de evolución legal',

# Roles en el ámbito de la justicia regenerativa
'facilitador de justicia regenerativa', 'mediador sistémico',
'especialista en reconstrucción social', 'coordinador de transformación comunitaria',
'asesor de procesos de sanación colectiva', 'defensor de resiliencia social',

# Roles en el ámbito de la gestión del conocimiento legal
'gestor de conocimiento jurídico', 'especialista en documentación legal',
'consultor de sistemas de información jurídica', 'analista de jurisprudencia',
'bibliotecario jurídico', 'curador de conocimiento legal',

# Roles en el ámbito de la neurociencia legal
'especialista en neurociencia jurídica', 'consultor de psicología legal',
'analista de comportamiento judicial', 'asesor de toma de decisiones legales',
'investigador de sesgos cognitivos en derecho', 'experto en neuroderechos',

# Roles en el ámbito de la innovación social
'innovador social', 'diseñador de sistemas de justicia',
'estratega de cambio social', 'consultor de transformación comunitaria',
'facilitador de innovación legal', 'coordinador de laboratorio de justicia',

# Roles en el ámbito de la gobernanza global
'especialista en derecho internacional', 'consultor de gobernanza global',
'mediador de conflictos internacionales', 'asesor de organizaciones multilaterales',
'estratega de diplomacia legal', 'coordinador de políticas transnacionales',





# Términos procesales
'teniendo', 'cuenta', 'accion', 'tutela', 'formulada', 'considerando', 
'vista', 'presente', 'accionados', 'admitir', 'interpuesta', 'afectada',
'usted', 'oficiosa', 'como', 'identificado', 'traves', 'mediante',
'solicitud', 'recurso', 'amparo', 'proteccion', 'vulneracion',
'presuntamente', 'considera', 'manifiesta', 'expone', 'argumenta',
'indica', 'refiere', 'sostiene', 'impetrar', 'promover',

# Términos de inicio de proceso
'iniciar', 'presentar', 'radicar', 'incoar', 'promover', 'ejercitar',
'interponer', 'demandar', 'solicitar', 'requerir', 'peticionar',
'instaurar', 'formular', 'proponer', 'plantear', 'iniciar',

# Términos de desarrollo procesal
'alegar', 'argumentar', 'manifestar', 'exponer', 'sostener', 'indicar',
'referir', 'precisar', 'aclarar', 'ampliar', 'modificar', 'ratificar',
'rectificar', 'complementar', 'adicionar', 'subsanar', 'corregir',

# Términos de pretensión y defensa
'pretender', 'defender', 'impugnar', 'recurrir', 'apelar', 'controvertir',
'objetar', 'contradecir', 'rebatir', 'refutar', 'cuestionar', 'impetrar',
'reclamar', 'exigir', 'demandar', 'solicitar', 'requerir',

# Términos de valoración probatoria
'probar', 'demostrar', 'acreditar', 'evidenciar', 'comprobar', 'constatar',
'verificar', 'validar', 'confirmar', 'corroborar', 'ratificar',
'desvirtuar', 'controvertir', 'refutar', 'objetar',

# Términos de argumentación jurídica
'fundar', 'fundamentar', 'motivar', 'razonar', 'argumentar', 'justificar',
'explicar', 'aclarar', 'precisar', 'desarrollar', 'sustentar', 'defender',
'probar', 'demostrar', 'evidenciar',

# Términos de notificación y comunicación
'notificar', 'comunicar', 'informar', 'emplazar', 'citar', 'convocar',
'requerir', 'apercibir', 'prevenir', 'advertir', 'intimar', 'conminar',

# Términos de resolución y decisión
'resolver', 'decidir', 'fallar', 'sentenciar', 'dictaminar', 'pronunciar',
'dirimir', 'laudar', 'confirmar', 'revocar', 'modificar', 'anular',
'subsanar', 'corregir', 'enmendar',

# Términos de medidas cautelares
'cautelar', 'precautelar', 'prevenir', 'proteger', 'tutelar', 'salvaguardar',
'resguardar', 'garantizar', 'preservar', 'suspender', 'interrumpir',
'paralizar', 'diferir',

# Términos de derechos y garantías
'amparar', 'proteger', 'tutelar', 'garantizar', 'defender', 'salvaguardar',
'respetar', 'restablecer', 'reparar', 'compensar', 'restaurar',
'reconocer', 'preservar', 'defender',

# Términos de participación procesal
'comparecer', 'intervenir', 'participar', 'coadyuvar', 'asistir',
'representar', 'apoderar', 'delegar', 'autorizar', 'facultar',

# Términos de valoración jurídica
'considerar', 'estimar', 'juzgar', 'evaluar', 'analizar', 'ponderar',
'examinar', 'estudiar', 'valorar', 'apreciar', 'conceptuar',
'dictaminar', 'informar',

# Términos de cumplimiento y ejecución
'cumplir', 'ejecutar', 'hacer efectivo', 'materializar', 'realizar',
'concretar', 'implementar', 'desarrollar', 'llevar a cabo',
'dar cumplimiento', 'acatar', 'obedecer',

# Términos de impugnación
'impugnar', 'recurrir', 'apelar', 'reclamar', 'contradecir',
'objetar', 'refutar', 'cuestionar', 'controvertir',

# Términos de interpretación
'interpretar', 'analizar', 'examinar', 'estudiar', 'dilucidar',
'aclarar', 'precisar', 'desentrañar', 'comprender', 'entender',

# Términos de valoración probatoria
'probar', 'demostrar', 'acreditar', 'evidenciar', 'comprobar',
'constatar', 'verificar', 'validar', 'confirmar', 'corroborar'

# Términos de contexto procesal avanzado
'dirimir', 'conceptualizar', 'sistematizar', 'contextualizar', 
'concatenar', 'interrelacionar', 'configurar', 'estructurar', 
'tipificar', 'caracterizar', 'dimensionar', 'cualificar',

# Términos de análisis hermenéutico
'interpretar', 'desentrañar', 'dilucidar', 'esclarecer', 
'desambiguar', 'decodificar', 'resignificar', 'reinterpretar', 
'deconstruir', 'reconstruir', 'contextualizar', 'problematizar',

# Términos de argumentación compleja
'concatenar', 'hilar', 'articular', 'engarzar', 'vincular', 
'interconectar', 'relacionar', 'correlacionar', 'sistematizar', 
'estructurar', 'configurar', 'fundamentar',

# Términos de valoración epistemológica
'problematizar', 'conceptualizar', 'teorizar', 'abstraer', 
'categorizar', 'generalizar', 'particularizar', 'singularizar', 
'universalizar', 'especificar', 'determinar',

# Términos de análisis crítico
'deconstruir', 'cuestionar', 'problematizar', 'desarticular', 
'desnaturalizar', 'desmontar', 'resignificar', 'reinterpretar', 
'reconfigurar', 'reconstruir', 'transformar',

# Términos de hermenéutica jurídica
'interpretar', 'significar', 'resignificar', 'decodificar', 
'reinterpretar', 'contextualizar', 'desambiguar', 'esclarecer', 
'dilucidar', 'desentrañar', 'comprender', 'analizar',

# Términos de construcción argumentativa
'argumentar', 'fundamentar', 'sostener', 'defender', 'justificar', 
'demostrar', 'probar', 'evidenciar', 'acreditar', 'corroborar', 
'confirmar', 'validar',

# Términos de análisis sistémico
'interrelacionar', 'concatenar', 'vincular', 'articular', 
'estructurar', 'configurar', 'sistematizar', 'integrar', 
'contextualizar', 'dimensionar',

# Términos de valoración ontológica
'ser', 'existir', 'acontecer', 'devenir', 'transformar', 
'configurar', 'manifestar', 'emerger', 'surgir', 'constituir',

# Términos de análisis fenomenológico
'aparecer', 'manifestarse', 'develar', 'revelar', 'mostrar', 
'exhibir', 'desplegar', 'emerger', 'surgir', 'configurarse',

# Términos de construcción dialéctica
'contradecir', 'refutar', 'cuestionar', 'objetar', 'controvertir', 
'problematizar', 'deconstruir', 'reinterpretar', 'resignificar',

# Términos de análisis pragmático
'contextualizar', 'significar', 'interpretar', 'comprender', 
'dimensionar', 'caracterizar', 'cualificar', 'especificar',

# Términos de valoración axiológica
'valorar', 'evaluar', 'ponderar', 'calibrar', 'estimar', 
'conceptuar', 'juzgar', 'apreciar', 'considerar',

# Términos de análisis semántico
'significar', 'denotar', 'connotar', 'interpretar', 'traducir', 
'desambiguar', 'esclarecer', 'dilucidar', 'desentrañar',

# Términos de construcción narrativa
'narrar', 'relatar', 'describir', 'caracterizar', 'contextualizar', 
'especificar', 'pormenorizar', 'detallar', 'precisar',

# Términos de análisis performativo
'performar', 'realizar', 'efectuar', 'concretar', 'materializar', 
'ejecutar', 'implementar', 'desarrollar', 'configurar',

# Términos de valoración prospectiva
'proyectar', 'anticipar', 'prever', 'predecir', 'prospectar', 
'visualizar', 'dimensionar', 'planificar', 'programar',





# Términos administrativos
'ha', 'recibido', 'respuesta', 'producto', 'conducta', 'informa', 
'acudido', 'médico', 'particular', 'posteriormente', 'ael',
'eps', 'calidad', 'tutelar', 'derecho', 'fundamental', 
'seguridad', 'social', 'acuerdo', 'informe', 'secretarial', 
'documento', 'expediente', 'radicado', 'trámite', 'proceso',
'procedimiento', 'actuación', 'gestión', 'administración',

# Términos de gestión administrativa
'gestionar', 'administrar', 'coordinar', 'organizar', 'planificar',
'implementar', 'desarrollar', 'ejecutar', 'supervisar', 'evaluar',
'controlar', 'monitorear', 'optimizar', 'revisar', 'auditar',

# Términos de comunicación administrativa
'notificar', 'comunicar', 'informar', 'emitir', 'remitir',
'transmitir', 'enviar', 'presentar', 'proporcionar', 'facilitar',
'divulgar', 'difundir', 'publicar', 'anunciar', 'advertir',

# Términos de documentación
'documentar', 'registrar', 'archivar', 'clasificar', 'catalogar',
'indexar', 'conservar', 'almacenar', 'digitalizar', 'formalizar',
'certificar', 'validar', 'autenticar', 'firmar', 'sellar',

# Términos de procedimientos administrativos
'proceder', 'actuar', 'intervenir', 'participar', 'comparecer',
'presentar', 'solicitar', 'requerir', 'demandar', 'exigir',
'proponer', 'formular', 'instaurar', 'iniciar', 'concluir',

# Términos de evaluación y control
'evaluar', 'valorar', 'ponderar', 'calibrar', 'examinar',
'analizar', 'revisar', 'auditar', 'inspeccionar', 'verificar',
'comprobar', 'certificar', 'validar', 'ratificar', 'confirmar',

# Términos de derechos y obligaciones
'derecho', 'obligación', 'responsabilidad', 'compromiso', 'garantía',
'protección', 'tutela', 'respaldo', 'amparo', 'defensa',

# Términos de normatividad y regulación
'reglamento', 'normativa', 'ley', 'decreto', 'resolución',
'circular', 'instrucción', 'directriz', 'protocolo', 'manual',

# Términos de relaciones interinstitucionales
'colaboración', 'coordinación', 'asociación', 'alianza', 'convenio',
'acuerdo', 'pacto', 'compromiso', 'interacción', 'sinergia',

# Términos de planificación y estrategia
'plan', 'estrategia', 'programa', 'proyecto', 'iniciativa',
'propuesta', 'objetivo', 'meta', 'prioridad', 'táctica',

# Términos de recursos
'recurso', 'financiero', 'humano', 'material', 'tecnológico',
'logístico', 'informático', 'físico', 'natural', 'económico',

# Términos de evaluación de calidad
'calidad', 'eficiencia', 'eficacia', 'satisfacción', 'mejora',
'optimización', 'rendimiento', 'desempeño', 'resultados', 'impacto',

# Términos de seguimiento y monitoreo
'seguimiento', 'monitoreo', 'control', 'evaluación', 'revisión',
'retroalimentación', 'ajuste', 'corrección', 'adaptación',

# Términos de gestión de riesgos
'riesgo', 'evaluación de riesgos', 'mitigación', 'prevención',
'gestión de crisis', 'plan de contingencia', 'análisis de impacto',
'estrategia de respuesta', 'recuperación',

# Términos de servicio al ciudadano
'atención', 'servicio', 'asistencia', 'apoyo', 'orientación',
'consultoría', 'información', 'acceso', 'facilitación', 'resolución',

# Términos de ética y transparencia
'transparencia', 'ética', 'responsabilidad', 'rendición de cuentas',
'compliance', 'integridad', 'honestidad', 'confianza', 'credibilidad',

# Términos de transformación digital
'digitalización', 'transformación digital', 'tecnologías emergentes',
'automatización', 'inteligencia artificial', 'machine learning',
'blockchain', 'big data', 'internet de las cosas', 'cloud computing',
'ciberseguridad', 'analítica de datos', 'realidad virtual',
'realidad aumentada', 'automatización de procesos',

# Términos de gestión del talento
'desarrollo profesional', 'gestión del talento', 'competencias',
'habilidades', 'formación', 'desarrollo de liderazgo',
'potencial', 'carrera profesional', 'mentoring', 'coaching',
'desarrollo de equipos', 'gestión del desempeño',

# Términos de gestión estratégica
'planificación estratégica', 'visión', 'misión', 'valores',
'objetivos estratégicos', 'mapa estratégico', 'cuadro de mando',
'indicadores clave', 'benchmarking estratégico', 'prospectiva',
'análisis FODA', 'ventaja competitiva', 'modelo de negocio',

# Términos de gestión de la innovación social
'innovación social', 'emprendimiento social', 'impacto social',
'transformación social', 'desarrollo comunitario', 'inclusión',
'responsabilidad social', 'valor compartido', 'ecosistema de innovación',
'laboratorio de innovación', 'diseño social', 'prototipado social',

# Términos de gestión de la experiencia
'experiencia del usuario', 'diseño de experiencia', 'customer journey',
'satisfacción', 'engagement', 'lealtad', 'personalización',
'omnicanalidad', 'servicio al cliente', 'atención integral',
'gestión de expectativas', 'retroalimentación',

# Términos de gestión de la complejidad
'pensamiento sistémico', 'gestión de la complejidad', 'adaptabilidad',
'resiliencia organizacional', 'gestión de la incertidumbre',
'pensamiento crítico', 'toma de decisiones', 'resolución de problemas',
'gestión del cambio', 'flexibilidad estratégica',

# Términos de gestión del conocimiento avanzado
'aprendizaje organizacional', 'gestión del capital intelectual',
'comunidades de práctica', 'inteligencia organizacional',
'gestión del conocimiento tácito', 'transferencia de conocimiento',
'memoria organizacional', 'aprendizaje continuo',
'desarrollo de capacidades', 'gestión del conocimiento estratégico',

# Términos de gestión de la sostenibilidad integral
'sostenibilidad integral', 'economía circular', 'impacto ambiental',
'huella de carbono', 'responsabilidad ambiental', 'objetivos de desarrollo sostenible',
'gestión ambiental', 'economía verde', 'innovación sostenible',
'desarrollo regenerativo', 'gestión de recursos naturales',

# Términos de gestión de la diversidad e inclusión
'diversidad e inclusión', 'equidad', 'inclusión organizacional',
'gestión de la diversidad', 'cultura inclusiva', 'no discriminación',
'igualdad de oportunidades', 'diversidad cognitiva', 'inteligencia cultural',
'liderazgo inclusivo', 'equipos diversos',

# Términos de gestión de la resiliencia
'resiliencia organizacional', 'gestión de la continuidad',
'adaptabilidad', 'gestión de crisis', 'recuperación',
'gestión de riesgos', 'plan de contingencia', 'capacidad de respuesta',
'transformación adaptativa', 'aprendizaje desde la adversidad',

# Términos de gestión ética y de valores
'ética organizacional', 'valores corporativos', 'integridad',
'transparencia', 'responsabilidad', 'gobernanza ética',
'código de conducta', 'cultura ética', 'toma de decisiones ética',
'responsabilidad social corporativa', 'compliance',

# Términos de gestión de la colaboración
'colaboración', 'trabajo en equipo', 'inteligencia colectiva',
'co-creación', 'colaboración interdisciplinaria', 'redes de colaboración',
'ecosistemas de innovación', 'colaboración intersectorial',
'alianzas estratégicas', 'comunidades de práctica',

# Términos de gestión del propósito
'propósito organizacional', 'misión transformadora',
'valor compartido', 'impacto positivo', 'sentido de trascendencia',
'alineamiento estratégico', 'cultura de propósito',
'liderazgo con sentido', 'compromiso organizacional'




# Verbos y frases comunes
'donde', 'indico', 'haber', 'llamada', 'quien', 'actúa', 
'informo', 'residente', 'está', 'ciudad', 'deba', 'acudir', 
'otras', 'acciones', 'constitucionales', 'pro', 'su', 
'solicita', 'pide', 'requiere', 'demanda', 'impetra',
'instancia', 'instaurar', 'ejercer', 'interponer',

# Verbos de acción
'realizar', 'efectuar', 'desarrollar', 'implementar', 
'gestionar', 'coordinar', 'organizar', 'planificar', 
'ejecutar', 'supervisar', 'evaluar', 'controlar', 
'analizar', 'investigar', 'comunicar', 'notificar',

# Verbos de comunicación
'decir', 'afirmar', 'manifestar', 'expresar', 
'comunicar', 'informar', 'notificar', 'advertir', 
'señalar', 'indicar', 'revelar', 'anunciar', 
'proclamar', 'declarar', 'exponer', 'relatar',

# Verbos de solicitud
'solicitar', 'pedir', 'requerir', 'demandar', 
'implorar', 'rogar', 'exigir', 'instar', 
'proponer', 'sugerir', 'reclamar', 'invocar',

# Verbos de respuesta
'responder', 'contestar', 'reaccionar', 'aclarar', 
'justificar', 'ratificar', 'confirmar', 'validar', 
'corroborar', 'sustentar', 'defender', 'argumentar',

# Verbos de evaluación
'evaluar', 'valorar', 'ponderar', 'calibrar', 
'analizar', 'examinar', 'considerar', 'reflexionar', 
'juzgar', 'estimar', 'sopesar', 'revisar',

# Verbos de acción legal
'interponer', 'impetrar', 'instaurar', 'promover', 
'ejercer', 'defender', 'representar', 'litigar', 
'procurar', 'abogar', 'intervenir', 'actuar',

# Frases comunes
'por medio de', 'en virtud de', 'a través de', 
'conforme a', 'de acuerdo con', 'en relación con', 
'con respecto a', 'en cumplimiento de', 'en atención a', 
'conforme a lo establecido', 'en el marco de',

# Frases de contexto
'con el fin de', 'a efectos de', 'con el propósito de', 
'con la intención de', 'en el contexto de', 
'conforme a la normativa', 'en cumplimiento de la ley',

# Frases de referencia
'según lo indicado', 'de acuerdo a lo señalado', 
'conforme a lo manifestado', 'en base a lo expuesto', 
'conforme a lo establecido', 'en virtud de lo dispuesto',

# Frases de conclusión
'por lo tanto', 'en consecuencia', 'así las cosas', 
'por consiguiente', 'de ahí que', 'en resumen', 
'conclusivamente', 'en definitiva',

# Frases de aclaración
'vale la pena señalar', 'es importante destacar', 
'cabe mencionar', 'es relevante indicar', 
'debe tenerse en cuenta', 'es necesario aclarar',

# Frases de transición
'por otro lado', 'en adición', 'además', 
'por otra parte', 'sin embargo', 'no obstante', 
'por el contrario', 'en cambio', 'a pesar de',

# Frases de temporalidad
'posteriormente', 'anteriormente', 'en el futuro', 
'actualmente', 'en el presente', 'en el pasado', 
'de inmediato', 'de forma inmediata', 'en breve',

# Verbos y frases comunes
'donde', 'indico', 'haber', 'llamada', 'quien', 'actúa', 
'informo', 'residente', 'está', 'ciudad', 'deba', 'acudir', 
'otras', 'acciones', 'constitucionales', 'pro', 'su', 
'solicita', 'pide', 'requiere', 'demanda', 'impetra',
'instancia', 'instaurar', 'ejercer', 'interponer',

# Verbos de acción
'realizar', 'efectuar', 'desarrollar', 'implementar', 
'gestionar', 'coordinar', 'organizar', 'planificar', 
'ejecutar', 'supervisar', 'evaluar', 'controlar', 
'analizar', 'investigar', 'comunicar', 'notificar',
'construir', 'crear', 'producir', 'diseñar', 'elaborar',

# Verbos de comunicación
'decir', 'afirmar', 'manifestar', 'expresar', 
'comunicar', 'informar', 'notificar', 'advertir', 
'señalar', 'indicar', 'revelar', 'anunciar', 
'proclamar', 'declarar', 'exponer', 'relatar',
'contar', 'describir', 'narrar', 'detallar',

# Verbos de solicitud
'solicitar', 'pedir', 'requerir', 'demandar', 
'implorar', 'rogar', 'exigir', 'instar', 
'proponer', 'sugerir', 'reclamar', 'invocar',
'presentar', 'formular', 'plantear', 'exponer',

# Verbos de respuesta
'responder', 'contestar', 'reaccionar', 'aclarar', 
'justificar', 'ratificar', 'confirmar', 'validar', 
'corroborar', 'sustentar', 'defender', 'argumentar',
'aceptar', 'rechazar', 'contradecir', 'rebatir',

# Verbos de evaluación
'evaluar', 'valorar', 'ponderar', 'calibrar', 
'analizar', 'examinar', 'considerar', 'reflexionar', 
'juzgar', 'estimar', 'sopesar', 'revisar',
'comprobar', 'verificar', 'certificar', 'validar',

# Verbos de acción legal
'interponer', 'impetrar', 'instaurar', 'promover', 
'ejercer', 'defender', 'representar', 'litigar', 
'procurar', 'abogar', 'intervenir', 'actuar',
'protestar', 'apelarse', 'reclamar', 'denunciar',

# Frases comunes
'por medio de', 'en virtud de', 'a través de', 
'conforme a', 'de acuerdo con', 'en relación con', 
'con respecto a', 'en cumplimiento de', 'en atención a', 
'conforme a lo establecido', 'en el marco de',

# Frases de contexto
'con el fin de', 'a efectos de', 'con el propósito de', 
'con la intención de', 'en el contexto de', 
'conforme a la normativa', 'en cumplimiento de la ley',
'con el objetivo de', 'con miras a',

# Frases de referencia
'según lo indicado', 'de acuerdo a lo señalado', 
'conforme a lo manifestado', 'en base a lo expuesto', 
'conforme a lo establecido', 'en virtud de lo dispuesto',
'como se ha mencionado', 'tal como se indica',

# Frases de conclusión
'por lo tanto', 'en consecuencia', 'así las cosas', 
'por consiguiente', 'de ahí que', 'en resumen', 
'conclusivamente', 'en definitiva', 'en síntesis',
'para finalizar', 'en conclusión',

# Frases de aclaración
'vale la pena señalar', 'es importante destacar', 
'cabe mencionar', 'es relevante indicar', 
'debe tenerse en cuenta', 'es necesario aclarar',
'para mayor claridad', 'en otras palabras',

# Frases de transición
'por otro lado', 'en adición', 'además', 
'por otra parte', 'sin embargo', 'no obstante', 
'por el contrario', 'en cambio', 'a pesar de',
'igualmente', 'asimismo',

# Frases de temporalidad
'posteriormente', 'anteriormente', 'en el futuro', 
'actualmente', 'en el presente', 'en el pasado', 
'de inmediato', 'de forma inmediata', 'en breve',
'próximamente', 'en el transcurso de'

# Verbos y frases comunes
'donde', 'indico', 'haber', 'llamada', 'quien', 'actúa', 
'informo', 'residente', 'está', 'ciudad', 'deba', 'acudir', 
'otras', 'acciones', 'constitucionales', 'pro', 'su', 
'solicita', 'pide', 'requiere', 'demanda', 'impetra',
'instancia', 'instaurar', 'ejercer', 'interponer',

# Verbos de acción
'realizar', 'efectuar', 'desarrollar', 'implementar', 
'gestionar', 'coordinar', 'organizar', 'planificar', 
'ejecutar', 'supervisar', 'evaluar', 'controlar', 
'analizar', 'investigar', 'comunicar', 'notificar',
'construir', 'crear', 'producir', 'diseñar', 'elaborar',
'optimizar', 'simplificar', 'facilitar', 'promover',

# Verbos de comunicación
'decir', 'afirmar', 'manifestar', 'expresar', 
'comunicar', 'informar', 'notificar', 'advertir', 
'señalar', 'indicar', 'revelar', 'anunciar', 
'proclamar', 'declarar', 'exponer', 'relatar',
'contar', 'describir', 'narrar', 'detallar',
'transmitir', 'difundir', 'divulgar', 'reiterar',

# Verbos de solicitud
'solicitar', 'pedir', 'requerir', 'demandar', 
'implorar', 'rogar', 'exigir', 'instar', 
'proponer', 'sugerir', 'reclamar', 'invocar',
'presentar', 'formular', 'plantear', 'exponer',
'instar a', 'convocar', 'invitar a', 'proponer a',

# Verbos de respuesta
'responder', 'contestar', 'reaccionar', 'aclarar', 
'justificar', 'ratificar', 'confirmar', 'validar', 
'corroborar', 'sustentar', 'defender', 'argumentar',
'aceptar', 'rechazar', 'contradecir', 'rebatir',
'comunicar', 'declarar', 'revelar', 'explicar',

# Verbos de evaluación
'evaluar', 'valorar', 'ponderar', 'calibrar', 
'analizar', 'examinar', 'considerar', 'reflexionar', 
'juzgar', 'estimar', 'sopesar', 'revisar',
'comprobar', 'verificar', 'certificar', 'validar',
'analizar', 'estudiar', 'investigar', 'revisar',

# Verbos de acción legal
'interponer', 'impetrar', 'instaurar', 'promover', 
'ejercer', 'defender', 'representar', 'litigar', 
'procurar', 'abogar', 'intervenir', 'actuar',
'protestar', 'apelarse', 'reclamar', 'denunciar',
'litigar', 'demandar', 'solicitar', 'exigir',

# Frases comunes
'por medio de', 'en virtud de', 'a través de', 
'conforme a', 'de acuerdo con', 'en relación con', 
'con respecto a', 'en cumplimiento de', 'en atención a', 
'conforme a lo establecido', 'en el marco de',
'conforme a la ley', 'en base a', 'en virtud de',

# Frases de contexto
'con el fin de', 'a efectos de', 'con el propósito de', 
'con la intención de', 'en el contexto de', 
'conforme a la normativa', 'en cumplimiento de la ley',
'con el objetivo de', 'con miras a', 'con el fin de',

# Frases de referencia
'según lo indicado', 'de acuerdo a lo señalado', 
'conforme a lo manifestado', 'en base a lo expuesto', 
'conforme a lo establecido', 'en virtud de lo dispuesto',
'como se ha mencionado', 'tal como se indica',
'conforme a lo estipulado', 'según lo acordado',

# Frases de conclusión
'por lo tanto', 'en consecuencia', 'así las cosas', 
'por consiguiente', 'de ahí que', 'en resumen', 
'conclusivamente', 'en definitiva', 'en síntesis',
'para finalizar', 'en conclusión', 'en resumen',

# Frases de aclaración
'vale la pena señalar', 'es importante destacar', 
'cabe mencionar', 'es relevante indicar', 
'debe tenerse en cuenta', 'es necesario aclarar',
'para mayor claridad', 'en otras palabras',
'para ser más claro', 'en términos simples',

# Frases de transición
'por otro lado', 'en adición', 'además', 
'por otra parte', 'sin embargo', 'no obstante', 
'por el contrario', 'en cambio', 'a pesar de',
'igualmente', 'asimismo', 'de igual manera',

# Frases de temporalidad
'posteriormente', 'anteriormente', 'en el futuro', 
'actualmente', 'en el presente', 'en el pasado', 
'de inmediato', 'de forma inmediata', 'en breve',
'próximamente', 'en el transcurso de', 'en el momento',

# Frases de condición
'si', 'en caso de que', 'a menos que', 'siempre que', 
'con tal de que', 'en la medida en que', 'suponiendo que',
'bajo la condición de que', 'en caso contrario',

# Frases de finalidad
'con el fin de', 'para', 'a fin de', 'con el objetivo de',
'con la finalidad de', 'con miras a', 'a efectos de',
'con el propósito de', 'con la intención de',

# Frases de comparación
'como', 'así como', 'de la misma manera', 'de igual forma',
'comparado con', 'en comparación con', 'similar a',
'por otro lado', 'en contraste con', 'a diferencia de',






# Términos de salud y bienestar
'salud', 'pueda', 'verse', 'afectado', 'las', 'trabas', 'administrativas',
'paciente', 'tratamiento', 'clínica', 'hospital', 
'sistema', 'eps', 'ips', 'afiliado', 'asegurado',
'diagnóstico', 'patología', 'terapia', 'medicamento',
'procedimiento', 'intervención', 'rehabilitación',

# Términos relacionados con la salud
'bienestar', 'prevención', 'promoción', 'calidad de vida',
'cuidado', 'atención', 'salud pública', 'salud mental',
'salud física', 'salud emocional', 'salud integral',
'cuidado preventivo', 'cuidado paliativo', 'cuidado crónico',

# Términos de diagnóstico
'diagnóstico médico', 'evaluación', 'examen', 'prueba',
'analítica', 'radiografía', 'ultrasonido', 'tomografía',
'biopsia', 'histopatología', 'resultados', 'síntomas',

# Términos de tratamiento
'tratamiento médico', 'terapia ocupacional', 'terapia física',
'terapia psicológica', 'medicación', 'cirugía', 'intervención quirúrgica',
'cuidados intensivos', 'hospitalización', 'seguimiento médico',
'plan de tratamiento', 'protocolos de atención',

# Términos de medicamentos
'medicamento recetado', 'fármaco', 'dosis', 'efectos secundarios',
'interacción', 'contraindicaciones', 'prescripción', 'farmacología',
'tratamiento farmacológico', 'medicina alternativa', 'suplemento',

# Términos de rehabilitación
'rehabilitación física', 'rehabilitación ocupacional', 'rehabilitación psicológica',
'terapia de rehabilitación', 'programa de rehabilitación', 'recuperación',
'mejora funcional', 'adaptación', 'integración',

# Términos de salud pública
'salud pública', 'epidemiología', 'prevención de enfermedades',
'promoción de la salud', 'programas de salud', 'políticas de salud',
'educación para la salud', 'vacunación', 'inmunización',

# Términos de bienestar emocional
'bienestar emocional', 'salud mental', 'estrés', 'ansiedad',
'depresión', 'apoyo psicológico', 'terapia cognitivo-conductual',
'psicoterapia', 'intervención psicológica', 'autocuidado',

# Términos de atención al paciente
'atención al paciente', 'cuidado del paciente', 'acompañamiento',
'asesoría médica', 'orientación', 'información al paciente',
'consentimiento informado', 'derechos del paciente',

# Términos de sistemas de salud
'sistema de salud', 'aseguramiento', 'cobertura', 'acceso a la salud',
'financiamiento', 'recursos de salud', 'infraestructura de salud',
'calidad de atención', 'satisfacción del paciente',

# Términos de enfermedades
'enfermedad crónica', 'enfermedad aguda', 'enfermedad infecciosa',
'patología crónica', 'trastorno', 'síndrome', 'condición médica',
'comorbilidad', 'epidemia', 'pandemia',

# Términos de promoción de la salud
'promoción de la salud', 'estilo de vida saludable', 'nutrición',
'ejercicio físico', 'prevención de enfermedades', 'educación en salud',
'campañas de salud', 'concientización',

# Términos de investigación en salud
'investigación médica', 'ensayo clínico', 'estudio de caso',
'metodología', 'análisis de datos', 'resultados de investigación',
'publicación científica', 'revisión sistemática',

# Términos de salud ocupacional
'salud ocupacional', 'prevención de riesgos laborales', 'ergonomía',
'seguridad en el trabajo', 'bienestar laboral', 'evaluación de riesgos',
'programas de salud laboral', 'cuidado del trabajador',

# Términos de salud especializada
'medicina especializada', 'medicina personalizada', 'medicina preventiva',
'medicina regenerativa', 'medicina integrativa', 'medicina de precisión',
'telemedicina', 'medicina digital', 'salud conectada', 'monitoreo remoto',

# Términos de salud mental avanzada
'neuropsicología', 'psiquiatría', 'psicoterapia', 'terapia cognitiva',
'terapia conductual', 'terapia familiar', 'terapia de grupo',
'intervención psicosocial', 'neuroplasticidad', 'resiliencia psicológica',
'inteligencia emocional', 'manejo del estrés', 'regulación emocional',

# Términos de medicina holística
'medicina holística', 'medicina alternativa', 'medicina complementaria',
'terapias naturales', 'medicina tradicional', 'fitoterapia',
'acupuntura', 'homeopatía', 'naturopatía', 'medicina ayurvédica',
'medicina tradicional china', 'medicina energética',

# Términos de tecnología médica
'tecnología médica', 'dispositivos médicos', 'inteligencia artificial médica',
'big data en salud', 'genómica', 'proteómica', 'bioinformática',
'medicina de precisión', 'telemedicina', 'salud digital',
'wearables', 'monitoreo continuo', 'diagnóstico predictivo',

# Términos de investigación biomédica
'investigación biomédica', 'ensayos clínicos', 'estudios epidemiológicos',
'investigación traslacional', 'medicina experimental', 'farmacogenómica',
'biotecnología', 'edición genética', 'terapia génica', 'medicina regenerativa',
'inmunoterapia', 'terapias avanzadas', 'medicina personalizada',

# Términos de salud global
'salud global', 'salud internacional', 'determinantes sociales de la salud',
'equidad en salud', 'cooperación sanitaria', 'salud sin fronteras',
'medicina transcultural', 'antropología médica', 'salud comunitaria',
'desarrollo sanitario', 'políticas globales de salud',

# Términos de neurociencias
'neurociencia', 'neurología', 'neurofisiología', 'neuropsicología',
'neurodegeneración', 'neuroprotección', 'neurorrehabilitación',
'neuroplasticidad', 'neurogénesis', 'neuroimagen',
'trastornos neurodegenerativos', 'estimulación cerebral',

# Términos de medicina regenerativa
'medicina regenerativa', 'terapia celular', 'terapia con células madre',
'ingeniería de tejidos', 'regeneración de órganos', 'medicina reparadora',
'terapias avanzadas', 'bioingeniería', 'medicina molecular',
'medicina personalizada', 'terapia génica',

# Términos de salud digital
'salud digital', 'e-salud', 'telemedicina', 'salud móvil',
'historias clínicas digitales', 'monitoreo remoto', 'consulta virtual',
'aplicaciones de salud', 'inteligencia artificial médica',
'big data en salud', 'análisis predictivo', 'salud conectada',

# Términos de salud preventiva avanzada
'medicina preventiva', 'prevención primaria', 'prevención secundaria',
'promoción de la salud', 'estilo de vida saludable', 'nutrición preventiva',
'medicina predictiva', 'biomarcadores', 'genética preventiva',
'evaluación de riesgos', 'screening', 'detección temprana',

# Términos de salud comunitaria
'salud comunitaria', 'medicina social', 'intervención comunitaria',
'educación para la salud', 'promoción de la salud', 'participación social',
'empoderamiento comunitario', 'redes de apoyo', 'salud colectiva',
'determinantes sociales', 'equidad en salud',

# Términos de salud laboral avanzada
'salud ocupacional', 'ergonomía', 'psicosociología laboral',
'prevención de riesgos', 'salud mental laboral', 'bienestar organizacional',
'cultura de seguridad', 'gestión del estrés laboral', 'clima laboral saludable',
'rehabilitación ocupacional', 'adaptación laboral',

# Términos de ética médica
'bioética', 'ética médica', 'derechos del paciente', 'consentimiento informado',
'dignidad humana', 'autonomía', 'confidencialidad', 'integridad profesional',
'investigación ética', 'dilemas bioéticos', 'comités de ética',
'principios éticos', 'responsabilidad profesional',
    



# Términos legales adicionales
'sobre', 'bajo', 'contra', 'desde', 'hacia', 'hasta', 
'sin', 'según', 'durante', 'tras', 'so', 'so pena',
'cc', 'cédula', 'ciudadanía', 'identificación', 'documento',
'nombre', 'representación', 'calidad', 'propio', 'derecho',
'instancia', 'jurisdicción', 'competencia', 'controversia',
'litigio', 'demanda', 'pretensión', 'fallo', 'sentencia',
'providencia', 'auto', 'resolución', 'dictamen',

# Términos de jurisdicción y competencia
'jurisdicción', 'competencia', 'fuero', 'territorio',
'ámbito', 'alcance', 'materia', 'especialidad', 'instancia',
'tribunal', 'juzgado', 'corte', 'sala', 'magistratura',

# Términos procesales
'proceso', 'procedimiento', 'actuación', 'diligencia',
'trámite', 'etapa', 'fase', 'término', 'plazo',
'recurso', 'apelación', 'casación', 'revisión',

# Términos de representación legal
'representación', 'personería', 'mandato', 'poder',
'apoderado', 'representante', 'defensor', 'patrocinio',
'asesoría', 'consultoría', 'intervención',

# Términos de identificación
'identificación', 'documento', 'cédula', 'pasaporte',
'registro', 'inscripción', 'certificación', 'autenticación',
'verificación', 'validación',

# Términos de derecho sustantivo
'derecho', 'norma', 'precepto', 'disposición', 'artículo',
'estatuto', 'código', 'ley', 'reglamento', 'decreto',
'principio', 'garantía', 'protección', 'tutela',

# Términos de resolución judicial
'sentencia', 'fallo', 'providencia', 'auto', 'resolución',
'dictamen', 'laudo', 'veredicto', 'decisión', 'pronunciamiento',
'considerando', 'argumentación', 'fundamentación',

# Términos de controversia
'controversia', 'litigio', 'conflicto', 'disputa',
'diferendo', 'desacuerdo', 'confrontación', 'discrepancia',
'divergencia', 'oposición',

# Términos de pretensión
'pretensión', 'demanda', 'solicitud', 'petición',
'requerimiento', 'reclamación', 'exigencia', 'reclamo',
'impugnación', 'contestación',

# Términos de derechos fundamentales
'derecho fundamental', 'garantía constitucional',
'derecho humano', 'libertad', 'igualdad', 'dignidad',
'protección', 'tutela', 'amparo', 'defensa',

# Términos de procedimiento
'procedimiento', 'trámite', 'diligencia', 'actuación',
'etapa', 'fase', 'término', 'plazo', 'recurso',
'instancia', 'apelación', 'casación', 'revisión',

# Términos de prueba
'prueba', 'evidencia', 'medio probatorio', 'testigo',
'peritaje', 'documental', 'testimonial', 'pericial',
'indicio', 'presunción', 'verificación', 'validación',

# Términos de medidas cautelares
'medida cautelar', 'suspensión', 'intervención',
'embargo', 'secuestro', 'incautación', 'prohibición',
'restricción', 'protección', 'aseguramiento',

# Términos de interpretación jurídica
'interpretación', 'hermenéutica', 'exégesis', 'análisis',
'construcción', 'significado', 'alcance', 'sentido',
'contexto', 'sistematización',

# Términos de argumentación legal
'argumentación', 'fundamentación', 'motivación',
'razonamiento', 'justificación', 'sustento', 'base',
'soporte', 'explicación', 'desarrollo',

# Términos de resolución alternativa
'mediación', 'conciliación', 'arbitraje', 'negociación',
'transacción', 'acuerdo', 'avenimiento', 'arreglo',
'solución', 'resolución',

# Términos de responsabilidad
'responsabilidad', 'culpa', 'dolo', 'negligencia',
'imprudencia', 'omisión', 'incumplimiento', 'daño',
'perjuicio', 'reparación', 'indemnización',

# Términos legales adicionales (continuación)

# Términos de derecho constitucional
'constitucionalidad', 'garantía constitucional', 'principio constitucional',
'control de constitucionalidad', 'bloque de constitucionalidad',
'interpretación constitucional', 'supremacía constitucional',
'derechos fundamentales', 'valores constitucionales',

# Términos de derecho internacional
'derecho internacional', 'tratado', 'convenio', 'protocolo',
'jurisdicción internacional', 'corte internacional', 'tribunal internacional',
'derecho humanitario', 'derechos humanos', 'derecho transnacional',
'soberanía', 'inmunidad', 'diplomacia', 'relaciones internacionales',

# Términos de derecho administrativo
'acto administrativo', 'procedimiento administrativo', 'función pública',
'servicio público', 'contratación estatal', 'gestión pública',
'responsabilidad administrativa', 'potestad administrativa',
'discrecionalidad', 'principios de la administración',

# Términos de derecho civil
'derecho civil', 'persona', 'personalidad jurídica', 'capacidad',
'obligación', 'contrato', 'propiedad', 'posesión', 'dominio',
'patrimonio', 'sucesión', 'herencia', 'familia', 'matrimonio',

# Términos de derecho penal
'derecho penal', 'tipo penal', 'conducta punible', 'dolo', 'culpa',
'imputabilidad', 'responsabilidad penal', 'pena', 'sanción',
'delito', 'tipicidad', 'antijuridicidad', 'culpabilidad',
'circunstancias', 'atenuantes', 'agravantes',

# Términos de derecho laboral
'derecho laboral', 'contrato de trabajo', 'jornada laboral',
'salario', 'prestaciones sociales', 'seguridad social',
'sindicalismo', 'negociación colectiva', 'huelga',
'despido', 'estabilidad laboral', 'derechos laborales',

# Términos de derecho mercantil
'derecho mercantil', 'sociedades', 'empresa', 'comerciante',
'acto de comercio', 'contrato mercantil', 'títulos valores',
'propiedad industrial', 'marca', 'patente', 'derecho societario',
'gobierno corporativo', 'responsabilidad empresarial',

# Términos de derecho procesal
'derecho procesal', 'acción', 'proceso', 'jurisdicción',
'competencia', 'partes procesales', 'prueba', 'alegato',
'recurso', 'impugnación', 'nulidad', 'cosa juzgada',
'principios procesales', 'debido proceso',

# Términos de derecho ambiental
'derecho ambiental', 'medio ambiente', 'recursos naturales',
'protección ambiental', 'desarrollo sostenible', 'ecosistema',
'biodiversidad', 'cambio climático', 'responsabilidad ecológica',
'daño ambiental', 'restauración', 'compensación ambiental',

# Términos de derechos humanos
'derechos humanos', 'dignidad humana', 'igualdad', 'no discriminación',
'libertad', 'integridad', 'debido proceso', 'tutela judicial',
'reparación', 'verdad', 'justicia', 'garantías',

# Términos de derecho tecnológico
'derecho tecnológico', 'propiedad intelectual', 'derecho digital',
'protección de datos', 'privacidad', 'ciberseguridad',
'comercio electrónico', 'firma digital', 'inteligencia artificial',
'blockchain', 'derechos digitales',

# Términos de argumentación jurídica
'hermenéutica jurídica', 'interpretación', 'argumentación',
'construcción jurídica', 'razonamiento legal', 'sistemática jurídica',
'principios generales', 'analogía', 'integración jurídica',

# Términos de ética jurídica
'ética jurídica', 'deontología', 'moral profesional',
'integridad', 'buena fe', 'principios éticos',
'responsabilidad profesional', 'conflicto de intereses',

# Términos de gestión jurídica
'gestión jurídica', 'consultoría', 'asesoría legal',
'representación', 'defensa', 'litigio', 'negociación',
'resolución de conflictos', 'mediación', 'arbitraje',

# Términos de innovación legal
'innovación jurídica', 'transformación legal', 'derecho emergente',
'nuevos paradigmas', 'tecnología legal', 'legal tech',
'inteligencia artificial jurídica', 'automatización legal',

# Términos de justicia restaurativa
'justicia restaurativa', 'reparación', 'reconciliación',
'diálogo', 'encuentro', 'comunidad', 'sanación',
'transformación de conflictos', 'restauración social',

# Términos legales adicionales (continuación)

# Términos de derecho administrativo
'licencia', 'permiso', 'autorización', 'concesión',
'contrato administrativo', 'actos administrativos', 'resolución administrativa',
'procedimiento administrativo sancionador', 'recurso administrativo',
'control administrativo', 'responsabilidad patrimonial',

# Términos de derecho civil
'contrato', 'obligación', 'responsabilidad civil', 'daño',
'perjuicio', 'indemnización', 'sucesión intestada', 'testamento',
'herencia', 'legítima', 'usufructo', 'comunidad de bienes',

# Términos de derecho penal
'delito', 'falta', 'tipificación', 'sanción penal',
'pena privativa de libertad', 'pena de muerte', 'reclusión',
'libertad condicional', 'suspensión de la pena', 'eximente',
'circunstancias atenuantes', 'circunstancias agravantes',

# Términos de derecho laboral
'contrato de trabajo', 'relación laboral', 'despido injustificado',
'vacaciones', 'licencia de maternidad', 'licencia de paternidad',
'jornada laboral', 'horas extras', 'salario mínimo',
'prestaciones sociales', 'seguridad social',

# Términos de derecho mercantil
'empresa', 'sociedad anónima', 'sociedad limitada', 'acción',
'participación', 'capital social', 'balance', 'estado de resultados',
'quiebra', 'concurso de acreedores', 'responsabilidad limitada',

# Términos de derecho internacional
'tratado internacional', 'convención', 'protocolo', 'derecho consuetudinario',
'jurisdicción universal', 'derecho de asilo', 'derecho de guerra',
'principio de no intervención', 'derecho de autodeterminación',

# Términos de derecho ambiental
'impacto ambiental', 'evaluación de impacto ambiental', 'licencia ambiental',
'contaminación', 'recursos naturales', 'biodiversidad', 'sostenibilidad',
'cambio climático', 'conservación', 'restauración ecológica',

# Términos de derechos humanos
'convención internacional', 'derechos civiles', 'derechos políticos',
'derechos económicos', 'derechos sociales', 'derechos culturales',
'discriminación', 'igualdad de género', 'derechos de la infancia',

# Términos de derecho tecnológico
'protección de datos personales', 'privacidad', 'cibercrimen',
'comercio electrónico', 'firma electrónica', 'contratos digitales',
'responsabilidad en línea', 'derechos de autor en internet',

# Términos de resolución de conflictos
'mediación', 'conciliación', 'arbitraje', 'negociación',
'resolución alternativa de disputas', 'acuerdo de conciliación',
'laudo arbitral', 'proceso de mediación',

# Términos de ética y deontología
'código de ética', 'deontología profesional', 'conflicto de intereses',
'transparencia', 'rendición de cuentas', 'responsabilidad social',
'conducta profesional', 'integridad',

# Términos de derecho procesal
'acción judicial', 'demanda', 'contestación', 'recurso de apelación',
'prueba', 'testimonio', 'documentación', 'informe pericial',
'notificación', 'emplazamiento', 'audiencia', 'sentencia',

# Términos de derecho de familia
'matrimonio', 'divorcio', 'separación', 'custodia',
'pensión alimentaria', 'adopción', 'patria potestad',
'violencia intrafamiliar', 'mediación familiar',

# Términos de derecho de la propiedad
'propiedad', 'posesión', 'usufructo', 'servidumbre',
'hipoteca', 'gravamen', 'expropiación', 'derecho de superficie',
'comunidad de bienes',

# Términos de derecho de la competencia
'competencia desleal', 'prácticas anticompetitivas', 'monopolio',
'concentración empresarial', 'abuso de posición dominante',
'regulación de mercados', 'defensa de la competencia',

# Términos de derecho de la seguridad social
'sistema de seguridad social', 'afiliación', 'prestaciones',
'pensiones', 'incapacidad', 'maternidad', 'paternidad',
'jubilación', 'cobertura', 'beneficios sociales',

# Términos de derecho de la infancia
'derechos del niño', 'protección infantil', 'bienestar infantil',
'educación', 'salud', 'participación', 'no discriminación',
'violencia contra niños', 'explotación infantil',

# Términos legales avanzados y emergentes

# Términos de derecho digital y tecnológico
'ciberderecho', 'derecho digital', 'inteligencia artificial legal',
'blockchain jurídico', 'contratos inteligentes', 'firma digital',
'identidad digital', 'derecho algorítmico', 'privacidad digital',
'gobernanza tecnológica', 'ética de la inteligencia artificial',
'derechos digitales', 'regulación de plataformas',

# Términos de derecho de la innovación
'propiedad intelectual', 'patente', 'marca', 'derechos de autor',
'licenciamiento', 'transferencia tecnológica', 'innovación regulatoria',
'emprendimiento legal', 'startups', 'ecosistema de innovación',
'propiedad industrial', 'secreto comercial', 'modelo de utilidad',

# Términos de derecho global y transnacional
'derecho global', 'gobernanza internacional', 'orden jurídico mundial',
'pluralismo jurídico', 'derecho comparado', 'sistemas legales híbridos',
'armonización legal', 'transplante jurídico', 'derecho cosmopolita',
'justicia global', 'regulación transfronteriza', 'derecho multinivel',

# Términos de justicia restaurativa y transformativa
'justicia restaurativa', 'círculos de diálogo', 'mediación transformativa',
'reparación integral', 'reconstrucción social', 'sanación comunitaria',
'reconciliación', 'memoria histórica', 'verdad', 'reparación simbólica',
'justicia transicional', 'memoria colectiva', 'reconstrucción del tejido social',

# Términos de derecho ambiental avanzado
'derecho ecosistémico', 'derechos de la naturaleza', 'justicia climática',
'economía circular', 'desarrollo regenerativo', 'bioderecho',
'derechos ambientales', 'gestión ecosistémica', 'resiliencia ambiental',
'justicia intergeneracional', 'derechos de las generaciones futuras',

# Términos de derechos humanos emergentes
'derechos emergentes', 'derechos digitales', 'derechos de la naturaleza',
'derechos de los animales', 'derechos de las comunidades',
'derechos colectivos', 'derechos interculturales', 'derechos lingüísticos',
'derechos de los pueblos indígenas', 'derechos de las minorías',

# Términos de gobernanza y democracia
'democracia deliberativa', 'participación ciudadana', 'gobierno abierto',
'transparencia', 'rendición de cuentas', 'ética pública',
'integridad institucional', 'control social', 'participación política',
'representación inclusiva', 'democracia digital',

# Términos de derecho de la diversidad
'diversidad jurídica', 'pluralismo legal', 'interculturalidad',
'justicia intercultural', 'derecho propio', 'sistemas normativos indígenas',
'derecho consuetudinario', 'jurisdicción especial', 'peritaje cultural',
'diálogo de saberes', 'hermenéutica intercultural',

# Términos de neurociencia jurídica
'neurociencia legal', 'derecho y neurociencia', 'neurorresponsabilidad',
'capacidad mental', 'imputabilidad neurológica', 'toma de decisiones',
'sesgo cognitivo', 'neuroderechos', 'ética neurotecnológica',
'consentimiento informado neurológico',

# Términos de derecho prospectivo
'derecho prospectivo', 'futurismo jurídico', 'anticipación regulatoria',
'escenarios jurídicos', 'innovación normativa', 'derecho experimental',
'laboratorio legislativo', 'prototipado legal', 'diseño jurídico',
'inteligencia estratégica', 'pensamiento sistémico',

# Términos de gestión integral del conflicto
'gestión sistémica de conflictos', 'transformación de conflictos',
'ecología de conflictos', 'inteligencia conflictual', 'mediación compleja',
'facilitación', 'diálogo constructivo', 'resolución creativa',
'prevención de conflictos', 'resiliencia social',

# Términos de ética aplicada
'ética aplicada', 'dilema ético', 'razonamiento ético',
'deliberación moral', 'principios éticos', 'valores fundamentales',
'integridad profesional', 'responsabilidad ética', 'consciencia moral',
'desarrollo ético', 'cultura ética',

# Términos de sostenibilidad jurídica
'derecho de la sostenibilidad', 'justicia ecosocial', 'economía del bien común',
'desarrollo sostenible', 'responsabilidad intergeneracional',
'gobernanza ecosistémica', 'derechos de la tierra', 'ciudadanía planetaria',
'economía regenerativa', 'justicia ambiental',
    




# Frases contextuales
'quien', 'actúa', 'nombre', 'representación', 'calidad', 'agente',
'oficioso', 'representante', 'legal', 'propio', 'derecho',
'en', 'virtud', 'de', 'conformidad', 'con', 'lo', 'establecido',

# Frases de representación
'en nombre de', 'por cuenta de', 'en representación de',
'como apoderado de', 'en calidad de', 'en virtud de',
'en ejercicio de', 'por mandato de', 'en nombre propio',

# Frases de contexto legal
'de conformidad con', 'según lo establecido', 'en cumplimiento de',
'de acuerdo a', 'en atención a', 'conforme a',
'en el marco de', 'en virtud de', 'a tenor de',

# Frases de legitimación
'actuando en derecho', 'con capacidad legal', 'en pleno uso de sus facultades',
'con representación suficiente', 'debidamente autorizado',
'en calidad de representante legal', 'con poder bastante',

# Frases de procedencia
'domiciliado en', 'residente en', 'con documento de identidad',
'identificado con', 'vecino de', 'natural de',
'con dirección en', 'con contacto en',

# Frases de intervención
'se presenta', 'interviene', 'participa',
'ejerce', 'promueve', 'solicita', 'requiere',
'manifiesta', 'expone', 'declara',

# Frases de propósito
'con el objeto de', 'a efectos de', 'con la finalidad de',
'con el propósito de', 'en aras de', 'en interés de',
'para los fines de', 'con miras a',

# Frases de fundamentación
'considerando', 'teniendo en cuenta', 'de acuerdo con',
'en mérito de', 'en base a', 'conforme a',
'de conformidad con', 'según', 'atendiendo a',

# Frases de calificación
'en calidad de', 'bajo la condición de', 'en su condición de',
'como', 'en tanto', 'en cuanto', 'en la medida de',
'según su naturaleza', 'de acuerdo a su naturaleza',

# Frases de atribución
'en uso de sus atribuciones', 'en ejercicio de sus funciones',
'por disposición de', 'en cumplimiento de', 'de acuerdo a sus competencias',
'en el ámbito de', 'dentro de sus facultades',

# Frases de temporalidad
'a partir de', 'desde', 'hasta', 'durante', 'en el momento de',
'con ocasión de', 'en el curso de', 'al momento de',
'en virtud del tiempo', 'en el transcurso de',

# Frases de modalidad
'de manera', 'bajo', 'en', 'con', 'según', 'conforme',
'de conformidad', 'en cumplimiento', 'en atención',
'de acuerdo', 'en virtud',

# Frases de vinculación
'en relación con', 'respecto a', 'con referencia a',
'en consideración de', 'en atención a', 'en mérito de',
'en relación a', 'con motivo de', 'en función de',

# Frases de condicionalidad
'siempre que', 'en caso de', 'bajo la condición de',
'a condición de', 'en la medida en que', 'salvo',
'excepto', 'sin perjuicio de', 'no obstante',

# Frases de finalidad
'a fin de', 'con el objeto de', 'con la intención de',
'para', 'con miras a', 'a efectos de',
'con el propósito de', 'en aras de', 'con la finalidad de',

# Frases de referencia
'según', 'conforme a', 'de acuerdo con', 'en virtud de',
'en mérito de', 'en base a', 'de conformidad con',
'atendiendo a', 'considerando', 'teniendo en cuenta',

# Frases contextuales avanzadas

# Frases de argumentación jurídica
'en mérito de la argumentación', 'conforme a la construcción jurídica',
'de acuerdo a la hermenéutica', 'según la interpretación sistemática',
'en virtud del razonamiento legal', 'atendiendo a la técnica jurídica',
'con fundamento en la dogmática', 'considerando el análisis jurisprudencial',

# Frases de legitimación compleja
'actuando en representación legal plena', 'con poder de representación ampliado',
'en ejercicio de la capacidad jurídica', 'con facultades especiales',
'investido de autoridad', 'con mandato expreso', 'con representación certificada',
'en uso de las atribuciones conferidas', 'con personería jurídica acreditada',

# Frases de contexto procesal
'en el marco del debido proceso', 'conforme a las garantías procesales',
'en observancia de los principios procesales', 'atendiendo al orden jurisdiccional',
'en cumplimiento de la tutela judicial efectiva', 'según las etapas procesales',
'de acuerdo a la normativa procesal', 'en virtud de la competencia establecida',

# Frases de fundamentación avanzada
'considerando los fundamentos de derecho', 'en base a la construcción argumentativa',
'atendiendo a la ratio decidendi', 'conforme a la técnica de ponderación',
'en mérito de la interpretación teleológica', 'según el análisis sistemático',
'de acuerdo a la hermenéutica jurídica', 'en virtud de la argumentación jurídica',

# Frases de contextualización
'en el contexto de', 'considerando el marco normativo',
'atendiendo a la realidad social', 'en consonancia con',
'en relación con el sistema jurídico', 'de acuerdo al contexto histórico',
'en virtud de la evolución normativa', 'conforme a la realidad contemporánea',

# Frases de intencionalidad jurídica
'con la intención de garantizar', 'a efectos de proteger',
'con el propósito de tutelar', 'en aras de preservar',
'con miras a salvaguardar', 'con el objetivo de amparar',
'para los fines de defender', 'con la finalidad de resguardar',

# Frases de modalización jurídica
'bajo el principio de', 'en observancia de',
'de conformidad con', 'en cumplimiento estricto',
'atendiendo al espíritu de', 'según la naturaleza de',
'en el marco de', 'conforme al sentido de',

# Frases de vinculación normativa
'en relación con la normativa', 'respecto al marco legal',
'de acuerdo a las disposiciones', 'en concordancia con',
'en aplicación de', 'según lo establecido en',
'en virtud de lo dispuesto', 'conforme a la regulación',

# Frases de temporalidad jurídica
'a partir de la vigencia', 'durante el período de',
'hasta la culminación de', 'en el momento procesal',
'con ocasión de', 'en el transcurso de',
'desde la entrada en vigor', 'en el lapso de',

# Frases de condición jurídica
'siempre que se cumplan', 'en caso de verificarse',
'bajo la condición de', 'a condición de',
'sin perjuicio de', 'no obstante',
'salvo lo dispuesto', 'excepto en los casos de',

# Frases de finalidad jurídica
'a fin de garantizar', 'con el objeto de proteger',
'para efectos de', 'con miras a',
'con la finalidad de tutelar', 'en aras de preservar',
'para los efectos legales', 'con el propósito de',

# Frases de referencia normativa
'según la normativa vigente', 'conforme a la legislación',
'de acuerdo a las disposiciones', 'en virtud de la normativa',
'atendiendo a la regulación', 'según lo prescrito',
'de conformidad con el ordenamiento', 'en el marco legal',

# Frases de interpretación
'en la interpretación de', 'según la hermenéutica',
'conforme al sentido', 'de acuerdo a la comprensión',
'en virtud de la construcción', 'atendiendo al significado',
'según la técnica interpretativa', 'en el contexto de',

# Frases de integración jurídica
'en ausencia de norma expresa', 'por analogía',
'según los principios generales', 'en aplicación supletoria',
'conforme a la integración jurídica', 'atendiendo a la laguna legal',
'en virtud de la construcción sistemática', 'según la técnica de integración',





# Términos de contexto
'caso', 'asunto', 'materia', 'objeto', 'pretensión', 'motivo',
'razón', 'fundamento', 'base', 'sustento', 'argumento',
'antecedente', 'consideración', 'análisis', 'estudio',

# Términos de contexto legal
'contexto legal', 'marco normativo', 'regulación', 'disposición',
'legislación', 'jurisprudencia', 'doctrina', 'principio',
'precepto', 'norma', 'artículo', 'sección', 'cláusula',

# Términos de contexto procesal
'proceso', 'procedimiento', 'trámite', 'etapa', 'fase',
'diligencia', 'actuación', 'recurso', 'apelación', 'instancia',
'jurisdicción', 'competencia', 'litigio', 'controversia',

# Términos de contexto argumentativo
'argumentación', 'razonamiento', 'justificación', 'exposición',
'defensa', 'sustentación', 'refutación', 'contrargumento',
'perspectiva', 'punto de vista', 'enfoque', 'posición',

# Términos de contexto fáctico
'hechos', 'circunstancias', 'situación', 'evento', 'incidente',
'contexto fáctico', 'antecedentes fácticos', 'realidad',
'escenario', 'condiciones', 'elementos', 'particularidades',

# Términos de contexto social
'contexto social', 'realidad social', 'dinámica social',
'impacto social', 'consecuencias sociales', 'percepción social',
'valores sociales', 'normas sociales', 'interacción social',

# Términos de contexto económico
'contexto económico', 'situación económica', 'análisis económico',
'impacto económico', 'condiciones económicas', 'factores económicos',
'variables económicas', 'tendencias económicas',

# Términos de contexto cultural
'contexto cultural', 'realidad cultural', 'valores culturales',
'prácticas culturales', 'tradiciones', 'costumbres', 'identidad cultural',
'perspectiva cultural', 'influencia cultural',

# Términos de contexto histórico
'contexto histórico', 'antecedentes históricos', 'evolución',
'proceso histórico', 'marco histórico', 'realidad histórica',
'perspectiva histórica', 'análisis histórico',

# Términos de contexto ético
'contexto ético', 'consideraciones éticas', 'dilemas éticos',
'valores éticos', 'principios éticos', 'responsabilidad ética',
'justificación ética', 'perspectiva ética',

# Términos de contexto político
'contexto político', 'situación política', 'análisis político',
'impacto político', 'dinámica política', 'factores políticos',
'decisiones políticas', 'realidad política',

# Términos de contexto normativo
'contexto normativo', 'marco normativo', 'regulación',
'disposición normativa', 'principios normativos', 'validez',
'eficacia normativa', 'interpretación normativa',

# Términos de contexto administrativo
'contexto administrativo', 'gestión administrativa', 'procedimientos',
'políticas administrativas', 'normas administrativas', 'organización',
'funcionamiento administrativo', 'estructura administrativa',

# Términos de contexto avanzados y multidimensionales

# Términos de contexto epistemológico
'marco epistemológico', 'paradigma', 'perspectiva cognitiva',
'construcción del conocimiento', 'modelo interpretativo',
'fundamentos epistemológicos', 'teoría del conocimiento',
'método de comprensión', 'estructura conceptual',

# Términos de contexto interdisciplinario
'interdisciplinariedad', 'transdisciplinariedad', 'convergencia disciplinar',
'diálogo de saberes', 'interseccionalidad', 'perspectiva integrada',
'enfoque holístico', 'complementariedad disciplinar',
'marco conceptual integrado',

# Términos de contexto sistémico
'sistema', 'ecosistema', 'red de relaciones', 'interconexión',
'complejidad', 'dinamismo', 'estructura sistémica',
'pensamiento sistémico', 'retroalimentación', 'autoorganización',
'emergencia', 'resiliencia sistémica',

# Términos de contexto crítico
'perspectiva crítica', 'deconstrucción', 'análisis crítico',
'problematización', 'cuestionamiento', 'reflexividad',
'meta-análisis', 'hermenéutica crítica', 'genealogía',
'desplazamiento conceptual', 'ruptura epistemológica',

# Términos de contexto prospectivo
'prospectiva', 'escenarios futuros', 'anticipación',
'tendencias emergentes', 'transformación', 'evolución',
'horizonte de sentido', 'imaginarios', 'futurización',
'construcción de futuro', 'pensamiento estratégico',

# Términos de contexto fenomenológico
'experiencia vivencial', 'mundo de la vida', 'significado',
'interpretación', 'subjetividad', 'intersubjetividad',
'comprensión fenomenológica', 'descripción densa',
'sentido de la experiencia', 'horizonte de significación',

# Términos de contexto hermenéutico
'interpretación', 'comprensión', 'sentido', 'significado',
'círculo hermenéutico', 'horizonte de interpretación',
'traducción cultural', 'diálogo hermenéutico',
'mediación interpretativa', 'comprensión contextual',

# Términos de contexto axiológico
'valores', 'sistema axiológico', 'jerarquía de valores',
'dimensión valorativa', 'valoración', 'estimativa',
'fundamentación axiológica', 'construcción de sentido',
'horizonte valorativo', 'ética de los valores',

# Términos de contexto genealógico
'genealogía', 'arqueología', 'génesis', 'devenir',
'trayectoria histórica', 'transformación', 'emergencia',
'discontinuidad', 'ruptura', 'condiciones de posibilidad',
'micropolítica', 'relaciones de poder',

# Términos de contexto ecológico
'ecosistema', 'interdependencia', 'complejidad ambiental',
'sostenibilidad', 'resiliencia ecológica', 'metabolismo social',
'justicia ecosocial', 'ciudadanía planetaria',
'perspectiva ecosistémica', 'ética ambiental',

# Términos de contexto comunicacional
'comunicación', 'discurso', 'narrativa', 'lenguaje',
'comunicación estratégica', 'construcción de sentido',
'interacción comunicativa', 'pragmática', 'semiótica',
'comunicación dialógica', 'contexto comunicacional',

# Términos de contexto tecnológico
'tecnologización', 'digitalización', 'mediación tecnológica',
'transformación digital', 'ecosistema tecnológico',
'inteligencia artificial', 'big data', 'tecnopolítica',
'ciberespacio', 'tecnosfera',

# Términos de contexto decolonial
'decolonialidad', 'colonialidad', 'pensamiento fronterizo',
'geopolítica del conocimiento', 'diferencia colonial',
'crítica decolonial', 'transmodernidad', 'pluriverso',
'epistemologías del sur', 'interculturalidad crítica',

# Términos de contexto ontológico
'ser', 'existencia', 'devenir', 'ontología',
'modos de ser', 'comprensión ontológica', 'estructura ontológica',
'dimensiones existenciales', 'horizonte ontológico',
'analítica existencial', 'condición humana',

# Términos de contexto dialéctico
'dialéctica', 'contradicción', 'síntesis', 'negación',
'transformación', 'movimiento', 'proceso', 'desarrollo',
'superación', 'mediación', 'totalidad', 'historicidad',

# Términos de contexto transnacional
'transnacionalidad', 'globalización', 'interconexión global',
'flujos transfronterizos', 'redes globales', 'movilidad',
'ciudadanía global', 'cosmopolitismo', 'multilateralidad',
'interdependencia mundial',
    



# Términos médicos adicionales
'diagnóstico', 'patología', 'síntoma', 'enfermedad', 'condición',
'tratamiento', 'medicamento', 'terapia', 'intervención',
'rehabilitación', 'crónico', 'agudo', 'recurrente',
'especialista', 'médico', 'facultativo', 'profesional',

# Términos de diagnóstico
'diagnóstico diferencial', 'evaluación clínica', 'examen médico',
'historia clínica', 'anamnesis', 'exploración física',
'pruebas diagnósticas', 'biomarcadores', 'screening',
'diagnóstico temprano', 'diagnóstico definitivo',

# Términos de patologías
'patología', 'síndrome', 'trastorno', 'afección',
'dolencia', 'padecimiento', 'alteración', 'anomalía',
'enfermedad congénita', 'enfermedad adquirida',
'enfermedad genética', 'enfermedad multisistémica',

# Términos de sintomatología
'síntoma', 'signo', 'manifestación', 'indicador',
'sintomatología', 'cuadro clínico', 'evolución sintomática',
'sintomatología primaria', 'sintomatología secundaria',
'expresión sintomática', 'progresión sintomática',

# Términos de tratamiento
'tratamiento farmacológico', 'tratamiento no farmacológico',
'terapia', 'intervención', 'procedimiento', 'protocolo',
'plan de tratamiento', 'esquema terapéutico',
'tratamiento integral', 'tratamiento personalizado',

# Términos de medicación
'medicamento', 'fármaco', 'principio activo',
'dosis', 'posología', 'prescripción', 'indicación',
'contraindicación', 'efectos secundarios', 'interacción medicamentosa',
'farmacoterapia', 'medicina basada en evidencia',

# Términos de especialidades médicas
'especialista', 'médico', 'facultativo', 'profesional de la salud',
'especialidad', 'subespecialidad', 'área de expertise',
'medicina especializada', 'práctica clínica', 'consulta médica',

# Términos de condición médica
'condición', 'estado de salud', 'perfil de salud',
'cronicidad', 'agudeza', 'recurrencia', 'progresión',
'estadio', 'severidad', 'complejidad', 'comorbilidad',

# Términos de intervención médica
'intervención', 'procedimiento', 'cirugía', 'operación',
'tratamiento quirúrgico', 'intervención mínimamente invasiva',
'técnica quirúrgica', 'protocolo de intervención',
'preparación preoperatoria', 'recuperación postoperatoria',

# Términos de rehabilitación
'rehabilitación', 'recuperación', 'terapia de recuperación',
'rehabilitación física', 'rehabilitación funcional',
'programa de rehabilitación', 'proceso de recuperación',
'terapia de rehabilitación', 'seguimiento rehabilitador',

# Términos de especialidades clínicas
'medicina interna', 'pediatría', 'geriatría', 'ginecología',
'cardiología', 'neurología', 'oncología', 'psiquiatría',
'neumología', 'endocrinología', 'dermatología', 'urología',

# Términos de procedimientos diagnósticos
'imagenología', 'radiografía', 'tomografía', 'resonancia magnética',
'ecografía', 'endoscopia', 'biopsia', 'análisis de laboratorio',
'prueba de sangre', 'prueba de función', 'estudio genético',

# Términos de medicina preventiva
'prevención', 'promoción de la salud', 'chequeo médico',
'screening', 'detección temprana', 'evaluación de riesgo',
'medicina preventiva', 'educación para la salud',
'intervención preventiva', 'estilo de vida saludable',

# Términos de medicina personalizada
'medicina personalizada', 'medicina de precisión',
'tratamiento individualizado', 'perfil genético',
'farmacogenómica', 'biomarcadores', 'terapia dirigida',
'medicina predictiva', 'medicina de precisión',

# Términos de salud mental
'salud mental', 'psicoterapia', 'terapia psicológica',
'evaluación psicológica', 'diagnóstico psiquiátrico',
'trastorno mental', 'intervención psicoterapéutica',
'rehabilitación psicosocial', 'salud emocional',

# Términos de medicina avanzada
'medicina regenerativa', 'terapia génica', 'medicina molecular',
'nanotecnología médica', 'terapia celular', 'medicina experimental',
'biotecnología médica', 'medicina traslacional',
'investigación biomédica', 'innovación médica',

# Términos médicos avanzados y multidisciplinarios

# Términos de medicina molecular y genómica
'genómica', 'proteómica', 'metabolómica', 'epigenética',
'edición genética', 'terapia génica', 'medicina molecular',
'biomarcadores genéticos', 'farmacogenómica',
'medicina personalizada', 'secuenciación genómica',
'biomedicina molecular', 'biología de sistemas',

# Términos de neurociencias médicas
'neuroplasticidad', 'neurogénesis', 'neuroimagen',
'conectividad cerebral', 'neurotransmisores',
'neurorrehabilitación', 'neurodegeneración',
'neuroinmunología', 'neurofisiología', 'neurocognición',
'neuropsicología', 'neuroetica', 'neurotecnología',

# Términos de medicina regenerativa
'medicina regenerativa', 'terapia celular', 'células madre',
'ingeniería de tejidos', 'bioimpresión', 'organoides',
'medicina reparadora', 'regeneración de órganos',
'biotecnología regenerativa', 'medicina reconstructiva',
'bioingeniería', 'medicina traslacional',

# Términos de medicina integrativa
'medicina integrativa', 'enfoque holístico', 'medicina complementaria',
'medicina tradicional', 'terapias alternativas',
'medicina mind-body', 'intervención integral',
'tratamiento multidimensional', 'salud holística',
'medicina preventiva integral', 'bienestar global',

# Términos de inmunología médica
'inmunología', 'sistema inmunológico', 'inmunoterapia',
'respuesta inmune', 'inmunomodulación', 'autoinmunidad',
'inmunodeficiencia', 'inmunosupresión', 'vacunología',
'inmunogenética', 'inmunooncología', 'inmunovigilancia',

# Términos de medicina digital y tecnológica
'telemedicina', 'salud digital', 'historia clínica electrónica',
'inteligencia artificial médica', 'big data en salud',
'monitoreo remoto', 'wearables médicos', 'salud móvil',
'diagnóstico predictivo', 'robótica médica',
'medicina de precisión digital', 'análisis predictivo',

# Términos de medicina ambiental y ecológica
'medicina ambiental', 'salud ecosistémica', 'epidemiología ambiental',
'toxicología', 'impacto ambiental en la salud', 'medicina ocupacional',
'salud planetaria', 'determinantes ambientales de la salud',
'medicina de ecosistemas', 'salud global', 'justicia ambiental',

# Términos de medicina social y comunitaria
'determinantes sociales de la salud', 'epidemiología social',
'salud comunitaria', 'medicina social', 'antropología médica',
'equidad en salud', 'salud intercultural', 'promoción de la salud',
'participación comunitaria', 'empoderamiento en salud',

# Términos de medicina psicosomática
'psicosomática', 'medicina mente-cuerpo', 'psiconeuroinmunología',
'estrés y salud', 'resiliencia', 'inteligencia emocional',
'medicina conductual', 'neuropsicología', 'salud mental integral',
'psiconeuroendocrinología', 'medicina existencial',

# Términos de medicina de sistemas
'medicina de sistemas', 'biología de sistemas',
'redes biomoleculares', 'modelado computacional',
'simulación médica', 'medicina predictiva',
'bioinformática', 'análisis de redes biológicas',
'medicina computacional', 'biología integrativa',

# Términos de medicina global y transcultural
'medicina global', 'salud internacional', 'medicina transcultural',
'epidemiología global', 'salud sin fronteras',
'determinantes globales de la salud', 'migración y salud',
'medicina humanitaria', 'cooperación sanitaria internacional',

# Términos de bioética médica
'bioética', 'ética médica', 'dilemas bioéticos',
'consentimiento informado', 'autonomía del paciente',
'dignidad humana', 'investigación ética',
'principios de la bioética', 'ética de la investigación',
'derechos del paciente', 'ética de la tecnología médica',

# Términos de medicina predictiva y preventiva
'medicina predictiva', 'screening genético', 'evaluación de riesgo',
'prevención primaria', 'prevención secundaria', 'prevención terciaria',
'biomarcadores predictivos', 'medicina anticipatoria',
'intervención temprana', 'promoción de la salud',

# Términos de medicina experimental
'medicina experimental', 'ensayos clínicos', 'investigación traslacional',
'medicina experimental', 'innovación médica', 'nuevos tratamientos',
'terapias emergentes', 'medicina de frontera', 'investigación biomédica',
'desarrollo farmacológico', 'medicina experimental avanzada',

    


# Términos de derechos
'derecho', 'fundamental', 'constitución', 'garantía',
'protección', 'amparo', 'tutela', 'vulneración',
'restablecimiento', 'reparación', 'compensación',

# Términos de derechos fundamentales
'derecho fundamental', 'garantía constitucional', 'derecho humano',
'libertad', 'igualdad', 'dignidad', 'autonomía',
'derechos civiles', 'derechos políticos', 'derechos sociales',
'derechos económicos', 'derechos culturales',

# Términos de protección jurídica
'protección jurídica', 'amparo legal', 'tutela jurisdiccional',
'defensa', 'garantía', 'salvaguarda', 'resguardo',
'protección integral', 'mecanismo de protección',
'sistema de protección', 'medidas de protección',

# Términos de vulneración de derechos
'vulneración', 'violación', 'conculcación', 'menoscabo',
'transgresión', 'afectación', 'lesión', 'daño',
'vulneración sistemática', 'vulneración estructural',
'vulneración individual', 'vulneración colectiva',

# Términos de restablecimiento de derechos
'restablecimiento', 'restitución', 'restauración',
'reparación integral', 'reintegración', 'recuperación',
'restablecimiento de la dignidad', 'restablecimiento del derecho',
'reparación simbólica', 'reparación transformadora',

# Términos de compensación
'compensación', 'indemnización', 'resarcimiento',
'reparación económica', 'reparación moral',
'compensación integral', 'compensación justa',
'medidas de compensación', 'compensación colectiva',

# Términos de derechos humanos
'derechos humanos', 'dignidad humana', 'universalidad',
'interdependencia', 'indivisibilidad', 'inalienabilidad',
'derechos civiles', 'derechos políticos', 'derechos económicos',
'derechos sociales', 'derechos culturales', 'derechos colectivos',

# Términos de garantías constitucionales
'garantía constitucional', 'principio constitucional',
'protección constitucional', 'reserva legal',
'principio de legalidad', 'debido proceso',
'tutela judicial efectiva', 'reserva de jurisdicción',

# Términos de tutela jurídica
'tutela', 'protección jurídica', 'defensa legal',
'amparo judicial', 'garantía jurisdiccional',
'tutela específica', 'tutela preventiva',
'tutela reparadora', 'tutela cautelar',

# Términos de derechos individuales
'derecho individual', 'libertad personal', 'autonomía',
'integridad', 'privacidad', 'identidad',
'libre desarrollo de la personalidad',
'derecho al honor', 'derecho a la imagen',

# Términos de derechos colectivos
'derecho colectivo', 'derechos de comunidades',
'derechos de pueblos', 'derechos de minorías',
'derechos indígenas', 'derechos ambientales',
'derechos de género', 'derechos culturales',

# Términos de derechos procesales
'derecho procesal', 'debido proceso', 'tutela judicial',
'derecho de defensa', 'derecho a la prueba',
'derecho al recurso', 'principio de contradicción',
'igualdad procesal', 'derecho a la jurisdicción',

# Términos de derechos sociales
'derecho social', 'derechos laborales', 'derecho a la educación',
'derecho a la salud', 'derecho a la vivienda',
'derecho a la seguridad social', 'derecho al trabajo',
'derecho a la alimentación', 'derecho al agua',

# Términos de derechos emergentes
'nuevos derechos', 'derechos digitales', 'derechos tecnológicos',
'derecho a la privacidad digital', 'derecho al olvido',
'derechos ambientales', 'derechos de la naturaleza',
'derechos de las generaciones futuras',

# Términos de reparación integral
'reparación integral', 'reparación transformadora',
'medidas de reparación', 'garantías de no repetición',
'rehabilitación', 'satisfacción', 'indemnización',
'memoria histórica', 'reparación simbólica',

# Términos de justicia
'justicia', 'justicia social', 'justicia restaurativa',
'equidad', 'igualdad', 'no discriminación',
'justicia de género', 'justicia intercultural',
'justicia transicional', 'justicia global',

# Términos de derechos
'derecho', 'fundamental', 'constitución', 'garantía',
'protección', 'amparo', 'tutela', 'vulneración',
'restablecimiento', 'reparación', 'compensación',

# Términos de derechos fundamentales
'derecho fundamental', 'garantía constitucional', 'derecho humano',
'libertad de expresión', 'libertad de asociación', 'derecho a la vida',
'igualdad ante la ley', 'derecho a la privacidad', 'derecho a la educación',
'derecho a la salud', 'derecho al trabajo', 'derecho a la vivienda',
'derecho a la no discriminación', 'derecho a la participación política',

# Términos de protección jurídica
'protección jurídica', 'amparo legal', 'tutela jurisdiccional',
'defensa legal', 'garantía', 'salvaguarda', 'resguardo',
'protección integral', 'mecanismo de protección',
'sistema de protección', 'medidas de protección',
'protección de derechos', 'defensa de derechos',

# Términos de vulneración de derechos
'vulneración', 'violación', 'conculcación', 'menoscabo',
'transgresión', 'afectación', 'lesión', 'daño',
'vulneración sistemática', 'vulneración estructural',
'vulneración individual', 'vulneración colectiva',
'vulneración de derechos humanos', 'vulneración de derechos fundamentales',

# Términos de restablecimiento de derechos
'restablecimiento', 'restitución', 'restauración',
'reparación integral', 'reintegración', 'recuperación',
'restablecimiento de la dignidad', 'restablecimiento del derecho',
'reparación simbólica', 'reparación transformadora',
'reparación colectiva', 'reparación individual',

# Términos de compensación
'compensación', 'indemnización', 'resarcimiento',
'reparación económica', 'reparación moral',
'compensación integral', 'compensación justa',
'medidas de compensación', 'compensación colectiva',
'compensación por daños', 'compensación por perjuicios',

# Términos de derechos humanos
'derechos humanos', 'dignidad humana', 'universalidad',
'interdependencia', 'indivisibilidad', 'inalienabilidad',
'derechos civiles', 'derechos políticos', 'derechos económicos',
'derechos sociales', 'derechos culturales', 'derechos de las mujeres',
'derechos de los niños', 'derechos de los pueblos indígenas',

# Términos de garantías constitucionales
'garantía constitucional', 'principio constitucional',
'protección constitucional', 'reserva legal',
'principio de legalidad', 'debido proceso',
'tutela judicial efectiva', 'reserva de jurisdicción',
'garantías de no repetición', 'garantías de protección',

# Términos de tutela jurídica
'tutela', 'protección jurídica', 'defensa legal',
'amparo judicial', 'garantía jurisdiccional',
'tutela específica', 'tutela preventiva',
'tutela reparadora', 'tutela cautelar',
'tutela de derechos fundamentales',

# Términos de derechos individuales
'derecho individual', 'libertad personal', 'autonomía',
'integridad', 'privacidad', 'identidad',
'libre desarrollo de la personalidad',
'derecho al honor', 'derecho a la imagen',
'derecho a la intimidad', 'derecho a la libertad de pensamiento',

# Términos de derechos colectivos
'derecho colectivo', 'derechos de comunidades',
'derechos de pueblos', 'derechos de minorías',
'derechos indígenas', 'derechos ambientales',
'derechos de género', 'derechos culturales',
'derechos de los trabajadores', 'derechos de los consumidores',

# Términos de derechos procesales
'derecho procesal', 'debido proceso', 'tutela judicial',
'derecho de defensa', 'derecho a la prueba',
'derecho al recurso', 'principio de contradicción',
'igualdad procesal', 'derecho a la jurisdicción',
'derecho a ser oído', 'derecho a la asistencia letrada',

# Términos de derechos sociales
'derecho social', 'derechos laborales', 'derecho a la educación',
'derecho a la salud', 'derecho a la vivienda',
'derecho a la seguridad social', 'derecho al trabajo',
'derecho a la alimentación', 'derecho al agua',
'derecho a un medio ambiente sano', 'derecho a la cultura',

# Términos de derechos emergentes
'nuevos derechos', 'derechos digitales', 'derechos tecnológicos',
'derecho a la privacidad digital', 'derecho al olvido',
'derechos ambientales', 'derechos de la naturaleza',
'derechos de las generaciones futuras',

# Términos de derechos avanzados y multidimensionales

# Términos de derechos transversales
'derechos transversales', 'interseccionalidad', 'enfoque de derechos',
'derechos interdependientes', 'derechos interrelacionados',
'derechos complementarios', 'derechos integrados',
'enfoque diferencial', 'perspectiva de derechos',
'derechos transformadores', 'derechos emancipadores',

# Términos de derechos globales
'derechos globales', 'ciudadanía global', 'cosmopolitismo',
'derechos transnacionales', 'justicia global',
'derechos más allá de fronteras', 'derechos universales',
'gobernanza global de derechos', 'sistema internacional de derechos',
'derechos sin fronteras', 'solidaridad internacional',

# Términos de derechos digitales
'derechos digitales', 'ciudadanía digital', 'derechos tecnológicos',
'privacidad digital', 'protección de datos personales',
'derecho al olvido', 'identidad digital', 'libertad digital',
'derecho de acceso a internet', 'neutralidad de la red',
'derechos en el ciberespacio', 'soberanía digital',

# Términos de derechos ambientales
'derechos ambientales', 'derechos de la naturaleza',
'justicia climática', 'derechos ecosistémicos',
'derechos de las generaciones futuras', 'ciudadanía planetaria',
'derechos de los ecosistemas', 'derechos de los animales',
'derecho a un ambiente sano', 'justicia ecológica',

# Términos de derechos de género
'derechos de género', 'perspectiva de género', 'igualdad de género',
'no discriminación', 'derechos de las mujeres',
'derechos LGBTIQ+', 'interseccionalidad de género',
'empoderamiento', 'autonomía', 'paridad',
'derechos reproductivos', 'derechos sexuales',

# Términos de derechos interculturales
'derechos interculturales', 'pluralismo jurídico',
'derechos de pueblos indígenas', 'autodeterminación',
'consulta previa', 'consentimiento libre e informado',
'identidad cultural', 'patrimonio cultural',
'diversidad cultural', 'diálogo intercultural',

# Términos de derechos emergentes
'nuevos derechos', 'derechos en transformación',
'derechos posthumanos', 'derechos de inteligencia artificial',
'derechos neurotecnológicos', 'derechos biométricos',
'derechos de la inteligencia artificial',
'derechos de los sistemas autónomos',
'derechos de las entidades sintéticas',

# Términos de justicia restaurativa
'justicia restaurativa', 'reparación integral',
'reconciliación', 'sanación', 'transformación de conflictos',
'diálogo restaurativo', 'círculos de paz',
'mediación transformadora', 'reparación simbólica',
'memoria histórica', 'reconstrucción del tejido social',

# Términos de derechos económicos
'derechos económicos', 'derecho al desarrollo',
'renta básica universal', 'economía de los derechos',
'distribución equitativa', 'justicia económica',
'derechos de los trabajadores', 'derechos de los consumidores',
'economía solidaria', 'derechos económicos colectivos',

# Términos de derechos epistémicos
'derechos epistémicos', 'justicia cognitiva',
'pluralismo epistemológico', 'decolonialidad',
'democratización del conocimiento',
'derechos de los saberes tradicionales',
'diálogo de saberes', 'ecología de saberes',
'conocimiento como derecho', 'justicia cognitiva global',

# Términos de derechos posthumanos
'derechos posthumanos', 'derechos más allá de lo humano',
'derechos de entidades sintéticas', 'derechos de la inteligencia artificial',
'derechos de sistemas autónomos', 'ciudadanía expandida',
'derechos de sistemas complejos', 'derechos de redes',
'derechos de ecosistemas tecnológicos',

# Términos de derechos de la complejidad
'derechos de la complejidad', 'derechos sistémicos',
'derechos de interconexión', 'derechos relacionales',
'derechos ecosistémicos', 'derechos de red',
'derechos de interdependencia', 'derechos emergentes',
'derechos de sistemas adaptativos',

# Términos de justicia transformadora
'justicia transformadora', 'justicia restaurativa',
'reparación integral', 'reconstrucción social',
'transformación de estructuras', 'cambio sistémico',
'empoderamiento colectivo', 'memoria histórica',
'reconciliación', 'sanación social',


    



# Artículos y preposiciones
'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
'de', 'del', 'al', 'en', 'por', 'para', 'con', 'sin',

# Artículos definidos
'el', 'la', 'los', 'las',
'lo', # artículo neutro
'el cual', 'la cual', 'los cuales', 'las cuales',

# Artículos indefinidos
'un', 'una', 'unos', 'unas',
'algún', 'alguna', 'algunos', 'algunas',
'cierto', 'cierta', 'ciertos', 'ciertas',

# Preposiciones simples
'de', 'a', 'en', 'por', 'para', 'con', 'sin', 'sobre',
'bajo', 'tras', 'entre', 'hacia', 'hasta', 'desde',

# Preposiciones compuestas
'del', 'al', 'por el', 'para el', 'con el', 'sin el',
'sobre el', 'bajo el', 'tras el', 'entre los',
'acerca de', 'cerca de', 'dentro de', 'fuera de',

# Preposiciones de relación
'contra', 'durante', 'mediante',
'salvo', 'según', 'so', 'tras', 'versus',

# Preposiciones complejas
'a través de', 'en virtud de', 'en función de',
'en relación con', 'de acuerdo con', 'en torno a',
'por medio de', 'en consideración de', 'en mérito de',

# Artículos contractos
'de la', 'a la', 'de los', 'a los',
'de las', 'a las',

# Preposiciones de especificación
'respecto a', 'referente a', 'concerniente a',
'relativo a', 'atinente a', 'tocante a',

# Preposiciones de causa o motivo
'por razón de', 'a causa de', 'en razón de',
'debido a', 'en virtud de', 'a consecuencia de',

# Preposiciones de finalidad
'para con', 'con miras a', 'a efectos de',
'a fin de', 'con el propósito de', 'en orden a',

# Preposiciones de modo
'con arreglo a', 'de conformidad con',
'en cumplimiento de', 'en atención a',
'según', 'conforme a', 'en virtud de',

# Preposiciones locativas
'dentro de', 'fuera de', 'cerca de', 'lejos de',
'junto a', 'frente a', 'detrás de', 'encima de',
'debajo de', 'alrededor de',

# Preposiciones temporales
'durante', 'antes de', 'después de',
'a partir de', 'desde', 'hasta',
'en el transcurso de', 'al momento de',

# Preposiciones comparativas
'como', 'tal como', 'así como',
'más que', 'menos que', 'igual que',

# Preposiciones de exclusión
'excepto', 'salvo', 'menos', 'sin',
'con excepción de', 'a excepción de',

# Preposiciones de inclusión
'incluso', 'incluyendo', 'además de',
'junto con', 'sumado a', 'añadido a',

# Preposiciones de distribución
'entre', 'por', 'para cada', 'por cada',
'a razón de', 'a proporción de',

# Preposiciones de origen
'de', 'desde', 'procedente de',
'originario de', 'proveniente de',

# Preposiciones de dirección
'hacia', 'para', 'rumbo a', 'con dirección a',
'en dirección a', 'camino a',

# Preposiciones de instrumento
'con', 'mediante', 'por medio de',
'a través de', 'por', 'utilizando',

# Preposiciones de intercambio
'por', 'a cambio de', 'en lugar de',
'en vez de', 'en sustitución de'
    
# Artículos y preposiciones avanzados y contextuales

# Artículos con funciones especiales
'lo' 'artículo neutro abstracto',
'lo que', 'lo cual', 'lo mismo',
'lo otro', 'lo demás', 'lo siguiente',

# Artículos con valor enfático
'tal', 'tal cual', 'dicho', 'mencionado',
'referido', 'citado', 'aludido',

# Preposiciones de relación compleja
'en virtud de', 'en función de', 'a tenor de',
'en mérito de', 'conforme a', 'de conformidad con',
'en consideración de', 'a la luz de', 'en razón de',

# Preposiciones de contexto legal
'según', 'conforme a', 'de acuerdo con',
'en cumplimiento de', 'en observancia de',
'en aplicación de', 'a los efectos de',

# Preposiciones de contexto académico
'según', 'de acuerdo a', 'en concordancia con',
'en relación con', 'en el marco de',
'desde la perspectiva de', 'bajo el enfoque de',

# Preposiciones de contexto científico
'de conformidad con', 'en concordancia con',
'según', 'en función de', 'en relación a',
'de acuerdo a la metodología', 'en el contexto de',

# Preposiciones de modalidad
'bajo', 'mediante', 'por medio de',
'a través de', 'en calidad de', 'en condición de',
'en tanto que', 'en cuanto a',

# Preposiciones de gradación
'hasta', 'inclusive', 'incluso',
'más allá de', 'por encima de', 'por debajo de',
'en grado de', 'al nivel de',

# Preposiciones de interacción
'con', 'junto a', 'frente a', 'en relación con',
'en interacción con', 'en diálogo con',
'en convergencia con', 'en articulación con',

# Preposiciones de transformación
'de', 'desde', 'hacia', 'en dirección a',
'en proceso de', 'en transición hacia',
'en transformación de', 'en evolución hacia',

# Preposiciones de perspectiva
'desde', 'bajo', 'desde la perspectiva de',
'desde el punto de vista de', 'en consideración de',
'a la luz de', 'desde el enfoque de',

# Preposiciones de temporalidad compleja
'durante', 'a lo largo de', 'en el transcurso de',
'en el marco temporal de', 'desde el momento de',
'hasta el punto de', 'en el período de',

# Preposiciones de causalidad
'por', 'debido a', 'a causa de',
'en virtud de', 'como consecuencia de',
'en razón de', 'derivado de', 'a resultas de',

# Preposiciones de finalidad avanzada
'a efectos de', 'con miras a', 'en orden a',
'con el propósito de', 'a fin de',
'con la intención de', 'para los efectos de',

# Preposiciones de condición
'en caso de', 'bajo la condición de',
'siempre que', 'a condición de',
'salvo', 'excepto', 'sin perjuicio de',

# Preposiciones de complementariedad
'además de', 'junto con', 'sumado a',
'en adición a', 'en complemento de',
'en conjunción con', 'en paralelo con',

# Preposiciones de contraste
'versus', 'frente a', 'en contraste con',
'a diferencia de', 'en oposición a',
'en contraposición de', 'en confrontación con',

# Preposiciones de interdependencia
'en relación con', 'en conexión con',
'en interacción de', 'en vinculación a',
'en correlación con', 'en articulación de',

# Preposiciones de abstracción
'en términos de', 'desde el punto de vista de',
'bajo el concepto de', 'en el marco de',
'desde la perspectiva de', 'en consideración de',

# Preposiciones de contextualización sistémica
'en el contexto de', 'dentro del sistema de',
'en relación al sistema', 'en interacción sistémica',
'en el marco ecosistémico', 'en la red de',

# Preposiciones de complejidad
'en interrelación con', 'en convergencia de',
'en diálogo con', 'en intersección de',
'en complementariedad', 'en retroalimentación con',



# Verbos comunes
'ser', 'estar', 'haber', 'tener', 'hacer', 'poder', 'deber',
'querer', 'saber', 'parecer', 'decir', 'manifestar', 'indicar',

# Verbos de existencia y estado
'ser', 'estar', 'existir', 'permanecer', 'continuar',
'seguir', 'mantenerse', 'resultar', 'parecer', 'convertirse',
'transformarse', 'devenir', 'revelarse', 'manifestarse',

# Verbos auxiliares
'haber', 'ser', 'estar', 'tener', 'poder', 'deber',
'querer', 'soler', 'ir', 'venir', 'andar',
'acabar', 'comenzar', 'empezar', 'terminar',

# Verbos de acción y realización
'hacer', 'realizar', 'ejecutar', 'efectuar',
'llevar a cabo', 'cumplir', 'desarrollar',
'implementar', 'materializar', 'concretar',
'consumar', 'lograr', 'alcanzar',

# Verbos de comunicación
'decir', 'manifestar', 'indicar', 'expresar',
'comunicar', 'informar', 'narrar', 'relatar',
'explicar', 'argumentar', 'exponer', 'significar',
'enunciar', 'proclamar', 'declarar', 'afirmar',

# Verbos de percepción y conocimiento
'saber', 'conocer', 'entender', 'comprender',
'percibir', 'observar', 'advertir', 'notar',
'distinguir', 'reconocer', 'identificar',
'interpretar', 'analizar', 'examinar',

# Verbos modales
'poder', 'deber', 'querer', 'intentar',
'tratar de', 'procurar', 'pretender',
'aspirar', 'desear', 'necesitar',
'requerir', 'precisar', 'exigir',

# Verbos de posesión y tenencia
'tener', 'poseer', 'contar con', 'disponer',
'mantener', 'conservar', 'retener', 'guardar',
'preservar', 'custodiar', 'administrar',

# Verbos de movimiento
'ir', 'venir', 'llegar', 'salir', 'entrar',
'regresar', 'volver', 'avanzar', 'retroceder',
'moverse', 'desplazarse', 'trasladarse',

# Verbos de cambio y transformación
'cambiar', 'transformar', 'modificar', 'alterar',
'convertir', 'mutar', 'evolucionar', 'desarrollar',
'adaptar', 'ajustar', 'variar', 'metamorfosear',

# Verbos de relación y vinculación
'relacionar', 'conectar', 'vincular', 'asociar',
'unir', 'enlazar', 'articular', 'integrar',
'concatenar', 'interrelacionar', 'correlacionar',

# Verbos de pensamiento y razonamiento
'pensar', 'reflexionar', 'meditar', 'considerar',
'razonar', 'analizar', 'evaluar', 'valorar',
'deliberar', 'discernir', 'especular', 'conjeturar',

# Verbos de proceso y desarrollo
'desarrollar', 'evolucionar', 'progresar',
'avanzar', 'crecer', 'madurar', 'prosperar',
'progresar', 'expandirse', 'transformarse',

# Verbos de interacción
'interactuar', 'dialogar', 'conversar',
'intercambiar', 'negociar', 'mediar',
'colaborar', 'cooperar', 'participar',

# Verbos de decisión y voluntad
'decidir', 'optar', 'elegir', 'seleccionar',
'determinar', 'resolver', 'acordar',
'comprometerse', 'disponerse', 'proponerse',

# Verbos de percepción emocional
'sentir', 'percibir', 'experimentar',
'vivenciar', 'experimentar', 'intuir',
'presenciar', 'vivir', 'palpar',

# Verbos de construcción conceptual
'construir', 'elaborar', 'formular',
'conceptualizar', 'teorizar', 'sistematizar',
'estructurar', 'configurar', 'articular',

# Verbos de transformación sistémica
'reorganizar', 'reconfigurar', 'restructurar',
'reinventar', 'reimaginar', 'redefinir',
'reconstruir', 'reinterpretar', 'resignificar',

# Verbos avanzados y multidimensionales

# Verbos de transformación ontológica
'devenir', 'metamorfosear', 'transfigurar', 'mutar',
'evolucionar', 'transformarse', 'redefinirse',
'reconfigurarse', 'reinventarse', 'trascenderse',
'desplazarse', 'descentrarse', 'deslocalizarse',

# Verbos de complejidad sistémica
'interrelacionar', 'autoconstruirse', 'autorganizarse',
'autopoietizarse', 'retroalimentarse', 'emergerse',
'reconfigurarse', 'interconectarse', 'convergerse',
'dialogar', 'complementarse', 'rizomatizarse',

# Verbos de consciencia y metacognición
'autorreflexionar', 'metaconocerse', 'autobservarse',
'deconstruirse', 'resignificarse', 'problematizarse',
'cuestionarse', 'descentrarse', 'desidentificarse',
'reinterpretarse', 'reconstruirse', 'descolonizarse',

# Verbos de interacción epistémica
'dialogar', 'conversar', 'interpelar', 'cuestionar',
'problematizar', 'deconstruir', 'complementar',
'integrar', 'articular', 'resignificar',
'transversalizar', 'contextualizar', 'politizar',

# Verbos de construcción relacional
'vincularse', 'conectarse', 'entrelazarse',
'tejerse', 'entretejer', 'rizomatizarse',
'constelarse', 'configurarse', 'tramarse',
'articularse', 'interconectarse', 'convergerse',

# Verbos de procesamiento cognitivo
'procesar', 'metabolizar', 'integrar', 'resignificar',
'deconstruir', 'reinterpretar', 'descomponer',
'reconstruir', 'transformar', 'reconfigurar',
'desplazar', 'problematizar', 'contextualizar',

# Verbos de transformación social
'politizar', 'concientizar', 'empoderar',
'descolonizar', 'horizontalizar', 'democratizar',
'problematizar', 'visibilizar', 'territorializar',
'desestructurar', 'resignificar', 'transversalizar',

# Verbos de emergencia y complejidad
'emerger', 'autoorganizarse', 'autoproducirse',
'autoconstruirse', 'autotransformarse', 'autorrealizarse',
'retroalimentarse', 'reconfigurarse', 'reinterpretarse',
'descentrarse', 'deslocalizarse', 'desterritorializarse',

# Verbos de intersubjetividad
'dialogar', 'conversar', 'interpelar', 'complementarse',
'reconocerse', 'alterarse', 'transformarse',
'descentrarse', 'desidentificarse', 'reconstruirse',
'resignificarse', 'problematizarse', 'contextualizarse',

# Verbos de mediación y traducción
'mediar', 'traducir', 'interpretar', 'transducir',
'transitar', 'atravesar', 'desplazar', 'conectar',
'articular', 'complementar', 'integrar', 'converger',

# Verbos de disrupción epistémica
'descolonizar', 'deconstruir', 'problematizar',
'cuestionar', 'descentrar', 'desidentificar',
'resignificar', 'reinterpretar', 'transversalizar',
'politizar', 'desestabilizar', 'desarticular',

# Verbos de transformación existencial
'devenir', 'trascender', 'transformarse', 'mutar',
'reconfigurarse', 'descentrarse', 'deslocalizarse',
'desterritorializarse', 'reinventarse', 'redefinirse',
'desidentificarse', 'problematizarse', 'resignificarse',

# Verbos de construcción ecosistémica
'interrelacionarse', 'entrelazarse', 'complementarse',
'dialogar', 'converger', 'metabolizarse',
'autorregularse', 'autoorganizarse', 'retroalimentarse',
'reconfigurarse', 'emerger', 'transformarse',

# Verbos de potenciación y empoderamiento
'empoderar', 'potenciar', 'activar', 'movilizar',
'concientizar', 'visibilizar', 'horizontalizar',
'democratizar', 'politizar', 'territorializar',
'descolonizar', 'transversalizar', 'resignificar',

# Verbos de expansión y trascendencia
'expandirse', 'trascender', 'superar', 'desbordar',
'descentrarse', 'deslocalizar', 'desterritorializar',
'transitar', 'mutar', 'transformarse', 'reinventarse',
'reconfigurarse', 'emergerse', 'convergerse',

# Verbos avanzados y multidimensionales

# Verbos de transformación y cambio
'transformar', 'cambiar', 'modificar', 'alterar',
'renovar', 'reformar', 'revolucionar', 'redefinir',
'metamorfosear', 'reconfigurar', 'revolucionar',
'innovar', 'reinventar', 'reestructurar',

# Verbos de acción y ejecución
'ejecutar', 'realizar', 'cumplir', 'llevar a cabo',
'efectuar', 'desarrollar', 'materializar', 'concretar',
'instaurar', 'implementar', 'producir', 'generar',

# Verbos de percepción y cognición
'percibir', 'observar', 'notar', 'sentir',
'comprender', 'entender', 'analizar', 'evaluar',
'interpretar', 'reflexionar', 'conocer', 'descubrir',

# Verbos de comunicación y expresión
'comunicar', 'expresar', 'declarar', 'afirmar',
'proclamar', 'anunciar', 'informar', 'narrar',
'contar', 'relatar', 'describir', 'explicar',

# Verbos de deseo y voluntad
'querer', 'desear', 'anhelar', 'aspirar',
'necesitar', 'preferir', 'intentar', 'procurar',
'decidir', 'optar', 'elegir', 'comprometerse',

# Verbos de relación y conexión
'conectar', 'relacionar', 'vincular', 'asociar',
'unir', 'articular', 'interactuar', 'dialogar',
'colaborar', 'cooperar', 'integrar', 'complementar',

# Verbos de movimiento y desplazamiento
'ir', 'venir', 'moverse', 'desplazarse',
'trasladarse', 'avanzar', 'retroceder', 'regresar',
'entrar', 'salir', 'llegar', 'partir',

# Verbos de creación y construcción
'crear', 'construir', 'elaborar', 'desarrollar',
'producir', 'fabricar', 'diseñar', 'formar',
'instaurar', 'fundar', 'gestar', 'originar',

# Verbos de evaluación y juicio
'valorar', 'juzgar', 'criticar', 'examinar',
'ponderar', 'sopesar', 'calificar', 'clasificar',
'analizar', 'estudiar', 'investigar', 'reflexionar',

# Verbos de influencia y persuasión
'influir', 'persuadir', 'convencer', 'motivar',
'sugerir', 'recomendar', 'inducir', 'instigar',
'animar', 'incitar', 'exhortar', 'persuadir',

# Verbos de cuidado y protección
'proteger', 'cuidar', 'salvaguardar', 'defender',
'preservar', 'mantener', 'resguardar', 'sostener',
'asegurar', 'garantizar', 'custodiar', 'atender',

# Verbos de análisis y síntesis
'analizar', 'sintetizar', 'descomponer', 'recomponer',
'interpretar', 'evaluar', 'comparar', 'contrastar',
'correlacionar', 'contextualizar', 'generalizar',

# Verbos de reflexión y autoconocimiento
'reflexionar', 'meditar', 'introspectar', 'autoevaluar',
'autoconocerse', 'autorreconocerse', 'autocriticarse',
'cuestionarse', 'desafiarse', 'redefinirse',

# Verbos de interacción social
'interactuar', 'dialogar', 'conversar', 'discutir',
'negociar', 'colaborar', 'cooperar', 'participar',
'contribuir', 'intercambiar', 'compartir',

# Verbos de resistencia y desafío
'resistir', 'desafiar', 'oponerse', 'contrarrestar',
'combatir', 'luchar', 'rebelarse', 'protestar',
'cuestionar', 'desestabilizar', 'desafiar',

# Verbos de adaptación y flexibilidad
'adaptar', 'ajustar', 'modular', 'flexibilizar',
'transformar', 'reconfigurar', 'reorientar',
'rediseñar', 'redefinir', 'reajustar',

# Verbos de exploración y descubrimiento
'explorar', 'investigar', 'indagar', 'descubrir',
'averiguar', 'sondear', 'examinar', 'probar',
'analizar', 'escudriñar', 'revelar',

# Verbos de celebración y reconocimiento
'celebrar', 'reconocer', 'valorar', 'aplaudir',
'elogiar', 'honrar', 'conmemorar', 'exaltar',
'agradecer', 'felicitar', 'apreciar'
    
# Términos adicionales de contexto legal
'notificación', 'comunicación', 'citación', 'emplazamiento',
'requerimiento', 'solicitud', 'petición', 'queja', 'denuncia',

# Términos de comunicación procesal
'notificación', 'comunicación oficial', 'citación judicial',
'emplazamiento legal', 'requerimiento formal',
'traslado de documentos', 'intimación', 'exhorto',
'oficio', 'circular', 'comunicado', 'aviso legal',

# Términos de solicitud y petición
'solicitud', 'petición', 'requerimiento',
'instancia', 'demanda', 'recurso', 'apelación',
'alegación', 'pretensión', 'moción', 'súplica',

# Términos de iniciación procesal
'denuncia', 'querella', 'demanda', 'reclamación',
'impugnación', 'alegato', 'contestación',
'reconvención', 'excepción', 'incidente',

# Términos de comunicación administrativa
'oficio', 'memorando', 'circular', 'informe',
'comunicación interna', 'parte', 'acta',
'diligencia', 'constancia', 'certificación',

# Términos de notificación
'cédula de notificación', 'aviso', 'edicto',
'publicación oficial', 'notificación personal',
'notificación electrónica', 'estrados judiciales',
'tablero de notificaciones', 'comunicación fehaciente',

# Términos de requerimiento
'requerimiento judicial', 'intimación', 'conminación',
'apercibimiento', 'prevención', 'exhortación',
'mandamiento', 'orden', 'instrucción',

# Términos de queja y denuncia
'queja', 'denuncia', 'querella', 'reclamación',
'impugnación', 'protesta', 'objeción',
'inconformidad', 'recurso', 'apelación',

# Términos de citación
'citación judicial', 'comparecencia', 'convocatoria',
'llamamiento', 'emplazamiento', 'citatorio',
'orden de comparecencia', 'notificación de comparecencia',

# Términos de comunicación procesal
'diligencia', 'actuación', 'trámite',
'procedimiento', 'proceso', 'expediente',
'causa', 'juicio', 'instancia',

# Términos de solicitud especializada
'solicitud de prueba', 'petición de diligencia',
'requerimiento de información', 'pedido de documentación',
'instancia de medida cautelar', 'moción procesal',
'recurso de revisión', 'apelación de sentencia',

# Términos de comunicación técnica
'informe pericial', 'dictamen', 'peritaje',
'certificación técnica', 'constancia especializada',
'documento técnico', 'evaluación pericial',

# Términos de comunicación probatoria
'ofrecimiento de prueba', 'proposición de evidencia',
'aportación documental', 'presentación de testigos',
'solicitud de prueba pericial', 'requerimiento probatorio',

# Términos de comunicación cautelar
'medida cautelar', 'solicitud de embargo',
'petición de suspensión', 'requerimiento preventivo',
'solicitud de intervención', 'medida precautoria',

# Términos de comunicación recursiva
'recurso de apelación', 'recurso de casación',
'recurso de revisión', 'recurso extraordinario',
'impugnación', 'alegación', 'contestación',

# Términos de comunicación de urgencia
'comunicación urgente', 'requerimiento inmediato',
'solicitud de emergencia', 'medida cautelar urgente',
'notificación perentoria', 'diligencia de urgencia',

# Términos de comunicación internacional
'exhorto internacional', 'comunicación diplomática',
'solicitud de cooperación judicial', 'requerimiento transnacional',
'notificación internacional', 'carta rogatoria',

# Términos de comunicación electrónica
'notificación electrónica', 'comunicación digital',
'documento electrónico', 'expediente digital',
'firma electrónica', 'comunicación telemática',
'notificación por medios electrónicos',

# Términos avanzados de contexto legal y comunicación jurídica

# Términos de comunicación jurídica estratégica
'estrategia procesal', 'argumentación legal', 'construcción jurídica',
'hermenéutica legal', 'interpretación normativa', 'técnica jurídica',
'argumentación dialéctica', 'discurso jurídico', 'narrativa legal',
'deconstrucción normativa', 'análisis hermenéutico',

# Términos de comunicación procesal compleja
'comunicación jurisdiccional', 'interacción procesal',
'diálogo judicial', 'interlocución legal', 'mediación jurídica',
'transacción procesal', 'negociación legal', 'resolución dialógica',
'comunicación sistémica', 'interconexión procesal',

# Términos de comunicación multimodal
'comunicación multicanal', 'comunicación multiplataforma',
'comunicación digital', 'comunicación telemática',
'notificación electrónica', 'expediente digital',
'firma electrónica', 'documento digital certificado',
'comunicación transmedia', 'interoperabilidad jurídica',

# Términos de comunicación epistémica
'construcción del conocimiento jurídico', 'epistemología legal',
'teoría jurídica', 'interpretación hermenéutica',
'deconstrucción normativa', 'análisis crítico',
'pensamiento jurídico complejo', 'meta-análisis legal',
'genealogía jurídica', 'arqueología normativa',

# Términos de comunicación transnacional
'comunicación jurídica internacional', 'derecho transnacional',
'cooperación judicial global', 'comunicación diplomática',
'carta rogatoria', 'exhorto internacional',
'jurisdicción multilateral', 'derecho comparado',
'comunicación intercultural', 'pluralismo jurídico',

# Términos de comunicación transformadora
'comunicación restaurativa', 'justicia dialógica',
'reparación integral', 'reconstrucción narrativa',
'transformación de conflictos', 'mediación transformadora',
'comunicación empática', 'reconocimiento jurídico',
'reparación simbólica', 'reconstrucción social',

# Términos de comunicación decolonial
'decolonialidad jurídica', 'epistemologías del sur',
'pluralismo jurídico', 'justicia intercultural',
'comunicación desde los márgenes', 'derecho insurgente',
'hermenéutica decolonial', 'juridicidad otra',
'pensamiento fronterizo', 'comunicación contrahegemónica',

# Términos de comunicación sistémica
'comunicación ecosistémica', 'derecho relacional',
'interconexión jurídica', 'sistemas legales complejos',
'autopoiesis jurídica', 'retroalimentación normativa',
'derecho en red', 'comunicación interdependiente',
'sistemas adaptativos', 'derecho emergente',

# Términos de comunicación ética
'ética comunicacional', 'bioética legal',
'principios de comunicación', 'integridad procesal',
'comunicación transparente', 'ética dialógica',
'responsabilidad comunicativa', 'principio de buena fe',
'comunicación restaurativa', 'justicia ética',

# Términos de comunicación tecnológica
'tecnologías jurídicas', 'inteligencia artificial legal',
'big data jurídico', 'blockchain legal', 'smart contracts',
'análisis predictivo', 'jurimetría', 'legal tech',
'automatización jurídica', 'transformación digital',

# Términos de comunicación prospectiva
'prospectiva jurídica', 'anticipación normativa',
'escenarios legales', 'futurización jurídica',
'derecho especulativo', 'innovación normativa',
'pensamiento estratégico', 'construcción de futuro',
'derecho emergente', 'juridicidad anticipatoria',

# Términos de comunicación ontológica
'ontología jurídica', 'ser jurídico', 'existencialidad legal',
'dimensiones del derecho', 'ser normativo',
'corporalidad jurídica', 'subjetividad legal',
'performatividad jurídica', 'derecho como experiencia',

# Términos de comunicación epistemológica
'epistemología jurídica', 'teoría del conocimiento legal',
'construcción de saberes', 'paradigmas jurídicos',
'marcos interpretativos', 'horizontes de comprensión',
'metateorías legales', 'reflexividad jurídica',
'crítica epistemológica', 'deconstrucción cognitiva',

# Términos de comunicación política
'comunicación político-jurídica', 'juridificación',
'politización del derecho', 'derecho como arena política',
'comunicación instituyente', 'transformación sociopolítica',
'derecho insurgente', 'comunicación contrahegemónica',
'juridicidad política', 'derecho como práctica emancipadora',

# Términos avanzados de contexto legal y comunicación jurídica

# Términos de comunicación jurídica estratégica
'estrategia procesal', 'argumentación legal', 'construcción jurídica',
'hermenéutica legal', 'interpretación normativa', 'técnica jurídica',
'argumentación dialéctica', 'discurso jurídico', 'narrativa legal',
'deconstrucción normativa', 'análisis hermenéutico',

# Términos de comunicación procesal compleja
'comunicación jurisdiccional', 'interacción procesal',
'diálogo judicial', 'interlocución legal', 'mediación jurídica',
'transacción procesal', 'negociación legal', 'resolución dialógica',
'comunicación sistémica', 'interconexión procesal',

# Términos de comunicación multimodal
'comunicación multicanal', 'comunicación multiplataforma',
'comunicación digital', 'comunicación telemática',
'notificación electrónica', 'expediente digital',
'firma electrónica', 'documento digital certificado',
'comunicación transmedia', 'interoperabilidad jurídica',

# Términos de comunicación epistémica
'construcción del conocimiento jurídico', 'epistemología legal',
'teoría jurídica', 'interpretación hermenéutica',
'deconstrucción normativa', 'análisis crítico',
'pensamiento jurídico complejo', 'meta-análisis legal',
'genealogía jurídica', 'arqueología normativa',

# Términos de comunicación transnacional
'comunicación jurídica internacional', 'derecho transnacional',
'cooperación judicial global', 'comunicación diplomática',
'carta rogatoria', 'exhorto internacional',
'jurisdicción multilateral', 'derecho comparado',
'comunicación intercultural', 'pluralismo jurídico',

# Términos de comunicación transformadora
'comunicación restaurativa', 'justicia dialógica',
'reparación integral', 'reconstrucción narrativa',
'transformación de conflictos', 'mediación transformadora',
'comunicación empática', 'reconocimiento jurídico',
'reparación simbólica', 'reconstrucción social',

# Términos de comunicación decolonial
'decolonialidad jurídica', 'epistemologías del sur',
'pluralismo jurídico', 'justicia intercultural',
'comunicación desde los márgenes', 'derecho insurgente',
'hermenéutica decolonial', 'juridicidad otra',
'pensamiento fronterizo', 'comunicación contrahegemónica',

# Términos de comunicación sistémica
'comunicación ecosistémica', 'derecho relacional',
'interconexión jurídica', 'sistemas legales complejos',
'autopoiesis jurídica', 'retroalimentación normativa',
'derecho en red', 'comunicación interdependiente',
'sistemas adaptativos', 'comunicación holística',

# Términos de comunicación ética
'ética comunicacional', 'bioética legal',
'principios de comunicación', 'integridad procesal',
'comunicación transparente', 'ética dialógica',
'responsabilidad comunicativa', 'principio de buena fe',
'comunicación restaurativa', 'justicia ética',

# Términos de comunicación tecnológica
'tecnologías jurídicas', 'inteligencia artificial legal',
'big data jurídico', 'blockchain legal', 'smart contracts',
'análisis predictivo', 'jurimetría', 'legal tech',
'automatización jurídica', 'transformación digital',

# Términos de comunicación prospectiva
'prospectiva jurídica', 'anticipación normativa',
'escenarios legales', 'futurización jurídica',
'derecho especulativo', 'innovación normativa',
'pensamiento estratégico', 'construcción de futuro',
'derecho emergente', 'juridicidad anticipatoria',

# Términos de comunicación ontológica
'ontología jurídica', 'ser jurídico', 'existencialidad legal',
'dimensiones del derecho', 'ser normativo',
'corporalidad jurídica', 'subjetividad legal',
'performatividad jurídica', 'derecho como experiencia',

# Términos de comunicación epistemológica
'epistemología jurídica', 'teoría del conocimiento legal',
'construcción de saberes', 'paradigmas jurídicos',
'marcos interpretativos', 'horizontes de comprensión',
'metateorías legales', 'reflexividad jurídica',
'crítica epistemológica', 'deconstrucción cognitiva',

# Términos de comunicación política
'comunicación político-jurídica', 'juridificación',
'politización del derecho', 'derecho como arena política',
'comunicación instituyente', 'transformación sociopolítica',
'derecho insurgente', 'comunicación contrahegemónica',
'juridicidad política', 'derecho como práctica emancipadora',

# Términos de comunicación de derechos humanos
'defensa de derechos humanos', 'activismo legal',
'justicia social', 'derechos fundamentales',
'comunicación de derechos', 'abogacía de derechos',
'promoción de derechos', 'educación en derechos',
'concientización sobre derechos', 'reparación de derechos',

# Términos de comunicación intercultural
'diálogo intercultural', 'comunicación intercultural',
'pluralismo cultural', 'derecho a la diversidad',
'respeto a la diversidad', 'interculturalidad',
'mediación intercultural', 'justicia intercultural',
'comunicación inclusiva', 'derechos culturales',

# Términos de comunicación en crisis
'comunicación de crisis', 'gestión de crisis',
'resiliencia jurídica', 'adaptación legal',
'comunicación de emergencia', 'respuesta legal',
'planificación de crisis', 'estrategia de crisis',
'comunicación proactiva', 'prevención de crisis',

# Términos de comunicación en litigio
'litigio estratégico', 'comunicación litigiosa',
'defensa legal', 'estrategia de defensa',
'argumentación en juicio', 'tácticas litigiosas',
'comunicación en sala', 'intervención judicial',
'presentación de pruebas', 'exposición de argumentos',

# Términos avanzados de contexto legal y comunicación jurídica

# Términos de comunicación jurídica estratégica
'estrategia procesal', 'argumentación legal', 'construcción jurídica',
'hermenéutica legal', 'interpretación normativa', 'técnica jurídica',
'argumentación dialéctica', 'discurso jurídico', 'narrativa legal',
'deconstrucción normativa', 'análisis hermenéutico',

# Términos de comunicación procesal compleja
'comunicación jurisdiccional', 'interacción procesal',
'diálogo judicial', 'interlocución legal', 'mediación jurídica',
'transacción procesal', 'negociación legal', 'resolución dialógica',
'comunicación sistémica', 'interconexión procesal',

# Términos de comunicación multimodal
'comunicación multicanal', 'comunicación multiplataforma',
'comunicación digital', 'comunicación telemática',
'notificación electrónica', 'expediente digital',
'firma electrónica', 'documento digital certificado',
'comunicación transmedia', 'interoperabilidad jurídica',

# Términos de comunicación epistémica
'construcción del conocimiento jurídico', 'epistemología legal',
'teoría jurídica', 'interpretación hermenéutica',
'deconstrucción normativa', 'análisis crítico',
'pensamiento jurídico complejo', 'meta-análisis legal',
'genealogía jurídica', 'arqueología normativa',

# Términos de comunicación transnacional
'comunicación jurídica internacional', 'derecho transnacional',
'cooperación judicial global', 'comunicación diplomática',
'carta rogatoria', 'exhorto internacional',
'jurisdicción multilateral', 'derecho comparado',
'comunicación intercultural', 'pluralismo jurídico',

# Términos de comunicación transformadora
'comunicación restaurativa', 'justicia dialógica',
'reparación integral', 'reconstrucción narrativa',
'transformación de conflictos', 'mediación transformadora',
'comunicación empática', 'reconocimiento jurídico',
'reparación simbólica', 'reconstrucción social',

# Términos de comunicación decolonial
'decolonialidad jurídica', 'epistemologías del sur',
'pluralismo jurídico', 'justicia intercultural',
'comunicación desde los márgenes', 'derecho insurgente',
'hermenéutica decolonial', 'juridicidad otra',
'pensamiento fronterizo', 'comunicación contrahegemónica',

# Términos de comunicación sistémica
'comunicación ecosistémica', 'derecho relacional',
'interconexión jurídica', 'sistemas legales complejos',
'autopoiesis jurídica', 'retroalimentación normativa',
'derecho en red', 'comunicación interdependiente',
'sistemas adaptativos', 'comunicación holística',

# Términos de comunicación ética
'ética comunicacional', 'bioética legal',
'principios de comunicación', 'integridad procesal',
'comunicación transparente', 'ética dialógica',
'responsabilidad comunicativa', 'principio de buena fe',
'comunicación restaurativa', 'justicia ética',

# Términos de comunicación tecnológica
'tecnologías jurídicas', 'inteligencia artificial legal',
'big data jurídico', 'blockchain legal', 'smart contracts',
'análisis predictivo', 'jurimetría', 'legal tech',
'automatización jurídica', 'transformación digital',

# Términos de comunicación prospectiva
'prospectiva jurídica', 'anticipación normativa',
'escenarios legales', 'futurización jurídica',
'derecho especulativo', 'innovación normativa',
'pensamiento estratégico', 'construcción de futuro',
'derecho emergente', 'juridicidad anticipatoria',

# Términos de comunicación ontológica
'ontología jurídica', 'ser jurídico', 'existencialidad legal',
'dimensiones del derecho', 'ser normativo',
'corporalidad jurídica', 'subjetividad legal',
'performatividad jurídica', 'derecho como experiencia',

# Términos de comunicación epistemológica
'epistemología jurídica', 'teoría del conocimiento legal',
'construcción de saberes', 'paradigmas jurídicos',
'marcos interpretativos', 'horizontes de comprensión',
'metateorías legales', 'reflexividad jurídica',
'crítica epistemológica', 'deconstrucción cognitiva',

# Términos de comunicación política
'comunicación político-jurídica', 'juridificación',
'politización del derecho', 'derecho como arena política',
'comunicación instituyente', 'transformación sociopolítica',
'derecho insurgente', 'comunicación contrahegemónica',
'juridicidad política', 'derecho como práctica emancipadora',

# Términos de comunicación de derechos humanos
'defensa de derechos humanos', 'activismo legal',
'justicia social', 'derechos fundamentales',
'comunicación de derechos', 'abogacía de derechos',
'promoción de derechos', 'educación en derechos',
'concientización sobre derechos',
'foc', 'escrito', 'allegado', 'oncologica', 'requiera',
'historia', 'clinica', 'encuentra', 'procura', 'adelantar',
'cancer', 'diabetes', 'hipertension', 'asma', 'alzheimer',
'parkinson', 'esquizofrenia', 'tuberculosis', 'zika',
"diabetes",
"hipertension",
"cancer",
"artritis",
"epilepsia",
"asma",
"bronquitis",
"alzheimer",
"parkinson",
"esquizofrenia",
"tuberculosis",
"hepatitis",
"dengue",
"chikungunya",
"covid",
"zika",
"sida",
"vih",
"insuficiencia",
"renal",
"infarto",
"cardiopatia",
"derrame",
"cerebral",
"meningitis",
"osteoporosis",
"lupus",
"anemia",
"cirrosis",
"colitis",
"dermatitis",
"fibromialgia",
"gastritis",
"glaucoma",
"leucemia",
"migraña",
"nefritis",
"obesidad",
"pancreatitis",
"psoriasis",
"rinitis",
"sindrome",
"down",
"tosferina",
"varicela",
"salmonelosis",
"sarampion",
"tifoidea",
"tuberculosis",
"ulcera",
"gastrica",
"hepatitis",
"bogota",
"medellin",
"cali",
"barranquilla",
"cartagena",
"bucaramanga",
"pereira",
"manizales",
"armenia",
"cucuta",
"ibague",
"villavicencio",
"neiva",
"santa",
"marta",
"pastos",
"monteria",
"quibdo",
"leticia",
"riohacha",
"popayan",
"valledupar",
"tunja",
"florencia",
"san",
"buenaventura",
"tumaco",
"yopal",
"sincelejo",
"girardot",
"soacha",
"rionegro",
"itagui",
"envigado",
"bello",
"pasto",
"soledad",
"dosquebradas",
"facatativa",
"zipaquira",
"sogamoso",
"colombia",
"ecuador",
"venezuela",
"peru",
"brasil",
"argentina",
"chile",
"uruguay",
"paraguay",
"bolivia",
"mexico",
"guatemala",
"honduras",
"nicaragua",
"costa",
"rica",
"panama",
"el",
"salvador",
"republica",
"dominicana",
"haiti",
"puerto",
"rico",
"cuba",
"estados",
"unidos",
"canada",
"españa",
"francia",
"italia",
"alemania",
"portugal",
"inglaterra",
"suecia",
"noruega",
"finlandia",
"rusia",
"china",
"japon",
"india",
"corea",
"del",
"sur",
"filipinas",
"malasia",
"australia",
"nueva",
"zelanda",
"sudafrica",
"constitucion",
"codigo",
"penal",
"codigo",
"civil",
"reglamento",
"ley",
"jurisprudencia",
"sentencia",
"demanda",
"fallo",
"apelacion",
"acuerdo",
"convencion",
"tratado",
"juez",
"magistrado",
"fiscal",
"abogado",
"demandante",
"demandado",
"acusado",
"defensor",
"notario",
"contrato",
"escritura",
"legislacion",
"decreto",
"resolucion",
"norma",
"sancion",
"multas",
"cautelar",
"custodia",
"tribunal",
"audiencia",
"litigio",
"mediacion",
"arbitraje",
"conciliacion",
"indulto",
"amnistia",
"recurso",
"penalizacion",
"peritaje",
"expediente",
"jurisdiccion",
"probatorio",
"interrogatorio",
"apelacion",
"infraccion",
"hospital",
"clínica",
"urgencias",
"urologia",
"neurologia",
"pediatria",
"oncologia",
"cardiologia",
"dermatologia",
"endocrinologia",
"neumologia",
"gastroenterologia",
"hematologia",
"oftalmologia",
"reumatologia",
"geriatria",
"nefrologia",
"fisioterapia",
"terapia",
"intensiva",
"cuidados",
"paliativos",
"anestesiologia",
"farmacologia",
"psiquiatria",
"psicologia",
"radiologia",
"biopsia",
"laboratorio",
"clinico",
"vacunacion",
"consulta",
"externa",
"enfermeria",
"epidemiologia",
"biomedicina",
"bioseguridad",
"telemedicina",
"historia",
"clinica",
"medicina",
"investigacion",
"diagnostico",
"clinica",
"prevencion",
"salud",
"rehabilitacion",
"nutricion",
"diagnostico",
"enfermedad",
"sintoma",
"enfermera",
"tratamiento",
"medico",
"medicamento",
"vacuna",
"farmacia",
"vacunacion",
"patologia",
"pandemia",
"brotes",
"epidemia",
"epidemico",
"epidemicos",
"epidemica",
}

