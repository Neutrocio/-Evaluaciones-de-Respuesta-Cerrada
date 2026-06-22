# 1. Entendimiento del Problema

## 1.1 Contexto

En el ámbito educativo, la corrección manual de exámenes de respuesta cerrada es una tarea repetitiva que consume tiempo y puede introducir errores humanos. Este proyecto propone automatizar dicho proceso mediante un sistema de software que permita a los estudiantes responder exámenes desde la terminal y recibir retroalimentación inmediata.

---

## 1.2 Descripción del Sistema

Se desarrollará un **sistema de evaluación automatizada por línea de comandos (CLI)** que permita:

1. Cargar exámenes desde archivos JSON con preguntas, opciones, respuestas correctas y puntajes.
2. Presentar las preguntas al usuario de forma secuencial.
3. Registrar las respuestas ingresadas.
4. Calificar automáticamente cada respuesta.
5. Calcular el puntaje total obtenido.
6. Mostrar retroalimentación por cada pregunta correcta e incorrecta.

---

## 1.3 Tipos de Preguntas

El sistema manejará cuatro tipos de preguntas de respuesta cerrada:

| # | Tipo | Descripción |
|---|------|-------------|
| 1 | **Opción múltiple** | Se presentan 4 opciones (A, B, C, D); el usuario selecciona una. |
| 2 | **Verdadero / Falso** | El usuario indica si un enunciado es verdadero o falso. |
| 3 | **Completar espacios** | Se muestra una oración incompleta; el usuario escribe la palabra o frase faltante. |
| 4 | **Emparejamiento** | Se presentan dos columnas; el usuario asocia cada elemento de la izquierda con uno de la derecha. |

---

## 1.4 Entradas del Sistema

```
Entrada 1: Archivo JSON
  └── Preguntas
  └── Opciones de respuesta (cuando aplica)
  └── Respuesta correcta
  └── Puntaje asignado por pregunta
  └── Retroalimentación para cada opción incorrecta

Entrada 2: Interacción del usuario
  └── Selección de examen desde el menú
  └── Respuestas ingresadas para cada pregunta
```

---

## 1.5 Salidas del Sistema

```
Salida 1: Resultado por pregunta
  └── Indicación de correcto / incorrecto
  └── Respuesta correcta (si el usuario falló)
  └── Retroalimentación predefinida

Salida 2: Resumen final
  └── Puntaje total obtenido
  └── Número de respuestas correctas
  └── Número de respuestas incorrectas
  └── Porcentaje de acierto
```

---

## 1.6 Restricciones y Supuestos

| Restricción / Supuesto | Detalle |
|------------------------|---------|
| **Entorno de ejecución** | El sistema corre en terminal (no requiere interfaz gráfica). |
| **Formato de datos** | Los exámenes se almacenan en archivos `.json` con una estructura definida. |
| **Comparación de texto** | Las respuestas se normalizan (sin distinción de mayúsculas/minúsculas, sin espacios extra) antes de comparar. |
| **Mínimo viable** | Al menos 5 preguntas por examen para la entrega de la Semana 8. |
| **LLM opcional** | La integración con modelo de lenguaje para generar preguntas es una extensión, no un requisito obligatorio. |

---

## 1.7 Alcance del Proyecto

### Incluido (obligatorio)
- Carga de exámenes desde JSON.
- Presentación de preguntas tipo opción múltiple, V/F, completar y emparejamiento.
- Corrección automática con normalización de texto.
- Cálculo de puntaje.
- Retroalimentación predefinida.
- Interfaz CLI funcional.

### Posible extensión (opcional)
- Generación automática de nuevas preguntas similares usando un LLM.
- Soporte para preguntas con múltiples respuestas correctas.
- Generación aleatoria de exámenes desde un banco de preguntas.
- Exportación de resultados a archivo.

---

## 1.8 Diagrama de Contexto

```
                     ┌─────────────────────────┐
                     │   SISTEMA DE EVALUACIÓN  │
                     │         CLI              │
  ┌──────────┐       │                         │       ┌──────────────┐
  │ Archivo  │──────▶│  Carga y valida         │──────▶│  Resultados  │
  │  JSON    │       │  preguntas              │       │  en pantalla │
  └──────────┘       │                         │       └──────────────┘
                     │                         │
  ┌──────────┐       │  Presenta preguntas     │
  │ Usuario  │◀─────▶│  y registra respuestas  │
  └──────────┘       │                         │
                     └─────────────────────────┘
```
