# ADR-004 – Arquitectura Orientada a Eventos

## Estado

Esperando Aprobación

---

## Contexto

El dominio presenta múltiples procesos desencadenados por cambios de estado y eventos operativos.

Ejemplos:

- Inicio de sesión.
- Finalización de intervalo.
- Saldo insuficiente.
- Solicitud de inspección.
- Solicitud de acarreo.

---

## Decisión

Adoptar un modelo interno orientado a eventos para la comunicación entre módulos.

Durante la Etapa 1 los eventos serán gestionados dentro del mismo proceso de ejecución.

---

## Justificación

- Desacoplamiento entre módulos.
- Mayor mantenibilidad.
- Evolución natural hacia EDA.
- Compatibilidad futura con IoT.

---

## Consecuencias

### Positivas

- Mejor separación de responsabilidades.
- Mayor extensibilidad.
- Facilidad de evolución futura.

### Negativas

- Mayor complejidad conceptual respecto a llamadas directas.

---

## Evolución Futura

Los eventos podrán migrar a mecanismos de mensajería externos sin modificar significativamente la lógica de negocio existente.