# ARQ-003 – Arquitectura Monolítica Modular por Capas

## Objetivo

Definir la arquitectura de software propuesta para la implementación de la Etapa 1 del Sistema Inteligente de Estacionamiento Medido Urbano.

La arquitectura busca priorizar:

- simplicidad de implementación,
- mantenibilidad,
- bajo acoplamiento,
- evolución futura hacia arquitecturas distribuidas,
- incorporación de sensores IoT y procesamiento orientado a eventos.

---

# Decisión Arquitectónica

Para la Etapa 1 se adopta una arquitectura:

- Monolítica
- Modular
- Orientada por capas

Todos los componentes del sistema se ejecutan dentro de una única aplicación, compartiendo:

- base de datos,
- configuración,
- despliegue,
- ciclo de vida.

---

# Justificación

La elección de una arquitectura monolítica modular permite:

- reducir complejidad inicial,
- acelerar el desarrollo del prototipo,
- facilitar pruebas,
- simplificar despliegue,
- validar el modelo de negocio antes de introducir complejidad distribuida.

Esta decisión resulta consistente con los objetivos de la Etapa 1, centrados en la digitalización del estacionamiento medido.

---

# Capas de la Arquitectura

## Presentación

Responsable de la interacción con usuarios y sistemas externos.

Funciones:

- App Usuario
- App Inspector
- APIs externas
- Servicios de consulta

---

## Aplicación

Responsable de coordinar los casos de uso del sistema.

Funciones:

- iniciar sesión
- finalizar sesión
- gestionar cobros
- gestionar infracciones
- ejecutar protocolo de acarreo

---

## Dominio

Responsable de implementar las reglas de negocio.

Funciones:

- gestión de estados
- cálculo de cobros
- cálculo de sanciones
- reglas de escalamiento
- generación de infracciones

---

## Persistencia

Responsable del almacenamiento de información.

Funciones:

- usuarios
- vehículos
- sesiones
- cobros
- infracciones
- auditoría

---

# Módulos del Sistema

La arquitectura se organiza en módulos funcionales.

## Gestión de Usuarios

Responsabilidades:

- registro
- autenticación
- administración de saldo

---

## Gestión de Vehículos

Responsabilidades:

- asociación vehículo-usuario
- seguimiento de estado
- historial

---

## Gestión de Sesiones

Responsabilidades:

- inicio de sesión
- control de intervalos
- cierre de sesión

---

## Gestión de Cobros

Responsabilidades:

- cálculo de tarifas
- control de saldo
- intervalos de espera

---

## Gestión de Infracciones

Responsabilidades:

- generación de infracciones
- cálculo de multas
- persistencia

---

## Gestión de Inspectores

Responsabilidades:

- validación de cierres
- verificación de vehículos

---

## Protocolo de Acarreo

Responsabilidades:

- coordinación con Departamento de Acarreo
- generación de sanciones asociadas
- finalización administrativa

---

# Beneficios Esperados

La arquitectura propuesta permite:

- alta cohesión funcional,
- bajo acoplamiento entre módulos,
- evolución controlada del sistema,
- incorporación futura de eventos distribuidos.

---

# Evolución Futura

La arquitectura se diseñó para evolucionar posteriormente hacia:

## Etapa 2

- Sensores IoT
- Detección automática de ocupación
- Validación automática de estacionamiento

## Etapa 3

- Reservas inteligentes
- Asignación dinámica de espacios
- Optimización urbana
- Smart Cities

---

# Relacionados

- ARQ-001 – Diagrama de Contexto
- ARQ-002 – Modelo Conceptual de Entidades
- DA-001 – Modelo de Cobro de Estacionamiento
- DA-002 – Supuestos Operativos y Simplificaciones del Dominio