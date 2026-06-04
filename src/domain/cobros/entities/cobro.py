from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.cobros.enums.estado_cobro import EstadoCobro
from domain.cobros.enums.tipo_cobro import TipoCobro
from domain.cobros.value_objects.intervalo_temporal import IntervaloTemporal
from domain.shared.money import Money


@dataclass(slots=True)
class Cobro:
    """
    Operación económica asociada a una sesión (ARQ-007, RF-011).
    """

    id: UUID
    sesion_id: UUID
    intervalo: IntervaloTemporal
    importe: Money
    tipo: TipoCobro
    timestamp_registro: datetime
    estado: EstadoCobro = EstadoCobro.PENDIENTE

    def marcar_debitado(self) -> None:
        self.estado = EstadoCobro.DEBITADO
