# UC-011 – Gestionar Cobros de Estacionamiento

## Descripción

El presente Caso de Uso describe el proceso periódico de gestión de cobros durante una sesión activa de estacionamiento.

El Sistema debe verificar la existencia de solicitudes de cierre de sesión, validar la disponibilidad de saldo del Usuario, efectuar los cobros correspondientes y gestionar los mecanismos de regularización y escalamiento sancionatorio cuando se detecten situaciones de saldo insuficiente.

---

# Actores

## Actor Primario

- Sistema

---

## Actores Secundarios

- Usuario

---

# Precondiciones

- Debe existir una sesión de estacionamiento activa.
- El vehículo debe encontrarse asociado a una sesión válida.
- El Usuario debe encontrarse registrado en el sistema.

---

# Postcondiciones

- El cobro correspondiente debe quedar registrado.
- El saldo del Usuario debe quedar actualizado.
- El estado sancionatorio del vehículo debe quedar actualizado cuando corresponda.
- El Protocolo de Acarreo debe iniciarse si el vehículo alcanza dicho estado.

---

# Flujo Principal

## Gestión Normal de Cobro

1. El Sistema registra el timestamp correspondiente al inicio del intervalo.
2. El Sistema verifica si existe una solicitud de cierre de sesión durante el intervalo en curso.
3. El Sistema registra el timestamp correspondiente al fin del intervalo.
4. El Sistema calcula el monto correspondiente al intervalo.
5. El Sistema verifica la disponibilidad de saldo del Usuario.
6. El Sistema debita el monto correspondiente.
7. El Sistema informa al Usuario el inicio de un nuevo intervalo.
8. El Sistema registra el timestamp correspondiente al inicio del nuevo intervalo.
9. El flujo retorna a FP2.

---

# Flujos Alternativos

## FA-01 – Alternativa de FP2: Solicitud de cierre durante el intervalo

1. El Sistema detecta una solicitud de cierre de sesión.
2. El Sistema deriva el procesamiento al UC-008 – Solicitar Cierre de Sesión.
3. El Caso de Uso finaliza.

---

## FA-02 – Alternativa de FP5: Saldo insuficiente

1. El Sistema detecta saldo insuficiente.
2. El Sistema inicia una ventana de regularización equivalente a un intervalo de estacionamiento.
3. El Sistema solicita una recarga de saldo al Usuario.

### FA-02.1 – El Usuario registra una recarga

1. El Usuario registra una recarga de saldo.
2. El Sistema calcula el importe correspondiente a los intervalos de espera acumulados.
3. El Sistema calcula el monto final adeudado.
4. El Sistema verifica si el saldo disponible resulta suficiente para cancelar la deuda acumulada.

#### FA-02.1.1 – Saldo suficiente

1. El Sistema debita el monto final correspondiente.
2. El Sistema informa al Usuario el inicio de un nuevo intervalo.
3. El Sistema registra el timestamp correspondiente al inicio del nuevo intervalo.
4. El flujo retorna a FP2.

#### FA-02.1.2 – Saldo insuficiente

1. El Sistema mantiene activa la ventana de regularización.
2. El Sistema solicita una nueva recarga de saldo.
3. El flujo retorna a FA-02.

---

### FA-02.2 – El Usuario no regulariza la deuda

1. Finaliza la ventana de regularización sin registrarse una recarga suficiente.
2. El Sistema aplica la RN-005 – Escalamiento por Falta de Regularización de Saldo.
3. El Sistema notifica al Usuario el nuevo estado sancionatorio.

#### FA-02.2.1 – El nuevo estado no es Acarreo

1. El Sistema incrementa la cantidad de intervalos de espera acumulados.
2. El Sistema inicia una nueva ventana de regularización.
3. El flujo retorna a FA-02.

#### FA-02.2.2 – El nuevo estado es Acarreo

1. El Sistema inicia el UC-010 – Ejecutar Protocolo de Acarreo.
2. El Caso de Uso finaliza.

---

# Reglas de Negocio Relacionadas

- RN-001 – Escalamiento Sancionatorio
- RN-005 – Escalamiento por Falta de Regularización de Saldo

---

# Requerimientos Funcionales Relacionados

- RF-011 – Gestión de Cobros
- RF-008 – Solicitud de Cierre de Sesión
- RF-009 – Fin de Sesión
- RF-010 – Protocolo de Acarreo

---

# Diagramas Relacionados

- DG-011 – Gestión de Cobros
- DG-008 – Flujo de Cierre de Sesión
- DG-010 – Protocolo de Acarreo
- FSM-Vehículos

---

# Modelos de Dominio Relacionados

- DA-001 – Modelo de Cobro de Estacionamiento
- DA-002 – Supuestos Operativos y Simplificaciones del Dominio