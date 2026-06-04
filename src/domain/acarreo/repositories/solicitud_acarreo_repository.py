from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from domain.acarreo.entities.solicitud_acarreo import SolicitudAcarreo
from domain.vehiculos.value_objects.patente import Patente


class SolicitudAcarreoRepository(ABC):
    """Puerto de persistencia para SolicitudAcarreo."""

    @abstractmethod
    def get_by_id(self, solicitud_id: UUID) -> SolicitudAcarreo | None:
        ...

    @abstractmethod
    def get_pendiente_by_patente(self, patente: Patente) -> SolicitudAcarreo | None:
        ...

    @abstractmethod
    def save(self, solicitud: SolicitudAcarreo) -> None:
        ...
