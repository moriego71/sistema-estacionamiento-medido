from enum import StrEnum


class EstadoEntrega(StrEnum):
    """Estado de entrega de una notificación (ARQ-007)."""

    PENDIENTE = "pendiente"
    ENVIADA = "enviada"
    FALLIDA = "fallida"
