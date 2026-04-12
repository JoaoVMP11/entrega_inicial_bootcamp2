# MedControl

**Versão Atual:** 1.0.0

## Descrição do Problema Real
O gerenciamento de múltiplas medicações é um desafio constante para a população idosa. A confusão com horários e dosagens frequentemente leva ao esquecimento de doses ou, em casos mais graves, à superdosagem acidental. Essa falta de controle compromete a eficácia dos tratamentos médicos e reduz a autonomia do idoso, gerando também ansiedade para os familiares e cuidadores que não possuem um meio centralizado e confiável para acompanhar a rotina médica.

## Proposta da Solução
O MedControl é uma aplicação web focada em usabilidade e simplicidade. A solução centraliza o catálogo de remédios e gera um painel de controle diário ("checklist"). O sistema adota uma abordagem de "Soft Login" (autenticação baseada em sessão, sem a complexidade de senhas), permitindo que idosos ou seus cuidadores acessem rapidamente a plataforma e deem "baixa" nos medicamentos tomados, gerando um histórico confiável de adesão ao tratamento.

## Público-Alvo
- **Idosos e Pacientes:** Que necessitam de uma ferramenta livre de distrações para acompanhar seus próprios horários.
- **Cuidadores e Familiares:** Que precisam gerenciar a rotina medicamentosa de um ou mais pacientes de forma organizada em um único dispositivo.

## Funcionalidades Principais
- **Soft Login (Gestão de Sessão):** Acesso rápido ao perfil informando apenas nome e e-mail.
- **Cadastro de Medicamentos:** Registro de remédios com suas respectivas dosagens e múltiplos horários.
- **Controle Diário (Checklist):** Tela dinâmica que lista os remédios do dia, permitindo marcar cada dose como concluída para evitar duplicidades.
- **Histórico de Adesão:** Relatório gerencial listando todos os medicamentos tomados corretamente nos dias anteriores.

## Tecnologias Utilizadas
- **Backend:** Python 3, Flask (Blueprints, Application Factory)
- **Banco de Dados:** MySQL (PyMySQL), SQLAlchemy (ORM), Flask-Migrate
- **Frontend:** HTML5 (Templates puros e Jinja2)
- **Qualidade de Código:** Flake8 (Linting)

---

## Instruções de Instalação

**1. Clone o repositório**
git clone https://github.com/JoaoVMP11/entrega_inicial_bootcamp2.git

cd entrega_inicial_bootcamp2

**2. Crie e ative o ambiente virtual**
python -m venv venv

No Windows: venv\Scripts\activate

No Linux/Mac: source venv/bin/activate

**3. Instale as dependências**
Para instalar as bibliotecas .

pip install -r requirements.txt

**4. Configure as Variáveis de Ambiente**
Crie um arquivo `.env` na raiz do projeto com as suas credenciais do MySQL:
DATABASE_URL=mysql+pymysql://seu_usuario:sua_senha@localhost/controle_remedios
SECRET_KEY=sua_chave_secreta_aqui

**5. Crie o banco de dados e rode as migrações**
Certifique-se de ter criado um banco vazio chamado `controle_remedios` no seu MySQL. Em seguida, rode:
flask --app run.py db init
flask --app run.py db migrate -m "primeira migracao"
flask --app run.py db upgrade

## Instruções de Execução

Com o banco de dados configurado e o ambiente virtual ativado, inicie o servidor local:
python run.py

Acesse `http://127.0.0.1:5000` no seu navegador para utilizar a aplicação.

## Instruções para Rodar os Testes

O projeto conta com testes automatizados construídos com a biblioteca pytest. Para garantir a segurança dos seus dados, os testes são isolados e rodam utilizando um banco de dados SQLite temporário em memória (`sqlite:///:memory:`), não afetando os registros do seu MySQL.

Para executar a suíte de testes, certifique-se de que o ambiente virtual está ativado e rode o comando abaixo na raiz do projeto:


pytest

## Instruções para Rodar o Lint

O projeto utiliza o Flake8 para garantir a padronização e qualidade do código Python (PEP 8). Para realizar a análise estática, execute:
flake8 .

---

## Autor

**João Vitor Mendes Peres**

**Link do Repositório Público:** https://github.com/JoaoVMP11/entrega_inicial_bootcamp2.git

## Evidências de Funcionamento

Abaixo estão as capturas de tela demonstrando o fluxo principal da aplicação em funcionamento local.

### 1. Tela de Acesso (Soft Login)
![Tela de Acesso](docs/login.png)
*Autenticação simplificada baseada em sessão, ideal para uso rápido por pacientes e cuidadores.*

### 2. Tela Inicial (Meus Medicamentos)
![Tela Inicial](docs/painel.png)
*Visão geral do catálogo de remédios do usuário e seus respectivos horários previstos.*

### 3. Cadastro de Medicamentos
![Tela de Cadastro](docs/cadastro.png)
*Formulário estrutural para inserção de um novo remédio e múltiplos horários de uma só vez.*

### 4. Controle Diário (Checklist)
![Controle Diário](docs/controle.png)
*Painel de uso diário onde o paciente ou cuidador dá "baixa" nos medicamentos tomados na data atual.*

### 5. Histórico de Adesão
![Histórico](docs/historico.png)
*Relatório gerencial listando o cruzamento de dados entre horários previstos e doses efetivamente tomadas.*