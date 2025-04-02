from flask import Blueprint, request, jsonify
from models.prontuario import Prontuario, db

prontuario_bp = Blueprint('prontuario', __name__)

# Endpoint para obter todos os prontuários
@prontuario_bp.route('/prontuarios', methods=['GET'])
def get_prontuarios():
    prontuarios = Prontuario.query.all()
    return jsonify([{'id': p.id_prontuario, 'descricao': p.descricao} for p in prontuarios])

# Endpoint para adicionar um novo prontuário
@prontuario_bp.route('/prontuarios', methods=['POST'])
def add_prontuario():
    data = request.get_json()
    novo_prontuario = Prontuario(
        descricao=data['descricao'],
        # Adicione outros campos conforme necessário
    )
    db.session.add(novo_prontuario)
    db.session.commit()
    return jsonify({'id': novo_prontuario.id_prontuario}), 201

# Endpoint para obter um prontuário específico
@prontuario_bp.route('/prontuarios/<int:id_prontuario>', methods=['GET'])
def get_prontuario(id_prontuario):
    prontuario = Prontuario.query.get(id_prontuario)
    if prontuario is None:
        return jsonify({'error': 'Prontuário não encontrado'}), 404
    return jsonify({'id': prontuario.id_prontuario, 'descricao': prontuario.descricao})

# Endpoint para atualizar um prontuário existente
@prontuario_bp.route('/prontuarios/<int:id_prontuario>', methods=['PUT'])
def update_prontuario(id_prontuario):
    prontuario = Prontuario.query.get(id_prontuario)
    if prontuario is None:
        return jsonify({'error': 'Prontuário não encontrado'}), 404
    data = request.get_json()
    prontuario.descricao = data.get('descricao', prontuario.descricao)
    # Atualize outros campos conforme necessário
    db.session.commit()
    return jsonify({'id': prontuario.id_prontuario, 'descricao': prontuario.descricao})

# Endpoint para excluir um prontuário
@prontuario_bp.route('/prontuarios/<int:id_prontuario>', methods=['DELETE'])
def delete_prontuario(id_prontuario):
    prontuario = Prontuario.query.get(id_prontuario)
    if prontuario is None:
        return jsonify({'error': 'Prontuário não encontrado'}), 404
    db.session.delete(prontuario)
    db.session.commit()
    return jsonify({'message': 'Prontuário excluído com sucesso'})