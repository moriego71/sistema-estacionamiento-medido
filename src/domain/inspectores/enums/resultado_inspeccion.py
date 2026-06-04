from enum import StrEnum


class ResultadoInspeccion(StrEnum):
    """Resultado de una verificación de inspector (FSM)."""

    OK = "ok"
    FALLO = "fallo"
