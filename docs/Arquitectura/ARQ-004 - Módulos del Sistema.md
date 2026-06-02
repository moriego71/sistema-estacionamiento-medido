# ARQ-004 – Módulos del Sistema

## Objetivo

Definir los módulos funcionales que componen el Sistema Inteligente de Estacionamiento Medido Urbano y delimitar sus responsabilidades dentro de la arquitectura monolítica modular propuesta para la Etapa 1.

---

# Principios de Diseño

La solución se organiza en módulos funcionales con responsabilidades claramente definidas.

Cada módulo encapsula reglas de negocio específicas y se comunica con otros módulos mediante interfaces y eventos del dominio.

Esta organización permite:

- alta cohesión funcional,
- bajo acoplamiento,
- mantenibilidad,
- evolución futura hacia arquitecturas distribuidas.

---

# Módulo de Gestión de Usuarios

## Responsabilidades

- Registro de usuarios.
- Administración de credenciales.
- Consulta de información personal.
- Gestión de saldo disponible.

## Información Administrada

- Usuarios.
- Saldo de cuenta.

---

# Módulo de Gestión de Vehículos

## Responsabilidades

- Registro de vehículos.
- Asociación vehículo-usuario.
- Consulta de vehículos registrados.
- Seguimiento del estado actual del vehículo.

## Información Administrada

- Patente.
- Datos descriptivos.
- Estado actual.

---

# Módulo de Gestión de Sesiones

## Responsabilidades

- Inicio de sesión de estacionamiento.
- Registro de timestamps.
- Solicitud de cierre.
- Finalización de sesión.

## Información Administrada

- Sesiones activas.
- Historial de sesiones.

---

# Módulo de Gestión de Cobros

## Responsabilidades

- Cálculo de tarifas.
- Cobro por intervalos.
- Gestión de saldo insuficiente.
- Gestión de intervalos de espera.
- Regularización de deuda.

## Información Administrada

- Cobros.
- Deudas pendientes.
- Historial de pagos.

---

# Módulo de Gestión de Infracciones

## Responsabilidades

- Generación de infracciones.
- Registro de sanciones.
- Cálculo de multas.
- Consulta de historial sancionatorio.

## Información Administrada

- Infracciones.
- Multas.
- Penalizaciones.

---

# Módulo de Gestión de Inspectores

## Responsabilidades

- Recepción de solicitudes de inspección.
- Registro de verificaciones.
- Validación de solicitudes de cierre.

## Información Administrada

- Inspecciones.
- Resultados de verificación.

---

# Módulo de Protocolo de Acarreo

## Responsabilidades

- Gestión de vehículos en estado Acarreo.
- Comunicación con el Departamento de Acarreo.
- Generación de sanciones asociadas.
- Finalización administrativa de sesiones.

## Información Administrada

- Solicitudes de acarreo.
- Resultado de intervenciones.

---

# Módulo de Notificaciones

## Responsabilidades

- Comunicación con usuarios.
- Comunicación con inspectores.
- Emisión de alertas operativas.

## Información Administrada

- Notificaciones emitidas.
- Historial de comunicaciones.

---

# Relación entre Módulos

Los módulos interactúan entre sí mediante operaciones del sistema y eventos del dominio.

La lógica de negocio permanece desacoplada de los mecanismos de comunicación utilizados por cada módulo.

---

# Relacionados

- ARQ-001 – Diagrama de Contexto
- ARQ-002 – Modelo Conceptual de Entidades
- ARQ-003 – Arquitectura Monolítica Modular por Capas
- ARQ-005 – Modelo de Eventos