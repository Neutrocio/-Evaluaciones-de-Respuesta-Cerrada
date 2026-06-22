# 2. Planificación del Proyecto

## 2.1 Objetivo

Desarrollar un sistema CLI de evaluación automatizada en Python, dividido en tres capas, que cargue exámenes desde JSON, presente preguntas, corrija respuestas y muestre retroalimentación. Entrega final: Semana 8.

---

## 2.2 Equipo y Roles

> ⚠️ **Nota:** Ajustar nombres según los integrantes reales del grupo.

| Integrante | Rol Principal | Responsabilidades |
|------------|---------------|-------------------|
| **Integrante 1** | Ingeniero de Datos | Diseño de la estructura JSON. Implementación de `cargar_examen()` y `validar_examen()` (Capa 1). |
| **Integrante 2** | Desarrollador de Lógica | Implementación de `corregir_examen()`, `normalizar_texto()` y `calcular_puntaje()` (Capa 2). |
| **Integrante 3** | Desarrollador CLI | Implementación del menú, presentación de preguntas y visualización de resultados (Capa 3). |
| **Integrante 4** | QA + Documentación | Pruebas, creación del README, mantenimiento del repositorio GitHub y video demostración. |

---

## 2.3 Cronograma Detallado

### Semana 2 — Diseño de Arquitectura ✅

| Tarea | Responsable | Entregable |
|-------|-------------|------------|
| Definir estructura del proyecto en GitHub | Todos | Repositorio con carpetas base |
| Redactar entendimiento del problema | Integrante 1 | `docs/entendimiento.md` |
| Redactar planificación | Integrante 4 | `docs/planificacion.md` |
| Diseñar arquitectura por capas | Integrantes 2 y 3 | `docs/diseño.md` |
| Crear diagrama de arquitectura | Integrante 3 | `diagramas/arquitectura.md` |
| Escribir pseudocódigo base | Todos | Carpeta `pseudocodigo/` |
| Definir estructura del JSON de examen | Integrante 1 | `examenes/ejemplo.json` |
| Revisión del diseño | Todos | `docs/revision_diseño.md` |

---

### Semana 4 — Prototipo Capas 1 y 2 ⏳

| Tarea | Responsable | Entregable |
|-------|-------------|------------|
| Implementar `cargar_examen()` | Integrante 1 | `src/datos/cargador.py` |
| Implementar `validar_examen()` | Integrante 1 | `src/datos/validador.py` |
| Implementar `normalizar_texto()` | Integrante 2 | `src/logica/normalizador.py` |
| Implementar `corregir_examen()` | Integrante 2 | `src/logica/corrector.py` |
| Implementar `calcular_puntaje()` | Integrante 2 | `src/logica/puntaje.py` |
| Pruebas unitarias de Capas 1 y 2 | Integrante 4 | `tests/test_datos.py`, `test_logica.py` |

---

### Semana 6 — Capa 3 + Integración LLM (opcional) ⏳

| Tarea | Responsable | Entregable |
|-------|-------------|------------|
| Implementar `mostrar_menu()` | Integrante 3 | `src/cli/menu.py` |
| Implementar `presentar_preguntas()` | Integrante 3 | `src/cli/presentador.py` |
| Implementar `mostrar_resultados()` | Integrante 3 | `src/cli/resultados.py` |
| Integrar las tres capas | Todos | `src/main.py` |
| Integración LLM (si aplica) | Integrante 2 | `src/llm/generador.py` |
| Demo funcional del flujo principal | Integrante 4 | CLI ejecutable |

---

### Semana 8 — Proyecto Final ⏳

| Tarea | Responsable | Entregable |
|-------|-------------|------------|
| Pruebas de integración completas | Integrante 4 | Reporte de pruebas |
| Corrección de errores finales | Todos | Código limpio en `main` |
| Actualizar README con instrucciones de ejecución | Integrante 4 | `README.md` final |
| Grabación del video demostración (máx. 5 min) | Todos | Video subido |
| Informe de lecciones aprendidas | Todos | `docs/lecciones.md` |

---

## 2.4 Diagrama de Gantt Simplificado

```
Tarea                            S2   S3   S4   S5   S6   S7   S8
─────────────────────────────────────────────────────────────────
Diseño y documentación           ████
Estructura JSON y Capa 1              ████████
Lógica y Capa 2                       ████████
CLI y Capa 3                                    ████████
Integración completa                                    ████
Pruebas y correcciones                                  ████
Video + entrega final                                        ████
```

---

## 2.5 Herramientas y Tecnologías

| Categoría | Herramienta |
|-----------|-------------|
| Lenguaje de programación | Python 3.10+ |
| Control de versiones | Git + GitHub |
| Formato de datos | JSON |
| Interfaz | CLI (módulo `argparse` o interactivo) |
| LLM (opcional) | API de Anthropic / OpenAI |
| Comunicación del equipo | WhatsApp / Discord |

---

## 2.6 Riesgos Identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Uno o más integrantes no cumple sus tareas | Media | Alto | Repartir tareas en pares cuando sea posible |
| Dificultad con el formato JSON | Baja | Medio | Usar el `ejemplo.json` como plantilla desde el inicio |
| Integración entre capas falla | Media | Alto | Definir interfaces claras entre capas desde la Semana 2 |
| LLM no funciona a tiempo | Media | Bajo | El LLM es opcional; el núcleo no depende de él |
