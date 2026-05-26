# Sistema Inteligente de Estacionamiento Medido Urbano

## Descripción General

Proyecto académico orientado al diseño de un sistema inteligente de estacionamiento medido urbano con arquitectura evolutiva y proyección hacia entornos Smart City.

El objetivo principal es construir una base conceptual sólida que permita evolucionar progresivamente desde un sistema tradicional digitalizado hacia un ecosistema inteligente basado en:

- IoT urbano,
- validación automática,
- sensado en tiempo real,
- asignación dinámica de espacios,
- optimización urbana.

---

# Autor

Diego Moreno

---

# Objetivo General

Diseñar un sistema de estacionamiento medido urbano dividido en tres etapas evolutivas:

## Etapa 1 – Digitalización del estacionamiento medido

Incluye:

- gestión de sesiones,
- validación manual,
- control sancionatorio,
- gestión administrativa,
- trazabilidad de estados,
- protocolo de acarreo.

---

## Etapa 2 – Integración IoT

Incluye futura incorporación de:

- sensores urbanos,
- validación automática,
- detección de ocupación,
- monitoreo inteligente.

---

## Etapa 3 – Asignación Dinámica Inteligente

Incluye futura evolución hacia:

- reservas inteligentes,
- asignación dinámica,
- recomendación de espacios,
- optimización urbana,
- integración Smart City.

---

# Estado Actual del Proyecto

Actualmente el proyecto se encuentra en etapa de:

- relevamiento de requerimientos,
- modelado funcional,
- análisis de dominio,
- definición de reglas de negocio,
- diagramas de actividad,
- modelado de estados,
- consolidación conceptual.

La arquitectura técnica definitiva aún no fue definida.

---

# Componentes Modelados

## Máquina de Estados

FSM principal de vehículos con estados:

- Activo
- Infracción
- Penalización
- Inspección
- Finalizado
- Acarreo

---

## Requerimientos Funcionales

### RF-008 – Solicitud de Cierre de Sesión

Gestión de:
- solicitud de cierre,
- inspección,
- validación,
- escalamiento sancionatorio.

---

### RF-009 – Fin de Sesión

Gestión de:
- cálculo último intervalo,
- validación de estado,
- finalización administrativa.

---

### RF-010 – Protocolo de Acarreo

Gestión de:
- intervención sancionatoria,
- generación de infracciones,
- cálculo económico,
- cierre administrativo de sesión.

---

# Casos de Uso

- UC-008 – Solicitar Cierre de Sesión
- UC-009 – Finalizar Sesión
- UC-010 – Ejecutar Protocolo de Acarreo

---

# Diagramas

## Diagramas realizados

- FSM-Vehiculos.drawio
- DG-008 – Flujo de Cierre de Sesión
- DG-009 – Finalizar Sesión
- DG-010 – Flujo de Protocolo de Acarreo

---

# Modelos de Dominio

## DA-001 – Modelo de Cobro de Estacionamiento

Define:
- cobro por intervalos,
- cálculo proporcional,
- comportamiento financiero base.

---

## DA-002 – Supuestos Operativos y Simplificaciones del Dominio

Define:
- simplificaciones deliberadas,
- restricciones de alcance,
- supuestos operativos,
- lineamientos evolutivos.

---

# Arquitectura Conceptual

Actualmente el proyecto mantiene una orientación modular por capas.

## Módulos identificados

- Gestión de Sesiones
- Gestión de Vehículos
- Gestión de Cobros
- Gestión de Infracciones
- Protocolo de Acarreo
- App Usuario
- App Inspector

---

# Consideraciones de Alcance

La Etapa 1 prioriza:

- estabilidad conceptual,
- consolidación del dominio,
- comportamiento sancionatorio,
- trazabilidad de estados.

No se modela aún:

- arquitectura técnica definitiva,
- microservicios,
- despliegue,
- sensores IoT,
- reconocimiento automático,
- asignación dinámica.

---

# Estructura del Proyecto

```text
Sistema-Estacionamiento/
│
├── docs/
│   ├── RF/
│   ├── RN/
│   ├── UC/
│   ├── DG/
│   ├── DA/
│   └── Modelos de Dominio/
│
├── diagramas/
│   ├── source/
│   └── exports/
│
└── README.md
```

---

# Herramientas Utilizadas

- VSCode
- Markdown
- Draw.io
- Git
- GitHub
- Notion

---

# Próximos Pasos

## Pendientes inmediatos

- RF-011 – Gestión de Cobros
- UC-011 – Gestión de Cobros
- DG-011 – Flujo de Gestión de Cobros

---

## Evolución futura

- integración IoT,
- sensores urbanos,
- validación automática,
- arquitectura distribuida,
- asignación dinámica inteligente.

---

# Estado Académico

El proyecto prioriza inicialmente la construcción de una base conceptual y funcional sólida que permita evolucionar posteriormente hacia arquitecturas inteligentes orientadas a Smart Cities.