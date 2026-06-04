from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from domain.acarreo.enums.resultado_acarreo import ResultadoAcarreo
from domain.sesiones.value_objects.ubicacion import Ubicacion
from domain.vehiculos.value_objects.patente import Patente


@dataclass(slots=True)
class SolicitudAcarreo:
    """
    Intervención solicitada al Departamento de Acarreo (ARQ-007, RF-010).
    """

    id: UUID
    patente: Patente
    ubicacion: Ubicacion
    sesion_id: UUID
    fecha_hora_solicitud: datetime
    resultado: ResultadoAcarreo = ResultadoAcarreo.PENDIENTE
    fecha_hora_respuesta: datetime | None = None

    def registrar_respuesta(
        self,
        resultado: ResultadoAcarreo,
        momento: datetime,
    ) -> None:
        self.resultado = resultado
        self.fecha_hora_respuesta = momento
