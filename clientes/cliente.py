from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image
from limpar import limpar
from clientes.add_cliente import AddCliente
from tkinter import ttk


class Cliente(AddCliente):
    def __init__(self, frame) -> None:
        self.principal = tk.Frame(frame, bg= 'white')

    def novo_cliente(self):
        self.btn_addcliente.configure(state='disabled')        
        self.novo_cliente = AddCliente(self.principal)       

        return self.novo_cliente
         
            
    def clientes(self):
        self.principal.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.67)
        #Botão_adicionar_cliente        
        self.btn_addcliente = Button(self.principal, text='ADICIONAR\n Cliente', bg=cor6, compound='center',bd=0, font=('arial 14 bold'), foreground='white', cursor='hand2', command=self.novo_cliente)
        self.btn_addcliente.place(relx=0.9, rely=0, relheight=0.1, relwidth=0.1)


    def buscar_cliente(self):
        self.search = Entry(self.principal, font=('arial 14'), bg=cor5, bd=0)
        self.search.insert(0, "Procure por...")
        self.search.bind("<FocusIn>", lambda event: self.search.delete(0, "end"))
        self.search.place(relx=0, rely=0, relheight=0.1, relwidth=0.8)
        #botão_pesquisar
        self.img_search = PhotoImage(file='imagens/search.png')
        self.btn_search = Button(self.principal, image=self.img_search, bg=cor5, bd=0, cursor='hand2')
        self.btn_search.place(relx=0.8, rely=0, relheight=0.1, relwidth=0.05)
        #Botão_imprimir
        self.img_print = PhotoImage(file='imagens/impressora.png')
        self.btn_print = Button(self.principal, image=self.img_print, bg=cor5, bd=0, cursor='hand2')
        self.btn_print.place(relx=0.85, rely=0, relheight=0.1, relwidth=0.05)

    def inserir_dados(self):
        self.ins_treeview = ttk.Treeview(self.principal)
        style = ttk.Style(self.ins_treeview)
        style.configure("Treeview.Heading", font=('Arial', 18), foreground='gray', padding=0)
        self.ins_treeview['columns'] = ('ID', 'NOME', 'TELEFONE', 'EMAIL','VALOR GASTO')
        self.ins_treeview.heading('#0', text='EDITAR', anchor=W)
        self.ins_treeview.heading('#1', text='ID', anchor=W)
        self.ins_treeview.heading('#2', text='NOME')
        self.ins_treeview.heading('#3', text='TELEFONE')
        self.ins_treeview.heading('#4', text='EMAIL')
        self.ins_treeview.heading('#5', text='VALOR GASTO' )
        self.ins_treeview.place(relx=0, rely=.1, relheight=.9, relwidth=1)
        self.ins_treeview.column("#0", width=110, stretch=FALSE)
        self.ins_treeview.column("ID",width=40, stretch=FALSE)
        self.ins_treeview.column("NOME", minwidth=600, stretch=TRUE)
        self.ins_treeview.column("TELEFONE", minwidth=250, stretch=TRUE)
        self.ins_treeview.column("EMAIL",minwidth=250, stretch=TRUE)
        self.ins_treeview.column("VALOR GASTO", minwidth=240, stretch=TRUE)
        
    

        