from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Prontuario(db.Model):
    __tablename__ = 'Prontuario'
    
    id_prontuario = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('Paciente.id_paciente'), nullable=False)
    id_medico = db.Column(db.Integer, db.ForeignKey('Medico.id_medico'), nullable=False)
    data_registro = db.Column(db.DateTime, server_default=db.func.now())
    diagnostico = db.Column(db.Text)
    prescricao = db.Column(db.Text)