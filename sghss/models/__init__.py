from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importe todos os modelos aqui para que fiquem disponíveis
from .paciente import Paciente  # Adicione esta linha
from .usuario import Usuario    # E outros modelos que você tiver

__all__ = ['db', 'Paciente', 'Usuario']  # Torne os modelos explicitamente disponíveis