from app.extensions import db
from datetime import date

class RegistroDiario(db.Model):
    __tablename__ = 'registros_diarios'

    id = db.Column(db.Integer, primary_key=True)
    data_registro = db.Column(db.Date, nullable=False, default=date.today)
    status = db.Column(db.Boolean, default=True)
    
    horario_id = db.Column(db.Integer, db.ForeignKey('horarios.id'), nullable=False)