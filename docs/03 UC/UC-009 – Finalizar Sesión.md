# UC-009 – Finalizar Sesión

## Objetivo

Procesar la finalización de una sesión de estacionamiento válida, calculando y cobrando el último intervalo pendiente, registrando la sesión y notificando al Usuario.

## Actor primario

- Usuario

## Actores secundarios

- Sistema de Cobros

## Disparador

El Sistema recibe un evento de FIN DE SESIÓN válido.

## Precondiciones

- Debe existir una sesión validada para finalizar.
- La sesión debe encontrarse autorizada para cierre.

# Flujo principal

1. El Sistema recibe el evento de FIN DE SESIÓN.
2. El Sistema verifica el estado final del vehículo.
3. El Sistema calcula el tiempo correspondiente al último intervalo de estacionamiento.
4. El Sistema calcula el saldo final correspondiente al último intervalo.
5. El Sistema ejecuta el cobro del último intervalo pendiente.
6. El Sistema registra la sesión como finalizada.
7. El Sistema deja disponible la información necesaria para el procesamiento de cobros.
8. El Sistema notifica al Usuario la finalización de la sesión.
9. El caso de uso finaliza.

# Flujos alternativos

## FA-FP02 – Protocolo de Acarreo

**Origen:** Paso 2 del Flujo Principal.

1. El Sistema detecta que el estado final del vehículo corresponde a acarreo.
2. El Sistema inicia Protocolo de Acarreo.
3. El caso de uso finaliza.

# Postcondiciones

- La sesión queda registrada como finalizada.
- La información queda disponible para procesamiento posterior.
- El Usuario recibe una notificación de cierre.
- El resultado del procesamiento queda registrado.

# Relacionados

- RF-009 – Finalización de Sesión
- DG-009 - Finalizar Sesión
- RN-002 - Acarreo impide finalización directa
- DG-009 – Flujo de Finalización de Sesión
- DA-001 – Modelo de Cobro de Estacionamiento