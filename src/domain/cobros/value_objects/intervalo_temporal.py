from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from domain.exceptions import InvalidValueError


@dataclass(frozen=True, slots=True)
class IntervaloTemporal:
    """
    Intervalo de cobro con timestamps de inicio y fin (DA-001).
    La ventana de regularización equivale a un intervalo.
    """

    inicio: datetime
    fin: datetime | None = None

    def __post_init__(self) -> None:
        if self.fin is not None and self.fin < self.inicio:
            raise InvalidValueError(
                "El fin del intervalo no puede ser anterior al inicio."
            )

    def cerrar(self, fin: datetime) -> IntervaloTemporal:
        if fin < self.inicio:
            raise InvalidValueError(
                "El fin del intervalo no puede ser anterior al inicio."
            )
        return IntervaloTemporal(inicio=self.inicio, fin=fin)
