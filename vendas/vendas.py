from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image, ImageTk
from compra.listadecompras import *
from estoque.banco_dados_estoque import dql_args
from tkinter import simpledialog
from tkinter import messagebox
import datetime
from vendas.bancodedadosvenda import vendas_dml
import pywhatkit as kt


class Vendas():
    def __init__(self, frame) -> None:
        self.principal = tk.Frame(frame, background='light gray')
        self.location_venda = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.frame_codigo = Frame(frame, background='light gray')
        self.titulos = Frame(frame)
        self.count = 0
        self.total = 0
        self.stringvar = StringVar()
        self.lista_vendas = []
        self.onde_estou()
        self.venda()
        self.init_entry()
        self.manter_foco_entry()

    def onde_estou(self):
        # aqui coloca o frame de localização usando o metodo place
        self.location_venda.place(
            relx=0, rely=0.14, relwidth=1, relheight=0.09)

        # coloca o nome da localização: COMPRA
        self.location_venda.create_text(
            100, 30, text='VENDAS', anchor=NW, font=('arial 18 bold underline'))

        # coloca a imagem de fundo e a torna responsiva
        self.img_location_compra = Image.open('imagens/location.png')
        self.img_location_compra_tk = ImageTk.PhotoImage(
            self.img_location_compra)
        self.location_venda.bind('<Configure>', self.resize_image)

    def resize_image(self, event):
        self.nova_imagem_venda = self.img_location_compra.resize(
            (event.width, event.height))
        self.nova_imagem_venda_tk = ImageTk.PhotoImage(self.nova_imagem_venda)
        self.location_venda.create_image(
            0, 0, anchor=NW, image=self.nova_imagem_venda_tk)
        self.location_venda.image = self.nova_imagem_venda_tk

    def init_entry(self):
        self.codigo = tk.Entry(
            self.frame_codigo,
            background='light gray',
            font=('arial 14 bold')
        )
        self.codigo.place(relx=.15, rely=.25, relwidth=.15, relheight=.5)
        self.codigo.bind(
            '<KeyRelease>', lambda event: self.info_produto(event))
        self.count = 0

    def venda(self):
        # aqui coloca o frame responsavel pela lista
        self.principal.place(relx=0.01, rely=0.32,
                             relwidth=0.98, relheight=0.65)
        self.frame_codigo.place(relx=0, rely=.23, relwidth=1, relheight=.06)
        self.titulos.place(relx=0.01, rely=.29, relwidth=.98, relheight=.03)
        Label(
            self.frame_codigo,
            font=('arial 16 bold'),
            text='Código de Barras:',
            bg='light gray'
        ).place(relx=0, rely=.25)

        Label(
            self.frame_codigo,
            font=('arial 16 bold'),
            text='Desconto %:',
            bg='light gray'
        ).place(relx=.31, rely=.25)

        self.desconto = Spinbox(
            self.frame_codigo,
            background='light gray',
            font=('arial 14 bold'),
            from_=0,
            to=999
        )
        self.desconto.place(relx=.41, rely=.25, relwidth=.05, relheight=.5)

        self.quantidade = Spinbox(
            self.frame_codigo,
            background='light gray',
            font=('arial 14 bold'),
            from_=1,
            to=999
        )
        self.quantidade.place(relx=.57, rely=.25, relwidth=.05, relheight=.5)

        Label(
            self.frame_codigo,
            text='Quantidade:',
            background='light gray',
            font=('arial 16 bold'),
        ).place(relx=.47, rely=.25)

        Label(
            self.titulos,
            text='Cód. Barras',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
        ).place(relx=0, rely=0.0, relwidth=.125, relheight=1)

        Label(
            self.titulos,
            text='Produto',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
        ).place(relx=.125, rely=0, relwidth=.125, relheight=1)

        Label(
            self.titulos,
            text='Categoria',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
        ).place(relx=.25, rely=0, relwidth=.125, relheight=1)

        Label(
            self.titulos,
            text='Marca',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
        ).place(relx=.375, rely=0, relwidth=.125, relheight=1)

        Label(
            self.titulos,
            text='Tamanho',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
        ).place(relx=.500, rely=0, relwidth=.125, relheight=1)

        Label(
            self.titulos,
            text='Cor',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
        ).place(relx=.625, rely=0, relwidth=.125, relheight=1)

        Label(
            self.titulos,
            text='Quantidade',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
        ).place(relx=.750, rely=0, relwidth=.0625, relheight=1)

        Label(
            self.titulos,
            text='Preço',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
        ).place(relx=.8125, rely=0, relwidth=.125, relheight=1)

        Label(
            self.titulos,
            text='Excluir',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
        ).place(relx=.9375, rely=0, relwidth=.0625, relheight=1)

        Label(
            self.frame_codigo,
            text='Total da Venda:',
            bg='light gray',
            font=('arial 12 bold')
        ).place(relx=.63, rely=.25)

        Label(
            self.frame_codigo,
            textvariable=self.stringvar,
            bg='light gray',
            font=('arial 26 bold'),
            foreground='green'
        ).place(relx=.73, rely=.10)

        Button(
            self.frame_codigo,
            text='Finalizar\nVenda',
            relief='flat',
            bd=0,
            highlightthickness=0,
            font=('arial 14 bold'),
            background='green',
            cursor='hand2',
            command=self.mostrar_dialogo_forma_pagamento
        ).place(relx=.93, rely=0, relheight=1, relwidth=.07)

        Button(
            self.frame_codigo,
            text='Aplicar\nDesconto',
            relief='flat',
            bd=0,
            highlightthickness=0,
            font=('arial 14 bold'),
            background='white',
            cursor='hand2',
            command=self.aplicar_desconto
        ).place(relx=.86, rely=0, relheight=1, relwidth=.07)

    def aplicar_desconto(self):
        desconto = int(self.desconto.get())/100*self.total
        self.stringvar.set(f'R${self.total-desconto:.2f}'.replace('.', ','))

    def clear_frame(self):
        for widget in self.principal.winfo_children():
            widget.pack_forget()

    def mostrar_vendas(self):
        self.clear_frame()
        self.vendas = ListaCompras(
            self.principal, self.lista_vendas, 100, self)

        for index, item in enumerate(self.lista_vendas):
            self.vendas.creat_venda(self.lista_vendas[index], index).pack(
                expand=True, fill='both', padx=10)

    def manter_foco_entry(self):
        self.codigo.focus_set()
        self.codigo.after(100, self.manter_foco_entry)

    def info_produto(self, event):

        codigo_barras = self.codigo.get()

        if len(codigo_barras) == 13:
            if self.count == 0:
                query = 'SELECT ID, descricao, categoria, marca, tamanho, cor, venda FROM estoque WHERE ID = ?'
                produto = dql_args(query, (codigo_barras,))
                self.lista_temporaria = []
                for item in produto[0]:
                    self.lista_temporaria.append(item)
                self.lista_temporaria.insert(6, self.quantidade.get())
                print(self.lista_temporaria)

                self.lista_vendas.append(self.lista_temporaria)
                print(self.lista_vendas)
                self.mostrar_vendas()
                self.codigo.delete(0, END)
                self.total_da_venda()

    def total_da_venda(self):
        if self.total == 0:
            for item in self.lista_vendas:
                self.total += int(item[-2])*float(item[-1])
                self.stringvar.set(f'R${self.total:.2f}'.replace('.', ','))

            return self.stringvar
        else:
            self.total -= self.total
            for item in self.lista_vendas:
                self.total += int(item[-2])*float(item[-1])
                self.stringvar.set(f'R${self.total:.2f}'.replace('.', ','))
            return self.stringvar

    def pegar_cliente(self):
        self.codigo.after_cancel(self.manter_foco_entry)
        cliente = simpledialog.askstring(
            "Vincular Cliente", 'Digite o Nome e Sobrenome do Cliente:').title()

        return cliente

    def mostrar_dialogo_forma_pagamento(self):
        self.forma_pagamento = StringVar()
        # Crie a janela de diálogo
        self.dialog = tk.Toplevel()
        self.dialog.title("Forma de Pagamento")
        # Crie botões para as opções de forma de pagamento
        opcoes = ["Dinheiro", "Crédito", "Débito", "PIX"]
        for opcao in opcoes:
            tk.Button(self.dialog, text=opcao,
                      command=lambda opcao=opcao: self.definir_forma_pagamento(opcao)).pack()

        self.dialog.protocol("WM_DELETE_WINDOW", lambda: self.definir_forma_pagamento(
            None))  # Lidar com o fechamento da janela
        # Ajuste o tamanho da janela conforme necessário
        self.dialog.geometry("300x150")
        self.dialog.attributes("-topmost", 1)  # Mantém a janela no topo

    # Função para definir a forma de pagamento e fechar a janela
    def definir_forma_pagamento(self, opcao):
        self.forma_pagamento.set(opcao)
        self.dialog.destroy()
        self.salvar_venda()

    def salvar_venda(self):
        self.data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        itens_formatados = []
        for sublista in self.lista_vendas:
            if len(sublista) >= 4:
                item1 = sublista[1]
                item2 = sublista[2]
                item4 = sublista[4]
                item6 = sublista[6]

                item_formatado = f"{item1} - {item2} - {item4} - {item6} unidade(s)"
                itens_formatados.append(item_formatado)

        self.resultado = ', '.join(itens_formatados)

        self.cliente = self.pegar_cliente()
        self.valor_forma_pagamento = self.forma_pagamento.get()
        self.info_desconto = f'{self.desconto.get()}%'
        self.total_bd = self.stringvar.get()

        query = "INSERT INTO venda (data, produtos, cliente, desconto, total, forma_pagamento) VALUES (?, ?, ?, ?, ?, ?)"
        vendas_dml(query, (self.data, self.resultado, self.cliente,
                   self.info_desconto, self.total_bd, self.valor_forma_pagamento))
        self.mensagem_whats()

    def mensagem_whats(self):
        mensagem = f'Em {self.data} foi realizada a venda de {self.total_bd} do(s) produto(s) {self.resultado} para o(a)  cliente {self.cliente}. Parabéns pela venda!'
        kt.sendwhatmsg_instantly(
            '+5511985518059', mensagem, tab_close=True, wait_time=10)
        messagebox.showinfo('Sucesso!', "Venda realizada com sucesso!")
