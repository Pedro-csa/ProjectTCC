from flask import Blueprint, request, jsonify
from models.consulta import Consulta
from . import db
from datetime import datetime
from flask_login import login_required

consulta_bp = Blueprint('consulta', __name__)

@consulta_bp.route('/consultas', methods=['POST'])
@login_required
def add_consulta():
    data = request.get_json()
    data_consulta = datetime.strptime(data['data_consulta'], '%Y-%m-%d %H:%M:%S')
    
    # Verifica conflito de horário
    conflito = Consulta.query.filter(
        Consulta.id_medico == data['id_medico'],
        Consulta.data_consulta == data_consulta
    ).first()
    if conflito:
        return jsonify({'error': 'Médico já possui consulta neste horário'}), 400
    
    nova_consulta = Consulta(
        id_paciente=data['id_paciente'],
        id_medico=data['id_medico'],
        data_consulta=data_consulta
    )
    db.session.add(nova_consulta)
    db.session.commit()
    return jsonify({'id': nova_consulta.id_consulta}), 201