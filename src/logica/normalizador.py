def normalizar_texto(texto):
    """Convierte texto a minúsculas, elimina espacios extra y tildes."""
    if not texto:
        return ""

    texto = texto.strip().lower()

    # Eliminar espacios múltiples internos
    while "  " in texto:
        texto = texto.replace("  ", " ")

    # Normalizar tildes
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u"
    }
    for con_tilde, sin_tilde in reemplazos.items():
        texto = texto.replace(con_tilde, sin_tilde)

    return texto
