from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from domain.exceptions import BusinessRuleViolationError
from domain.shared.money import Money
from domain.usuarios.enums.estado_usuario import EstadoUsuario
from domain.usuarios.value_objects.email import Email


@dataclass(slots=True)
class Usuario:
    """
    Cuenta registrada en el sistema (ARQ-007).
    Agregado raíz del módulo de usuarios.
    """

    id: UUID
    nombre: str
    apellido: str
    email: Email
    telefono: str
    saldo: Money
    fecha_registro: datetime
    estado: EstadoUsuario = EstadoUsuario.ACTIVO
    _version: int = field(default=0, repr=False)

    @property
    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def acreditar_saldo(self, monto: Money) -> None:
        """RF-005: incrementa el saldo disponible."""
        self.saldo = self.saldo + monto

    def debitar(self, monto: Money) -> None:
        """Descuenta saldo si hay fondos suficientes (DA-001)."""
        if not self.saldo.is_sufficient_for(monto):
            raise BusinessRuleViolationError("Saldo insuficiente.")
        self.saldo = self.saldo - monto
