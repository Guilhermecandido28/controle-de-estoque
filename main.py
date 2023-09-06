from tkinter import *
from styles.cores import *
import tkinter as tk
from PIL import Image, ImageTk
from formations import format_cpf
from tkinter import ttk

janela = Tk()

class Applicantion():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.buttons()
        self.buscar()
        self.add_client()                               
        janela.mainloop()
    def tela(self):
        self.janela.title('Controle fincanceiro')
        self.janela.geometry('1500x1000')
        self.janela.configure(background= cor5)
    
    def frames(self):
        self.header = tk.Frame(self.janela, bg=cor3)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.09)
        self.menu = tk.Frame(self.janela, bg=cor4)
        self.menu.place(relx=0, rely=0.09, relwidth=1, relheight=0.05)
        self.location = tk.Frame(self.janela, bg=cor1)
        self.location.place(relx=0, rely=0.14, relwidth=1, relheight=0.09)        
        self.principal = tk.Frame(self.janela, bg= 'white')
        self.principal.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.67)
        

    def buttons(self):
        #Botão cliente
        self.img_cliente = PhotoImage(file='imagens/cliente.png')
        self.btn_clientes = Button(self.menu, text='Clientes', image=self.img_cliente, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'))
        self.btn_clientes.place(relx=0, rely=0, relwidth=0.14, relheight=1)
        #botão vendas
        self.img_vendas = PhotoImage(file='imagens/vendas.png')
        self.btn_vendas = Button(self.menu, text='Vendas', image=self.img_vendas, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'))
        self.btn_vendas.place(relx=0.14, rely=0, relwidth=0.14, relheight=1)
        # Fornecedor
        self.img_fornecedor = PhotoImage(file='imagens/fornecedor.png')
        self.btn_fornecedor = Button(self.menu, text='Fornecedor', image=self.img_fornecedor, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'))
        self.btn_fornecedor.place(relx=0.28, rely=0, relwidth=0.14, relheight=1)
        #estoque
        self.img_estoque= PhotoImage(file='imagens/estoque.png')
        self.btn_estoque = Button(self.menu, text='Estoque', image=self.img_estoque, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'))
        self.btn_estoque.place(relx=0.42, rely=0, relwidth=0.14, relheight=1)
        #compras
        self.img_compras= PhotoImage(file='imagens/compras.png')
        self.btn_compras = Button(self.menu, text='Compras', image=self.img_compras, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'))
        self.btn_compras.place(relx=0.56, rely=0, relwidth=0.14, relheight=1)
        #financeiro
        self.img_financeiro= PhotoImage(file='imagens/financeiro.png')
        self.btn_financeiro = Button(self.menu, text='Financeiro', image=self.img_financeiro, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'))
        self.btn_financeiro.place(relx=0.7, rely=0, relwidth=0.14, relheight=1)
        #configurações
        self.img_settings= PhotoImage(file='imagens/settings.png')
        self.btn_settings = Button(self.menu, text='Configurações', image=self.img_settings, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'))
        self.btn_settings.place(relx=0.84, rely=0, relwidth=0.14, relheight=1)
        #home
        self.img_home = PhotoImage(file='imagens/home.png')
        self.btn_home = Button(self.header, image=self.img_home, bg=cor3, bd=0, font=('arial 12 bold'))
        self.btn_home.place(relx=0, rely=0, relheight=1, relwidth=0.05)
        

    def buscar(self):        
        self.search = Entry(self.principal, font=('arial 14'), bg=cor5, bd=0)
        self.search.insert(0, "Procure por...")
        self.search.bind("<FocusIn>", lambda event: self.search.delete(0, "end"))
        self.search.place(relx=0, rely=0, relheight=0.1, relwidth=0.8)
        #botão_pesquisar
        self.img_search = PhotoImage(file='imagens/search.png')
        self.btn_search = Button(self.principal, image=self.img_search, bg=cor5, bd=0)
        self.btn_search.place(relx=0.8, rely=0, relheight=0.1, relwidth=0.05)
        #Botão_imprimir
        self.img_print = PhotoImage(file='imagens/impressora.png')
        self.btn_print = Button(self.principal, image=self.img_print, bg=cor5, bd=0)
        self.btn_print.place(relx=0.85, rely=0, relheight=0.1, relwidth=0.05)
    
    def add_client(self):
        #Botão_adicionar_cliente        
        self.btn_addcliente = Button(self.principal, text='ADICIONAR\n Cliente', bg=cor6, compound='center',bd=0, font=('arial 14 bold'), foreground='white')
        self.btn_addcliente.place(relx=0.9, rely=0, relheight=0.1, relwidth=0.1)
        #título 
        self.titulo = Label(self.principal, text='Ficha de Cadastro de Clientes', bg='white', font=('arial 16 bold'))
        self.titulo.place(relx=0., rely=0.1, relwidth=0.5, relheight=0.1)
        #imagem        
        self.icone_cliente = PhotoImage(file='imagens/pessoa.png')        
        self.label_cliente = Label(self.principal, image=self.icone_cliente, bg='white')        
        self.label_cliente.place(relx=0.01, rely=0.12)
        self.linha = Frame(self.principal, bg=cor5)
        self.linha.place(relx=0.146, rely=0.17, relwidth=0.71, relheight=0.004)
        # Entrys
            #nome
        self.title_nome = Label(self.principal, text='NOME:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_nome.place(relx=0.148, rely=0.195)
        self.e_nome = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_nome.place(relx=0.150, rely=0.24, relwidth=0.25, relheight=0.04)
        self.e_nome.insert(0, "Nome do Cliente")
        self.e_nome.bind("<FocusIn>", lambda event: self.e_nome.delete(0, "end"))
            #sobrenome
        self.title_sobrenome = Label(self.principal, text='SOBRENOME:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_sobrenome.place(relx=0.416, rely=0.195)
        self.e_sobrenome = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_sobrenome.place(relx=0.42, rely=0.24, relwidth=0.25, relheight=0.04)
        self.e_sobrenome.insert(0, "Sobrenome ou Apelido")
        self.e_sobrenome.bind("<FocusIn>", lambda event: self.e_sobrenome.delete(0, "end"))
            #CPF
        self.title_cpf = Label(self.principal, text='CPF', font=('arial 12'), foreground= cor4, bg='white')
        self.title_cpf.place(relx=0.148, rely=0.30)
        self.e_cpf = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_cpf.place(relx=0.150, rely=0.35, relwidth=0.15, relheight=0.04)
        self.e_cpf.insert(0, 'Digite apenas números')
        self.e_cpf.bind("<FocusIn>", lambda event: self.e_cpf.delete(0, "end"))        
        self.e_cpf.bind("<KeyRelease>", lambda event: format_cpf(self.e_cpf))    
    
Applicantion()

        
          

    