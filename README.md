# gerenciador de tarefas

Este projeto servira para aprimoramos nossa lógica de progamação ao mesmo tempo em que exploramos conceitose técnicas de progamação back-end e fullstack. vamos utilizar e desenvolver o conceito de MVC (model-view-controller), algumas particularidades funcional, persistência de dados (MySQL), microframework Flask e gerenciador de pacotes de python (Astral uv).

### alguns passo iniciais para preparar o projeto:
1. caso não esteja instalado, prepare o uv no seu OS, voce encontra o script de instalação no site <https://docs.astral.sh/uv/#installation>
```bash
    powershell -ExecutionPolicy ByPass -c "irm
https://astral.sh/uv/install.ps1 | iex"
```

2. Faça a inicialização do projeto com o comando:
```bash
uv init
```

até então utilizávamos um layout de pacote (package layout) denomimado flat-layout. o uv adota uma estruturação mais moderna chamada src-layout, que previne erros de importação comouns chamados `ìmport shadowing` (importações mascaradas). 

3. crie um ambiente virtual do python:
```bash
uv venv
```

Ative o ambiente virtual, se necessário:
```powershell
.\.venv\Scripts\activete.ps1 # no Powershell do windows
source .venv/Scripts/activate # no Git bash do windows
source .venv/bin/activate # no Bash do Linux
```

4. instale o flask 
```bash
uv add flask
```

sera criado um arquivo uv.lock contendo as dependêcias (requerimentos) e versões dos pacotes do seu projeto.

5. crie um arquivo `app.py` contendo o código inicial do projeto
```python
from flask import flask

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Servidor online!'
```

6. teste a aplicação iniciando o servidor do Flask
```bash
uv run flask run
```