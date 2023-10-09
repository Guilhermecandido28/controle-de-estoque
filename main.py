from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image
from limpar import limpar
from clientes.cliente import Cliente
from tkinter import messagebox
from home import Home
from PIL import Image, ImageTk
from estoque.estoque import Estoque
from fornecedor.fornecedor import Fornecedor



janela = Tk()



class Applicantion(Cliente, Home, Estoque):
    
    def __init__(self):
        self.janela = janela 
        self.tela()
        self.frames()        
        self.buttons()
        self.home_widgets_criados = False
        self.cliente_widgets_criados = False
        self.estoque_widgets_criados = False 
        self.fornecedor_widgets_criados = False               
        janela.mainloop()
        
 
    def tela(self):
        self.janela.title('Controle fincanceiro')
        self.janela.geometry('1500x1000')
        self.janela.configure(background= "#8A8A8A")
        janela.minsize(1500, 1000)


    def frames(self):
        self.header = tk.Frame(self.janela, bg=cor3)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.09)
        self.menu = tk.Frame(self.janela, bg=cor4)
        self.menu.place(relx=0, rely=0.09, relwidth=1, relheight=0.05)
        
                
    def cliente(self):
        global cliente
        if not self.cliente_widgets_criados:                        
            cliente = Cliente(self.janela)
            cliente.clientes()
            cliente.buscar_cliente()        
            cliente.inserir_dados()
            cliente.clientes_na_treeview()
            self.esquecer_functions()
            self.cliente_widgets_criados = True 
        else:
            pass          
          
         
    def estoque(self):
        global estoque
        if not self.estoque_widgets_criados:
            estoque = Estoque(self.janela)
            estoque.estoques()
            self.esquecer_functions()
            self.estoque_widgets_criados = True
        else:
            pass
    
    def fornecedor(self):
        global fornecedor
        if not self.fornecedor_widgets_criados:
            fornecedor = Fornecedor(self.janela)
            fornecedor.fornecedores()
            self.esquecer_functions()
            self.fornecedor_widgets_criados = True
        else:
            pass

    def home(self):
        global home
        if not self.home_widgets_criados:
            home = Home(self.janela)
            home.frame_home()
            self.esquecer_functions()
            self.home_widgets_criados = True
        else:
            pass

            
    def esquecer_functions(self):
        if self.cliente_widgets_criados:        
            cliente.principal.place_forget()
            cliente.location.place_forget()
            cliente.f_editar_cliente.place_forget()
            cliente.f_add_cliente.place_forget()
            self.cliente_widgets_criados = False            
        if self.estoque_widgets_criados:          
            estoque.principal.place_forget()
            estoque.location_est.place_forget()
            estoque.f_add_estoque.place_forget()
            estoque.f_editar_estoque.place_forget()
            self.estoque_widgets_criados = False            
        if self.home_widgets_criados:
            home.home.place_forget()
            self.home_widgets_criados = False
        if self.fornecedor_widgets_criados:
            fornecedor.principal.place_forget()
            fornecedor.location_est.place_forget()
            fornecedor.f_add_fornecedor.place_forget()
            fornecedor.f_editar_fornecedor.place_forget()
            self.fornecedor_widgets_criados = False
                   
 
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
        self.btn_fornecedor = Button(self.menu, text='Fornecedor', image=self.img_fornecedor, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.fornecedor)
        self.btn_fornecedor.place(relx=0.28, rely=0, relwidth=0.14, relheight=1)
        #estoque
        self.img_estoque= PhotoImage(file='imagens/estoque.png')
        self.btn_estoque = Button(self.menu, text='Estoque', image=self.img_estoque, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.estoque)
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
        self.btn_home = Button(self.header, image=self.img_home, bg=cor3, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.home)
        self.btn_home.place(relx=0, rely=0, relheight=1, relwidth=0.05)   
  
              
Applicantion()