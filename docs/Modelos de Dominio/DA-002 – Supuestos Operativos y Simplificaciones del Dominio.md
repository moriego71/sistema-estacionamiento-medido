# DA-002 – Supuestos Operativos y Simplificaciones del Dominio

## Objetivo

Definir los supuestos operativos, simplificaciones deliberadas y restricciones de alcance consideradas durante el modelado conceptual del sistema de estacionamiento medido urbano.

El presente documento tiene como finalidad delimitar el comportamiento actualmente modelado en la Etapa 1 del sistema, justificando las decisiones de abstracción adoptadas para reducir complejidad operativa y priorizar la consolidación del dominio principal.

---

# 1. Supuestos Operativos

## SO-001 – Resultado operativo del Departamento de Acarreo

El sistema considera únicamente el resultado operativo informado por el Departamento de Acarreo respecto del estado físico del vehículo.

Los posibles resultados contemplados son:

- vehículo encontrado estacionado,
- vehículo no encontrado estacionado.

El sistema no modela el proceso logístico interno asociado al despacho, recorrido o coordinación operativa de las grúas.

---

## SO-002 – Ejecución exitosa del acarreo

El sistema asume que, una vez informado que la grúa encontró el vehículo estacionado, el acarreo se ejecuta correctamente sin inconvenientes operativos posteriores.

No se contemplan escenarios de:

- fallas mecánicas,
- cancelaciones posteriores,
- conflictos operativos,
- imposibilidad física de remoción.

---

## SO-003 – Disponibilidad de servicios externos

El sistema asume disponibilidad operativa de los servicios externos involucrados en el proceso sancionatorio y administrativo.

No se modelan:

- caídas de servicios,
- indisponibilidad de comunicación,
- demoras de organismos externos,
- errores de sincronización interinstitucional.

---

## SO-004 – Liberación automática de recursos operativos

La liberación de recursos operativos externos asociados al protocolo de acarreo se considera automática al finalizar la sesión.

El sistema no administra explícitamente la disponibilidad logística del Departamento de Acarreo.

---

# 2. Simplificaciones Deliberadas del Dominio

## SD-001 – Simplificación del flujo de acarreo

El modelo conceptual actual abstrae el comportamiento operativo detallado del proceso de acarreo, enfocándose únicamente en las consecuencias administrativas y sancionatorias derivadas del mismo.

---

## SD-002 – Resolución simplificada del estado Acarreo

El estado Acarreo se modela como un estado sancionatorio único, sin subdivisiones internas.

No se contemplan subestados tales como:

- Acarreo pendiente,
- Acarreo en curso,
- Acarreo ejecutado,
- Acarreo cancelado.

---

## SD-003 – Simplificación de intervención humana

El modelo no contempla interacciones conflictivas entre:

- inspectores,
- operadores,
- usuarios,
- personal de acarreo.

Toda interacción operativa se considera correctamente ejecutada y comunicada al sistema.

---

## SD-004 – Simplificación temporal

El sistema no modela tiempos reales asociados a:

- llegada de grúas,
- demoras operativas,
- tiempos administrativos,
- colas de atención,
- congestión urbana.

---

## SD-005 – Simplificación asociación usuario/vehículo

Para la Etapa 1 se asume que cada vehículo se encuentra asociado a una única cuenta de usuario responsable de la gestión de saldo, estacionamiento e infracciones. No se modelan esquemas de propiedad compartida ni múltiples usuarios operando sobre un mismo vehículo.

# 3. Restricciones de Alcance de Etapa 1

## RA-001 – Ausencia de integración IoT

La Etapa 1 no contempla integración con:

- sensores urbanos,
- cámaras inteligentes,
- reconocimiento automático de patentes,
- validación automática de ocupación,
- telemetría en tiempo real.

La validación del estado del vehículo depende de la intervención operativa humana.

---

## RA-002 – Ausencia de asignación dinámica

La Etapa 1 no implementa mecanismos de:

- reserva inteligente,
- recomendación de espacios,
- asignación dinámica,
- optimización urbana,
- predicción de ocupación.

---

## RA-003 – Arquitectura técnica no definida

Durante la presente etapa no se define arquitectura técnica definitiva respecto de:

- infraestructura,
- despliegue,
- microservicios,
- mensajería,
- persistencia distribuida,
- tecnologías específicas.

La etapa actual se enfoca exclusivamente en la consolidación funcional y conceptual del dominio.

---

# 4. Consideraciones para Evolución Futura

## EF-001 – Evolución hacia IoT urbano

El modelo conceptual actual se diseña con orientación evolutiva para permitir futuras integraciones con:

- sensores de ocupación,
- validación automática,
- detección inteligente de infracciones,
- monitoreo urbano en tiempo real.

---

## EF-002 – Evolución hacia asignación dinámica

La arquitectura conceptual contempla futura evolución hacia mecanismos de:

- reservas inteligentes,
- recomendación de estacionamiento,
- optimización de ocupación urbana,
- asignación dinámica de espacios.

---

## EF-003 – Evolución arquitectónica

La modularización actual del dominio busca facilitar una futura transición hacia arquitecturas escalables basadas en:

- eventos,
- servicios desacoplados,
- procesamiento distribuido,
- integración de componentes inteligentes.

---

# Conclusión

Las simplificaciones y restricciones definidas en el presente documento son deliberadas y responden a la necesidad de consolidar inicialmente el dominio funcional y sancionatorio del sistema de estacionamiento medido urbano.

La Etapa 1 prioriza la estabilidad conceptual, trazabilidad operativa y consistencia del modelo de negocio, estableciendo las bases necesarias para futuras evoluciones tecnológicas orientadas a Smart Cities e integración IoT.