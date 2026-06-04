from enum import StrEnum


class EstadoSancionatorio(StrEnum):
    """
    Estado sancionatorio del vehículo (FSM, RN-001).
    Conservado durante inspección según RN-003.
    """

    ACTIVO = "activo"
    INFRACCION = "infraccion"
    PENALIZACION = "penalizacion"
    ACARREO = "acarreo"
