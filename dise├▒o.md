# 3. Diseño del Sistema

## 3.1 Visión General

El sistema se divide en **tres capas independientes** que se comunican de forma descendente. Esta separación permite modificar una capa sin afectar las demás, facilita las pruebas unitarias y hace el código más mantenible.

```
     ┌─────────────────────────────────────┐
     │            USUARIO                  │
     └──────────────────┬──────────────────┘
                        │  Ingresa respuestas / Ve resultados
                        ▼
     ┌─────────────────────────────────────┐
     │          CAPA 3: CLI                │
     │  (Interacción con el usuario)       │
     │                                     │
     │  mostrar_menu()                     │
     │  mostrar_instrucciones()            │
     │  presentar_preguntas()              │
     │  mostrar_resultados()               │
     └──────────────────┬──────────────────┘
                        │  Llama a funciones de corrección
                        ▼
     ┌─────────────────────────────────────┐
     │         CAPA 2: LÓGICA             │
     │  (Procesamiento y calificación)     │
     │                                     │
     │  corregir_examen()                  │
     │  normalizar_texto()                 │
     │  calcular_puntaje()                 │
     │  generar_retroalimentacion()        │
     └──────────────────┬──────────────────┘
                        │  Solicita datos del examen
                        ▼
     ┌─────────────────────────────────────┐
     │         CAPA 1: DATOS              │
     │  (Acceso a archivos)               │
     │                                     │
     │  cargar_examen()                    │
     │  validar_examen()                   │
     │  listar_examenes()                  │
     └──────────────────┬──────────────────┘
                        │  Lee archivos
                        ▼
     ┌─────────────────────────────────────┐
     │         ARCHIVOS JSON              │
     │  (Banco de preguntas)              │
     └─────────────────────────────────────┘
```

---

## 3.2 Capa 1: Datos

**Responsabilidad:** Leer y validar archivos JSON que contienen los exámenes.

### Funciones

#### `cargar_examen(ruta_archivo)`
- **Entrada:** Ruta relativa o absoluta al archivo `.json`
- **Proceso:** Abre el archivo, lo parsea como JSON, retorna la estructura
- **Salida:** Diccionario Python con los datos del examen
- **Errores que maneja:** Archivo no encontrado, JSON malformado

#### `validar_examen(datos)`
- **Entrada:** Diccionario con los datos del examen
- **Proceso:** Verifica que existan los campos obligatorios (`titulo`, `preguntas`, `tipo`, `respuesta_correcta`, `puntaje`)
- **Salida:** `True` si válido, lanza excepción si no
- **Errores que maneja:** Campos faltantes, tipos incorrectos

#### `listar_examenes(directorio)`
- **Entrada:** Ruta al directorio de exámenes
- **Proceso:** Busca todos los archivos `.json` en esa carpeta
- **Salida:** Lista de nombres de archivos disponibles

### Estructura de Datos (JSON)

```json
{
  "titulo": "Examen de Historia",
  "descripcion": "Preguntas sobre la Revolución Francesa",
  "preguntas": [
    {
      "id": 1,
      "tipo": "opcion_multiple",
      "enunciado": "¿En qué año comenzó la Revolución Francesa?",
      "opciones": {
        "A": "1776",
        "B": "1789",
        "C": "1804",
        "D": "1815"
      },
      "respuesta_correcta": "B",
      "puntaje": 20,
      "retroalimentacion": {
        "A": "1776 fue la independencia de EE.UU., no la Revolución Francesa.",
        "C": "1804 fue la coronación de Napoleón.",
        "D": "1815 fue la batalla de Waterloo."
      }
    },
    {
      "id": 2,
      "tipo": "verdadero_falso",
      "enunciado": "La Revolución Francesa comenzó con la toma de la Bastilla.",
      "respuesta_correcta": "verdadero",
      "puntaje": 10,
      "retroalimentacion": {
        "falso": "La toma de la Bastilla el 14 de julio de 1789 es considerada el inicio simbólico."
      }
    },
    {
      "id": 3,
      "tipo": "completar",
      "enunciado": "El lema de la Revolución Francesa era: Libertad, Igualdad y ___.",
      "respuesta_correcta": "fraternidad",
      "puntaje": 15,
      "retroalimentacion": {
        "default": "El tercer valor era 'Fraternidad', que significa hermandad entre ciudadanos."
      }
    },
    {
      "id": 4,
      "tipo": "emparejamiento",
      "enunciado": "Relaciona cada evento con su año:",
      "columna_izquierda": ["Toma de la Bastilla", "Ejecución de Luis XVI", "Declaración de los Derechos del Hombre"],
      "columna_derecha": ["1789", "1793", "1789"],
      "respuesta_correcta": {"1": "1789", "2": "1793", "3": "1789"},
      "puntaje": 15,
      "retroalimentacion": {
        "default": "Revisa la cronología de eventos de la Revolución Francesa."
      }
    }
  ]
}
```

---

## 3.3 Capa 2: Lógica

**Responsabilidad:** Comparar respuestas, calcular puntajes y generar retroalimentación.

### Funciones

#### `normalizar_texto(texto)`
- **Entrada:** Cadena de texto con la respuesta del usuario
- **Proceso:** Convierte a minúsculas, elimina espacios extras, elimina tildes opcionales
- **Salida:** Texto normalizado
- **Ejemplo:** `"  FraterNidad  "` → `"fraternidad"`

#### `corregir_pregunta(pregunta, respuesta_usuario)`
- **Entrada:** Diccionario de una pregunta + respuesta ingresada por el usuario
- **Proceso:** Normaliza ambas respuestas, las compara según el tipo de pregunta
- **Salida:** `{"correcto": True/False, "puntaje_obtenido": int, "retroalimentacion": str}`

#### `corregir_examen(preguntas, respuestas_usuario)`
- **Entrada:** Lista de preguntas + lista de respuestas del usuario
- **Proceso:** Llama a `corregir_pregunta()` para cada par, acumula resultados
- **Salida:** Lista de resultados por pregunta

#### `calcular_puntaje(resultados)`
- **Entrada:** Lista de resultados de `corregir_examen()`
- **Proceso:** Suma los puntajes obtenidos, calcula el porcentaje sobre el total posible
- **Salida:** Diccionario `{"total_obtenido": int, "total_posible": int, "porcentaje": float, "correctas": int, "incorrectas": int}`

#### `generar_retroalimentacion(pregunta, respuesta_usuario)`
- **Entrada:** Pregunta + respuesta del usuario
- **Proceso:** Busca en el campo `retroalimentacion` del JSON el mensaje para esa respuesta incorrecta
- **Salida:** Cadena de texto con la retroalimentación

---

## 3.4 Capa 3: CLI

**Responsabilidad:** Gestionar toda la interacción con el usuario a través de la terminal.

### Funciones

#### `mostrar_menu()`
- Muestra el menú principal con las opciones disponibles
- Opciones: (1) Seleccionar examen, (2) Ver instrucciones, (3) Salir

#### `mostrar_instrucciones()`
- Explica al usuario cómo responder cada tipo de pregunta

#### `seleccionar_examen(lista_examenes)`
- Muestra los exámenes disponibles y permite al usuario elegir uno

#### `presentar_preguntas(preguntas)`
- Itera sobre cada pregunta, la muestra con su formato correcto
- Según el tipo, muestra las opciones correspondientes
- Registra y retorna la respuesta del usuario

#### `mostrar_resultados(puntaje, resultados)`
- Muestra el resultado pregunta por pregunta
- Muestra el resumen final con porcentaje y cantidad de aciertos

---

## 3.5 Estructura de Carpetas del Código Fuente

```
src/
├── main.py                  ← Punto de entrada del programa
│
├── datos/
│   ├── __init__.py
│   ├── cargador.py          ← cargar_examen(), listar_examenes()
│   └── validador.py         ← validar_examen()
│
├── logica/
│   ├── __init__.py
│   ├── corrector.py         ← corregir_pregunta(), corregir_examen()
│   ├── normalizador.py      ← normalizar_texto()
│   └── puntaje.py           ← calcular_puntaje(), generar_retroalimentacion()
│
└── cli/
    ├── __init__.py
    ├── menu.py              ← mostrar_menu(), seleccionar_examen()
    ├── presentador.py       ← presentar_preguntas(), mostrar_instrucciones()
    └── resultados.py        ← mostrar_resultados()
```

---

## 3.6 Flujo de Ejecución

```
1. Usuario ejecuta: python src/main.py
2. Se muestran los exámenes disponibles (listar_examenes)
3. Usuario selecciona un examen
4. Se carga y valida el examen (cargar_examen + validar_examen)
5. Se muestran instrucciones (mostrar_instrucciones)
6. Para cada pregunta:
   a. Se presenta la pregunta al usuario (presentar_preguntas)
   b. Se registra la respuesta
7. Se corrigen todas las respuestas (corregir_examen)
8. Se calcula el puntaje (calcular_puntaje)
9. Se muestran los resultados detallados (mostrar_resultados)
10. Se regresa al menú principal
```
