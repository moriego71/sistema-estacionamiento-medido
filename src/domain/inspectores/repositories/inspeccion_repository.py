from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from domain.inspectores.entities.inspeccion import Inspeccion


class InspeccionRepository(ABC):
    """Puerto de persistencia para Inspeccion."""

    @abstractmethod
    def get_by_id(self, inspeccion_id: UUID) -> Inspeccion | None:
        ...

    @abstractmethod
    def list_by_sesion(self, sesion_id: UUID) -> list[Inspeccion]:
        ...

    @abstractmethod
    def save(self, inspeccion: Inspeccion) -> None:
        ...
