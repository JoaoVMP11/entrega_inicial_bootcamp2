from app.models.usuario import Usuario
from app.extensions import db

def test_pagina_entrar_carrega(client):
    """Testa se a página de entrar retorna status 200 (OK) e contém a palavra MedControl"""
    resposta = client.get('/entrar')
    
    assert resposta.status_code == 200
    assert b'MedControl' in resposta.data  # O 'b' indica que é um dado do tipo byte (HTML puro)

def test_soft_login_cria_usuario(client, app):
    """Testa se preencher o formulário cria um usuário no banco e redireciona"""
    resposta = client.post('/entrar', data={
        'nome': 'João Teste',
        'email': 'joao@teste.com'
    })
    
    # Ao fazer login com sucesso, a aplicação redireciona (código 302) para o painel
    assert resposta.status_code == 302
    
    # Verifica se o usuário realmente foi salvo no banco de dados temporário
    with app.app_context():
        usuario = Usuario.query.filter_by(email='joao@teste.com').first()
        assert usuario is not None
        assert usuario.nome == 'João Teste'