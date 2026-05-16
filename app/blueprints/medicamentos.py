from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models.remedio import Remedio, Horario
from app.models.registro import RegistroDiario
from app.utils import obter_frase_do_dia
from datetime import date, datetime
from flask import session

medicamentos_bp = Blueprint('medicamentos', __name__, url_prefix='/medicamentos')

USUARIO_ATUAL_ID = 1

@medicamentos_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    """Página de Cadastro de Remédios e Horários."""
    if request.method == 'POST':
        nome = request.form.get('nome')
        dosagem = request.form.get('dosagem')

        if 'usuario_id' not in session:
            return redirect(url_for('auth.entrar'))
        
        usuario_id = session['usuario_id']
        
        # Pega a lista de horários preenchidos no formulário
        horarios_str = request.form.getlist('horarios') 
        
        # Cria o remédio
        novo_remedio = Remedio(nome=nome, dosagem=dosagem, usuario_id=usuario_id)
        db.session.add(novo_remedio)
        db.session.flush() 
        
        # Cria os horários vinculados ao remédio
        for h in horarios_str:
            if h.strip(): 
                hora_obj = datetime.strptime(h, '%H:%M').time()
                novo_horario = Horario(hora_prevista=hora_obj, remedio_id=novo_remedio.id)
                db.session.add(novo_horario)
        
        db.session.commit()
        flash('Remédio cadastrado com sucesso!')
        return redirect(url_for('painel.index'))
        
    return render_template('medicamentos/cadastrar.html')

@medicamentos_bp.route('/controle')
def controle_diario():
    """Página de Checklist Diário."""
    hoje = date.today()

    if 'usuario_id' not in session:
        return redirect(url_for('auth.entrar'))
        
    usuario_id = session['usuario_id']
    
    # Traz todos os horários previstos para o usuário
    horarios_previstos = Horario.query.join(Remedio).filter(
        Remedio.usuario_id == usuario_id
    ).order_by(Horario.hora_prevista).all()
    
    # Descobre quais horários já ganharam "check" hoje
    registros_hoje = RegistroDiario.query.filter_by(data_registro=hoje).all()
    horarios_tomados_ids = [registro.horario_id for registro in registros_hoje if registro.status]

    frase_motivacional = obter_frase_do_dia()
    
    return render_template(
        'medicamentos/controle.html', 
        horarios=horarios_previstos, 
        tomados_ids=horarios_tomados_ids, 
        hoje=hoje, 
        frase_do_dia=frase_motivacional
    )

@medicamentos_bp.route('/marcar/<int:horario_id>', methods=['POST'])
def marcar_tomado(horario_id):
    """Rota invisível (ação) acionada quando o botão 'Tomar' é clicado."""
    hoje = date.today()
    
    # verifica se já não foi tomado hoje para evitar duplicação no banco
    registro_existente = RegistroDiario.query.filter_by(horario_id=horario_id, data_registro=hoje).first()
    
    if not registro_existente:
        novo_registro = RegistroDiario(horario_id=horario_id, data_registro=hoje, status=True)
        db.session.add(novo_registro)
        db.session.commit()
        flash('Medicamento registrado com sucesso!')
        
    return redirect(url_for('medicamentos.controle_diario'))