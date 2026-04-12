import os
from flask import Flask
from dotenv import load_dotenv
from app.extensions import db, migrate

load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        app.config.update(test_config)
    else:

        pass

    # Inicializa as extensões com a instância da aplicação atual
    db.init_app(app)
    migrate.init_app(app, db)

    # Importa os modelos
    with app.app_context():
        from app.models import usuario, remedio, registro

    from app.blueprints.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.blueprints.painel import painel_bp
    app.register_blueprint(painel_bp)
    
    from app.blueprints.medicamentos import medicamentos_bp
    app.register_blueprint(medicamentos_bp)

    return app