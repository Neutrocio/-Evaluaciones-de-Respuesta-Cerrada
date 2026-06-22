# Pseudocódigo — Capa 1: Datos

## Archivo: `src/datos/cargador.py`

---

### Función: `listar_examenes(directorio)`

```
FUNCIÓN listar_examenes(directorio):
  
  SI directorio no existe:
    RETORNAR lista vacía []
  
  archivos_json ← BUSCAR todos los archivos "*.json" en directorio
  
  SI archivos_json está vacío:
    RETORNAR lista vacía []
  
  RETORNAR archivos_json

FIN listar_examenes
```

---

### Función: `cargar_examen(ruta_archivo)`

```
FUNCIÓN cargar_examen(ruta_archivo):

  SI archivo no existe en ruta_archivo:
    LANZAR error: "Archivo no encontrado: {ruta_archivo}"
  
  INTENTAR:
    contenido ← ABRIR archivo en ruta_archivo
    datos ← PARSEAR contenido como JSON
    CERRAR archivo
  
  SI error de JSON (formato inválido):
    LANZAR error: "El archivo no tiene formato JSON válido."
  
  SI error de lectura (permisos, etc.):
    LANZAR error: "No se pudo leer el archivo."
  
  // Validar antes de retornar
  LLAMAR validar_examen(datos)
  
  RETORNAR datos

FIN cargar_examen
```

---

### Función: `validar_examen(datos)`

```
FUNCIÓN validar_examen(datos):

  // Verificar campos obligatorios del examen
  SI datos no contiene campo "titulo":
    LANZAR error: "El examen debe tener un campo 'titulo'."
  
  SI datos no contiene campo "preguntas":
    LANZAR error: "El examen debe tener un campo 'preguntas'."
  
  SI datos["preguntas"] está vacío:
    LANZAR error: "El examen debe tener al menos una pregunta."
  
  // Validar cada pregunta
  PARA CADA pregunta EN datos["preguntas"]:
    
    SI pregunta no contiene "id":
      LANZAR error: "Pregunta sin 'id'."
    
    SI pregunta no contiene "tipo":
      LANZAR error: "Pregunta {id} sin 'tipo'."
    
    SI pregunta["tipo"] no está en ["opcion_multiple", "verdadero_falso", "completar", "emparejamiento"]:
      LANZAR error: "Tipo de pregunta desconocido: {tipo}."
    
    SI pregunta no contiene "enunciado":
      LANZAR error: "Pregunta {id} sin 'enunciado'."
    
    SI pregunta no contiene "respuesta_correcta":
      LANZAR error: "Pregunta {id} sin 'respuesta_correcta'."
    
    SI pregunta no contiene "puntaje":
      LANZAR error: "Pregunta {id} sin 'puntaje'."
    
    // Validaciones específicas por tipo
    SI pregunta["tipo"] == "opcion_multiple":
      SI pregunta no contiene "opciones":
        LANZAR error: "Pregunta {id} de opción múltiple sin 'opciones'."
  
  RETORNAR verdadero

FIN validar_examen
```
