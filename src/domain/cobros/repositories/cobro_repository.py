from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from domain.cobros.entities.cobro import Cobro


class CobroRepository(ABC):
    """Puerto de persistencia para Cobro."""

    @abstractmethod
    def get_by_id(self, cobro_id: UUID) -> Cobro | None:
        ...

    @abstractmethod
    def list_by_sesion(self, sesion_id: UUID) -> list[Cobro]:
        ...

    @abstractmethod
    def save(self, cobro: Cobro) -> None:
        ...
