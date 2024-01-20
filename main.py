from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from limpar import limpar
from clientes.cliente import Cliente
from home import Home
from estoque.estoque import Estoque
from fornecedor.fornecedor import Fornecedor
from compra.compra import Compra
from vendas.vendas import Vendas
from financeiro.financeiro import Financeiro
from trocas.troca import Troca
import os
import requests
from tkinter import messagebox
import wget
from subprocess import Popen
from packaging import version



janela = Tk()



class Applicantion(Cliente, Home, Estoque, Compra, Vendas, Financeiro, Troca):
    
    def __init__(self):
        self.janela = janela 
        self.tela()
        self.frames()        
        self.buttons()
        self.home_widgets_criados = False
        self.cliente_widgets_criados = False
        self.estoque_widgets_criados = False 
        self.fornecedor_widgets_criados = False 
        self.compra_widgets_criados = False 
        self.venda_widgets_criados = False  
        self.financeiro_widgets_criados = False  
        self.troca_widgets_criados = False
        self.check_updates()            
        janela.mainloop()        


    def check_updates(self):
        github_api_url = 'https://api.github.com/repos/Guilhermecandido28/controle-de-estoque/releases/latest'

        try:
            response = requests.get(github_api_url)
            response.raise_for_status()
            latest_version = response.json()['name']

            
            current_version = '1.6'

            
            if version.parse(latest_version) > version.parse(current_version):
                resposta = messagebox.askquestion('Atualização Disponível',
                                                f'Nova versão {latest_version} disponível! Deseja atualizar?')

                if resposta == 'yes':
                    
                    installer_url = 'https://github.com/Guilhermecandido28/controle-de-estoque/releases/latest/download/mysetup.exe'

                    
                    installer_path = wget.download(installer_url)

                    
                    Popen([installer_path])

                    messagebox.showinfo('Atualização Concluída',
                                        f'A versão {latest_version} foi instalada com sucesso. O aplicativo será reiniciado.')
                    os.remove(installer_path)
                else:
                    messagebox.showinfo('Atualização Cancelada', 'Você optou por não atualizar neste momento.')
            else:
                pass
        except requests.RequestException as e:
            messagebox.showwarning('Erro de Conexão', f'Erro ao verificar atualizações: {str(e)}')

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
    def venda(self):
        global venda
        if not self.venda_widgets_criados:                        
            venda = Vendas(self.janela)
            self.esquecer_functions()
            self.venda_widgets_criados = True 
        else:
            pass

    def compra(self):
        global compra 
        if not self.compra_widgets_criados:
            compra = Compra(self.janela)
            compra.filtro_busca_compra()
            self.esquecer_functions()
            self.compra_widgets_criados = True
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

    def financa(self):
        global financeiro
        if not self.financeiro_widgets_criados:
            financeiro = Financeiro(self.janela)
            financeiro.financeiro()
            self.esquecer_functions()
            self.financeiro_widgets_criados = True
        else:
            pass


    def trocas(self):
        global troca
        if not self.troca_widgets_criados:
            troca = Troca(self.janela)
            troca.troca()
            self.esquecer_functions()
            self.troca_widgets_criados = True
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
        if self.compra_widgets_criados:
            compra.f_filtros_busca.place_forget()
            compra.principal.place_forget()            
            compra.location_compra.place_forget()
            compra.f_add_compra.place_forget()
            compra.titulos.place_forget()
            self.compra_widgets_criados = False
        if self.venda_widgets_criados:            
            venda.principal.place_forget() 
            venda.location_venda.place_forget()  
            venda.frame_codigo.place_forget() 
            venda.titulos.place_forget() 
            self.venda_widgets_criados = False
        if self.financeiro_widgets_criados:
            financeiro.principal.place_forget()
            financeiro.location_financeiro.place_forget()
            self.financeiro_widgets_criados = False
        if self.troca_widgets_criados:
            troca.principal.place_forget()
            troca.location_troca.place_forget()
            
            self.troca_widgets_criados = False

                   
 
    def buttons(self):         
        #Botão cliente
        cliente= os.path.abspath('imagens/cliente.png')
        self.img_cliente = PhotoImage(file=cliente)
        self.btn_clientes = Button(self.menu, text='Clientes', image=self.img_cliente, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.cliente)
        self.btn_clientes.place(relx=0, rely=0, relwidth=0.14, relheight=1)
        #botão vendas
        vendas = os.path.abspath('imagens/vendas.png')
        self.img_vendas = PhotoImage(file=vendas)
        self.btn_vendas = Button(self.menu, text='Vendas', image=self.img_vendas, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.venda)
        self.btn_vendas.place(relx=0.14, rely=0, relwidth=0.14, relheight=1)
        # Fornecedor
        fornecedor = os.path.abspath('imagens/fornecedor.png')
        self.img_fornecedor = PhotoImage(file=fornecedor)

        self.btn_fornecedor = Button(self.menu, text='Fornecedor', image=self.img_fornecedor, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.fornecedor)
        self.btn_fornecedor.place(relx=0.28, rely=0, relwidth=0.14, relheight=1)
        #estoque
        estoque = os.path.abspath('imagens/estoque.png')
        self.img_estoque= PhotoImage(file=estoque)
        self.btn_estoque = Button(self.menu, text='Estoque', image=self.img_estoque, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.estoque)
        self.btn_estoque.place(relx=0.42, rely=0, relwidth=0.14, relheight=1)
        #compras
        compras = os.path.abspath('imagens/compras.png')
        self.img_compras= PhotoImage(file=compras)
        self.btn_compras = Button(self.menu, text='Compras', image=self.img_compras, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.compra)
        self.btn_compras.place(relx=0.56, rely=0, relwidth=0.14, relheight=1)
        #financeiro
        financeiro = os.path.abspath('imagens/financeiro.png')
        self.img_financeiro= PhotoImage(file=financeiro)
        self.btn_financeiro = Button(self.menu, text='Financeiro', image=self.img_financeiro, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.financa)
        self.btn_financeiro.place(relx=0.7, rely=0, relwidth=0.14, relheight=1)
        #troca
        troca = os.path.abspath('imagens/troca.png')
        self.img_settings= PhotoImage(file=troca)
        self.btn_settings = Button(self.menu, text='Trocas', image=self.img_settings, compound=LEFT, bg=cor4, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.trocas)
        self.btn_settings.place(relx=0.84, rely=0, relwidth=0.14, relheight=1)
        #home
        home = os.path.abspath('imagens/home.png')
        self.img_home = PhotoImage(file=home)
        self.btn_home = Button(self.header, image=self.img_home, bg=cor3, bd=0, font=('arial 12 bold'), cursor='hand2', command=self.home)
        self.btn_home.place(relx=0, rely=0, relheight=1, relwidth=0.05)   
  
              
Applicantion()