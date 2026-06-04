from enum import StrEnum


class EstadoUsuario(StrEnum):
    """Estado de la cuenta de usuario."""

    ACTIVO = "activo"
    INACTIVO = "inactivo"
