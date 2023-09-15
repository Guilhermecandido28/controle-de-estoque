from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image
from limpar import limpar
from clientes.add_cliente import AddCliente


class Cliente(AddCliente):
    def __init__(self, frame) -> None:
        self.principal = tk.Frame(frame, bg= 'white')

    def novo_cliente(self):
        novo_cliente = AddCliente(self.principal)
        return novo_cliente

        
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

    def cabecalho(self):
        #Labels
        self.lb_id = Label(self.principal, text='ID', foreground=cor5, background='white', font=('arial 14 bold'), anchor=N, bd=0, padx=0, pady=0)
        self.lb_nome = Label(self.principal, text='NOME', foreground=cor5, background='white', font=('arial 14 bold'))
        self.lb_telefone = Label(self.principal, text='TELEFONE', foreground=cor5, background='white', font=('arial 14 bold'))
        self.lb_email = Label(self.principal, text='E-MAIL', foreground=cor5, background='white', font=('arial 14 bold'))
        self.lb_editar = Label(self.principal, text='EDITAR', foreground=cor5, background='white', font=('arial 14 bold'))
        self.lb_id.place(relx=.02, rely=0.11, relheight=1)
        self.lb_nome.place(relx=0.06, rely=0.11)
        self.lb_telefone.place(relx=0.46, rely=0.11)
        self.lb_email.place(relx=0.66, rely=0.11)
        self.lb_editar.place(relx=0.92, rely=0.11)
    
    def inserir_dados(self):
        #lista de clientes:
        self.lista_clientes = []
        #Frame
        self.frame = Frame(self.principal, bg='gray')
        self.frame.place(relx=0.02, rely=0.15, relwidth=.98, relheight=.85)
        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = Scrollbar(self.canvas)
        self.scrollbar.pack(side=RIGHT, fill= Y) 
        self.canvas.create_text(50,30 + 50, text='guilherme', anchor=tk.W)