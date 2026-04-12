import os
from flask import Flask
from dotenv import load_dotenv
from app.extensions import db, migrate

load_dotenv()


def create_app():
    app = Flask(__name__)


    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

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