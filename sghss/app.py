from flask import Flask
from sghss.routes.paciente_routes import paciente_bp
from sghss.routes.usuario_routes import usuario_bp

app = Flask(__name__)

# Registre os blueprints com prefixos
app.register_blueprint(paciente_bp, url_prefix='/api')
app.register_blueprint(usuario_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)