# RN-005 – Escalamiento por Falta de Regularización de Saldo

## Descripción

Cuando un Usuario no regulariza una situación de saldo insuficiente dentro de la ventana de regularización otorgada por el Sistema, el vehículo debe escalar al siguiente estado sancionatorio definido por la Máquina de Estados del sistema.

El proceso de escalamiento puede repetirse sucesivamente mientras persista la falta de regularización.

---

## Regla

- El Sistema debe otorgar una ventana de regularización equivalente a un intervalo de estacionamiento cuando detecte saldo insuficiente.
- Si el Usuario recarga saldo dentro de la ventana de regularización:
  - El Sistema debe continuar el proceso normal de Gestión de Cobros.
- Si el Usuario no recarga saldo dentro de la ventana de regularización:
  - El Sistema debe aplicar el Escalamiento Sancionatorio correspondiente.
- Si la situación de saldo insuficiente persiste:
  - El Sistema debe iniciar una nueva ventana de regularización.
  - El Sistema debe continuar aplicando Escalamiento Sancionatorio por cada ventana vencida sin regularización.
- El proceso finaliza cuando:
  - el Usuario regulariza su situación mediante una recarga de saldo, o
  - el vehículo alcanza el estado Acarreo.

---

## Consideraciones

- La secuencia de estados sancionatorios aplicables se encuentra definida por la Máquina de Estados del sistema.
- La cantidad de intervalos consecutivos transcurridos sin regularización debe conservarse para garantizar la correcta aplicación del escalamiento sancionatorio.
- El estado Acarreo constituye el máximo nivel sancionatorio contemplado por el sistema.

---

## Relacionados

- RN-001 – Escalamiento Sancionatorio
- RF-011 – Gestión de Cobros
- UC-011 – Gestión de Cobros
- DG-011 – Gestión de Cobros
- FSM-Vehículos