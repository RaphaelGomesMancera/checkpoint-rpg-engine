# O Despertar do Kernel Ancestral – RPG Engine

Projeto desenvolvido em Python + Flask com Oracle PL/SQL.

## Objetivo
Simular a passagem de turnos de um RPG, onde uma névoa venenosa causa dano em todos os heróis ativos.

## Tecnologias utilizadas
- Python
- Flask
- Oracle Database
- PL/SQL
- HTML/CSS
- Vercel

## Funcionalidades
- Listagem dos heróis cadastrados no banco Oracle
- Botão "Próximo Turno"
- Execução de bloco PL/SQL para processar dano por turno
- Atualização automática de HP e status dos heróis

## Estrutura do projeto
- `app.py`: aplicação Flask
- `templates/index.html`: interface web
- `.env`: variáveis de ambiente para conexão com Oracle
- `vercel.json`: configuração de deploy
- `requirements.txt`: dependências do projeto

## Requisitos atendidos

### Python
- conexão com Oracle usando `oracledb`
- uso de variáveis de ambiente com `python-dotenv`
- interface web com Flask
- rota para processar o turno

### PL/SQL
- bloco anônimo
- variáveis
- cursor
- loop
- atualização de HP
- alteração de status para `CAÍDO`

## Como executar localmente

1. Criar e ativar ambiente virtual  
2. Instalar dependências:

`pip install -r requirements.txt`

3. Configurar o arquivo `.env`:

`DB_USER=seu_usuario`  
`DB_PASSWORD=sua_senha`  
`DB_DSN=seu_host:1521/seu_service_name`

4. Executar:

`python app.py`

5. Acessar:

`http://127.0.0.1:5000`

## Banco de dados
A tabela utilizada no projeto é `TB_HEROIS`.

## Autores
- Raphael Gomes Mancera
- Guilherme de Andrade Martini