# ARQ-007 – Persistencia Conceptual

## Objetivo

Definir el modelo conceptual de persistencia para la Etapa 1 del Sistema Inteligente de Estacionamiento Medido Urbano.

Este documento identifica las principales entidades de información que deberán almacenarse de forma permanente y las relaciones existentes entre ellas.

El presente modelo tiene carácter conceptual y no constituye un diseño físico de base de datos.


---

# Alcance

La persistencia conceptual contempla exclusivamente los elementos necesarios para soportar:

- gestión de usuarios,
- gestión de vehículos,
- sesiones de estacionamiento,
- cobros,
- infracciones,
- inspecciones,
- protocolo de acarreo.

---


# Principios de Diseño

La persistencia debe garantizar:

- integridad de la información,
- trazabilidad de eventos,
- consistencia del estado de los vehículos,
- recuperación histórica de operaciones,
- evolución futura hacia nuevas funcionalidades.

---



# Entidad Usuario

## Descripción

Representa una cuenta registrada en el sistema.

## Atributos Conceptuales

- id_usuario
- nombre
- apellido
- email
- telefono
- saldo_actual
- fecha_registro
- estado

## Relaciones

- Un Usuario puede registrar múltiples Vehículos.
- Un Usuario puede recibir múltiples Notificaciones.

---


# Entidad Vehículo

## Descripción

Representa un vehículo habilitado para utilizar el sistema.

## Atributos Conceptuales

- patente
- marca
- modelo
- color
- estado_actual
- fecha_registro

## Relaciones

- Un Vehículo pertenece a un Usuario.
- Un Vehículo puede generar múltiples Sesiones.
- Un Vehículo puede generar múltiples Infracciones.
- Un Vehículo puede generar múltiples Inspecciones.

---


# Entidad Sesión

## Descripción

Representa un período de estacionamiento medido.

## Atributos Conceptuales

- id_sesion
- patente
- ubicacion
- time_start
- time_stop
- estado_final
- duracion_total

## Relaciones

- Una Sesión pertenece a un Vehículo.
- Una Sesión puede generar múltiples Cobros.
- Una Sesión puede generar una Infracción.

---


# Entidad Cobro

## Descripción

Representa una operación de cálculo económico asociada a una sesión.

## Atributos Conceptuales

- id_cobro
- id_sesion
- intervalo_desde
- intervalo_hasta
- timestamp
- importe
- tipo_cobro
- estado

## Tipos Conceptuales

- Intervalo de estacionamiento
- Intervalo de espera
- Cobro final de sesión


## Relaciones

- Un Cobro pertenece a una Sesión.

---

# Entidad Infracción

## Descripción

Representa una sanción administrativa asociada a un vehículo.

## Atributos Conceptuales

- id_infraccion
- patente
- fecha_generacion
- importe_intervalos
- importe_multa
- importe_acarreo
- importe_total
- estado_pago

## Relaciones

- Una Infracción pertenece a un Vehículo.
- Una Infracción puede originarse en una Sesión.

---

# Entidad Inspección

## Descripción

Representa una verificación realizada por un inspector.

## Atributos Conceptuales

- id_inspeccion
- patente
- fecha_hora
- resultado
- observaciones

## Relaciones

- Una Inspección pertenece a un Vehículo.
- Una Inspección puede estar asociada a una Sesión.

---

# Entidad Notificación

## Descripción

Representa una comunicación emitida por el sistema.

## Atributos Conceptuales

- id_notificacion
- id_usuario
- fecha_hora
- tipo
- mensaje
- estado_entrega

## Relaciones

- Una Notificación pertenece a un Usuario.

---

# Entidad Solicitud de Acarreo

## Descripción

Representa una intervención solicitada al Departamento de Acarreo.

## Atributos Conceptuales

- id_solicitud
- patente
- ubicacion
- fecha_hora_solicitud
- fecha_hora_respuesta
- resultado

## Resultados Posibles

- Vehículo encontrado
- Vehículo no encontrado

## Relaciones

- Una Solicitud de Acarreo pertenece a un Vehículo.
- Una Solicitud de Acarreo puede originar una Infracción.

---

# Relaciones Conceptuales Principales

```text
Usuario
  │
  └── 1:N Vehículo

Vehículo
  │
  ├── 1:N Sesión
  ├── 1:N Infracción
  ├── 1:N Inspección
  └── 1:N SolicitudAcarreo

Sesión
  │
  ├── 1:N Cobro
  └── 0..1 Infracción

Usuario
  │
  └── 1:N Notificación
```

---

# Consideraciones de Persistencia

La persistencia deberá garantizar:

- conservación histórica de sesiones,
- conservación histórica de cobros,
- trazabilidad de cambios de estado,
- trazabilidad de sanciones,
- auditoría de operaciones relevantes.

---

# Evolución Futura

El modelo conceptual podrá extenderse en futuras etapas incorporando:

## Etapa 2

- Sensores IoT
- Eventos de ocupación
- Detección automática de presencia

## Etapa 3

- Espacios de estacionamiento
- Reservas
- Asignación dinámica
- Métricas urbanas
- Optimización de ocupación

---

# Relacionados

- ARQ-002 – Modelo Conceptual de Entidades
- ARQ-003 – Arquitectura Monolítica Modular por Capas
- ARQ-006 – Estructura de Implementación Python
- DA-001 – Modelo de Cobro de Estacionamiento
- DA-002 – Supuestos Operativos y Simplificaciones del Dominio