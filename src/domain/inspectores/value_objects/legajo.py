from __future__ import annotations

from dataclasses import dataclass

from domain.exceptions import InvalidValueError


@dataclass(frozen=True, slots=True)
class Legajo:
    """Identificador único del inspector (RF-003)."""

    value: str

    def __post_init__(self) -> None:
        texto = self.value.strip()
        if not texto:
            raise InvalidValueError("El legajo no puede estar vacío.")
        object.__setattr__(self, "value", texto)
