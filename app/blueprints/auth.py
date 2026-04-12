from flask import Blueprint, render_template, request, redirect, url_for, session
from app.extensions import db
from app.models.usuario import Usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        
        # Procura se o e-mail já existe no banco
        usuario = Usuario.query.filter_by(email=email).first()
        
        # Se não existir, cria o usuário na hora
        if not usuario:
            usuario = Usuario(nome=nome, email=email)
            db.session.add(usuario)
            db.session.commit()
            
        # Guarda o ID do usuário na sessão do navegador
        session['usuario_id'] = usuario.id
        
        return redirect(url_for('painel.index'))
        
    return render_template('auth/entrar.html')

@auth_bp.route('/sair')
def sair():
    
    session.pop('usuario_id', None)
    return redirect(url_for('auth.entrar'))