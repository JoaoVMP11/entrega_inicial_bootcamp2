import pytest
from app import create_app
from app.extensions import db

# tests/conftest.py

@pytest.fixture
def app():
    # Este é o "presente" que a create_app agora aceita receber
    configs_de_teste = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "SECRET_KEY": "chave-de-teste"
    }
    
    # Agora a chamada abaixo não vai mais dar TypeError
    app = create_app(configs_de_teste)
    
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    # Cria um "cliente falso" para simular o navegador
    return app.test_client()