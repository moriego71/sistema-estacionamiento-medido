from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.notificaciones.enums.estado_entrega import EstadoEntrega
from domain.notificaciones.enums.tipo_notificacion import TipoNotificacion


@dataclass(slots=True)
class Notificacion:
    """Comunicación emitida por el sistema (ARQ-007)."""

    id: UUID
    usuario_id: UUID
    fecha_hora: datetime
    tipo: TipoNotificacion
    mensaje: str
    estado_entrega: EstadoEntrega = EstadoEntrega.PENDIENTE

    def marcar_enviada(self) -> None:
        self.estado_entrega = EstadoEntrega.ENVIADA
