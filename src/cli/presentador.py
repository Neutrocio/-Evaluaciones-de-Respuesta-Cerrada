def mostrar_instrucciones():
    print()
    print("=" * 50)
    print("             INSTRUCCIONES")
    print("=" * 50)
    print()
    print("Este examen tiene 2 tipos de preguntas:")
    print()
    print("1. OPCIÓN MÚLTIPLE")
    print("   Escribe la letra de tu respuesta: A, B, C o D")
    print()
    print("2. VERDADERO / FALSO")
    print("   Escribe: verdadero  o  falso")
    print("   También puedes escribir: v  o  f")
    print()
    print("3. EMPAREJAMIENTO")
    print("   Escribe las asociaciones así: 1-A, 2-C, 3-B")
    print()
    print("=" * 50)
    input("\nPresiona ENTER para continuar...")


def presentar_preguntas(preguntas):
    """Presenta cada pregunta y retorna lista de respuestas del usuario."""
    respuestas = []
    total = len(preguntas)

    for i, pregunta in enumerate(preguntas, start=1):
        print()
        print("-" * 50)
        print(f"Pregunta {i} de {total}  [{pregunta['puntaje']} puntos]")
        print()
        print(pregunta["enunciado"])
        print()

        if pregunta["tipo"] == "opcion_multiple":
            for letra, texto in pregunta["opciones"].items():
                print(f"  {letra}) {texto}")
            print()
            respuesta = _pedir_respuesta_multiple()

        elif pregunta["tipo"] == "verdadero_falso":
            print("  Opciones: verdadero / falso")
            print()
            respuesta = _pedir_respuesta_vf()

        elif pregunta["tipo"] == "emparejamiento":
            _mostrar_columnas(pregunta)
            respuesta = input("Tu respuesta (ej: 1-A, 2-C, 3-B): ").strip()

        else:
            respuesta = input("Tu respuesta: ").strip()

        respuestas.append(respuesta)

    return respuestas


def _pedir_respuesta_multiple():
    opciones_validas = ["a", "b", "c", "d"]
    while True:
        respuesta = input("Tu respuesta (A/B/C/D): ").strip().lower()
        if respuesta in opciones_validas:
            return respuesta.upper()
        print("Opción no válida. Escribe A, B, C o D.")


def _pedir_respuesta_vf():
    validas = ["verdadero", "falso", "v", "f"]
    while True:
        respuesta = input("Tu respuesta (verdadero/falso): ").strip().lower()
        if respuesta in validas:
            return respuesta
        print("Opción no válida. Escribe verdadero o falso.")


def _mostrar_columnas(pregunta):
    izquierda = pregunta.get("columna_izquierda", [])
    derecha    = pregunta.get("columna_derecha", [])

    print("  Columna A                    Columna B")
    print()

    for j, item in enumerate(izquierda, start=1):
        print(f"  {j}. {item}")

    print()
    letras = "ABCD"
    for j, item in enumerate(derecha):
        print(f"  {letras[j]}. {item}")
    print()
