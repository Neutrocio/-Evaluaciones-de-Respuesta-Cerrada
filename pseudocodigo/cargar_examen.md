# Pseudocódigo — Capa 1: Datos

## Archivo: `src/datos/cargador.py`

---

### Función: `listar_examenes(directorio)`

```
FUNCIÓN listar_examenes(directorio):

  SI directorio no existe O no es accesible:
    RETORNAR lista vacía []

  archivos_json ← BUSCAR todos los archivos "*.json" en directorio
  examenes ← []

  PARA CADA archivo EN archivos_json:
    TRY:
      contenido ← PARSEAR_JSON(archivo)
      SI contenido es válido:
        AGREGAR contenido A examenes
    CATCH error:
      REGISTRAR advertencia("Archivo inválido: " + archivo)
      CONTINUAR

  RETORNAR examenes

FIN listar_examenes
```

---

### Función: `cargar_examen(ruta_archivo)`

```
/*
 * Carga y valida un examen desde un archivo JSON.
 * Lanza: ArchivoNoEncontrado, JSONInválido, ErrorLectura, ErrorValidación
 */
FUNCIÓN cargar_examen(ruta_archivo):

  SI archivo no existe en ruta_archivo:
    LANZAR ArchivoNoEncontrado: "Archivo no encontrado: {ruta_archivo}"

  INTENTAR:
    contenido ← ABRIR archivo en ruta_archivo
    datos    ← PARSEAR contenido como JSON

  ATRAPAR error de JSON:
    LANZAR JSONInválido: "JSON inválido en {ruta_archivo}: {error.detalle}"

  ATRAPAR error de lectura:
    LANZAR ErrorLectura: "No se pudo leer {ruta_archivo}: {error.detalle}"

  FINALMENTE:
    SI archivo está abierto: CERRAR archivo

  LLAMAR validar_examen(datos)  // propaga ErrorValidación si falla

  RETORNAR datos

FIN cargar_examen
```

---

### Función: `validar_examen(datos)`

```
FUNCIÓN validar_examen(datos):
  errores ← []

  // ── Campos raíz ──────────────────────────────────────────
  SI datos no contiene "titulo" O datos["titulo"] no es texto:
    AGREGAR "El examen debe tener un 'titulo' de tipo texto." A errores

  SI datos no contiene "preguntas" O datos["preguntas"] no es lista:
    AGREGAR "El examen debe tener un campo 'preguntas' de tipo lista." A errores
    // Sin preguntas no tiene sentido continuar
    LANZAR ErrorValidacion(errores)

  SI datos["preguntas"] está vacío:
    AGREGAR "El examen debe tener al menos una pregunta." A errores
    LANZAR ErrorValidacion(errores)

  // ── Validar preguntas ────────────────────────────────────
  ids_vistos ← conjunto vacío

  PARA CADA (índice, pregunta) EN ENUMERAR(datos["preguntas"]):
    prefijo ← "Pregunta #{índice + 1}"

    // Identificador
    SI pregunta no contiene "id":
      AGREGAR "{prefijo}: falta campo 'id'." A errores
      id ← "desconocido"
    SINO:
      id ← pregunta["id"]
      prefijo ← "Pregunta '{id}'"
      SI id EN ids_vistos:
        AGREGAR "{prefijo}: 'id' duplicado." A errores
      AGREGAR id A ids_vistos

    // Campos obligatorios comunes
    PARA CADA campo EN ["tipo", "enunciado", "respuesta_correcta", "puntaje"]:
      SI pregunta no contiene campo:
        AGREGAR "{prefijo}: falta campo '{campo}'." A errores

    // Tipo válido
    tipos_validos ← ["opcion_multiple", "verdadero_falso", "completar", "emparejamiento"]
    SI "tipo" EN pregunta Y pregunta["tipo"] no está en tipos_validos:
      AGREGAR "{prefijo}: tipo '{pregunta['tipo']}' no reconocido." A errores

    // Puntaje numérico y positivo
    SI "puntaje" EN pregunta:
      SI pregunta["puntaje"] no es número O pregunta["puntaje"] <= 0:
        AGREGAR "{prefijo}: 'puntaje' debe ser un número mayor que 0." A errores

    // Validaciones específicas por tipo
    SI "tipo" EN pregunta:
      SEGÚN pregunta["tipo"]:

        CASO "opcion_multiple":
          SI pregunta no contiene "opciones" O pregunta["opciones"] no es lista:
            AGREGAR "{prefijo}: debe tener 'opciones' de tipo lista." A errores
          SINO SI pregunta["opciones"] tiene menos de 2 elementos:
            AGREGAR "{prefijo}: debe tener al menos 2 opciones." A errores
          SINO SI "respuesta_correcta" EN pregunta:
            SI pregunta["respuesta_correcta"] no está en pregunta["opciones"]:
              AGREGAR "{prefijo}: 'respuesta_correcta' no coincide con ninguna opción." A errores

        CASO "verdadero_falso":
          SI "respuesta_correcta" EN pregunta:
            SI pregunta["respuesta_correcta"] no está en [verdadero, falso, "V", "F"]:
              AGREGAR "{prefijo}: 'respuesta_correcta' debe ser verdadero/falso." A errores

        CASO "emparejamiento":
          SI pregunta no contiene "pares" O pregunta["pares"] no es lista:
            AGREGAR "{prefijo}: debe tener 'pares' de tipo lista." A errores
          SINO SI pregunta["pares"] tiene menos de 2 elementos:
            AGREGAR "{prefijo}: debe tener al menos 2 pares." A errores

        CASO "completar":
          SI "enunciado" EN pregunta:
            SI pregunta["enunciado"] no contiene "___":
              AGREGAR "{prefijo}: enunciado de 'completar' debe incluir '___'." A errores

  // ── Resultado ────────────────────────────────────────────
  SI errores no está vacío:
    LANZAR ErrorValidacion(errores)   // lanza la lista completa

  RETORNAR verdadero

FIN validar_examen
```
