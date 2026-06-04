from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from domain.exceptions import InvalidValueError


@dataclass(frozen=True, slots=True)
class Money:
    """Importe monetario del dominio (saldo, cobros, multas)."""

    amount: Decimal

    def __post_init__(self) -> None:
        if self.amount < Decimal("0"):
            raise InvalidValueError("El importe no puede ser negativo.")

    @classmethod
    def zero(cls) -> Money:
        return cls(Decimal("0"))

    @classmethod
    def from_float(cls, value: float) -> Money:
        return cls(Decimal(str(value)))

    def __add__(self, other: Money) -> Money:
        return Money(self.amount + other.amount)

    def __sub__(self, other: Money) -> Money:
        result = self.amount - other.amount
        if result < Decimal("0"):
            raise InvalidValueError("El saldo resultante no puede ser negativo.")
        return Money(result)

    def __ge__(self, other: Money) -> bool:
        return self.amount >= other.amount

    def __gt__(self, other: Money) -> bool:
        return self.amount > other.amount

    def is_sufficient_for(self, required: Money) -> bool:
        return self >= required

    def __mul__(self, factor: int) -> Money:
        if factor < 0:
            raise InvalidValueError("El factor no puede ser negativo.")
        return Money(self.amount * factor)
