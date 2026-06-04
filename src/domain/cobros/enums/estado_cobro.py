from enum import StrEnum


class EstadoCobro(StrEnum):
    """Estado de una operación de cobro registrada."""

    PENDIENTE = "pendiente"
    DEBITADO = "debitado"
    CANCELADO = "cancelado"
