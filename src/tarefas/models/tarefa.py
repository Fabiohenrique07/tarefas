from tarefas.models.database import Database

 
class Tarefa:
    """
    Gerencia as tarefas criadas pelo formulário principal.
    """
 
    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao
 
    def salvarTarefa(self):
        """Salva a tarefa no banco de dados."""
 
        sql = """
            INSERT INTO tarefas
            (titulo_tarefa, data_conclusao)
            VALUES (%s, %s)
        """
 
        params = (self.titulo, self.data_conclusao)
 
        with Database() as db:
            db.executar(sql, params)


    @staticmethod 
    def listarTarefas():
        """Retorna uma lista com todas as tarefas cadastradas."""

        sql = '''SELECT id_tarefa, titulo_tarefa, data_conclusao
        FROM tarefa LIMIT 100;'''

        with Database() as db:
            tarefas_bancos = db.executar(sql)

        return tarefas_bancos if tarefas_bancos else []
 
 
# Área 51 - Testes
# if __name__ == '__main__':
#   tarefa = Tarefa('Minha nova tarefa')
#  tarefa.salvarTarefa()