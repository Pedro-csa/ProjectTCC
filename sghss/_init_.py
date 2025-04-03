from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Configurações OBRIGATÓRIAS
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importação EVITANDO import circular
    from .routes.paciente_routes import paciente_bp
    app.register_blueprint(paciente_bp, url_prefix='/api')

    return app  # ESSA LINHA É ESSENCIAL