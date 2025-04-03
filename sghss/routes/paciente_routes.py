from flask import Blueprint, request, jsonify
from flask_login import login_required
from sghss.models import Paciente, db

paciente_bp = Blueprint('paciente', __name__)

# Rota GET (separada)
@paciente_bp.route('/', methods=['GET'])
def listar_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([p.to_dict() for p in pacientes])

# Rota POST (separada)
@paciente_bp.route('/', methods=['POST'])
@login_required
def criar_paciente():
    data = request.get_json()
    if current_user.tipo_usuario not in ['Admin', 'Recepcionista']:
        return jsonify({'error': 'Acesso negado'}), 403
    
    data = request.get_json()
    if not CPF().validate(data.get('cpf')):
        return jsonify({'error': 'CPF inválido'}), 400
    
    novo_paciente = Paciente(
        nome=data['nome'],
        cpf=data['cpf'],
        data_nascimento=data['data_nascimento'],
        email=data['email']
    )
    db.session.add(novo_paciente)
    db.session.commit()
    # Sua lógica de criação aqui
    return jsonify({"message": "Paciente criado"}), 201