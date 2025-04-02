from . import db
from datetime import datetime

class Paciente(db.Model):
    __tablename__ = 'Paciente'
    
    id_paciente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    endereco = db.Column(db.String(255))
    telefone = db.Column(db.String(15))
    email = db.Column(db.String(100), unique=True)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    consultas = db.relationship('Consulta', backref='paciente', lazy=True)
    prontuarios = db.relationship('Prontuario', backref='paciente', lazy=True)