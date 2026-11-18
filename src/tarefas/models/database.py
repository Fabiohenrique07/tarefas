from os import getenv
from pathlib import Path
 
import mysql.connector as mc
from dotenv import load_dotenv
from mysql.connector import Error
 
 
class Database:
    """
    Classe responsável pela conexão com o banco de dados.
    """
 
    def __init__(self):
        load_dotenv()
 
        self.host = getenv('DB_HOST')
        self.username = getenv('DB_USER')
        self.password = getenv('DB_PASSWORD')
        self.database = getenv('DB_SCHEMA')
 
        self.connection = None
        self.cursor = None
 
    def conectar(self):
 
        try:
            self.connection = mc.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
 
            self.cursor = self.connection.cursor(dictionary=True)
 
            print('Conexão realizada com sucesso!')
 
        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None
 
    def desconectar(self):
 
        if self.cursor:
            self.cursor.close()
 
        if self.connection and self.connection.is_connected():
            self.connection.close()
 
    def executar(self, sql, params=None):
 
        if not self.connection or not self.cursor:
            print('Conexão não estabelecida!')
            return None
 
        try:
            self.cursor.execute(sql, params)
 
            if self.cursor.description:
                return self.cursor.fetchall()

            self.connection.commit()
 
            return self.cursor.rowcount
 
        except Error as e:
            self.connection.rollback()
            print(f'Erro ao executar comando: {e}')
            return None
 
    def __enter__(self):
        self.conectar()
        return self
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.desconectar()
 
 
BASE_DIR = Path(__file__).resolve().parent.parent
SQL_PATH = BASE_DIR / 'data' / 'tarefas.sql'
 
 
def init_db(sql_filepath=SQL_PATH):
 
    load_dotenv()
 
    conexao = None
    cursor = None
 
    try:
        conexao = mc.connect(
            host=getenv('DB_HOST'),
            user=getenv('DB_USER'),
            password=getenv('DB_PASSWORD')
        )
 
        cursor = conexao.cursor()
 
        with open(sql_filepath, 'r', encoding='utf-8') as arquivo:
            comandos = arquivo.read()

        for comando in comandos.split(';'):
            if comando.strip():
                cursor.execute(comando)
 
        conexao.commit()
 
        print('Banco inicializado com sucesso!')
 
    except Error as e:
        print(f'Erro no banco: {e}')
 
    except FileNotFoundError:
        print('Arquivo tarefas.sql não encontrado!')
 
    finally:
        if cursor:
            cursor.close()
 
        if conexao and conexao.is_connected():
            conexao.close()