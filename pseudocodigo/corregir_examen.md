# Pseudocódigo — Capa 2: Corrección del Examen

## Archivo: `src/logica/corrector.py`

---

### Función: `normalizar_texto(texto)`

```
FUNCIÓN normalizar_texto(texto):

  SI texto es nulo o vacío:
    RETORNAR ""
  
  texto ← CONVERTIR texto a minúsculas
  texto ← ELIMINAR espacios al inicio y al final
  texto ← REEMPLAZAR múltiples espacios internos por un solo espacio
  
  // Normalización de acentos (opcional pero recomendado)
  texto ← REEMPLAZAR "á" por "a"
  texto ← REEMPLAZAR "é" por "e"
  texto ← REEMPLAZAR "í" por "i"
  texto ← REEMPLAZAR "ó" por "o"
  texto ← REEMPLAZAR "ú" por "u"
  texto ← REEMPLAZAR "ü" por "u"
  
  RETORNAR texto

FIN normalizar_texto


EJEMPLO:
  normalizar_texto("  FraterNidad  ")  →  "fraternidad"
  normalizar_texto("VERDADERO")        →  "verdadero"
  normalizar_texto("  b  ")            →  "b"
```

---

### Función: `corregir_pregunta(pregunta, respuesta_usuario)`

```
FUNCIÓN corregir_pregunta(pregunta, respuesta_usuario):

  respuesta_norm ← LLAMAR normalizar_texto(respuesta_usuario)
  correcta_norm  ← LLAMAR normalizar_texto(pregunta["respuesta_correcta"])
  
  resultado ← {
    "id":                  pregunta["id"],
    "tipo":                pregunta["tipo"],
    "correcto":            falso,
    "puntaje_obtenido":    0,
    "respuesta_usuario":   respuesta_usuario,
    "respuesta_correcta":  pregunta["respuesta_correcta"],
    "retroalimentacion":   ""
  }
  
  SI pregunta["tipo"] == "opcion_multiple":
    SI respuesta_norm == correcta_norm:
      resultado["correcto"] ← verdadero
      resultado["puntaje_obtenido"] ← pregunta["puntaje"]
    SI NO:
      resultado["retroalimentacion"] ← BUSCAR en pregunta["retroalimentacion"][respuesta_norm]
      SI no existe entrada:
        resultado["retroalimentacion"] ← "Respuesta incorrecta."
  
  SI pregunta["tipo"] == "verdadero_falso":
    // Aceptar variantes: "v" = "verdadero", "f" = "falso"
    SI respuesta_norm == "v":
      respuesta_norm ← "verdadero"
    SI respuesta_norm == "f":
      respuesta_norm ← "falso"
    
    SI respuesta_norm == correcta_norm:
      resultado["correcto"] ← verdadero
      resultado["puntaje_obtenido"] ← pregunta["puntaje"]
    SI NO:
      resultado["retroalimentacion"] ← BUSCAR en pregunta["retroalimentacion"][respuesta_norm]
  
  SI pregunta["tipo"] == "completar":
    // También revisar respuestas alternativas si existen
    respuestas_validas ← [correcta_norm]
    
    SI pregunta contiene "respuestas_alternativas":
      PARA CADA alt EN pregunta["respuestas_alternativas"]:
        AGREGAR normalizar_texto(alt) A respuestas_validas
    
    SI respuesta_norm ESTÁ EN respuestas_validas:
      resultado["correcto"] ← verdadero
      resultado["puntaje_obtenido"] ← pregunta["puntaje"]
    SI NO:
      resultado["retroalimentacion"] ← pregunta["retroalimentacion"]["default"]
  
  SI pregunta["tipo"] == "emparejamiento":
    // respuesta_usuario esperada: "1-A, 2-C, 3-B"
    pares_usuario ← PARSEAR respuesta_norm en pares {numero: letra}
    pares_correctos ← pregunta["respuesta_correcta"]
    
    SI pares_usuario == pares_correctos:
      resultado["correcto"] ← verdadero
      resultado["puntaje_obtenido"] ← pregunta["puntaje"]
    SI NO:
      resultado["retroalimentacion"] ← pregunta["retroalimentacion"]["default"]
  
  RETORNAR resultado

FIN corregir_pregunta
```

---

### Función: `corregir_examen(preguntas, respuestas_usuario)`

```
FUNCIÓN corregir_examen(preguntas, respuestas_usuario):

  SI LONGITUD(preguntas) != LONGITUD(respuestas_usuario):
    LANZAR error: "El número de respuestas no coincide con el número de preguntas."
  
  resultados ← lista vacía []
  
  PARA CADA (pregunta, respuesta) EN ZIP(preguntas, respuestas_usuario):
    resultado ← LLAMAR corregir_pregunta(pregunta, respuesta)
    AGREGAR resultado A resultados
  
  RETORNAR resultados

FIN corregir_examen
```

---

### Función: `calcular_puntaje(resultados)`

```
FUNCIÓN calcular_puntaje(resultados):

  total_obtenido ← 0
  total_posible  ← 0
  correctas      ← 0
  incorrectas    ← 0
  
  PARA CADA resultado EN resultados:
    total_obtenido ← total_obtenido + resultado["puntaje_obtenido"]
    // Necesitamos el puntaje máximo de cada pregunta
    // (guardamos puntaje_maximo en el resultado al corregir)
    total_posible  ← total_posible + resultado["puntaje_maximo"]
    
    SI resultado["correcto"] == verdadero:
      correctas ← correctas + 1
    SI NO:
      incorrectas ← incorrectas + 1
  
  SI total_posible == 0:
    porcentaje ← 0
  SI NO:
    porcentaje ← REDONDEAR((total_obtenido / total_posible) * 100, 1)
  
  RETORNAR {
    "total_obtenido": total_obtenido,
    "total_posible":  total_posible,
    "porcentaje":     porcentaje,
    "correctas":      correctas,
    "incorrectas":    incorrectas
  }

FIN calcular_puntaje
```
