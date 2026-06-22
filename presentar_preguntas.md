# Pseudocódigo — Capa 3: Presentación de Preguntas

## Archivo: `src/cli/presentador.py`

---

### Función: `mostrar_instrucciones()`

```
FUNCIÓN mostrar_instrucciones():

  MOSTRAR "════════ INSTRUCCIONES ════════"
  MOSTRAR "Este examen contiene 4 tipos de preguntas:"
  MOSTRAR ""
  MOSTRAR "1. OPCIÓN MÚLTIPLE"
  MOSTRAR "   → Escribe la letra de tu respuesta: A, B, C o D"
  MOSTRAR ""
  MOSTRAR "2. VERDADERO / FALSO"
  MOSTRAR "   → Escribe: verdadero  o  falso"
  MOSTRAR ""
  MOSTRAR "3. COMPLETAR ESPACIOS"
  MOSTRAR "   → Escribe la palabra o frase que falta"
  MOSTRAR ""
  MOSTRAR "4. EMPAREJAMIENTO"
  MOSTRAR "   → Escribe las asociaciones en formato: 1-A, 2-C, 3-B"
  MOSTRAR "══════════════════════════════"
  MOSTRAR ""
  ESPERAR que el usuario presione ENTER para continuar

FIN mostrar_instrucciones
```

---

### Función: `presentar_preguntas(preguntas)`

```
FUNCIÓN presentar_preguntas(preguntas):

  respuestas_usuario ← lista vacía []
  total_preguntas ← LONGITUD de preguntas

  PARA CADA pregunta EN preguntas (con índice i):
    
    MOSTRAR "────────────────────────────────"
    MOSTRAR "Pregunta {i+1} de {total_preguntas}  [{pregunta['puntaje']} puntos]"
    MOSTRAR ""
    MOSTRAR pregunta["enunciado"]
    MOSTRAR ""
    
    // Presentación según el tipo
    SI pregunta["tipo"] == "opcion_multiple":
      PARA CADA (letra, texto) EN pregunta["opciones"]:
        MOSTRAR "  {letra}) {texto}"
      MOSTRAR ""
      respuesta ← LEER entrada del usuario, pedir "Tu respuesta (A/B/C/D): "
    
    SI pregunta["tipo"] == "verdadero_falso":
      MOSTRAR "  Opciones: verdadero / falso"
      MOSTRAR ""
      respuesta ← LEER entrada del usuario, pedir "Tu respuesta: "
    
    SI pregunta["tipo"] == "completar":
      respuesta ← LEER entrada del usuario, pedir "Completa el espacio: "
    
    SI pregunta["tipo"] == "emparejamiento":
      MOSTRAR "  Columna A              Columna B"
      PARA CADA (num, item) EN pregunta["columna_izquierda"] (con índice):
        MOSTRAR "  {num+1}. {item}"
      MOSTRAR ""
      PARA CADA (letra, item) EN pregunta["columna_derecha"] (con índice):
        MOSTRAR "  {letra}. {item}"
      MOSTRAR ""
      respuesta ← LEER entrada del usuario, pedir "Tu respuesta (ej: 1-A, 2-C, 3-B): "
    
    AGREGAR respuesta A respuestas_usuario
  
  RETORNAR respuestas_usuario

FIN presentar_preguntas
```

---

### Función: `mostrar_resultados(puntaje, resultados)`

```
FUNCIÓN mostrar_resultados(puntaje, resultados):

  MOSTRAR ""
  MOSTRAR "╔══════════════════════════════════╗"
  MOSTRAR "║         RESULTADOS DEL EXAMEN    ║"
  MOSTRAR "╚══════════════════════════════════╝"
  MOSTRAR ""

  // Detalle por pregunta
  PARA CADA resultado EN resultados (con índice i):
    
    SI resultado["correcto"] == verdadero:
      MOSTRAR "Pregunta {i+1}: ✅ CORRECTO  (+{resultado['puntaje_obtenido']} pts)"
    
    SI NO:
      MOSTRAR "Pregunta {i+1}: ❌ INCORRECTO  (+0 pts)"
      MOSTRAR "   Respuesta correcta: {resultado['respuesta_correcta']}"
      SI resultado["retroalimentacion"] no está vacío:
        MOSTRAR "   💡 {resultado['retroalimentacion']}"
    
    MOSTRAR ""
  
  // Resumen final
  MOSTRAR "────────────────────────────────────"
  MOSTRAR "PUNTAJE TOTAL:  {puntaje['total_obtenido']} / {puntaje['total_posible']} puntos"
  MOSTRAR "PORCENTAJE:     {puntaje['porcentaje']}%"
  MOSTRAR "CORRECTAS:      {puntaje['correctas']}"
  MOSTRAR "INCORRECTAS:    {puntaje['incorrectas']}"
  MOSTRAR "────────────────────────────────────"
  
  // Mensaje según desempeño
  SI puntaje["porcentaje"] >= 90:
    MOSTRAR "🏆 ¡Excelente! Obtuviste más del 90%."
  SI puntaje["porcentaje"] >= 70:
    MOSTRAR "👍 ¡Buen trabajo! Aprobaste el examen."
  SI puntaje["porcentaje"] >= 50:
    MOSTRAR "⚠️  Pasaste, pero puedes mejorar."
  SI NO:
    MOSTRAR "❌ No aprobaste. Revisa el material e intenta de nuevo."

FIN mostrar_resultados
```
