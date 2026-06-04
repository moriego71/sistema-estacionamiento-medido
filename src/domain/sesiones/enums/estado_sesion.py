from enum import StrEnum


class EstadoSesion(StrEnum):
    """Estados operativos de una sesión (FSM – Vehículos y Sesiones)."""

    ACTIVO = "activo"
    EN_INSPECCION = "en_inspeccion"
    INFRACCION = "infraccion"
    PENALIZACION = "penalizacion"
    ACARREO = "acarreo"
    FINALIZADO = "finalizado"
