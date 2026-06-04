from __future__ import annotations

from abc import ABC, abstractmethod
from uuid import UUID

from domain.usuarios.entities.usuario import Usuario
from domain.usuarios.value_objects.email import Email


class UsuarioRepository(ABC):
    """Puerto de persistencia para el agregado Usuario."""

    @abstractmethod
    def get_by_id(self, usuario_id: UUID) -> Usuario | None:
        ...

    @abstractmethod
    def get_by_email(self, email: Email) -> Usuario | None:
        ...

    @abstractmethod
    def save(self, usuario: Usuario) -> None:
        ...

    @abstractmethod
    def exists_by_email(self, email: Email) -> bool:
        ...
