from __future__ import annotations

from dataclasses import dataclass

from domain.exceptions import InvalidValueError
from domain.shared.money import Money


@dataclass(frozen=True, slots=True)
class MontoFinal:
    """
    Importe total a cobrar (DA-001 §6).
    Monto Final = tarifa intervalo regular + importe de espera (si aplica).
    """

    tarifa_intervalo: Money
    importe_espera: Money = Money.zero()

    @property
    def total(self) -> Money:
        return self.tarifa_intervalo + self.importe_espera

    @classmethod
    def calcular(
        cls,
        tarifa_intervalo: Money,
        cantidad_intervalos_espera: int,
        tarifa_por_intervalo_espera: Money,
    ) -> MontoFinal:
        if cantidad_intervalos_espera < 0:
            raise InvalidValueError(
                "La cantidad de intervalos de espera no puede ser negativa."
            )
        importe_espera = tarifa_por_intervalo_espera * cantidad_intervalos_espera
        return cls(
            tarifa_intervalo=tarifa_intervalo,
            importe_espera=importe_espera,
        )
