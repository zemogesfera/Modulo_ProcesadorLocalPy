import re

def eliminar_caracteres_especiales(texto):
    # Regex para eliminar cualquier carácter que no sea letra, número o espacio
    texto_limpio = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s]', '', texto)
    return texto_limpio