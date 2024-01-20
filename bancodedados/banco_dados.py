# import sqlite3

# # Conectar-se ao banco de dados (ou criá-lo se não existir)
# conn = sqlite3.connect("compra.db")

# # Criar um cursor
# cursor = conn.cursor()

# # Definir a estrutura da tabela
# cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
#                   id INTEGER PRIMARY KEY,
#                   data_compra DATE,
#                   data_entrega DATE,
#                   codigo_de_barras TEXT,
#                   produto TEXT,
#                   fornecedor TEXT,
#                   forma_de_pagamento TEXT,
#                   parcelamento TEXT,
#                   vencimento TEXT,
#                   quantidade INTEGER,
#                   frete REAL,
#                   desconto REAL,
#                   status TEXT
#                 )''')

# # Confirmar as alterações e fechar a conexão
# conn.commit()
# conn.close()



import sqlite3 
from sqlite3 import Error
import os


class BancoDeDados():
    def __init__(self):
        self.folderBanco = "c:\\.controleestoque"
        self.nomeBanco = "banco.db"
        self.pathBanco = os.path.join(self.folderBanco, self.nomeBanco)
       

    def _criarDiretorio(self, directory_path):
        """
        Cria um diretório se ele não existir e o torna oculto.

        Args:
        - directory_path (str): Caminho para o diretório a ser criado e oculto.
        """
        os.mkdir(directory_path)
        # Torna o diretório oculto
        os.system(f"attrib +h {directory_path}")

    def _executarScriptSQL(self):
        """
        Executa um script SQL para criar o banco de dados.

        Args:
        - directory_path (str): Caminho para o diretório onde o banco de dados será criado.
        """
        diretorio = os.path.join('bancodedados', "create.sql")
        diretorio_absoluto =  os.path.abspath(diretorio)

        with open(diretorio_absoluto, 'r') as sql_file:
            sql_script = sql_file.read()

        db = sqlite3.connect(self.pathBanco)
        cursor = db.cursor()
        cursor.executescript(sql_script)
        db.commit()
        db.close()

    def conexao_banco(self):
        con = None
        if not os.path.exists(self.folderBanco):
            self._criarDiretorio(self.folderBanco)
            self._executarScriptSQL()
            con=sqlite3.connect(self.pathBanco)
        else:
            con=sqlite3.connect(self.pathBanco)
        return con



    def dql(self, query): #select
        vcon=self.conexao_banco()
        c=vcon.cursor()
        c.execute(query)
        res=c.fetchall()
        vcon.close()
        return res

    def dql_args(self, query, params): #select
        vcon=self.conexao_banco()
        c=vcon.cursor()
        c.execute(query, params)
        res=c.fetchall()
        vcon.close()
        return res

    def dml(self, query, params=None): # insert, update, delete
        try:
            vcon=self.conexao_banco()
            c=vcon.cursor()
            c.execute(query, params)
            vcon.commit()
            vcon.close()
        except Error as ex:
            print(ex)
