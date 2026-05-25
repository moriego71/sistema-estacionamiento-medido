# UC-010 – Ejecutar Protocolo de Acarreo

## Descripción

El presente Caso de Uso describe el proceso ejecutado cuando un vehículo ingresa en estado de Acarreo debido a incumplimientos detectados durante el flujo de validación y cierre de sesión.

El protocolo permite gestionar administrativamente la infracción correspondiente, calcular los montos sancionatorios asociados y finalizar la sesión de manera administrativa.

---

# Actores

## Actor Primario

- Sistema

> El presente Caso de Uso es iniciado automáticamente por el Sistema como consecuencia de una transición válida al estado Acarreo.

---

## Actores Secundarios

- Inspector
- Departamento de Acarreo
- Sistema de Cobros
- Usuario

---

# Precondiciones

- El vehículo debe encontrarse en estado Acarreo.
- Debe existir una sesión activa asociada al vehículo.
- El protocolo debe haber sido iniciado desde un flujo sancionatorio válido.

---

# Postcondiciones

- La infracción debe quedar registrada.
- La sesión debe finalizar administrativamente.
- El Usuario debe ser notificado.
- El estado final del vehículo debe quedar persistido.

---

# Flujo Principal

## Inicio del Protocolo

1. El Sistema detecta que el vehículo ingresó en estado Acarreo.
2. El Sistema inicia el Protocolo de Acarreo.
3. El Sistema envía la solicitud de intervención al Departamento de Acarreo.
4. El Departamento de Acarreo informa que la grúa encontró el vehículo estacionado.
5. El Sistema aplica el monto completo de acarreo.
6. El Sistema calcula el tiempo correspondiente al último intervalo pendiente.
7. El Sistema calcula el saldo correspondiente al último intervalo.
8. El Sistema aplica la multa correspondiente.
9. El Sistema confecciona la infracción integrando:
   - saldo pendiente,
   - monto de acarreo,
   - multa.
10. El Sistema genera la infracción asociándola a la patente del vehículo.
11. El Sistema registra la infracción en la base de datos.
12. El Sistema registra la infracción en la aplicación del Usuario.
13. El Sistema registra la finalización administrativa de la sesión.
14. El Sistema notifica al Usuario la infracción generada y la finalización de la sesión.
15. El Caso de Uso finaliza.

---

# Flujos Alternativos

## FA-01 – Alternativa de FP4: Vehículo no encontrado por la grúa

1. El Departamento de Acarreo informa que la grúa no encontró el vehículo estacionado.
2. El Sistema aplica el 50% del monto de acarreo.
3. Se vuelve al flujo principal en FP6.

---

# Reglas de Negocio Relacionadas

- RN-001 – Escalamiento Sancionatorio
- RN-002 – Acarreo impide finalización directa

---

# Requerimientos Funcionales Relacionados

- RF-010 – Protocolo de Acarreo
- RF-009 – Fin de Sesión

---

# Diagramas Relacionados

- DG-010 – Flujo de Protocolo de Acarreo
- FSM-Vehiculos

---

# Modelos de Dominio Relacionados

- DA-001 – Modelo de Cobro de Estacionamiento
- DA-002 – Supuestos Operativos y Simplificaciones del Dominio