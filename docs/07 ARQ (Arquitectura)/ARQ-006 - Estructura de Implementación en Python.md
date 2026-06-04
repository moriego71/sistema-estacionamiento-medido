# ARQ-006 – Estructura de Implementación Python

## Objetivo

Definir la organización física del código fuente para la implementación de la Etapa 1 del Sistema Inteligente de Estacionamiento Medido Urbano.

La estructura propuesta se encuentra alineada con la arquitectura monolítica modular por capas definida en ARQ-003 y con los módulos funcionales identificados en ARQ-004.

---

# Principios de Diseño

La implementación deberá respetar los siguientes principios:

- Separación de responsabilidades.
- Bajo acoplamiento entre módulos.
- Alta cohesión funcional.
- Independencia del dominio respecto de tecnologías externas.
- Evolución futura hacia arquitecturas distribuidas y orientadas a eventos.

---

# Estructura General del Proyecto

```text
sistema-estacionamiento-medido/
│
├── docs/
│
├── src/
│
├── tests/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# Organización Interna del Código

```text
src/
│
├── presentation/
│
├── application/
│
├── domain/
│
├── infrastructure/
│
└── shared/
```

---

# Capa de Presentación

## Propósito

Gestionar la interacción con usuarios y sistemas externos.

## Estructura

```text
presentation/
│
├── api/
├── controllers/
├── requests/
└── responses/
```

## Responsabilidades

- Recepción de solicitudes.
- Validación básica de datos.
- Exposición de endpoints.
- Formateo de respuestas.

---

# Capa de Aplicación

## Propósito

Orquestar los casos de uso del sistema.

## Estructura

```text
application/
│
├── commands/
├── services/
├── use_cases/
└── events/
```

## Responsabilidades

- Coordinación de procesos.
- Ejecución de casos de uso.
- Publicación de eventos.
- Comunicación entre módulos.

---

# Capa de Dominio

## Propósito

Contener las reglas de negocio del sistema.

## Estructura

```text
domain/
│
├── usuarios/
├── vehiculos/
├── sesiones/
├── cobros/
├── infracciones/
├── inspectores/
├── acarreo/
└── notificaciones/
```

---

# Módulo Usuarios

## Responsabilidades

- Gestión de cuentas.
- Administración de saldo.
- Consulta de información del usuario.

---

# Módulo Vehículos

## Responsabilidades

- Registro de vehículos.
- Gestión de estados.
- Asociación usuario-vehículo.

---

# Módulo Sesiones

## Responsabilidades

- Inicio de sesión.
- Cierre de sesión.
- Registro de timestamps.

---

# Módulo Cobros

## Responsabilidades

- Cálculo de tarifas.
- Gestión de intervalos.
- Gestión de saldo insuficiente.
- Gestión de intervalos de espera.

---

# Módulo Infracciones

## Responsabilidades

- Generación de infracciones.
- Gestión de multas.
- Historial sancionatorio.

---

# Módulo Inspectores

## Responsabilidades

- Validación de solicitudes de cierre.
- Registro de verificaciones.

---

# Módulo Acarreo

## Responsabilidades

- Gestión del Protocolo de Acarreo.
- Integración con Departamento de Acarreo.

---

# Módulo Notificaciones

## Responsabilidades

- Comunicación con usuarios.
- Comunicación con inspectores.
- Emisión de alertas.

---

# Capa de Infraestructura

## Propósito

Implementar las dependencias tecnológicas externas.

## Estructura

```text
infrastructure/
│
├── database/
├── repositories/
├── messaging/
├── notifications/
└── integrations/
```

## Responsabilidades

- Persistencia.
- Acceso a datos.
- Integraciones externas.
- Servicios de mensajería.

---

# Capa Compartida

## Propósito

Centralizar componentes reutilizables.

## Estructura

```text
shared/
│
├── exceptions/
├── constants/
├── utils/
└── config/
```

## Responsabilidades

- Configuración.
- Utilidades comunes.
- Constantes globales.
- Manejo de excepciones.

---

# Estructura de Pruebas

```text
tests/
│
├── unit/
├── integration/
└── acceptance/
```

## Tipos de Pruebas

### Unitarias (Unit Test)

Validan reglas de negocio aisladas.

### Integración (Integration Test)

Validan interacción entre módulos.

### Aceptación (E2E)

Validan flujos completos del sistema.

---

# Gestión de Eventos

La arquitectura contempla un mecanismo interno de publicación y consumo de eventos de dominio.

Ejemplos:

- SesionIniciada
- CobroRealizado
- SaldoInsuficienteDetectado
- SolicitudCierreSesion
- InfraccionGenerada
- VehiculoEnAcarreo
- SesionFinalizada

Los eventos inicialmente serán gestionados dentro del mismo proceso de ejecución.

---

# Evolución Futura

La estructura propuesta permite evolucionar progresivamente hacia:

## Etapa 2

- Sensores IoT.
- Validación automática.
- Integración con dispositivos externos.

## Etapa 3

- Reservas inteligentes.
- Asignación dinámica de espacios.
- Arquitecturas distribuidas.
- Procesamiento orientado a eventos.

---

# Relacionados

- ARQ-003 – Arquitectura Monolítica Modular por Capas
- ARQ-004 – Módulos del Sistema
- ARQ-005 – Modelo de Eventos
- DA-001 – Modelo de Cobro de Estacionamiento
- DA-002 – Supuestos Operativos y Simplificaciones del Dominio