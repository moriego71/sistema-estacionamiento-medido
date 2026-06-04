# ARQ-009 – Diseño Físico del Proyecto Python

## Objetivo

Definir la estructura física del proyecto para la implementación de la Etapa 1 del Sistema Inteligente de Estacionamiento Medido Urbano.

El diseño propuesto implementa la arquitectura monolítica modular definida en ARQ-003 y la organización funcional definida en ARQ-004.

---

# Tecnologías Seleccionadas

## Lenguaje

- Python 3.13+

---

## Persistencia

- SQLite (desarrollo inicial)
- PostgreSQL (evolución futura)

---

## ORM

- SQLAlchemy

---

## Validación de Datos

- Pydantic

---

## Testing

- Pytest

---

## Gestión de Dependencias

- pip

---

## Control de Versiones

- Git
- GitHub

---

# Estructura Física del Proyecto

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
├── .gitignore
│
└── README.md
```

---

# Estructura del Código Fuente

```text
src/
│
├── application/
├── domain/
├── infrastructure/
├── presentation/
└── shared/
```

---

# Capa Domain

Contiene las reglas de negocio.

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

## Ejemplo

```text
vehiculos/
│
├── entities/
├── services/
├── repositories/
└── events/
```

---

# Capa Application

Coordina los casos de uso.

```text
application/
│
├── use_cases/
├── commands/
├── services/
└── event_handlers/
```

---

# Capa Infrastructure

Implementa detalles tecnológicos.

```text
infrastructure/
│
├── database/
├── repositories/
├── messaging/
├── notifications/
└── integrations/
```

---

## Base de Datos

```text
database/
│
├── models/
├── migrations/
└── session.py
```

---

# Capa Presentation

Gestiona interacción con actores externos.

```text
presentation/
│
├── api/
├── controllers/
├── requests/
└── responses/
```

---

# Capa Shared

Componentes reutilizables.

```text
shared/
│
├── config/
├── constants/
├── exceptions/
└── utils/
```

---

# Gestión de Eventos

Los eventos serán implementados mediante un Event Bus interno.

## Eventos Iniciales

- SesionIniciada
- IntervaloFinalizado
- CobroRealizado
- SaldoInsuficienteDetectado
- SolicitudRecargaEmitida
- SaldoRegularizado
- SolicitudCierreSesion
- InspeccionSolicitada
- VehiculoEnInfraccion
- VehiculoEnPenalizacion
- VehiculoEnAcarreo
- SolicitudAcarreoEmitida
- InfraccionGenerada
- SesionFinalizada

---

# Persistencia

La persistencia será implementada mediante SQLAlchemy.

## Entidades Iniciales

- Usuario
- Vehiculo
- Sesion
- Cobro
- Infraccion
- Inspeccion
- SolicitudAcarreo
- Notificacion

---

# Testing

La estructura de pruebas será:

```text
tests/
│
├── unit/
├── integration/
└── acceptance/
```

---

## Unit Tests

Validan reglas de negocio aisladas.

---

## Integration Tests

Validan interacción entre módulos.

---

## Acceptance Tests (E2E)

Validan casos de uso completos.

---

# Archivo requirements.txt

Dependencias iniciales previstas:

```text
sqlalchemy
pydantic
pytest
```

---

# Convenciones de Desarrollo

## Nombres de Archivos

```text
snake_case.py
```

Ejemplo:

```text
vehiculo_service.py
sesion_repository.py
cobro_use_case.py
```

---

## Nombres de Clases

```text
PascalCase
```

Ejemplo:

```text
Vehiculo
Sesion
Cobro
Infraccion
```

---

## Nombres de Variables

```text
snake_case
```

Ejemplo:

```text
saldo_actual
estado_vehiculo
fecha_inicio
```

---

# Evolución Futura

La estructura propuesta permite incorporar:

- FastAPI
- PostgreSQL
- RabbitMQ
- MQTT
- Sensores IoT
- Microservicios
- Procesamiento distribuido

sin modificar significativamente la organización interna del dominio.

---

# Relacionados

- ARQ-003 – Arquitectura Monolítica Modular por Capas
- ARQ-004 – Módulos del Sistema
- ARQ-005 – Modelo de Eventos
- ARQ-006 – Estructura de Implementación Python
- ARQ-007 – Persistencia Conceptual