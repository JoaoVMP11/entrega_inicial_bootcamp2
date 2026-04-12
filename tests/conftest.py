import pytest
from app import create_app
from app.extensions import db

@pytest.fixture
def app():
    # Criamos um dicionário com as configurações de teste
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "SECRET_KEY": "test-key"
    }
    
    # Passamos esse dicionário para a sua factory
    # Certifique-se de que sua função create_app(config_mix=None) aceite um argumento
    app = create_app(test_config)
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    # Cria um "cliente falso" para simular o navegador
    return app.test_client()