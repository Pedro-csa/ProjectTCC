import pytest
import sys
import os
from os.path import dirname, join

# Adiciona o diretório raiz ao PATH
sys.path.insert(0, dirname(dirname(__file__)))

from sghss.app import app, db
from sghss.models.paciente import Paciente

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_add_paciente(client):
    response = client.post('/pacientes', json={
        'nome': 'Maria',
        'cpf': '12345678901',
        'data_nascimento': '1990-01-01',
        'email': 'maria@teste.com'
    })
    assert response.status_code == 201
    assert Paciente.query.count() == 1