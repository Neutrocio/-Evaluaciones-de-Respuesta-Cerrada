# Diagrama de Arquitectura — Sistema de Evaluación CLI

## Diagrama Principal por Capas

```
╔══════════════════════════════════════════════════════════════════╗
║                         USUARIO                                  ║
║         Interactúa con el sistema desde la terminal              ║
╚══════════════════════════════╦═══════════════════════════════════╝
                               │
                    (ingresa respuestas,
                     lee preguntas y resultados)
                               │
╔══════════════════════════════▼═══════════════════════════════════╗
║                    CAPA 3: CLI                                   ║
║                                                                  ║
║   ┌──────────────┐  ┌─────────────────┐  ┌──────────────────┐   ║
║   │mostrar_menu()│  │presentar_       │  │mostrar_          │   ║
║   │              │  │preguntas()      │  │resultados()      │   ║
║   └──────────────┘  └─────────────────┘  └──────────────────┘   ║
║                                                                  ║
║   ┌──────────────────────┐  ┌─────────────────────────────────┐  ║
║   │mostrar_instrucciones()│  │seleccionar_examen()             │  ║
║   └──────────────────────┘  └─────────────────────────────────┘  ║
╚══════════════════════════════╦═══════════════════════════════════╝
                               │
                    (solicita corrección y puntaje)
                               │
╔══════════════════════════════▼═══════════════════════════════════╗
║                    CAPA 2: LÓGICA                                ║
║                                                                  ║
║   ┌─────────────────┐  ┌──────────────────┐  ┌───────────────┐  ║
║   │normalizar_      │  │corregir_         │  │calcular_      │  ║
║   │texto()          │  │examen()          │  │puntaje()      │  ║
║   └─────────────────┘  └──────────────────┘  └───────────────┘  ║
║                                                                  ║
║   ┌────────────────────────────────┐                             ║
║   │generar_retroalimentacion()     │                             ║
║   └────────────────────────────────┘                             ║
╚══════════════════════════════╦═══════════════════════════════════╝
                               │
                    (solicita datos del examen)
                               │
╔══════════════════════════════▼═══════════════════════════════════╗
║                    CAPA 1: DATOS                                 ║
║                                                                  ║
║   ┌─────────────────┐  ┌──────────────────┐  ┌───────────────┐  ║
║   │cargar_examen()  │  │validar_examen()  │  │listar_        │  ║
║   │                 │  │                  │  │examenes()     │  ║
║   └─────────────────┘  └──────────────────┘  └───────────────┘  ║
╚══════════════════════════════╦═══════════════════════════════════╝
                               │
                         (lee archivos)
                               │
╔══════════════════════════════▼═══════════════════════════════════╗
║                    ARCHIVOS JSON                                 ║
║                                                                  ║
║    examenes/                                                     ║
║    ├── historia.json                                             ║
║    ├── matematicas.json                                          ║
║    └── ejemplo.json                                              ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Diagrama de Flujo de Ejecución

```
  INICIO
    │
    ▼
 Ejecutar main.py
    │
    ▼
 listar_examenes()
 ┌──────────────────────────────────┐
 │  Muestra: [1] historia.json     │
 │           [2] matematicas.json  │
 └──────────────────────────────────┘
    │
    ▼
 Usuario selecciona un examen
    │
    ▼
 cargar_examen() → validar_examen()
    │                     │
    │              ┌──────┴───────┐
    │              │  ¿Válido?    │
    │              │  NO → Error  │
    │              └──────┬───────┘
    │                     │ SÍ
    ▼                     ▼
 mostrar_instrucciones()
    │
    ▼
 Para cada pregunta:
 ┌────────────────────────────────────────┐
 │  presentar_preguntas()                 │
 │  └── Muestra enunciado + opciones      │
 │                                        │
 │  Usuario ingresa respuesta             │
 │                                        │
 │  normalizar_texto(respuesta_usuario)   │
 │  corregir_pregunta(pregunta, respuesta)│
 └────────────────────────────────────────┘
    │
    ▼
 calcular_puntaje(resultados)
    │
    ▼
 mostrar_resultados()
 ┌─────────────────────────────────────────┐
 │  Pregunta 1: Correcto — 20 puntos    │
 │  Pregunta 2: Incorrecto — 0 puntos   │
 │     → Retroalimentación: "..."          │
 │  ...                                    │
 │  PUNTAJE TOTAL: 65/100 (65%)            │
 └─────────────────────────────────────────┘
    │
    ▼
 mostrar_menu()
 ¿Continuar o salir?
    │
    ▼
  FIN
```

---

## Diagrama de Dependencias entre Módulos

```
main.py
  │
  ├──▶ cli/menu.py
  │      └──▶ datos/cargador.py
  │                └──▶ [archivos JSON]
  │
  ├──▶ cli/presentador.py
  │
  └──▶ cli/resultados.py
         └──▶ logica/corrector.py
                ├──▶ logica/normalizador.py
                └──▶ logica/puntaje.py
```

> **Regla:** Las flechas van siempre de capas superiores a inferiores.  
> Nunca una capa inferior importa de una capa superior.
