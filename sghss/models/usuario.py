from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = 'Usuario'
    
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    tipo_usuario = db.Column(db.String(20), nullable=False)  # Admin, Médico, Recepcionista
    
    # Métodos para Flask-Login
    def set_password(self, senha):
        self.senha_hash = generate_password_hash(senha)
    
    def check_password(self, senha):
        return check_password_hash(self.senha_hash, senha)