from __future__ import annotations

from dataclasses import dataclass

from domain.exceptions import InvalidValueError


@dataclass(frozen=True, slots=True)
class Ubicacion:
    """Ubicación declarada del vehículo al iniciar sesión (RF-007)."""

    descripcion: str

    def __post_init__(self) -> None:
        texto = self.descripcion.strip()
        if not texto:
            raise InvalidValueError("La ubicación no puede estar vacía.")
        object.__setattr__(self, "descripcion", texto)
