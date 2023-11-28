from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image
from limpar import limpar
from PIL import Image, ImageTk
from datetime import datetime
from bancodedados.banco_dados import *

import pandas as pd
import sqlite3



class Home():
    def __init__(self, frame):
        self.home = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.banco_estoque = BancoDeDados('estoque.db')
        self.banco_vendas = BancoDeDados('vendas.db')
        self.valores()

    def frame_home(self):
        self.layout_home = Image.open('imagens/layout_home1.png')
        self.home.place(relx=0.10, rely=.15, relheight=.8, relwidth=.8)
        self.layout_home_tk = PhotoImage(self.layout_home)
        self.home.bind('<Configure>', self.resize_layout)

    def resize_layout(self, event):
        self.nova_layout = self.layout_home.resize((event.width, event.height))
        self.nova_layout_tk = ImageTk.PhotoImage(self.nova_layout)
        self.home.create_image(0, 0, anchor=NW, image=self.nova_layout_tk)
        self.home.image = self.nova_layout_tk

    def valores(self):
        self.seta_cima = PhotoImage(file='imagens/seta_cima.png')
        self.seta_baixo = PhotoImage(file='imagens/seta_baixo.png')
        # estoque baixo
        id_produto = "SELECT ID from estoque"
        estoque_baixo = "SELECT estoque_minimo from estoque"
        qtd_estoque = "SELECT quantidade from estoque"
        query_id = self.banco_estoque.dql(id_produto)
        query_estoque_baixo = self.banco_estoque.dql(estoque_baixo)
        query_qtd_estoque = self.banco_estoque.dql(qtd_estoque)
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
            dic_estoque["produto"] = ", ".join(
                map(str, dic_estoque["produto"]))
            dic_estoque["estoque_min"] = ", ".join(
                map(str, dic_estoque["estoque_min"]))
            dic_estoque["quantidade"] = ", ".join(
                map(str, dic_estoque["quantidade"]))

            self.bx_estoque = Button(self.home, text=contagem_estoque_baixo, font=(
                'arial 36 bold'), foreground='#B80502', bg='#A6A6A6', highlightthickness=0, bd=0, cursor='hand2')
            self.bx_estoque.config(activebackground=self.bx_estoque.cget("bg"))
        else:
            print("Erro: As consultas não retornaram a mesma quantidade de dados.")

        self.bx_estoque.place(relx=0.06, rely=.07,
                              relheight=0.045, relwidth=0.069)
        # ----------- fim do estoque baixo ------------------------------------------#

        self.pedidos_receber = Label(
            self.home,
            text='02',
            font=('arial 36 bold'),
            foreground='#FFFFFF',
            bg='#A6A6A6')
        self.pedidos_receber.place(relx=0.04, rely=.19, relwidth=0.10)

        query_produtos = "SELECT id from estoque"
        produtos = self.banco_estoque.dql(query_produtos)
        qtd_produtos = len(produtos)

        self.p_cadastrados = Button(
            self.home,
            text=qtd_produtos,
            font=('arial 42 bold'),
            foreground='#FFFFFF',
            bg='#A6A6A6',
            highlightthickness=0,
            bd=0,
            justify='center')
        self.p_cadastrados.config(activebackground=self.bx_estoque.cget("bg"))
        self.p_cadastrados.place(relx=0.07, rely=.32, relheight=0.051, relwidth=.155)

        self.vendas_hoje = StringVar()
        data_hoje = datetime.today().strftime('%d/%m/%Y')        
        query = f"SELECT total FROM venda WHERE data LIKE '%{data_hoje}%'"
        total_vendas_dia = self.banco_vendas.dql(query)
        total_vendas_dia = [float(x[0].replace('R$', '').replace(',','.')) for x in total_vendas_dia]
        self.vendas_hoje.set(f'{sum(total_vendas_dia):.2f}'.replace('.',','))
        
        self.vendas_dia = Label(
            self.home,
            image=self.seta_cima,
            compound='right',            
            textvariable=self.vendas_hoje,
            font=('arial 36 bold'),
            foreground='#FFFFFF',
            bg='#A6A6A6')
        self.vendas_dia.place(relx=.605, rely=.04, relwidth=0.18)

        self.vendas_do_mes = StringVar()
                
        # Conecte-se ao banco de dados SQLite
        conn = sqlite3.connect('vendas/vendas.db')

        # Execute a query e carregue os dados em um DataFrame do pandas
        df = pd.read_sql_query("SELECT * FROM venda", conn)
        df = df[['data', 'total']]
        df['data'] = pd.to_datetime(df['data'], format= '%d/%m/%Y %H:%M:%S')
        df_atual = df[df['data'].dt.month == pd.Timestamp.now().month]
        # Remova o símbolo 'R$' e converta a coluna para float
        df_atual['total'] = df_atual['total'].str.replace('R$', '').str.replace(',', '.').astype(float)

        # Some todos os valores na coluna 'total'
        soma_total = df_atual['total'].sum()

        self.vendas_do_mes.set(f'{float(soma_total):.2f}'.replace('.',','))
        conn.close()

        self.vendas_mes = Label(
            self.home,
            image=self.seta_cima,
            compound='right',
            textvariable=self.vendas_do_mes,
            font=('arial 36 bold'),
            foreground='#FFFFFF',
            bg='#A6A6A6')
        self.vendas_mes.place(relx=.605, rely=.17, relwidth=0.18)

        meses = {1: 'JANEIRO',
        2: 'FEVEREIRO',
        3: 'MARÇO',
        4: 'ABRIL',
        5: 'MAIO',
        6: 'JUNHO',
        7: 'JULHO',
        8: 'AGOSTO',
        9: 'SETEMBRO',
        10: 'OUTUBRO',
        11: 'NOVEMBRO',
        12: 'DEZEMBRO', }

        self.titulo_vendas_mes = Label(
            self.home,
            text=f'VENDAS DE {meses[datetime.now().month]}',
            font=('inter 9'),
            fg='white',
            bg='#A6A6A6')
        self.titulo_vendas_mes.place(relx=.63, rely=.244)

        query_cliente = f"SELECT cliente FROM venda WHERE data LIKE '%{data_hoje}%'"
        clientes = self.banco_vendas.dql(query_cliente)
        clientes = [x[0] for x in clientes]
        clientes = set(clientes)

        self.qtd_clientes = Label(
        self.home,
        text=len(clientes),
        font=('arial 42 bold'),
        foreground='#FFFFFF',
        bg='#A6A6A6')
        self.qtd_clientes.place(relx=.64, rely=.30)

        self.a_receber = Label(
        self.home,
        image=self.seta_cima,
        compound='right',
        text='1350,00',
        font=('arial 36 bold'),
        foreground='#FFFFFF',
        bg='#A6A6A6')
        self.a_receber.place(relx=.10, rely=.62)

        self.a_pagar = Label(
        self.home,
        image=self.seta_baixo,
        compound='right',
        text='678,56',
        font=('arial 36 bold'),
        foreground='#FFFFFF',
        bg='#A6A6A6')
        self.a_pagar.place(relx=.10, rely=.84)

    
        forma_credito = StringVar()
        consulta_credito = 'Crédito'
        query_credito =f"SELECT total FROM venda WHERE forma_pagamento LIKE '%{consulta_credito}%'"
        credito = self.banco_vendas.dql(query_credito)
        credito = [float(x[0].replace('R$', '0').replace(',','.')) for x in credito]
        forma_credito.set(f'{sum(credito):.2f}'.replace('.',','))

        self.credito = Label(
        self.home,
        image=self.seta_cima,
        compound='right',
        textvariable= forma_credito,
        font=('arial 24 bold'),
        foreground='#FFFFFF',
        bg='#A6A6A6')
        self.credito.place(relx=.68, rely=.565)

        forma_debito = StringVar()
        consulta_debito = 'Débito'
        query_debito =f"SELECT total FROM venda WHERE forma_pagamento LIKE '%{consulta_debito}%'"
        debito = self.banco_vendas.dql(query_debito)
        debito = [float(x[0].replace('R$', '0').replace(',','.')) for x in debito]
        forma_debito.set(f'{sum(debito):.2f}'.replace('.',','))

        self.debito = Label(
        self.home,
        image=self.seta_cima,
        compound='right',
        textvariable=forma_debito,
        font=('arial 24 bold'),
        foreground='#FFFFFF',
        bg='#A6A6A6')
        self.debito.place(relx=.68, rely=.65)
        
        forma_dinheiro = StringVar()
        consulta_dinheiro = 'Dinheiro'
        query_dinheiro =f"SELECT total FROM venda WHERE forma_pagamento LIKE '%{consulta_dinheiro}%'"
        dinheiro = self.banco_vendas.dql(query_dinheiro)
        dinheiro = [float(x[0].replace('R$', '0').replace(',','.')) for x in dinheiro]
        forma_dinheiro.set(f'{sum(dinheiro):.2f}'.replace('.',','))

        self.dinheiro = Label(
        self.home,
        image=self.seta_cima,
        compound='right',
        textvariable= forma_dinheiro,
        font=('arial 24 bold'),
        foreground='#FFFFFF',
        bg='#A6A6A6')
        self.dinheiro.place(relx=.68, rely=.735)

        forma_pix = StringVar()
        consulta_pix = 'Pix'
        query_pix =f"SELECT total FROM venda WHERE forma_pagamento LIKE '%{consulta_pix}%'"
        pix = self.banco_vendas.dql(query_pix)
        pix = [float(x[0].replace('R$', '0').replace(',','.')) for x in pix]
        forma_pix.set(f'{sum(pix):.2f}'.replace('.',','))

        self.pix = Label(
        self.home,
        image=self.seta_cima,
        compound='right',
        textvariable= forma_pix,
        font=('arial 24 bold'),
        foreground='#FFFFFF',
        bg='#A6A6A6')
        self.pix.place(relx=.63, rely=.817)

        self.total = Label(
        self.home,
        text='TOTAL:',
        font=('inter 16 bold'),
        foreground='#FFFFFF',
        bg='#A6A6A6')
        self.total.place(relx=.55, rely=.90)

        total = f'{sum(dinheiro)+sum(credito)+sum(pix)+sum(debito):.2f}'.replace('.',',')
        self.valor_total = Label(
        self.home,
        image=self.seta_cima,
        compound='right',
        text=total,
        font=('inter 22 bold'),
        foreground='#FFFFFF',
        bg='#A6A6A6')
        self.valor_total.place(relx=.68, rely=.89)
