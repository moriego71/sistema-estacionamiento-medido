# UC-008 – Solicitar Cierre de Sesión

## Objetivo

Permitir que un Usuario solicite el cierre de una sesión de estacionamiento activa, sometiendo la solicitud a un proceso de validación mediante inspección antes de confirmar o rechazar la finalización.

# Actor primario

- Usuario

# Actores secundarios

- Inspector
- Departamento de Acarreo

## Disparador

El Usuario solicita finalizar una sesión de estacionamiento activa desde la aplicación.

## Precondiciones

- El Usuario debe encontrarse autenticado.
- Debe existir una sesión activa asociada al vehículo.
- El vehículo debe encontrarse en un estado válido para solicitar cierre de sesión.

# Flujo principal

1. El Usuario solicita el cierre de sesión.
2. El Sistema registra el time_stop.
3. El Sistema inicia el proceso de validación.
4. El Sistema solicita una inspección del vehículo.
5. El Inspector verifica la situación del vehículo.
6. Si el Inspector confirma que el vehículo ya no se encuentra estacionado:
    - El Sistema finaliza la sesión.
    - El Sistema deja disponible la información para módulos de cobros e infracciones.
7. El caso de uso finaliza.

# Flujos alternativos

## FA-FP06 – Cierre inválido

1. El Inspector informa que el vehículo continúa estacionado.
2. El Sistema rechaza el cierre de sesión.
3. El Sistema aplica la transición de estado sancionatoria correspondiente.
4. El Sistema notifica al Usuario la situación de cierre inválido y el nuevo estado del vehículo.
5. Si la transición de estado resulta en Acarreo:
    - El Sistema inicia el protocolo de acarreo.
    - El Sistema deriva la gestión al departamento correspondiente.

# Postcondiciones

- La sesión queda finalizada.
o
- El vehículo queda asociado a un nuevo estado sancionatorio.
- El evento queda registrado en el sistema.
- La información queda disponible para procesamiento posterior.

# Reglas relacionadas

- RN-001 – Escalamiento Sancionatorio
- RN-002 – Acarreo impide finalización directa
- RN-003 – Conservación de Estado Previo

# Diagramas relacionados

- FSM – Vehículos y Sesiones
- DG-008 – Flujo de Cierre de Sesión

# Requerimientos relacionados

- RF-008 – Solicitud de Cierre de Sesión
