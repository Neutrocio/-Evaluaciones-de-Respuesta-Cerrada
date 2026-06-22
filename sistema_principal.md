# Pseudocódigo — Sistema Principal

## Archivo: `main.py`

Este módulo es el punto de entrada del programa. Coordina las tres capas.

---

```
INICIO main()

  MOSTRAR bienvenida al sistema

  REPETIR:
    LLAMAR mostrar_menu()
    opcion ← LEER entrada del usuario

    SI opcion == "1":  // Iniciar examen
      examenes ← LLAMAR listar_examenes("examenes/")
      
      SI examenes está vacío:
        MOSTRAR "No hay exámenes disponibles."
        CONTINUAR al siguiente ciclo
      
      LLAMAR mostrar_lista_examenes(examenes)
      seleccion ← LEER entrada del usuario
      archivo ← examenes[seleccion]
      
      datos_examen ← LLAMAR cargar_examen(archivo)
      
      SI datos_examen es inválido:
        MOSTRAR "Error al cargar el examen."
        CONTINUAR al siguiente ciclo
      
      LLAMAR mostrar_instrucciones()
      
      respuestas_usuario ← LLAMAR presentar_preguntas(datos_examen["preguntas"])
      
      resultados ← LLAMAR corregir_examen(
                      datos_examen["preguntas"],
                      respuestas_usuario
                   )
      
      puntaje ← LLAMAR calcular_puntaje(resultados)
      
      LLAMAR mostrar_resultados(puntaje, resultados)
    
    SI opcion == "2":  // Instrucciones
      LLAMAR mostrar_instrucciones()
    
    SI opcion == "3":  // Salir
      MOSTRAR "¡Hasta luego!"
      TERMINAR programa
    
    SI NO:
      MOSTRAR "Opción no válida. Intente de nuevo."

FIN main()
```
