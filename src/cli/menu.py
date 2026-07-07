import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_bienvenida():
    limpiar_pantalla()
    print("=" * 50)
    print("   SISTEMA DE EVALUACIÓN AUTOMATIZADA CLI")
    print("=" * 50)
    print()


def mostrar_menu():
    print("\n¿Qué deseas hacer?")
    print("  1. Iniciar examen")
    print("  2. Ver instrucciones")
    print("  3. Salir")
    print()


def seleccionar_examen(examenes):
    """Muestra la lista de exámenes y retorna el nombre del elegido."""
    print("Exámenes disponibles:")
    print()
    for i, nombre in enumerate(examenes, start=1):
        print(f"  {i}. {nombre}")
    print()

    while True:
        opcion = input("Elige el número del examen: ").strip()
        if opcion.isdigit():
            indice = int(opcion) - 1
            if 0 <= indice < len(examenes):
                return examenes[indice]
        print("Opción no válida. Intenta de nuevo.")
