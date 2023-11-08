import sqlite3 
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = os.path.abspath(os.path.join(pastaApp, 'vendas.db'))
print(nomeBanco)
if not os.path.exists(nomeBanco):
    print("O banco de dados não existe no caminho especificado.")

# import sqlite3

# # Conectar ao banco de dados ou criar se não existir
# conn = sqlite3.connect('vendas.db')

# # Criar um cursor
# cursor = conn.cursor()

# # Query para criar a tabela "produtos"
# query = '''
# CREATE TABLE venda (
#     ID INTEGER PRIMARY KEY,
#     data DATE,
#     produtos TEXT,
#     cliente TEXT ,
#     desconto TEXT,
#     total TEXT
# );
# '''

# # Executar a query
# cursor.execute(query)

# # Commit para aplicar as alterações
# conn.commit()

# # Fechar a conexão
# conn.close()


def conexao_banco():
    con= None
    try:
        con=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)
    return con

def vendas_dql(query): #select
    vcon=conexao_banco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def vendas_dql_arg(query, var): #select
    vcon=conexao_banco()
    c=vcon.cursor()
    c.execute(query, var)
    res=c.fetchall()
    vcon.close()
    return res

def vendas_dml(query, params=None): # insert, update, delete
    try:
        vcon=conexao_banco()
        c=vcon.cursor()
        c.execute(query, params)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)
