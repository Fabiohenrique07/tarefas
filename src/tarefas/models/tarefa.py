from tarefas.models.database import Database
 
 
class Tarefa:
    """
    Classe responsável por gerenciar as tarefas.
    """
 
    def __init__(self, titulo, id=None, data_conclusao=None):
        self.id = id
        self.titulo = titulo
        self.data_conclusao = data_conclusao
 
    def salvarTarefa(self):
 
        sql = '''
            INSERT INTO tarefas
            (titulo_tarefa, data_conclusao)
            VALUES (%s, %s);
        '''
 
        params = (self.titulo, self.data_conclusao)
 
        with Database() as db:
            return db.executar(sql, params)

    @staticmethod
    def listarTarefas():
 
        sql = '''
            SELECT id_tarefa, titulo_tarefa, data_conclusao
            FROM tarefas
            LIMIT 100;
        '''
 
        with Database() as db:
            tarefas = db.executar(sql)
 
        return tarefas if tarefas else []
 
    @staticmethod
    def buscarTarefa(id):
 
        sql = '''
            SELECT id_tarefa, titulo_tarefa, data_conclusao
            FROM tarefas
            WHERE id_tarefa = %s;
        '''
 
        with Database() as db:
            resultado = db.executar(sql, (id,))
 
        if resultado:
            return resultado[0]
 
        return None
 
    # (DELETE)
    @staticmethod
    def apagarTarefa(id):
 
        sql = '''
            DELETE FROM tarefas
            WHERE id_tarefa = %s;
        '''
 
        with Database() as db:
            return db.executar(sql, (id,))
 
    # (UPDATE)
    @staticmethod
    def atualizarTarefa(id, titulo, data_conclusao):
 
        sql = '''
            UPDATE tarefas
            SET titulo_tarefa = %s,
                data_conclusao = %s
            WHERE id_tarefa = %s;
        '''
 
        params = (titulo, data_conclusao, id)
 
        with Database() as db:
            return db.executar(sql, params)