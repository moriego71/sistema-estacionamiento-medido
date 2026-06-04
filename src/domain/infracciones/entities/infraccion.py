from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.infracciones.enums.estado_pago_infraccion import EstadoPagoInfraccion
from domain.shared.money import Money
from domain.vehiculos.value_objects.patente import Patente


@dataclass(slots=True)
class Infraccion:
    """
    Sanción administrativa asociada a un vehículo (ARQ-007, RF-010).
    """

    id: UUID
    patente: Patente
    fecha_generacion: datetime
    importe_intervalos: Money
    importe_multa: Money
    importe_acarreo: Money
    sesion_id: UUID | None = None
    estado_pago: EstadoPagoInfraccion = EstadoPagoInfraccion.PENDIENTE

    @property
    def importe_total(self) -> Money:
        return self.importe_intervalos + self.importe_multa + self.importe_acarreo
