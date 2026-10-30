from datetime import datetime
from inspect import isdatadescriptor

from tarefas.models.database import Database


class Tarefa:
    """Provê métodos para armazenar, recuperador e processar os dados das
    tarefas criadas a partir do formulario principal.
    """
    def __init__(self, id = None, titulo, data_conclusao = None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao


    def salvarTarefa(self):
        """Salva a tarefa no banco de dados."""

        sql = 'INSERT INTO tarefa (titulo_tarefa, data_conclusao) VALUES (%s, %s):'
        params = (self.titulo, self.data_conclusao) # protege
        with Database() as db:
            db.executar(sql, params)

# Área 51 (testes)
tarefa = Tarefa('Minha nova terefa')
tarefa.salvarTarefa