from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from domain.inspectores.entities.inspector import Inspector
from domain.inspectores.value_objects.legajo import Legajo
from domain.usuarios.value_objects.email import Email


class InspectorRepository(ABC):
    """Puerto de persistencia para Inspector."""

    @abstractmethod
    def get_by_id(self, inspector_id: UUID) -> Inspector | None:
        ...

    @abstractmethod
    def get_by_legajo(self, legajo: Legajo) -> Inspector | None:
        ...

    @abstractmethod
    def get_by_email(self, email: Email) -> Inspector | None:
        ...

    @abstractmethod
    def save(self, inspector: Inspector) -> None:
        ...
