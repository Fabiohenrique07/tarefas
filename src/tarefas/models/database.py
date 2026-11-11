 
from os import getenv
from pathlib import Path
 
import mysql.connector as mc
from dotenv import load_dotenv
from mysql.connector import Error
 
 
class Database:
    """
    Classe responsável pela conexão e operações
    com o banco de dados MySQL.
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
                database=self.database,
                user=self.username,
                password=self.password
            )
 
            self.cursor = self.connection.cursor(dictionary=True)
 
            print('Conexão ao banco realizada com sucesso!')
 
        except Error as e:
            print(f'Erro de conexão: {e}')
            self.connection = None
            self.cursor = None
            raise
 
    def desconectar(self):
        if self.cursor:
            self.cursor.close()
 
        if self.connection and self.connection.is_connected():
            self.connection.close()
 
        print('Conexão encerrada!')
 
    def executar(self, sql, params=None):
        """Executa comandos SQL."""
 
        if not self.connection or not self.cursor:
            raise RuntimeError('Conexão não estabelecida!')
 
        try:
            self.cursor.execute(sql, params)
            self.connection.commit()
 
            return self.cursor.rowcount
 
        except Error as e:
            self.connection.rollback()
            print(f'Erro de execução: {e}')
            raise
 
    # Permite utilizar with Database() as db
    def __enter__(self):
        self.conectar()
        return self
 
    def __exit__(self, exc_type, exc_value, traceback):
        self.desconectar()
 
 
# Caminho do arquivo SQL
BASE_DIR = Path(__file__).resolve().parent.parent
SQL_PATH = BASE_DIR / "data" / "tarefas.sql"
 
 
def init_db(sql_filepath=SQL_PATH):
    """Inicializa o banco de dados e suas tabelas."""
 
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
            sql = arquivo.read()
 
        # Executa cada instrução separadamente
        comandos = sql.split(';')
 
        for comando in comandos:
            comando = comando.strip()
 
            if comando:
                cursor.execute(comando)
 
        conexao.commit()
 
        print('Banco de dados e tabelas inicializados!')
 
    except Error as e:
        print(f'Erro MySQL: {e}')
 
    except FileNotFoundError:
        print(f'Arquivo SQL não encontrado: {sql_filepath}')
 
    finally:
        if cursor:
            cursor.close()
 
        if conexao and conexao.is_connected():
            conexao.close()
 