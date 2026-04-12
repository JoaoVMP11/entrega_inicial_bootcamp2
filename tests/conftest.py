import pytest
from app import create_app
from app.extensions import db

@pytest.fixture
def app():
    # Cria a aplicação com as configurações normais
    app = create_app()
    
    # Sobrescreve as configurações para focar no ambiente de testes
    app.config.update({
        "TESTING": True,
        # Usa um banco SQLite na memória RAM, que é apagado no final do teste
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False, # Desativa segurança de formulários nos testes
    })

    # Cria o banco de dados temporário e injeta o contexto da aplicação
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    # Cria um "cliente falso" para simular o navegador
    return app.test_client()