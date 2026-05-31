# RF-011 – Gestión de Cobros

## Descripción

El presente Requerimiento Funcional describe el proceso de gestión de cobro durante una sesión activa de estacionamiento.

El Sistema debe administrar el cobro periódico de los intervalos de estacionamiento, verificar la disponibilidad de saldo del Usuario y aplicar los mecanismos de regularización y escalamiento sancionatorio cuando corresponda.

Asimismo, el proceso debe integrarse con los flujos de Solicitud de Cierre de Sesión y Protocolo de Acarreo.

---

## Criterios de aceptación

### Gestión de Intervalos

- El Sistema debe registrar el timestamp correspondiente al inicio de cada intervalo de estacionamiento.
- El Sistema debe verificar si existe una solicitud de cierre de sesión durante el intervalo en curso.
- Si existe una solicitud de cierre:
  - El Sistema debe derivar el procesamiento al flujo de Solicitud de Cierre de Sesión.
  - El proceso de Gestión de Cobros debe finalizar.

---

### Cobro de Intervalos

- Si no existe una solicitud de cierre:
  - El Sistema debe registrar el timestamp correspondiente al fin del intervalo.
  - El Sistema debe calcular el monto correspondiente al intervalo.
  - El Sistema debe verificar la disponibilidad de saldo del Usuario.

- Si el Usuario posee saldo suficiente:
  - El Sistema debe debitar el monto calculado.
  - El Sistema debe informar al Usuario el inicio de un nuevo intervalo.
  - El Sistema debe registrar el timestamp correspondiente al inicio del nuevo intervalo.
  - El Sistema debe reiniciar el ciclo de Gestión de Cobros.

---

### Saldo Insuficiente

- Si el Usuario no posee saldo suficiente:
  - El Sistema debe iniciar una ventana de regularización equivalente a un intervalo de estacionamiento.
  - El Sistema debe emitir una solicitud de recarga de saldo al Usuario.

- Si durante la ventana de regularización el Usuario registra una recarga:
  - El Sistema debe calcular el importe correspondiente a los intervalos de espera acumulados.
  - El Sistema debe calcular el monto final adeudado.
  - El Sistema debe verificar si el saldo disponible resulta suficiente para cancelar la deuda acumulada.

- Si el saldo disponible resulta suficiente:
  - El Sistema debe debitar el monto final correspondiente.
  - El Sistema debe informar al Usuario el inicio de un nuevo intervalo.
  - El Sistema debe registrar el timestamp correspondiente al inicio del nuevo intervalo.
  - El Sistema debe continuar el ciclo normal de cobro.

- Si el saldo disponible continúa siendo insuficiente:
  - El Sistema debe mantener activa la ventana de regularización.
  - El Sistema debe solicitar una nueva recarga de saldo.

---

### Escalamiento Sancionatorio

- Si finaliza la ventana de regularización sin que el Usuario regularice la deuda:
  - El Sistema debe aplicar el Escalamiento Sancionatorio correspondiente.
  - El Sistema debe notificar al Usuario el nuevo estado sancionatorio.

- Si el nuevo estado no corresponde a Acarreo:
  - El Sistema debe incrementar la cantidad de intervalos de espera acumulados.
  - El Sistema debe iniciar una nueva ventana de regularización.

- Si el nuevo estado corresponde a Acarreo:
  - El Sistema debe iniciar el Protocolo de Acarreo.
  - El proceso de Gestión de Cobros debe finalizar.

---

## Relacionados

- RF-008 – Solicitud de Cierre de Sesión
- RF-009 – Fin de Sesión
- RF-010 – Protocolo de Acarreo
- RN-001 – Escalamiento Sancionatorio
- RN-005 – Escalamiento por Falta de Regularización de Saldo
- DA-001 – Modelo de Cobro de Estacionamiento
- DG-011 – Gestión de Cobros