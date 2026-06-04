from enum import StrEnum


class ResultadoAcarreo(StrEnum):
    """
    Resultado operativo del Departamento de Acarreo (DA-002 SO-001).
    """

    VEHICULO_ENCONTRADO = "vehiculo_encontrado"
    VEHICULO_NO_ENCONTRADO = "vehiculo_no_encontrado"
    PENDIENTE = "pendiente"
