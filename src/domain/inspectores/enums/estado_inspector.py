from enum import StrEnum


class EstadoInspector(StrEnum):
    """Estado de la cuenta del inspector (RF-003)."""

    ACTIVO = "activo"
    INACTIVO = "inactivo"
