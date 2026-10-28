import mysql.connector as mc

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.username = 'root'
        self.password = 'admin'
        self.database = 'tarefas'
        self.connection = None
        self.cursor = None

    def conectar(self):
        try:
            self.connection = mc.connect(
                host = self.host,
                database = self.database,
                user = self.username,
                password = self.password
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                print('Conexão ao banco de dados realizada com sucesso!')
        except Error as e:
            print
print(carro)