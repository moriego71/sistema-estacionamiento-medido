# Sistema Inteligente de Estacionamiento Medido Urbano

## Descripción General

Proyecto académico orientado al diseño de un sistema inteligente de estacionamiento medido urbano con arquitectura evolutiva y proyección hacia entornos Smart City.

La propuesta contempla una evolución progresiva desde un sistema digital de estacionamiento medido hacia un ecosistema inteligente basado en IoT, validación automática y asignación dinámica de espacios urbanos.

---

# Objetivo General

Diseñar un sistema de estacionamiento medido urbano capaz de evolucionar en tres etapas:

## Etapa 1 – Digitalización del Estacionamiento Medido

Incluye:

- registro de usuarios,
- gestión de vehículos,
- gestión de inspectores,
- gestión de sesiones de estacionamiento,
- gestión de saldo,
- validación de estacionamiento,
- gestión de infracciones,
- protocolo de acarreo.

## Etapa 2 – Integración IoT

Incluye futura incorporación de:

- sensores urbanos,
- validación automática,
- detección de ocupación,
- monitoreo inteligente.

## Etapa 3 – Asignación Dinámica Inteligente

Incluye futura evolución hacia:

- reservas inteligentes,
- asignación dinámica de espacios,
- optimización urbana,
- integración Smart City.

---

# Estado Actual del Proyecto

Actualmente el proyecto se encuentra en etapa de:

- relevamiento de requerimientos,
- modelado funcional,
- análisis de dominio,
- definición de reglas de negocio,
- modelado de estados,
- diagramas de actividad,
- consolidación conceptual.

La arquitectura técnica definitiva aún no ha sido definida.

---

# Requerimientos Funcionales

## RF-001 – Registro de Usuarios

Permite registrar nuevos usuarios en el sistema.

## RF-002 – Gestión de Vehículos

Permite administrar los vehículos asociados a cada usuario.

## RF-003 – Registro de Inspectores

Permite registrar inspectores habilitados para operar en el sistema.

## RF-004 – Gestión del Inspector

Permite consultar y administrar información operativa del inspector.

## RF-005 – Carga de Saldo

Permite acreditar saldo para el pago del estacionamiento.

## RF-006 – Consultas del Usuario

Permite consultar sesiones, saldo e infracciones.

## RF-007 – Inicio de Sesión de Estacionamiento

Permite iniciar una sesión activa de estacionamiento.

## RF-008 – Solicitud de Cierre de Sesión

Gestiona la solicitud de cierre e inicio del proceso de validación.

## RF-009 – Fin de Sesión

Gestiona la finalización válida de una sesión de estacionamiento.

## RF-010 – Protocolo de Acarreo

Gestiona administrativamente el proceso sancionatorio asociado al acarreo.

## RF-011 – Gestión de Cobros

Pendiente de definición.

---

# Reglas de Negocio

Actualmente se encuentran definidas las siguientes reglas:

- RN-001 – Escalamiento Sancionatorio
- RN-002 – Acarreo impide finalización directa
- RN-003 – Conservación de Estado Previo

---

# Casos de Uso

Actualmente se encuentran modelados:

- UC-008 – Solicitar Cierre de Sesión
- UC-009 – Finalizar Sesión
- UC-010 – Ejecutar Protocolo de Acarreo

---

# Diagramas

## Máquina de Estados

- FSM-Vehiculos

Estados modelados:

- Activo
- Infracción
- Penalización
- Inspección
- Finalizado
- Acarreo

## Diagramas de Actividad

- DG-008 – Flujo de Cierre de Sesión
- DG-009 – Finalizar Sesión
- DG-010 – Protocolo de Acarreo

---

# Modelos de Dominio

## DA-001 – Modelo de Cobro de Estacionamiento

Define el comportamiento conceptual del cobro por intervalos.

## DA-002 – Supuestos Operativos y Simplificaciones del Dominio

Documenta:

- supuestos operativos,
- simplificaciones deliberadas,
- restricciones de alcance,
- evolución futura prevista.

---

# Arquitectura Conceptual

Actualmente el proyecto adopta una orientación modular por capas.

Módulos identificados:

- Gestión de Sesiones
- Gestión de Vehículos
- Gestión de Cobros
- Gestión de Infracciones
- Protocolo de Acarreo
- App Usuario
- App Inspector

La arquitectura técnica definitiva será definida una vez consolidado el modelo de dominio.

---

# Estructura del Repositorio

```text
sistema-estacionamiento-medido/
│
├── docs/
│   ├── RF/
│   ├── RN/
│   ├── UC/
│   ├── diagramas/
│   └── Modelos de Dominio/
│
├── README.md
│
└── .gitignore
```

---

# Próximos Pasos

## Pendientes inmediatos

- RF-011 – Gestión de Cobros
- UC-011 – Gestión de Cobros
- DG-011 – Gestión de Cobros

## Evolución futura

- integración IoT,
- validación automática,
- sensores urbanos,
- arquitectura distribuida,
- asignación dinámica inteligente,
- optimización urbana.

---

# Estado Académico

El proyecto se encuentra en fase de consolidación conceptual y modelado del dominio, constituyendo la base para futuras etapas de investigación vinculadas a IoT, Smart Cities y optimización urbana.
