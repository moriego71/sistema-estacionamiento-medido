from __future__ import annotations

import re
from dataclasses import dataclass

from domain.exceptions import InvalidValueError

_EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@dataclass(frozen=True, slots=True)
class Email:
    """Dirección de correo del usuario."""

    value: str

    def __post_init__(self) -> None:
        normalized = self.value.strip().lower()
        if not _EMAIL_PATTERN.match(normalized):
            raise InvalidValueError(f"Email inválido: {self.value!r}")
        object.__setattr__(self, "value", normalized)
