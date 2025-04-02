from . import db  # Importa a instância do db do arquivo __init__.py

class Medico(db.Model):
    __tablename__ = 'Medico'
    
    id_medico = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    crm = db.Column(db.String(20), unique=True, nullable=False)
    especialidade = db.Column(db.String(100))
    telefone = db.Column(db.String(15))
    email = db.Column(db.String(100), unique=True)
    data_contratacao = db.Column(db.Date)