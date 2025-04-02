from flask import Blueprint, request, jsonify
from flask_login import login_required
from sghss.models import db, Paciente

paciente_bp = Blueprint('paciente', __name__)

# Rota para listar pacientes (GET)
@paciente_bp.route('/pacientes', methods=['GET'])
@login_required
def listar_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([{
        'id': p.id_paciente,
        'nome': p.nome
    } for p in pacientes])

# Rota para criar paciente (POST)
@paciente_bp.route('/pacientes', methods=['POST'])
@login_required
def criar_paciente():
    data = request.get_json()
    # Sua lógica de criação aqui
    return jsonify({"message": "Paciente criado"}), 201