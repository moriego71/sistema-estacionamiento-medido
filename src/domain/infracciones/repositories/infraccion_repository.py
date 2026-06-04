from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from domain.infracciones.entities.infraccion import Infraccion
from domain.vehiculos.value_objects.patente import Patente


class InfraccionRepository(ABC):
    """Puerto de persistencia para Infraccion."""

    @abstractmethod
    def get_by_id(self, infraccion_id: UUID) -> Infraccion | None:
        ...

    @abstractmethod
    def list_by_patente(self, patente: Patente) -> list[Infraccion]:
        ...

    @abstractmethod
    def save(self, infraccion: Infraccion) -> None:
        ...
