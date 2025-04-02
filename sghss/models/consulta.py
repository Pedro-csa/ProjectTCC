from . import db
from datetime import datetime

class Consulta(db.Model):
    __tablename__ = 'Consulta'
    
    id_consulta = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('Paciente.id_paciente'), nullable=False)
    id_medico = db.Column(db.Integer, db.ForeignKey('Medico.id_medico'), nullable=False)
    data_consulta = db.Column(db.DateTime, nullable=False)
    descricao = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=False, default='Agendada')
    
    # Relacionamento com Prontuario (1:1)
    prontuario = db.relationship('Prontuario', backref='consulta', uselist=False)