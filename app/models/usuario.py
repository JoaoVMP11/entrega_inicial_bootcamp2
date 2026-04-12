from app.extensions import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # relacionamento: um usuário pode ter vários remédios cadastrados
    remedios = db.relationship('Remedio', backref='dono', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Usuario {self.nome}>'