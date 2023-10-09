import sqlite3 
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = os.path.abspath(os.path.join(pastaApp, 'fornecedores.db'))
print(nomeBanco)
if not os.path.exists(nomeBanco):
    print("O banco de dados não existe no caminho especificado.")

# import sqlite3

# # Conectar ao banco de dados ou criar se não existir
# conn = sqlite3.connect('fornecedores.db')

# # Criar um cursor
# cursor = conn.cursor()

# # Query para criar a tabela "produtos"
# query = '''
# CREATE TABLE fornecedor (
#     ID INTEGER PRIMARY KEY,
#     nome TEXT CHECK(length(nome) <= 200),
#     categoria TEXT CHECK(length(categoria) <= 100),
#     cnpj TEXT CHECK(length(cnpj) <= 20),
#     email TEXT,
#     telefone TEXT,
#     OBS TEXT CHECK(length(OBS) <= 200),
#     CEP TEXT CHECK(length(CEP) <= 9),
#     rua TEXT CHECK(length(rua) <= 100),
#     numero TEXT,
#     bairro TEXT,
#     cidade TEXT,
#     estado TEXT,
#     lista_produtos TEXT,
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

def fornecedor_dql(query): #select
    vcon=conexao_banco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def fornecedor_dml(query, params=None): # insert, update, delete
    try:
        vcon=conexao_banco()
        c=vcon.cursor()
        c.execute(query, params)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)
