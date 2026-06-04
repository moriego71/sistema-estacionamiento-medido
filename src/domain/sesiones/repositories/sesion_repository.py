from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from domain.sesiones.entities.sesion import Sesion
from domain.vehiculos.value_objects.patente import Patente


class SesionRepository(ABC):
    """Puerto de persistencia para Sesion."""

    @abstractmethod
    def get_by_id(self, sesion_id: UUID) -> Sesion | None:
        ...

    @abstractmethod
    def get_activa_by_patente(self, patente: Patente) -> Sesion | None:
        ...

    @abstractmethod
    def save(self, sesion: Sesion) -> None:
        ...
