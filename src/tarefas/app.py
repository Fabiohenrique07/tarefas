from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for
from tarefas.models.database import init_db
from tarefas.models.tarefa import Tarefa
 
 
app = Flask(__name__)
 
with app.app_context():
    init_db()
 
 
@app.route('/test')
def test():
    return 'Servidor online!'
 
 
@app.route('/', methods=['GET', 'POST'])
def home():
 
    if request.method == 'POST':
 
        titulo_form = request.form.get('tituloTarefa', '').strip()
 
        data_form = request.form.get('dataConclusao') or None
 
        if titulo_form:
 
            if data_form:
                data_form = datetime.strptime(data_form, '%Y-%m-%d')
 
            tarefa = Tarefa(
                titulo=titulo_form,
                data_conclusao=data_form
            )

            tarefa.salvarTarefa()
 
        return redirect(url_for('home'))
 
    tarefas = Tarefa.listarTarefas()
 
    return render_template(
        'base.html',
        titulo_da_pagina='Minha lista de tarefas',
        tarefas_da_pagina=tarefas,
        tarefa_editar=None
    )
 
 
@app.route('/delete/<int:id>', methods=['POST'])
def apagar_id_especificado(id):
 
    Tarefa.apagarTarefa(id)
 
    return redirect(url_for('home'))
 
 
@app.route('/editar/<int:id>')
def editar_tarefa(id):
 
    tarefa = Tarefa.buscarTarefa(id)
 
    if tarefa is None:
        return redirect(url_for('home'))
 
    tarefas = Tarefa.listarTarefas()
 
    return render_template(
        'base.html',
        titulo_da_pagina='Editar tarefa',
        tarefas_da_pagina=tarefas,
        tarefa_editar=tarefa
    )
 
 
@app.route('/update/<int:id>', methods=['POST'])
def atualizar_id_especificado(id):
 
    titulo = request.form.get('tituloTarefa', '').strip()
 
    data = request.form.get('dataConclusao') or None
 
    if not titulo:
        return redirect(url_for('editar_tarefa', id=id))
 
    if data:
        data = datetime.strptime(data, '%Y-%m-%d')

    Tarefa.atualizarTarefa(id, titulo, data)
 
    return redirect(url_for('home'))
 
 
if __name__ == '__main__':
    app.run(debug=True)