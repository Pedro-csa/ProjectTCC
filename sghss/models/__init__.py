from .paciente import Paciente
from . import db  # Importe outros modelos aqui

__all__ = ['db', 'Paciente']  # Torne os modelos acessíveis