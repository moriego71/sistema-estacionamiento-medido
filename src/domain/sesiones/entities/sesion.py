from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from domain.exceptions import BusinessRuleViolationError
from domain.sesiones.enums.estado_sesion import EstadoSesion
from domain.sesiones.value_objects.ubicacion import Ubicacion
from domain.vehiculos.enums.estado_sancionatorio import EstadoSancionatorio
from domain.vehiculos.value_objects.patente import Patente


@dataclass(slots=True)
class Sesion:
    """
    Período de estacionamiento medido (ARQ-007, RF-007).
    Agregado raíz del módulo de sesiones.
    """

    id: UUID
    patente: Patente
    ubicacion: Ubicacion
    time_start: datetime
    estado: EstadoSesion = EstadoSesion.ACTIVO
    time_stop: datetime | None = None
    estado_sancionatorio_previo: EstadoSancionatorio | None = None
    intervalos_espera_acumulados: int = 0
    solicitud_cierre_pendiente: bool = False
    _cobros_ids: list[UUID] = field(default_factory=list, repr=False)

    @property
    def activa(self) -> bool:
        return self.estado not in (
            EstadoSesion.FINALIZADO,
            EstadoSesion.ACARREO,
        )

    @property
    def en_acarreo(self) -> bool:
        return self.estado == EstadoSesion.ACARREO

    def solicitar_cierre(self, momento: datetime) -> None:
        """RF-008: registra time_stop e inicia validación."""
        if self.en_acarreo:
            raise BusinessRuleViolationError(
                "RN-002: en acarreo no se admite cierre directo por el usuario."
            )
        self.time_stop = momento
        self.solicitud_cierre_pendiente = True
        self.estado = EstadoSesion.EN_INSPECCION

    def registrar_estado_previo(self, estado: EstadoSancionatorio) -> None:
        """RN-003: conserva estado previo al entrar en inspección."""
        self.estado_sancionatorio_previo = estado

    def finalizar(self, momento: datetime) -> None:
        """RF-009: cierre definitivo de la sesión."""
        self.time_stop = momento
        self.estado = EstadoSesion.FINALIZADO
        self.solicitud_cierre_pendiente = False

    def incrementar_intervalos_espera(self) -> None:
        """DA-001: acumula intervalos de espera por ventana vencida."""
        self.intervalos_espera_acumulados += 1
