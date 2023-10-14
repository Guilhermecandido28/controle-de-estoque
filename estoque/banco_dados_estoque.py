import sqlite3 
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = os.path.abspath(os.path.join(pastaApp, 'estoques.db'))
print(nomeBanco)
if not os.path.exists(nomeBanco):
    print("O banco de dados não existe no caminho especificado.")

# import sqlite3

# # Conectar ao banco de dados ou criar se não existir
# conn = sqlite3.connect('estoques.db')

# # Criar um cursor
# cursor = conn.cursor()

# # Query para criar a tabela "produtos"
# query = '''
# CREATE TABLE estoque (
#     ID INTEGER VARCHAR(12) PRIMARY KEY,
#     descricao TEXT CHECK(length(descricao) <= 200),
#     categoria TEXT CHECK(length(categoria) <= 100),
#     marca TEXT CHECK(length(marca) <= 100),
#     estoque_minimo INTEGER,
#     quantidade INTEGER,
#     observacoes TEXT CHECK(length(observacoes) <= 200),
#     tamanho TEXT CHECK(length(tamanho) <= 3),
#     cor TEXT CHECK(length(cor) <= 70),
#     custo NUMERIC,
#     venda NUMERIC,
#     imagem BLOB
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

def dql(query): #select
    vcon=conexao_banco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dql_args(query, params): #select
    vcon=conexao_banco()
    c=vcon.cursor()
    c.execute(query, params)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query, params=None): # insert, update, delete
    try:
        vcon=conexao_banco()
        c=vcon.cursor()
        c.execute(query, params)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)
