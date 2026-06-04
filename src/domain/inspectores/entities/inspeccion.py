from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.inspectores.enums.resultado_inspeccion import ResultadoInspeccion
from domain.vehiculos.value_objects.patente import Patente


@dataclass(slots=True)
class Inspeccion:
    """Verificación realizada por un inspector (ARQ-007, RF-008)."""

    id: UUID
    patente: Patente
    inspector_id: UUID
    fecha_hora: datetime
    resultado: ResultadoInspeccion
    sesion_id: UUID | None = None
    observaciones: str = ""
