from enum import StrEnum


class TipoCobro(StrEnum):
    """Tipos conceptuales de cobro (ARQ-007, DA-001)."""

    INTERVALO_ESTACIONAMIENTO = "intervalo_estacionamiento"
    INTERVALO_ESPERA = "intervalo_espera"
    COBRO_FINAL_SESION = "cobro_final_sesion"
