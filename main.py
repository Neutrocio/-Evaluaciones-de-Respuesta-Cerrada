import sys
import os

# Permite importar desde src/ directamente
sys.path.insert(0, os.path.dirname(__file__))

from datos.cargador import listar_examenes, cargar_examen
from logica.corrector import corregir_examen
from logica.puntaje import calcular_puntaje
from cli.menu import mostrar_bienvenida, mostrar_menu, seleccionar_examen
from cli.presentador import mostrar_instrucciones, presentar_preguntas
from cli.resultados import mostrar_resultados

DIRECTORIO_EXAMENES = os.path.join(os.path.dirname(__file__), "..", "examenes")


def main():
    mostrar_bienvenida()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            # Listar exámenes disponibles
            examenes = listar_examenes(DIRECTORIO_EXAMENES)

            if not examenes:
                print("\nNo hay exámenes disponibles en la carpeta 'examenes/'.")
                input("Presiona ENTER para volver al menú...")
                continue

            # Seleccionar examen
            nombre_archivo = seleccionar_examen(examenes)
            ruta = os.path.join(DIRECTORIO_EXAMENES, nombre_archivo)

            # Cargar y validar
            try:
                examen = cargar_examen(ruta)
            except (FileNotFoundError, ValueError) as e:
                print(f"\nError al cargar el examen: {e}")
                input("Presiona ENTER para volver al menú...")
                continue

            print(f"\nExamen cargado: {examen['titulo']}")
            if "descripcion" in examen:
                print(f"{examen['descripcion']}")

            # Instrucciones
            mostrar_instrucciones()

            # Presentar preguntas y recoger respuestas
            respuestas = presentar_preguntas(examen["preguntas"])

            # Corregir
            resultados = corregir_examen(examen["preguntas"], respuestas)

            # Calcular puntaje
            puntaje = calcular_puntaje(resultados)

            # Mostrar resultados
            mostrar_resultados(puntaje, resultados)

            input("Presiona ENTER para volver al menú...")

        elif opcion == "2":
            mostrar_instrucciones()

        elif opcion == "3":
            print("\nHasta luego!\n")
            break

        else:
            print("\nOpción no válida. Escribe 1, 2 o 3.")


if __name__ == "__main__":
    main()
