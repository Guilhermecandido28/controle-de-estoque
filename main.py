from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image
from limpar import limpar
from clientes.cliente import Cliente



janela = Tk()


class Applicantion(Cliente):
    def __init__(self):
        self.janela = janela        
        self.tela()
        self.frames()
        self.buttons()
        self.temporario = Label(text='voce esta no home', font=('arial 18 bold'))
        self.temporario.place(relx=.5, rely=.5)                  
        janela.mainloop()

    def tela(self):
        self.janela.title('Controle fincanceiro')
        self.janela.geometry('1500x1000')
        self.janela.configure(background= cor5)
        janela.minsize(1500, 1000)
    
    def frames(self):
        self.header = tk.Frame(self.janela, bg=cor3)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.09)
        self.menu = tk.Frame(self.janela, bg=cor4)
        self.menu.place(relx=0, rely=0.09, relwidth=1, relheight=0.05)
        self.location = tk.Frame(self.janela, bg=cor1)
        self.location.place(relx=0, rely=0.14, relwidth=1, relheight=0.09)        
    def cliente(self):
        cliente = Cliente(self.janela)
        cliente.clientes()
        cliente.buscar_cliente()        
        cliente.inserir_dados()
        cliente.clientes_na_treeview()

             
    def buttons(self):
        
 
        #Botão cliente
        self.img_cliente = PhotoImage(file='imagens/cliente.png')
        self.btn_clientes = Button(self.menu, text='Clientes', image=self.img_cliente, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.cliente)
        self.btn_clientes.place(relx=0, rely=0, relwidth=0.14, relheight=1)
        #botão vendas
        self.img_vendas = PhotoImage(file='imagens/vendas.png')
        self.btn_vendas = Button(self.menu, text='Vendas', image=self.img_vendas, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2')
        self.btn_vendas.place(relx=0.14, rely=0, relwidth=0.14, relheight=1)
        # Fornecedor
        self.img_fornecedor = PhotoImage(file='imagens/fornecedor.png')
        self.btn_fornecedor = Button(self.menu, text='Fornecedor', image=self.img_fornecedor, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2')
        self.btn_fornecedor.place(relx=0.28, rely=0, relwidth=0.14, relheight=1)
        #estoque
        self.img_estoque= PhotoImage(file='imagens/estoque.png')
        self.btn_estoque = Button(self.menu, text='Estoque', image=self.img_estoque, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2')
        self.btn_estoque.place(relx=0.42, rely=0, relwidth=0.14, relheight=1)
        #compras
        self.img_compras= PhotoImage(file='imagens/compras.png')
        self.btn_compras = Button(self.menu, text='Compras', image=self.img_compras, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2')
        self.btn_compras.place(relx=0.56, rely=0, relwidth=0.14, relheight=1)
        #financeiro
        self.img_financeiro= PhotoImage(file='imagens/financeiro.png')
        self.btn_financeiro = Button(self.menu, text='Financeiro', image=self.img_financeiro, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2')
        self.btn_financeiro.place(relx=0.7, rely=0, relwidth=0.14, relheight=1)
        #configurações
        self.img_settings= PhotoImage(file='imagens/settings.png')
        self.btn_settings = Button(self.menu, text='Configurações', image=self.img_settings, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2')
        self.btn_settings.place(relx=0.84, rely=0, relwidth=0.14, relheight=1)
        #home
        self.img_home = PhotoImage(file='imagens/home.png')
        self.btn_home = Button(self.header, image=self.img_home, bg=cor3, bd=0, font=('arial 12 bold'), cursor='hand2')
        self.btn_home.place(relx=0, rely=0, relheight=1, relwidth=0.05)

    
               
Applicantion()