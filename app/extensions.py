from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancia o banco de dados
db = SQLAlchemy()
migrate = Migrate()