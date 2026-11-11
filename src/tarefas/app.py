from flask import Flask, render_template

from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa

app = Flask(__name__)

with app.app_context():
    init_db()

@app.route('/test')
def test():
    return 'Servidor online!'

@app.route('/')
def home():

    tarefas = Tarefa.ListarTarefas()

    return render_template(
        'base.html',
        titulo_da_pagina ='minha lista de tarefas', 
        tarefas_da_pagina =tarefas
    )

if __name__ == '__main__':
    app.run()