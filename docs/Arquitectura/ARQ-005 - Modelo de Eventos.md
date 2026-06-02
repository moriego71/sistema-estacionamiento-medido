# ARQ-005 – Modelo de Eventos

## Objetivo

Definir los eventos relevantes del dominio que representan cambios de estado significativos dentro del Sistema Inteligente de Estacionamiento Medido Urbano.

El modelo de eventos constituye la base conceptual para una futura evolución hacia arquitecturas orientadas a eventos e integración con dispositivos IoT.

---

# Concepto de Evento

Un evento representa un hecho relevante ocurrido dentro del dominio del sistema.

Los eventos son generados por usuarios, inspectores o procesos automáticos y pueden ser consumidos por distintos módulos del sistema.

---

# Eventos de Gestión de Sesiones

## SesionIniciada

Generado cuando un usuario inicia una sesión de estacionamiento.

---

## IntervaloIniciado

Generado al comenzar un nuevo intervalo de estacionamiento.

---

## IntervaloFinalizado

Generado al finalizar un intervalo de estacionamiento.

---

## SolicitudCierreSesion

Generado cuando el usuario solicita finalizar una sesión.

---

## SesionFinalizada

Generado cuando una sesión concluye definitivamente.

---

# Eventos de Gestión de Cobros

## CobroRealizado

Generado cuando un cobro es debitado exitosamente.

---

## SaldoInsuficienteDetectado

Generado cuando el sistema detecta imposibilidad de efectuar un cobro por falta de saldo.

---

## SolicitudRecargaEmitida

Generado cuando se solicita una recarga de saldo al usuario.

---

## SaldoRecargado

Generado cuando el usuario incorpora saldo a su cuenta.

---

## SaldoRegularizado

Generado cuando la deuda pendiente es cancelada exitosamente.

---

# Eventos de Gestión Sancionatoria

## EstadoEscalado

Generado cuando un vehículo cambia a un estado sancionatorio superior.

---

## VehiculoEnInfraccion

Generado cuando un vehículo ingresa en estado Infracción.

---

## VehiculoEnPenalizacion

Generado cuando un vehículo ingresa en estado Penalización.

---

## VehiculoEnAcarreo

Generado cuando un vehículo ingresa en estado Acarreo.

---

## InfraccionGenerada

Generado cuando el sistema confecciona una infracción.

---

# Eventos de Inspección

## InspeccionSolicitada

Generado cuando el sistema requiere la intervención de un inspector.

---

## InspeccionRealizada

Generado cuando un inspector informa el resultado de una verificación.

---

## FalsoFinSesionDetectado

Generado cuando un inspector determina que el vehículo continúa estacionado luego de una solicitud de cierre.

---

# Eventos de Acarreo

## SolicitudAcarreoEmitida

Generado cuando el sistema comunica una solicitud al Departamento de Acarreo.

---

## VehiculoEncontrado

Generado cuando la grúa informa que encontró el vehículo estacionado.

---

## VehiculoNoEncontrado

Generado cuando la grúa informa que el vehículo ya no se encuentra estacionado.

---

## ProtocoloAcarreoFinalizado

Generado cuando concluye administrativamente el Protocolo de Acarreo.

---

# Beneficios Arquitectónicos

La utilización de eventos permite:

- desacoplar módulos funcionales,
- simplificar la evolución del sistema,
- facilitar integración con sensores IoT,
- habilitar procesamiento asíncrono futuro,
- preparar una eventual migración hacia arquitecturas distribuidas.

---

# Evolución Futura

Los eventos definidos constituyen la base conceptual para:

- Event Driven Architecture (EDA),
- integración IoT,
- sensores de ocupación,
- reservas inteligentes,
- asignación dinámica de espacios,
- procesamiento distribuido.

---

# Relacionados

- ARQ-003 – Arquitectura Monolítica Modular por Capas
- ARQ-004 – Módulos del Sistema
- FSM-Vehiculos
- RF-008 – Solicitud de Cierre de Sesión
- RF-009 – Fin de Sesión
- RF-010 – Protocolo de Acarreo
- RF-011 – Gestión de Cobro