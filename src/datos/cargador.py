import json
import os


def listar_examenes(directorio="examenes"):
    """Retorna lista de archivos .json disponibles en el directorio."""
    if not os.path.exists(directorio):
        return []

    archivos = [f for f in os.listdir(directorio) if f.endswith(".json")]
    return sorted(archivos)


def cargar_examen(ruta_archivo):
    """Lee y retorna el contenido de un archivo JSON de examen."""
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")

    with open(ruta_archivo, "r", encoding="utf-8") as f:
        try:
            datos = json.load(f)
        except json.JSONDecodeError:
            raise ValueError(f"El archivo no tiene formato JSON válido: {ruta_archivo}")

    validar_examen(datos)
    return datos


def validar_examen(datos):
    """Verifica que el JSON tenga la estructura correcta."""
    if "titulo" not in datos:
        raise ValueError("El examen debe tener un campo 'titulo'.")

    if "preguntas" not in datos:
        raise ValueError("El examen debe tener un campo 'preguntas'.")

    if len(datos["preguntas"]) == 0:
        raise ValueError("El examen debe tener al menos una pregunta.")

    tipos_validos = ["opcion_multiple", "verdadero_falso", "emparejamiento"]

    for pregunta in datos["preguntas"]:
        pid = pregunta.get("id", "?")

        if "tipo" not in pregunta:
            raise ValueError(f"Pregunta {pid}: falta el campo 'tipo'.")

        if pregunta["tipo"] not in tipos_validos:
            raise ValueError(f"Pregunta {pid}: tipo '{pregunta['tipo']}' no válido.")

        if "enunciado" not in pregunta:
            raise ValueError(f"Pregunta {pid}: falta el campo 'enunciado'.")

        if "respuesta_correcta" not in pregunta:
            raise ValueError(f"Pregunta {pid}: falta el campo 'respuesta_correcta'.")

        if "puntaje" not in pregunta:
            raise ValueError(f"Pregunta {pid}: falta el campo 'puntaje'.")

        if pregunta["tipo"] == "opcion_multiple" and "opciones" not in pregunta:
            raise ValueError(f"Pregunta {pid}: opción múltiple sin campo 'opciones'.")

    return True
