from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from limpar import limpar
from tkinter import ttk
from tkinter import messagebox
from estoque.banco_dados_estoque import *
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import customtkinter as ctk
from fornecedor.banco_dados_fornecedor import fornecedor_dql, fornecedor_dql_arg
from estoque.banco_dados_estoque import dql
from compra.listadecompras import ListaCompras


class AddCompra():
    def __init__(self, frame):
        self.principal = frame
        self.layout_add_compra()
    def layout_add_compra(self):
        #-------------------------Cabecalho------------------------------#
        self.principal.place(relx=0.01, rely=.25, relwidth = .98, relheight = .72)
        ttk.Label(self.principal, text='Cadastrar Nova Compra', font=('arial 18 bold'), background='white').place(relx=.05, rely=0.025)  # titulo principal
        ttk.Separator(self.principal, orient='vertical').place(relx=0.05, rely=.07, relwidth=.9)

        #--------------------------Frames secundários-----------------------------#
        self.frame_data_compra = Frame(self.principal, background='white', bd=1, relief='solid')
        self.frame_pedido = Frame(self.principal, background='light gray' ,bd=0)
        self.frame_data_compra.place(relx=0.05, rely=.15, relwidth=.9, relheight=.1)
        self.frame_pedido.place(relx=0.05, rely=.45, relwidth=.5, relheight=.15)
        
        #------------------------------Labels -------------------------------------------#
        ttk.Label(self.principal, text='Compra:', font=('arial 14 bold'), foreground=cor4, background='white').place(relx=.05, rely=.1)
        ttk.Label(self.principal, text='Fornecedor:', font=('arial 14 bold'), foreground=cor4, background='white').place(relx=.05, rely=.27)
        ttk.Label(self.principal, text='Produto:', font=('arial 14 bold'), foreground=cor4, background='white').place(relx=.30, rely=.27)
        ttk.Label(self.principal, text='Valores:', font=('arial 14 bold'), foreground=cor4, background='white').place(relx=.05, rely=.4)
        self.msg_erro = ttk.Label(self.principal, text='Selecione um fornecedor primeiro.', foreground='red', background='white')
        self.msg_erro.place(relx=0.30, rely=.36)
        ttk.Label(self.frame_pedido, text='Cod. Barras:', background='light gray', font=('arial 12 bold')).place(relx=0, rely=0)
        ttk.Label(self.frame_pedido, text='Item:', background='light gray', font=('arial 12 bold')).place(relx=.2, rely=0)
        ttk.Label(self.frame_pedido, text='QTDE:', background='light gray', font=('arial 12 bold')).place(relx=.4, rely=0)
        ttk.Label(self.frame_pedido, text='Preço:', background='light gray', font=('arial 12 bold')).place(relx=.55, rely=0)
        ttk.Label(self.frame_pedido, text='Total:', background='light gray', font=('arial 12 bold')).place(relx=.7, rely=0)
        ttk.Label(self.frame_pedido, text='Obs:', background='light gray', font=('arial 12 bold')).place(relx=0, rely=.7)
        

        #------------------------------- Entrys -----------------------------------------#        
        self.fornecedores = ttk.Combobox(self.principal, values=self.obter_fornecedores(), font=('Arial', 14))
        self.fornecedores.place(relx=0.05, rely=.32, relwidth=.20)
        self.fornecedores.bind('<<ComboboxSelected>>', lambda event: self.obter_produtos(event))
        self.produtos = ttk.Combobox(self.principal, font=('Arial', 12) )
        self.produtos.place(relx=0.30, rely=.32, relwidth=.20)
        self.produtos.bind('<<ComboboxSelected>>', lambda event: self.obter_info_produtos(event))
        self.qtde = Spinbox(self.frame_pedido, background='light gray', font=('arial 12 bold'), bd=0, highlightthickness=0, from_=0, to=1000, command=self.total_relativo)
        self.qtde.bind('<KeyRelease>', lambda event: self.chamar_função(event))
        self.qtde.place(relx=.425, rely=.20, relheight=.25, relwidth=.06)
        self.obs = Entry(self.frame_pedido, background='light gray', font=('arial 12'))
        self.obs.place(relx=.07, rely=.7, relwidth=.75, relheight=.2)

        #-----------------------------------Botões ----------------------------------------#
        Button(self.frame_pedido, bg='gray', text='Incluir\n Pedido', cursor='hand2', font=('arial 12 bold')).place(relx=.85, rely=0, relwidth=.15, relheight=1)
        
    def chamar_função(self, event):        
        self.total_relativo()
        
    def total_relativo(self):
        global preço
        try:
            preço = info[0][2]
            preço = float(preço)*int(self.qtde.get())
            self.label_total = ttk.Label(self.frame_pedido, text=f'R${preço:.2f}', background='light gray', font=('arial 10 '))
            if preço < 100:
                self.label_total.place(relx=0.7, rely=.2,relwidth=.1)
            else: 
                self.label_total.place(relx=0.7, rely=.2)
        except:
            pass
        
    def obter_info_produtos(self, event):
        global info, info_produtos
        info_produtos = self.produtos.get()
        info_produtos = info_produtos.split(' - ')        
        query = 'SELECT ID, descricao, custo FROM estoque WHERE descricao = ? AND categoria = ? AND marca = ?'
        info = dql_args(query, (info_produtos[0].strip(), info_produtos[1].strip(), info_produtos[2].strip()))
        ttk.Label(self.frame_pedido, text=info[0][0], background='light gray', font=('arial 10 ')).place(relx=0, rely=.2)
        ttk.Label(self.frame_pedido, text=info[0][1], background='light gray', font=('arial 10 ')).place(relx=0.2, rely=.2)
        ttk.Label(self.frame_pedido, text=f'R${info[0][2]}', background='light gray', font=('arial 10 ')).place(relx=0.55, rely=.2)
        if int(self.qtde.get()) > 0:
            self.label_total = ttk.Label(self.frame_pedido, text=f'R${float(info[0][2])*int(self.qtde.get()):.2f}', background='light gray', font=('arial 10 '))
            self.label_total.place(relx=0.7, rely=.2)

    def obter_fornecedores(self):
        lista_fornecedores = []
        query = "SELECT nome FROM fornecedor"
        fornecedores = fornecedor_dql(query)
        for fornecedor in fornecedores:
            lista_fornecedores.append(fornecedor[0])
        return lista_fornecedores
    
    def obter_produtos(self, event):
        self.msg_erro.place_forget()        
        fornecedor = self.fornecedores.get()
        self.lista_produtos = []
        query = "SELECT lista_produtos FROM fornecedor WHERE nome = ?"
        produtos = fornecedor_dql_arg(query, (fornecedor,))
        produtos = produtos[0][0].split(';')
        for produto in produtos:
            self.lista_produtos.append(produto)
        self.produtos['values'] = self.lista_produtos

