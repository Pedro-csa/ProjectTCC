from flask import Blueprint, request, jsonify, flash
from flask_login import login_user, logout_user, current_user, login_required
from sghss.models.usuario import Usuario
from sghss.models import db  # Certifique-se de que o modelo Usuario está definido corretamente
from werkzeug.security import generate_password_hash, check_password_hash

usuario_bp = Blueprint('usuario', __name__)

# Rota para registro de usuário
@usuario_bp.route('/usuarios', methods=['POST'])
def register():
    data = request.get_json()
    if 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email e senha são obrigatórios.'}), 400

    # Verifica se o usuário já existe
    if Usuario.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Usuário já existe.'}), 400

    # Cria um novo usuário
    novo_usuario = Usuario(
        email=data['email'],
        password=generate_password_hash(data['password'])  # Armazena a senha de forma segura
    )
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'message': 'Usuário registrado com sucesso!'}), 201

# Rota para login de usuário
@usuario_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email e senha são obrigatórios.'}), 400

    usuario = Usuario.query.filter_by(email=data['email']).first()
    if usuario and check_password_hash(usuario.password, data['password']):
        login_user(usuario)
        return jsonify({'message': 'Login realizado com sucesso!'}), 200
    return jsonify({'error': 'Email ou senha inválidos.'}), 401

# Rota para logout de usuário
@usuario_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout realizado com sucesso!'}), 200

# Rota para visualizar perfil do usuário
@usuario_bp.route('/perfil', methods=['GET'])
@login_required
def perfil():
    return jsonify({'email': current_user.email}), 200