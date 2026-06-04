from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.inspectores.enums.estado_inspector import EstadoInspector
from domain.inspectores.value_objects.legajo import Legajo
from domain.usuarios.value_objects.email import Email


@dataclass(slots=True)
class Inspector:
    """Inspector habilitado para operar en el sistema (RF-003)."""

    id: UUID
    nombre: str
    apellido: str
    email: Email
    legajo: Legajo
    fecha_registro: datetime
    estado: EstadoInspector = EstadoInspector.ACTIVO
