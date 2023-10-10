from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image
from limpar import limpar
from PIL import Image, ImageTk
from datetime import datetime
from estoque.banco_dados_estoque import *



class Home():
    def __init__(self, frame):
        self.home = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.valores()
    
    def frame_home(self):
        self.layout_home = Image.open('imagens/layout_home1.png')       
        self.home.place(relx=0.10, rely=.15, relheight=.8, relwidth=.8)        
        self.layout_home_tk = PhotoImage(self.layout_home)
        self.home.bind('<Configure>', self.resize_layout)


    def resize_layout(self, event):
        self.nova_layout = self.layout_home.resize((event.width, event.height))
        self.nova_layout_tk = ImageTk.PhotoImage(self.nova_layout)
        self.home.create_image(0,0, anchor = NW, image = self.nova_layout_tk)
        self.home.image = self.nova_layout_tk

    def valores(self):
        self.seta_cima = PhotoImage(file='imagens/seta_cima.png')
        self.seta_baixo = PhotoImage(file='imagens/seta_baixo.png')
        # estoque baixo
        id_produto = "SELECT ID from estoque"
        estoque_baixo = "SELECT estoque_minimo from estoque"
        qtd_estoque = "SELECT quantidade from estoque"
        query_id = dql(id_produto)
        query_estoque_baixo = dql(estoque_baixo)
        query_qtd_estoque = dql(qtd_estoque)       
        dic_estoque = {}
        contagem_estoque_baixo = 0
        if (
        query_id
        and query_estoque_baixo
        and query_qtd_estoque
        and len(query_id) == len(query_estoque_baixo)
        and len(query_id) == len(query_qtd_estoque)):
            for i in range(len(query_id)):
                id_produto = query_id[i][0]  
                estoque_min = query_estoque_baixo[i][0]  
                quantidade = query_qtd_estoque[i][0]                  
                dic_estoque.setdefault("produto", []).append(id_produto)
                dic_estoque.setdefault("estoque_min", []).append(estoque_min)
                dic_estoque.setdefault("quantidade", []).append(quantidade)
                if estoque_min == quantidade:
                    contagem_estoque_baixo += 1            
            dic_estoque["produto"] = ", ".join(map(str, dic_estoque["produto"]))
            dic_estoque["estoque_min"] = ", ".join(map(str, dic_estoque["estoque_min"]))
            dic_estoque["quantidade"] = ", ".join(map(str, dic_estoque["quantidade"]))

            self.bx_estoque = Button(self.home, text=contagem_estoque_baixo, font=('arial 36 bold'), foreground='#B80502', bg='#A6A6A6', highlightthickness=0, bd=0, cursor='hand2')
            self.bx_estoque.config(activebackground=self.bx_estoque.cget("bg"))
        else:
            print("Erro: As consultas não retornaram a mesma quantidade de dados.")
                       
        self.bx_estoque.place(relx=0.06, rely=.07, relheight=0.045, relwidth=0.069)
        #----------- fim do estoque baixo ------------------------------------------#

        self.pedidos_receber = Label(self.home, text='02', font=('arial 36 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.pedidos_receber.place(relx=0.04, rely=.19,relwidth=0.10)
        query_produtos = "SELECT id from estoque"
        produtos = dql(query_produtos)
        qtd_produtos = len(produtos)
               
        self.p_cadastrados = Button(self.home, text=qtd_produtos, font=('arial 42 bold'), foreground='#FFFFFF', bg='#A6A6A6', highlightthickness=0, bd=0, justify='center')
        self.p_cadastrados.config(activebackground=self.bx_estoque.cget("bg"))
        self.p_cadastrados.place(relx=0.07, rely=.32, relheight=0.051, relwidth=.155)        
        self.vendas_dia = Label(self.home, image=self.seta_cima, compound='right', text='1050,00', font=('arial 36 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.vendas_dia.place(relx=.605, rely=.04,relwidth=0.18)
        self.vendas_mes = Label(self.home, image=self.seta_cima, compound='right', text='50,00', font=('arial 36 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.vendas_mes.place(relx=.605, rely=.17,relwidth=0.18)
        meses = {1: 'JANEIRO', 2: 'FEVEREIRO', 3: 'MARÇO', 4: 'ABRIL', 5: 'MAIO', 6: 'JUNHO', 7: 'JULHO', 8: 'AGOSTO', 9: 'SETEMBRO', 10: 'OUTUBRO', 11: 'NOVEMBRO', 12: 'DEZEMBRO',}
        self.titulo_vendas_mes = Label(self.home, text=f'VENDAS DE {meses[datetime.now().month]}', font=('inter 9'), fg='white', bg='#A6A6A6')
        self.titulo_vendas_mes.place(relx=.63, rely=.244)
        self.qtd_clientes = Label(self.home, text='04', font=('arial 42 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.qtd_clientes.place(relx=.64, rely=.30)
        self.a_receber = Label(self.home, image=self.seta_cima, compound='right', text='1350,00', font=('arial 36 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.a_receber.place(relx=.10, rely=.62)
        self.a_pagar = Label(self.home, image=self.seta_baixo, compound='right', text='678,56', font=('arial 36 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.a_pagar.place(relx=.10, rely=.84)
        self.credito = Label(self.home, image=self.seta_cima, compound='right', text='37,72', font=('arial 24 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.credito.place(relx=.68, rely=.565)
        self.debito = Label(self.home, image=self.seta_cima, compound='right', text='1350,00', font=('arial 24 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.debito.place(relx=.68, rely=.65)
        self.dinheiro = Label(self.home, image=self.seta_cima, compound='right', text='1350,00', font=('arial 24 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.dinheiro.place(relx=.68, rely=.735)
        self.pix = Label(self.home, image=self.seta_cima, compound='right', text='1350,00', font=('arial 24 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.pix.place(relx=.63, rely=.817)
        self.total = Label(self.home, text='TOTAL:', font=('inter 16 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.total.place(relx=.55, rely=.90)
        self.valor_total = Label(self.home, image=self.seta_cima, compound='right', text='R$ 7000', font=('inter 22 bold'), foreground='#FFFFFF', bg='#A6A6A6')
        self.valor_total.place(relx=.68, rely=.89)
        