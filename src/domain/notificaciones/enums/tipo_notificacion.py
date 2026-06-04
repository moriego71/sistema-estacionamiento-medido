from enum import StrEnum


class TipoNotificacion(StrEnum):
    """Tipos de comunicación emitida por el sistema."""

    COBRO_REALIZADO = "cobro_realizado"
    SALDO_INSUFICIENTE = "saldo_insuficiente"
    SOLICITUD_RECARGA = "solicitud_recarga"
    ESCALAMIENTO_SANCIONATORIO = "escalamiento_sancionatorio"
    INFRACCION_GENERADA = "infraccion_generada"
    SESION_FINALIZADA = "sesion_finalizada"
    SOLICITUD_INSPECCION = "solicitud_inspeccion"
