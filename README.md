# 📚 Sistema de Evaluación CLI

> Proyecto académico — Evaluaciones de Respuesta Cerrada  
> Grupos 1 y 2 | Entrega Semana 2

---

## 🧭 Descripción General

Sistema de evaluación automatizada por línea de comandos (CLI) que permite cargar exámenes desde archivos JSON, presentar preguntas al estudiante, registrar sus respuestas, calificarlas automáticamente y mostrar retroalimentación inmediata.

---

## 🗂️ Estructura del Repositorio

```
sistema-evaluacion-cli/
│
├── README.md                        ← Este archivo
│
├── docs/
│   ├── entendimiento.md             ← Análisis del problema
│   ├── planificacion.md             ← Roles, tareas y cronograma
│   ├── diseño.md                    ← Arquitectura por capas
│   └── revision_diseño.md          ← Validación del diseño
│
├── diagramas/
│   └── arquitectura.md              ← Diagrama de arquitectura (texto)
│
├── pseudocodigo/
│   ├── sistema_principal.md         ← Flujo general del sistema
│   ├── cargar_examen.md             ← Capa 1: Datos
│   ├── presentar_preguntas.md       ← Capa 3: CLI
│   └── corregir_examen.md          ← Capa 2: Lógica
│
├── src/
│   └── (implementación — Semanas 4-8)
│
└── examenes/
    └── ejemplo.json                 ← Banco de preguntas de ejemplo
```

---

## 🏗️ Arquitectura por Capas

```
     Usuario
        │
        ▼
┌───────────────┐
│   Capa 3      │  CLI — Interacción con el usuario
│   (cli/)      │  menú, presentación, resultados
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   Capa 2      │  Lógica — Corrección y puntaje
│   (logica/)   │  comparación, normalización, feedback
└───────┬───────┘
        │
        ▼
┌───────────────┐
│   Capa 1      │  Datos — Carga de archivos
│   (datos/)    │  leer JSON, validar estructura
└───────┬───────┘
        │
        ▼
   Archivos JSON
```

---

## 📋 Tipos de Preguntas Soportados

| Tipo | Descripción |
|------|-------------|
| Opción múltiple (una respuesta) | El usuario selecciona una opción correcta |
| Verdadero / Falso | El usuario indica V o F |
| Completar espacios | El usuario escribe la palabra que falta |
| Emparejamiento | El usuario asocia columnas o conceptos |

---

## 📅 Cronograma de Entregas

| Semana | Hito | Estado |
|--------|------|--------|
| Semana 2 | Diseño de arquitectura + repositorio | ✅ En progreso |
| Semana 4 | Prototipo Capa 1 y Capa 2 | ⏳ Pendiente |
| Semana 6 | Integración LLM + Capa 3 básica | ⏳ Pendiente |
| Semana 8 | Proyecto final completo | ⏳ Pendiente |

---

## 🔧 Tecnologías Previstas

- **Lenguaje:** Python 3
- **Entrada de datos:** Archivos JSON
- **Interfaz:** CLI (línea de comandos)
- **LLM (opcional):** API para generación de preguntas similares

---

## 📄 Documentación

Toda la documentación técnica se encuentra en la carpeta [`/docs`](./docs/).
