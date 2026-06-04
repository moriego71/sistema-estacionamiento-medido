"""Excepciones del dominio."""


class DomainError(Exception):
    """Error base del dominio."""


class InvalidValueError(DomainError):
    """Valor inválido para un objeto de valor o atributo de entidad."""


class EntityNotFoundError(DomainError):
    """Entidad solicitada inexistente."""


class BusinessRuleViolationError(DomainError):
    """Violación de una regla de negocio."""
