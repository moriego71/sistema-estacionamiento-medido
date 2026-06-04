from __future__ import annotations

import re
from dataclasses import dataclass

from domain.exceptions import InvalidValueError

# Formatos argentinos habituales: ABC123 o AB123CD (Mercosur)
_PATENTE_PATTERN = re.compile(
    r"^[A-Z]{2,3}\d{3}[A-Z]{0,2}$|^[A-Z]{2}\d{3}[A-Z]{2}$"
)


@dataclass(frozen=True, slots=True)
class Patente:
    """Identificador único del vehículo (RF-002)."""

    value: str

    def __post_init__(self) -> None:
        normalized = self.value.strip().upper().replace(" ", "").replace("-", "")
        if not _PATENTE_PATTERN.match(normalized):
            raise InvalidValueError(f"Patente inválida: {self.value!r}")
        object.__setattr__(self, "value", normalized)

    def __str__(self) -> str:
        return self.value
