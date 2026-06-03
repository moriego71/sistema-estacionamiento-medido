# DA-001 – Modelo de Cobro de Estacionamiento

## 1. Objetivo

El presente documento define el modelo conceptual de cobro utilizado por el Sistema Inteligente de Estacionamiento Medido Urbano.

Su propósito es establecer los criterios de cálculo, registro y regularización de los importes asociados a una sesión de estacionamiento, así como las reglas aplicables ante situaciones de saldo insuficiente, finalización de sesión e inicio del Protocolo de Acarreo.

Este modelo constituye la base conceptual para los procesos de Gestión de Cobros, Fin de Sesión y Protocolo de Acarreo.

---

## 2. Conceptos del Modelo

### Sesión de Estacionamiento

Representa el período comprendido entre el inicio y la finalización de una sesión activa de estacionamiento asociada a un vehículo.

---

### Intervalo de Cobro

Unidad temporal mínima utilizada por el sistema para efectuar los cobros periódicos del estacionamiento.

Todos los cálculos de cobro se realizan sobre intervalos discretos de duración fija.

---

### Timestamp de Inicio de Intervalo

Marca temporal registrada al comenzar un nuevo intervalo de estacionamiento.

---

### Timestamp de Fin de Intervalo

Marca temporal registrada al finalizar un intervalo de estacionamiento.

Su emisión habilita el cálculo del importe correspondiente al intervalo finalizado.

---

### Ventana de Regularización

Período de tiempo otorgado al Usuario cuando se detecta una situación de saldo insuficiente.

Durante esta ventana el Usuario puede efectuar una recarga de saldo para regularizar la deuda acumulada.

La duración de la ventana de regularización es equivalente a un intervalo de estacionamiento.

---

### Intervalo de Espera

Intervalo transcurrido durante una Ventana de Regularización en el cual el Usuario no dispone de saldo suficiente para afrontar los cargos correspondientes.

Los intervalos de espera generan deuda acumulada.

---

### Importe de Espera

Monto acumulado generado por los intervalos de espera pendientes de regularización.

Su valor depende de:

- cantidad de intervalos de espera acumulados;
- tarifa vigente asociada al estado del vehículo.

---

### Monto Final

Importe total que debe ser cobrado por el Sistema en un determinado momento.

Puede estar compuesto por:

- tarifa de intervalo regular;
- importe de espera acumulado.

---

## 3. Modelo de Cobro por Intervalos

El Sistema debe operar mediante un esquema de cobro periódico basado en intervalos temporales.

Al inicio de cada intervalo:

- se registra un timestamp de inicio.

Al finalizar cada intervalo:

- se registra un timestamp de fin;
- se calcula el importe correspondiente al intervalo;
- se verifica la disponibilidad de saldo.

Si existe saldo suficiente:

- el Sistema efectúa el débito correspondiente;
- se inicia un nuevo intervalo.

El ciclo se repite mientras la sesión permanezca activa.

---

## 4. Gestión de Saldo Insuficiente

Cuando el Sistema detecta que el Usuario no posee saldo suficiente para afrontar el cobro correspondiente:

- se inicia una Ventana de Regularización;
- se solicita una recarga de saldo al Usuario.

Durante la ventana de regularización:

- la sesión continúa activa;
- el Sistema monitorea la situación de saldo.

Si el Usuario regulariza su situación:

- el Sistema calcula la deuda acumulada;
- efectúa el cobro correspondiente;
- reinicia el ciclo normal de cobro.

Si el Usuario no regulariza su situación:

- el Sistema aplica el mecanismo de Escalamiento Sancionatorio definido por las reglas de negocio correspondientes.

---

## 5. Intervalos de Espera

Cada ventana de regularización vencida sin recarga genera un nuevo intervalo de espera.

Los intervalos de espera poseen las siguientes características:

- deben registrarse para fines de trazabilidad;
- generan deuda acumulada;
- participan del cálculo del Monto Final;
- pueden originar escalamiento sancionatorio.

La cantidad de intervalos de espera acumulados debe conservarse durante toda la sesión.

---

## 6. Cálculo del Monto Final

### Situación Normal

Cuando no existen intervalos de espera pendientes:

```text
Monto Final = Tarifa de Intervalo Regular
```

### Situación con Intervalos de Espera

Cuando existen intervalos de espera acumulados:

```text
Monto Final =
Tarifa de Intervalo Regular +
Importe de Espera
```

Donde:

```text
Importe de Espera =
Cantidad de Intervalos de Espera ×
Tarifa correspondiente al estado sancionatotiro vigente de la sesión.
```

El Sistema debe verificar que el saldo disponible resulte suficiente para cubrir el Monto Final calculado.

---

## 7. Finalización de Sesión

Cuando el Usuario solicita finalizar una sesión:

- el Sistema registra el timestamp correspondiente a la solicitud de cierre;
- se inicia el proceso de validación definido por RF-008.

Si la sesión puede finalizar normalmente:

- se calcula el tiempo consumido dentro del último intervalo;
- se calcula el importe proporcional correspondiente;
- se registra la finalización de la sesión.

El cálculo del último intervalo debe realizarse independientemente de los cobros periódicos ya efectuados.

---

## 8. Integración con Protocolo de Acarreo

Cuando un vehículo alcanza el estado Acarreo:

- la sesión no puede finalizar mediante el flujo normal;
- debe iniciarse el Protocolo de Acarreo.

Durante dicho protocolo:

- se calcula el saldo pendiente correspondiente al último intervalo;
- se determina el monto de acarreo aplicable;
- se aplica la multa correspondiente;
- se confecciona la infracción resultante.

La infracción queda asociada a la patente del vehículo y pendiente de pago.

---

## 9. Ejemplos de Cálculo

### Ejemplo 1 – Cobro Normal

```text
Tarifa por intervalo = $100

Monto Final = $100
```

---

### Ejemplo 2 – Regularización con un intervalo de espera

```text
Tarifa por intervalo = $100

Intervalos de espera = 1

Importe Espera = $100

Monto Final =
$100 + $100

Monto Final = $200
```

---

### Ejemplo 3 – Regularización con tres intervalos de espera

```text
Tarifa por intervalo = $100

Intervalos de espera = 3

Importe Espera = $300

Monto Final =
$100 + $300

Monto Final = $400
```

---

## 10. Decisión de Modelado – Estados Sancionatorios

### Objetivo

Establecer la pertenencia y el alcance de los estados sancionatorios utilizados por el Sistema Inteligente de Estacionamiento Medido Urbano.

---

### Definición

Los estados sancionatorios forman parte del ciclo de vida de una Sesión de Estacionamiento.

No constituyen un atributo persistente del Vehículo.

Cada nueva sesión inicia en estado **Activo**, independientemente de las sanciones o infracciones registradas en sesiones anteriores.

---

### Estados Sancionatorios

Durante una sesión activa pueden producirse las siguientes transiciones:

```text
Activo
   ↓
Infracción
   ↓
Penalización
   ↓
Acarreo
```

Las transiciones se encuentran definidas por:

* RN-001 – Escalamiento Sancionatorio
* RN-005 – Escalamiento por Falta de Regularización de Saldo

---

### Alcance Temporal

El estado sancionatorio existe únicamente mientras la sesión permanece activa.

Al finalizar la sesión:

* el estado sancionatorio deja de existir;
* no se transfiere a futuras sesiones;
* no modifica el estado inicial de un nuevo estacionamiento.

Por lo tanto, toda nueva sesión comienza en estado **Activo**.

---

### Relación con las Infracciones

Las infracciones generadas durante una sesión pueden registrarse de forma permanente y asociarse a la patente del vehículo.

Dichos registros constituyen historial administrativo y permiten:

* consultas posteriores;
* auditoría;
* trazabilidad;
* futuras integraciones institucionales.

Sin embargo, ese historial no participa del cálculo del estado inicial de una nueva sesión.

---

### Consecuencia para el Modelo de Dominio

Se distinguen dos conceptos independientes:

#### Estado Operativo de la Sesión

Describe la situación actual de una sesión de estacionamiento.

Ejemplos:

* Activa
* En Inspección
* Finalizada

#### Historial de Infracciones

Describe registros persistentes asociados a una patente.

Ejemplos:

* infracciones pendientes;
* infracciones abonadas;
* infracciones históricas.

El historial constituye información de consulta y persistencia, mientras que el estado sancionatorio pertenece exclusivamente al ciclo de vida de la sesión.


## 11. Relacionados

### Requerimientos Funcionales

- RF-008 – Solicitud de Cierre de Sesión
- RF-009 – Fin de Sesión
- RF-010 – Protocolo de Acarreo
- RF-011 – Gestión de Cobros

---

### Reglas de Negocio

- RN-001 – Escalamiento Sancionatorio
- RN-002 – Acarreo impide finalización directa
- RN-005 – Escalamiento por Falta de Regularización de Saldo

---

### Casos de Uso

- UC-008 – Solicitar Cierre de Sesión
- UC-009 – Finalizar Sesión
- UC-010 – Ejecutar Protocolo de Acarreo
- UC-011 – Gestionar Cobros

---

### Diagramas

- DG-008 – Flujo de Cierre de Sesión
- DG-009 – Fin de Sesión
- DG-010 – Protocolo de Acarreo
- DG-011 – Gestión de Cobros
- FSM-Vehículos