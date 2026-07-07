def calcular_puntaje(resultados):
    """Calcula el puntaje total a partir de los resultados."""
    total_obtenido = 0
    total_posible  = 0
    correctas      = 0
    incorrectas    = 0

    for resultado in resultados:
        total_obtenido += resultado["puntaje_obtenido"]
        total_posible  += resultado["puntaje_maximo"]

        if resultado["correcto"]:
            correctas += 1
        else:
            incorrectas += 1

    if total_posible == 0:
        porcentaje = 0.0
    else:
        porcentaje = round((total_obtenido / total_posible) * 100, 1)

    return {
        "total_obtenido": total_obtenido,
        "total_posible":  total_posible,
        "porcentaje":     porcentaje,
        "correctas":      correctas,
        "incorrectas":    incorrectas
    }
