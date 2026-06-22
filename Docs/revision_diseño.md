# 4. Revisión del Diseño

## 4.1 Objetivo de la Revisión

Verificar que el diseño propuesto cumple con todos los requisitos funcionales y no funcionales del proyecto, y que la arquitectura por capas es coherente, escalable y libre de dependencias circulares.

---

## 4.2 Validación de Requisitos Funcionales

| # | Requisito | ¿Se cumple? | Capa responsable | Función(es) clave |
|---|-----------|:-----------:|------------------|-------------------|
| 1 | Cargar examen desde archivo JSON | ✅ Sí | Capa 1 (Datos) | `cargar_examen()` |
| 2 | Validar estructura del JSON | ✅ Sí | Capa 1 (Datos) | `validar_examen()` |
| 3 | Listar exámenes disponibles | ✅ Sí | Capa 1 (Datos) | `listar_examenes()` |
| 4 | Presentar preguntas al usuario | ✅ Sí | Capa 3 (CLI) | `presentar_preguntas()` |
| 5 | Soportar preguntas de opción múltiple | ✅ Sí | Capas 2 y 3 | `corregir_pregunta()` + `presentar_preguntas()` |
| 6 | Soportar preguntas verdadero/falso | ✅ Sí | Capas 2 y 3 | `corregir_pregunta()` + `presentar_preguntas()` |
| 7 | Soportar preguntas de completar espacios | ✅ Sí | Capas 2 y 3 | `normalizar_texto()` + `corregir_pregunta()` |
| 8 | Soportar preguntas de emparejamiento | ✅ Sí | Capas 2 y 3 | `corregir_pregunta()` + `presentar_preguntas()` |
| 9 | Registrar respuestas del usuario | ✅ Sí | Capa 3 (CLI) | `presentar_preguntas()` |
| 10 | Corregir respuestas automáticamente | ✅ Sí | Capa 2 (Lógica) | `corregir_examen()` |
| 11 | Normalizar texto (mayúsculas/espacios) | ✅ Sí | Capa 2 (Lógica) | `normalizar_texto()` |
| 12 | Calcular puntaje total | ✅ Sí | Capa 2 (Lógica) | `calcular_puntaje()` |
| 13 | Mostrar retroalimentación por error | ✅ Sí | Capas 2 y 3 | `generar_retroalimentacion()` + `mostrar_resultados()` |
| 14 | Mostrar resumen de resultados | ✅ Sí | Capa 3 (CLI) | `mostrar_resultados()` |
| 15 | Menú de navegación del sistema | ✅ Sí | Capa 3 (CLI) | `mostrar_menu()` |

---

## 4.3 Validación de la Arquitectura por Capas

| Principio | ¿Se cumple? | Observaciones |
|-----------|:-----------:|---------------|
| La Capa 3 (CLI) llama a la Capa 2 (Lógica) | ✅ Sí | CLI delega corrección a la capa de lógica |
| La Capa 2 (Lógica) llama a la Capa 1 (Datos) | ✅ Sí | Lógica recibe datos ya cargados por la Capa 1 |
| La Capa 1 (Datos) no conoce las capas superiores | ✅ Sí | Solo lee archivos y devuelve estructuras de datos |
| No existen dependencias circulares | ✅ Sí | El flujo es siempre descendente: CLI → Lógica → Datos |
| Cada capa tiene una sola responsabilidad | ✅ Sí | Datos: I/O; Lógica: procesamiento; CLI: presentación |

---

## 4.4 Validación del Formato de Datos

| Elemento | ¿Definido? | Dónde |
|----------|:----------:|-------|
| Estructura del archivo JSON | ✅ Sí | `docs/diseño.md` sección 3.2 |
| Tipos de pregunta soportados | ✅ Sí | `docs/entendimiento.md` sección 1.3 |
| Formato de respuesta correcta | ✅ Sí | `examenes/ejemplo.json` |
| Formato de retroalimentación | ✅ Sí | `examenes/ejemplo.json` |
| Asignación de puntaje por pregunta | ✅ Sí | Campo `puntaje` en cada pregunta JSON |

---

## 4.5 Problemas Identificados en el Diseño

| # | Problema | Gravedad | Solución Propuesta |
|---|----------|----------|--------------------|
| 1 | El tipo `emparejamiento` es más complejo de presentar en CLI | Media | Mostrar columnas numeradas y pedir asociación en formato `1-A, 2-B, 3-A` |
| 2 | Preguntas de `completar` pueden tener múltiples respuestas válidas | Baja | Definir un campo `respuestas_alternativas` en el JSON para variantes aceptadas |
| 3 | No se maneja el caso de un JSON vacío (sin preguntas) | Media | Agregar verificación en `validar_examen()` que el array de preguntas tenga al menos 1 elemento |
| 4 | No hay persistencia de resultados (se pierden al cerrar) | Baja | Extensión opcional: guardar resultados en archivo `.txt` o `.json` |

---

## 4.6 Comparación con los Requisitos del Profesor

| Requisito del Enunciado | Diseño Actual | Observaciones |
|-------------------------|---------------|---------------|
| Preguntas de opción múltiple | ✅ Incluido | Soporta A/B/C/D |
| Preguntas verdadero/falso | ✅ Incluido | Normaliza V/F/verdadero/falso |
| Preguntas de completar | ✅ Incluido | Con normalización de texto |
| Preguntas de emparejamiento | ✅ Incluido | Ver nota en sección 4.5 |
| Entrada: JSON con preguntas y puntaje | ✅ Incluido | Estructura definida en Capa 1 |
| Salida: puntaje total | ✅ Incluido | `calcular_puntaje()` |
| Salida: correctas/incorrectas por pregunta | ✅ Incluido | `corregir_examen()` |
| Retroalimentación predefinida | ✅ Incluido | Campo `retroalimentacion` en JSON |
| Arquitectura por capas | ✅ Incluido | 3 capas bien separadas |
| Mínimo 5 preguntas | ✅ Incluido | `ejemplo.json` tiene 5+ preguntas |
| CLI funcional (entregable Semana 8) | ✅ Planificado | Capa 3 completa en Semana 6 |
| LLM para generar preguntas | ⚠️ Opcional | Planificado como extensión en Semana 6 |

---

## 4.7 Conclusión de la Revisión

El diseño propuesto **cumple con todos los requisitos funcionales** establecidos por el profesor y la arquitectura por capas es sólida, sin dependencias circulares y con responsabilidades claramente definidas.

Los problemas identificados en la sección 4.5 son de baja a media gravedad y tienen soluciones concretas que pueden implementarse durante las semanas de desarrollo (Semanas 4–6).

El equipo está listo para comenzar la implementación en la Semana 4 con una base arquitectónica bien documentada.
