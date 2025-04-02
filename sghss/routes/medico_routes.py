from flask import Blueprint, request, jsonify
from models.medico import Medico, db

medico_bp = Blueprint('medico', __name__)

@medico_bp.route('/medicos', methods=['GET'])
def get_medicos():
    medicos = Medico.query.all()
    return jsonify([{'id': m.id_medico, 'nome': m.nome, 'crm': m.crm} for m in medicos])

@medico_bp.route('/medicos/<int:id_medico>', methods=['GET'])
def get_medico(id_medico):
    medico = Medico.query.get(id_medico)
    if medico is None:
        return jsonify({'error': 'Médico não encontrado'}), 404
    return jsonify({'id': medico.id_medico, 'nome': medico.nome, 'crm': medico.crm})

@medico_bp.route('/medicos/<int:id_medico>', methods=['PUT'])
def update_medico(id_medico):
    medico = Medico.query.get(id_medico)
    if medico is None:
        return jsonify({'error': 'Médico não encontrado'}), 404
    data = request.get_json()
    medico.nome = data.get('nome', medico.nome)
    medico.crm = data.get('crm', medico.crm)
    medico.especialidade = data.get('especialidade', medico.especialidade)
    medico.telefone = data.get('telefone', medico.telefone)
    medico.email = data.get('email', medico.email)
    medico.data_contratacao = data.get('data_contratacao', medico.data_contratacao)
    db.session.commit()
    return jsonify({'id': medico.id_medico, 'nome': medico.nome, 'crm': medico.crm})

@medico_bp.route('/medicos/<int:id_medico>', methods=['DELETE'])
def delete_medico(id_medico):
    medico = Medico.query.get(id_medico)
    if medico is None:
        return jsonify({'error': 'Médico não encontrado'}), 404
    db.session.delete(medico)
    db.session.commit()
    return jsonify({'message': 'Médico excluído com sucesso'})