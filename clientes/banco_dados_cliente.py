import sqlite3 
from sqlite3 import Error
import os

pastaApp = os.path.dirname(__file__)
nomeBanco = pastaApp+'\\clientes.db'


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

def dml(query, params=None): # insert, update, delete
    try:
        vcon=conexao_banco()
        c=vcon.cursor()
        c.execute(query, params)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)
