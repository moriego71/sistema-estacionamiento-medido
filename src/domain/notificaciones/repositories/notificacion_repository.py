from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from domain.notificaciones.entities.notificacion import Notificacion


class NotificacionRepository(ABC):
    """Puerto de persistencia para Notificacion."""

    @abstractmethod
    def get_by_id(self, notificacion_id: UUID) -> Notificacion | None:
        ...

    @abstractmethod
    def list_by_usuario(self, usuario_id: UUID) -> list[Notificacion]:
        ...

    @abstractmethod
    def save(self, notificacion: Notificacion) -> None:
        ...
