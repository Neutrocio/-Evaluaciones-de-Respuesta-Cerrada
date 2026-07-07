import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from logica.normalizador import normalizar_texto


def corregir_pregunta(pregunta, respuesta_usuario):
    """Corrige una pregunta individual y retorna el resultado."""
    respuesta_norm = normalizar_texto(str(respuesta_usuario))
    correcta_norm  = normalizar_texto(str(pregunta["respuesta_correcta"]))

    resultado = {
        "id":                 pregunta["id"],
        "tipo":               pregunta["tipo"],
        "enunciado":          pregunta["enunciado"],
        "correcto":           False,
        "puntaje_obtenido":   0,
        "puntaje_maximo":     pregunta["puntaje"],
        "respuesta_usuario":  respuesta_usuario,
        "respuesta_correcta": pregunta["respuesta_correcta"],
        "retroalimentacion":  ""
    }

    if pregunta["tipo"] == "opcion_multiple":
        if respuesta_norm == correcta_norm:
            resultado["correcto"] = True
            resultado["puntaje_obtenido"] = pregunta["puntaje"]
        else:
            retro = pregunta.get("retroalimentacion", {})
            resultado["retroalimentacion"] = retro.get(
                respuesta_norm.upper(),
                "Respuesta incorrecta."
            )

    elif pregunta["tipo"] == "verdadero_falso":
        # Aceptar variantes cortas
        if respuesta_norm == "v":
            respuesta_norm = "verdadero"
        elif respuesta_norm == "f":
            respuesta_norm = "falso"

        if respuesta_norm == correcta_norm:
            resultado["correcto"] = True
            resultado["puntaje_obtenido"] = pregunta["puntaje"]
        else:
            retro = pregunta.get("retroalimentacion", {})
            resultado["retroalimentacion"] = retro.get(
                respuesta_norm,
                "Respuesta incorrecta."
            )

    elif pregunta["tipo"] == "emparejamiento":
        # Respuesta esperada: "1-B, 2-A, 3-D"
        pares_usuario   = _parsear_emparejamiento(respuesta_norm)
        pares_correctos = {
            str(k): normalizar_texto(str(v))
            for k, v in pregunta["respuesta_correcta"].items()
        }

        if pares_usuario == pares_correctos:
            resultado["correcto"] = True
            resultado["puntaje_obtenido"] = pregunta["puntaje"]
        else:
            retro = pregunta.get("retroalimentacion", {})
            resultado["retroalimentacion"] = retro.get(
                "default",
                "Respuesta incorrecta."
            )

    return resultado


def _parsear_emparejamiento(texto):
    """Convierte '1-b, 2-a, 3-d' en {'1': 'b', '2': 'a', '3': 'd'}."""
    pares = {}
    partes = texto.replace(" ", "").split(",")
    for parte in partes:
        if "-" in parte:
            izq, der = parte.split("-", 1)
            pares[izq.strip()] = der.strip()
    return pares


def corregir_examen(preguntas, respuestas_usuario):
    """Corrige todas las preguntas y retorna lista de resultados."""
    if len(preguntas) != len(respuestas_usuario):
        raise ValueError("El número de respuestas no coincide con el de preguntas.")

    resultados = []
    for pregunta, respuesta in zip(preguntas, respuestas_usuario):
        resultado = corregir_pregunta(pregunta, respuesta)
        resultados.append(resultado)

    return resultados
