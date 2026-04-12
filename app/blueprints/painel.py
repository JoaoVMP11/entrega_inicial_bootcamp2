from flask import Blueprint, render_template, session, redirect, url_for
from app.models.remedio import Remedio, Horario
from app.models.registro import RegistroDiario
from datetime import date

painel_bp = Blueprint('painel', __name__)

@painel_bp.route('/')
def index():
    # Se o usuário não ta logado, manda para a tela de entrar
    if 'usuario_id' not in session:
        return redirect(url_for('auth.entrar'))
        
    usuario_id = session['usuario_id']
    remedios = Remedio.query.filter_by(usuario_id=usuario_id).all()
    return render_template('painel/index.html', remedios=remedios)

@painel_bp.route('/historico')
def historico():
    """Página de Histórico: Mostra os remédios que foram tomados."""

    # Filtra apenas os remédios deste usuário e que o status seja True (tomado)

    if 'usuario_id' not in session:
        return redirect(url_for('auth.entrar'))
        
    usuario_id = session['usuario_id']

    registros = RegistroDiario.query.join(Horario).join(Remedio).filter(
        Remedio.usuario_id == usuario_id,
        RegistroDiario.status == True
    ).order_by(RegistroDiario.data_registro.desc(), Horario.hora_prevista).all()
    
    return render_template('painel/historico.html', registros=registros)