from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image, ImageTk
from bancodedados.banco_dados import *
from tkinter import messagebox
from functions.functions import OndeEstou

class Troca():
    def __init__(self, frame):
        self.principal = tk.Frame(frame, background='light gray')
        self.location_troca = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.var_entrada = StringVar()
        self.var_saida = StringVar()
        self.banco = BancoDeDados()
        self.onde_estou()

    def onde_estou(self):
        local = OndeEstou(self.location_troca, 'Trocas', '../imagens/location.png')
        local.localizador()
        

    def troca(self):
        self.principal.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.72)
        Label(self.principal,
              text='Entrada:',
              font=('arial 28 bold'),
              bg='light gray').place(relx=.1, rely=.3)
        
        self.entrada = Entry(
            self.principal,
            background= 'white',
            font= ('arial 28')
                    )
        self.entrada.place(relx=.25, rely=.3)

        Label(self.principal,
              text='Saída:',
              font=('arial 28 bold'),
              bg='light gray').place(relx=.1, rely=.5)

        self.saida = Entry(
            self.principal,
            background= 'white',
            font= ('arial 28')
                    )
        self.saida.place(relx=.25, rely=.5)

        Button(
            self.principal,
            text="VER TROCA",
            font=('arial 18 bold'),
            command=self.descricao
        ).place(relx=.6, rely=.4)
    

        Button(
            self.principal,
            text="CONFIRMAR",
            font=('arial 18 bold'),
            command=self.salvar_troca
        ).place(relx=.8, rely=.4),
    

    def descricao(self):
        cod_entrada = self.entrada.get()
        cod_saida =self.saida.get()
        query= 'SELECT descricao, marca, tamanho, cor FROM estoque WHERE ID = ?'
        entrada = self.banco.dql_args(query, (cod_entrada,))
        saida = self.banco.dql_args(query, (cod_saida,))
        entrada_formatada = ' - '.join(entrada[0]) if entrada else ''
        saida_formatada = ' - '.join(saida[0]) if saida else ''        
        self.var_entrada.set(entrada_formatada)
        self.var_saida.set(saida_formatada)
        
        Label(
            self.principal,
            textvariable=self.var_entrada,
            background='light gray',
            font=('arial 16')
        ).place(relx = .6, rely= .3)

        Label(
            self.principal,
            textvariable=self.var_saida,
            background='light gray',
            font=('arial 16')
        ).place(relx = .6, rely= .5)

    def salvar_troca(self):
        query_entrada = 'UPDATE estoque SET quantidade = quantidade + 1 WHERE ID = ?'
        query_saida = 'UPDATE estoque SET quantidade = quantidade - 1 WHERE ID = ?'
        self.banco.dml(query_entrada, (self.entrada.get(),))
        self.banco.dml(query_saida, (self.saida.get(),))
        messagebox.showinfo('Sucesso', 'Troca realizada com sucesso.')
        

        


