from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from domain.vehiculos.entities.vehiculo import Vehiculo
from domain.vehiculos.value_objects.patente import Patente


class VehiculoRepository(ABC):
    """Puerto de persistencia para Vehiculo."""

    @abstractmethod
    def get_by_patente(self, patente: Patente) -> Vehiculo | None:
        ...

    @abstractmethod
    def list_by_usuario(self, usuario_id: UUID) -> list[Vehiculo]:
        ...

    @abstractmethod
    def save(self, vehiculo: Vehiculo) -> None:
        ...

    @abstractmethod
    def exists_patente(self, patente: Patente) -> bool:
        ...
