# ADR-003 – Persistencia Relacional

## Estado

Esperando Aprobación

---

## Contexto

La Etapa 1 requiere consistencia transaccional, trazabilidad histórica y relaciones claramente definidas entre entidades del dominio.

---

## Decisión

Utilizar una base de datos relacional como mecanismo principal de persistencia.

---

## Justificación

- Integridad referencial.
- Consistencia transaccional.
- Modelo alineado con las entidades identificadas.
- Amplia madurez tecnológica.

---

## Consecuencias

### Positivas

- Modelo robusto.
- Facilidad de auditoría.
- Soporte para consultas complejas.

### Negativas

- Menor flexibilidad frente a datos no estructurados.

---

## Evolución Futura

Podrán incorporarse mecanismos complementarios de persistencia especializados para telemetría, eventos o analítica avanzada.