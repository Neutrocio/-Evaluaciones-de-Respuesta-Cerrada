def mostrar_resultados(puntaje, resultados):
    print()
    print("=" * 50)
    print("           RESULTADOS DEL EXAMEN")
    print("=" * 50)
    print()

    for i, resultado in enumerate(resultados, start=1):
        if resultado["correcto"]:
            estado = "CORRECTO"
            pts    = f"+{resultado['puntaje_obtenido']} pts"
        else:
            estado = "INCORRECTO"
            pts    = "+0 pts"

        print(f"Pregunta {i}: {estado}  ({pts})")

        if not resultado["correcto"]:
            print(f"   Respuesta correcta: {resultado['respuesta_correcta']}")
            if resultado["retroalimentacion"]:
                print(f"   Explicacion: {resultado['retroalimentacion']}")

        print()

    print("-" * 50)
    print(f"PUNTAJE TOTAL : {puntaje['total_obtenido']} / {puntaje['total_posible']} puntos")
    print(f"PORCENTAJE    : {puntaje['porcentaje']}%")
    print(f"CORRECTAS     : {puntaje['correctas']}")
    print(f"INCORRECTAS   : {puntaje['incorrectas']}")
    print("-" * 50)
    print()

    if puntaje["porcentaje"] >= 90:
        print("Excelente! Obtuviste mas del 90%.")
    elif puntaje["porcentaje"] >= 70:
        print("Buen trabajo! Aprobaste el examen.")
    elif puntaje["porcentaje"] >= 50:
        print("Pasaste, pero puedes mejorar.")
    else:
        print("No aprobaste. Revisa el material e intentalo de nuevo.")

    print()
