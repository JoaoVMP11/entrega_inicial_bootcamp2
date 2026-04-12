from app.extensions import db

class Remedio(db.Model):
    __tablename__ = 'remedios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    dosagem = db.Column(db.String(50)) 
    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    # relacionamento: um remédio tem vários horários previstos
    horarios = db.relationship('Horario', backref='remedio', lazy=True, cascade="all, delete-orphan")

class Horario(db.Model):
    __tablename__ = 'horarios'

    id = db.Column(db.Integer, primary_key=True)
    hora_prevista = db.Column(db.Time, nullable=False) 
    
    remedio_id = db.Column(db.Integer, db.ForeignKey('remedios.id'), nullable=False)
    
    # Relacionamento com o histórico 
    registros = db.relationship('RegistroDiario', backref='horario_ref', lazy=True)
    