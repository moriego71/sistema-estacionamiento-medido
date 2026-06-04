from enum import StrEnum


class EstadoPagoInfraccion(StrEnum):
    """Estado de pago de una infracción (ARQ-007)."""

    PENDIENTE = "pendiente"
    PAGADA = "pagada"
