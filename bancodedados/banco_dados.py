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
        self.pastaApp = "c:\\.controleestoque\\"  
        self.nomeBanco = self.pastaApp+'banco.db'


    def conexao_banco(self):
        con= None
        try:
            con=sqlite3.connect(self.nomeBanco)
        except Error as ex:
            print(ex)
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
