from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.exceptions import BusinessRuleViolationError
from domain.vehiculos.enums.estado_sancionatorio import EstadoSancionatorio
from domain.vehiculos.value_objects.patente import Patente


@dataclass(slots=True)
class Vehiculo:
    """
    Vehículo habilitado asociado a un usuario (ARQ-007, RF-002).
    """

    patente: Patente
    usuario_id: UUID
    marca: str
    modelo: str
    color: str
    estado_sancionatorio: EstadoSancionatorio
    fecha_registro: datetime
    activo: bool = True

    def escalar_sancion(self) -> None:
        """RN-001: Activo → Infracción → Penalización → Acarreo."""
        transiciones = {
            EstadoSancionatorio.ACTIVO: EstadoSancionatorio.INFRACCION,
            EstadoSancionatorio.INFRACCION: EstadoSancionatorio.PENALIZACION,
            EstadoSancionatorio.PENALIZACION: EstadoSancionatorio.ACARREO,
        }
        siguiente = transiciones.get(self.estado_sancionatorio)
        if siguiente is None:
            raise BusinessRuleViolationError(
                "No existe escalamiento desde el estado actual."
            )
        self.estado_sancionatorio = siguiente

    @property
    def en_acarreo(self) -> bool:
        return self.estado_sancionatorio == EstadoSancionatorio.ACARREO
