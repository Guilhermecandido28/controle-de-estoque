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
from compra.listadecompras import ListaCompras
from compra.add_compra import AddCompra



class Compra():
    def __init__(self, frame) -> None:
        self.principal = tk.Frame(frame, background='black')
        self.f_editar_compra = tk.Frame(frame, bg='white')
        self.f_add_compra = tk.Frame(frame, bg= 'white')
        self.location_compra = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.f_filtros_busca = tk.Frame(frame, bg='#8A8A8A')
        self.titulos = tk.Frame(frame, bg='#8A8A8A')
        self.nova_compra()
        self.lista_compras()
        self.filtros_busca()
        self.onde_estou()

    def lista_compras(self):
        self.text_list = [
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
    ('Produtos', '13/10/2023', '17/10/2023', 'pendente', 'editar'),
             ]
        lista_compras = ListaCompras(self.principal, self.text_list, 100)
        for index, item in enumerate(self.text_list):
            lista_compras.creat_compra(index, item).pack(expand= True, fill='both', padx=10)

    def onde_estou(self):
        #aqui coloca o frame de localização usando o metodo place
        self.location_compra.place(relx=0, rely=0.14, relwidth=1, relheight=0.09)

            # coloca o nome da localização: COMPRA
        self.location_compra.create_text(100,30, text='COMPRA', anchor=NW, font=('arial 18 bold underline'))

            # coloca a imagem de fundo e a torna responsiva
        self.img_location_compra = Image.open('imagens/location.png')
        self.img_location_compra_tk = ImageTk.PhotoImage(self.img_location_compra)
        self.location_compra.bind('<Configure>', self.resize_image)


    def filtro_busca_compra(self):
        #aqui é o campo buscar
        self.search_compra = Entry(self.f_filtros_busca, font=('arial 14'), bg="#8A8A8A", bd=0)

            #aqui insere um texto explicativo
        self.search_compra.insert(0, "Procure por compra...")

            #aqui quando o campo é selecionado, deleta o texto explicativo
        self.search_compra.bind("<FocusIn>", lambda event: self.search_compra.delete(0, "end"))

            #aqui coloca o campo buscar no layout
        self.search_compra.place(relx=0, rely=0, relheight=1, relwidth=0.4)

        #botão_pesquisar
            #coloca a imagem no botão
        self.img_search_compra = PhotoImage(file='imagens/search.png')
        self.btn_search_compra = Button(self.f_filtros_busca, image=self.img_search_compra, bg="#8A8A8A", bd=0, cursor='hand2')
        self.btn_search_compra.place(relx=0.3, rely=0.15)
        self.search_compra.bind('<Return>', self.on_enter_compra)
        #Botão_imprimir
        self.img_print_compra = PhotoImage(file='imagens/impressora.png')
        self.btn_print_compra = Button(self.f_filtros_busca, image=self.img_print_compra, bg="#8A8A8A", bd=0, cursor='hand2')
        self.btn_print_compra.place(relx=0.35, rely=0.15)
        
        # botão de adicionar compra
        self.btn_addcompra = Button(self.f_filtros_busca, text='ADICIONAR\n Compra', bg='light gray', compound='center',bd=0, font=('arial 14 bold'), foreground='black', cursor='hand2', command=self.adicionar_compra)
            # coloca o botão no layout
        self.btn_addcompra.place(relx=0.9, rely=0, relheight=1, relwidth=0.1)

        # aqui é posto o frame que vai conter o cabeçalho da lista       
        self.titulos.place(relx=0.01, rely=.3, relwidth=0.98, relheight=.02)

        # titulo numero
        self.n_compra = Label(self.titulos, text='N°', bg='#8A8A8A', font=('arial 10 bold'),  borderwidth=2, relief='solid')
            #aqui é posto o titulo numero no layout
        self.n_compra.place(relx=0, rely=0, relheight=1, relwidth=.08)

        #titulo fornecedor
        self.fornecedor_compra = Label(self.titulos, text='Produto', bg='#8A8A8A', font=('arial 10 bold'),  borderwidth=2, relief='solid')
            #aqui é posto o titulo fornecedor no layout
        self.fornecedor_compra.place(relx=0.08, rely=0, relheight=1, relwidth=.32)

        #titulo data de emissão
        self.data_emissao = Label(self.titulos, text='DATA EMISSÃO', bg='#8A8A8A', font=('arial 10 bold'),  borderwidth=2, relief='solid')
            #aqui é posto o titulo data de emissão no laytout
        self.data_emissao.place(relx=.4, rely=0, relheight=1, relwidth=.15)

        #titulo data de entrega
        self.data_entrega = Label(self.titulos, text='DATA ENTREGA', bg='#8A8A8A', font=('arial 10 bold'),  borderwidth=2, relief='solid')
            #aqui é posto o titulo data de entrega no layout
        self.data_entrega.place(relx=.55, rely=0, relheight=1, relwidth=.15)

        #titulo pagamento
        self.valor_pagamento = Label(self.titulos, text='PAGAMENTO', bg='#8A8A8A', font=('arial 10 bold'),  borderwidth=2, relief='solid')
            #aqui é posto o titulo pagamento no layout
        self.valor_pagamento.place(relx=.7, rely=0, relheight=1, relwidth=.15)

        self.editar = Label(self.titulos, text='EDITAR', bg='#8A8A8A', font=('arial 10 bold'),  borderwidth=2, relief='solid')
        self.editar.place(relx=.85, rely=0, relheight=1, relwidth=0.15)

    def editar_compra(self):
        #aqui é posto o frame para editar a compra
        self.editar.place(relx=.85, rely=0, relheight=1, relwidth=.15) 

    def nova_compra(self):
        #aqui coloca o frame responsavel pela lista
        self.principal.place(relx=0.01, rely=0.32, relwidth=0.98, relheight=0.65)
        

    def adicionar_compra(self):
        self.add_compra = AddCompra(self.f_add_compra)
        self.principal.place_forget()
        self.f_filtros_busca.place_forget()
        self.titulos.place_forget()

    def resize_image(self, event):
        self.nova_imagem_compra = self.img_location_compra.resize((event.width, event.height))
        self.nova_imagem_compra_tk = ImageTk.PhotoImage(self.nova_imagem_compra)
        self.location_compra.create_image(0,0, anchor = NW, image = self.nova_imagem_compra_tk)
        self.location_compra.image = self.nova_imagem_compra_tk
    


    
    def filtros_busca(self):
        # frame do filtro de busca
        self.f_filtros_busca.place(relx=0.01, rely=0.23, relheight=0.07, relwidth=0.98)

        # titulo da data de inicio
        self.title_data_inicio = Label(self.f_filtros_busca, text='Data de Início', bg="#8A8A8A", font=('arial 10 bold'))

        #titulo da data fim 
        self.title_data_fim = Label(self.f_filtros_busca, text='Data Fim', bg="#8A8A8A", font=('arial 10 bold'))

        # a entry da do calendario de inicio      
        self.calendario_inicio = DateEntry(self.f_filtros_busca, selectmode= 'day', background="#8A8A8A", font=('arial 14 bold'))

        #a entry do calendario fim
        self.calendario_fim = DateEntry(self.f_filtros_busca, selectmode= 'day', background="#8A8A8A", font=('arial 14 bold'))

        # aqui pega a data de inicio selecionada e formata a data de inicio
        self.fdata_inicio = self.calendario_inicio.get_date()
        self.fdata_inicio = self.fdata_inicio.strftime('%d/%m/%Y')

        # label da data de inicio
        self.data_inicio = Label(self.f_filtros_busca, text=self.fdata_inicio, bg='#8A8A8A', font=('arial 14 bold'))

        #aqui pega a data fim selecionada e formata
        self.fdata_fim = self.calendario_fim.get_date()
        self.fdata_fim = self.fdata_fim.strftime('%d/%m/%Y')

        # label da data fim
        self.data_fim = Label(self.f_filtros_busca, text=self.fdata_fim, bg='#8A8A8A', font=('arial 14 bold'))

        # label pagamento 
        self.pagamentos = Label(self.f_filtros_busca, text='Pagamentos', bg='#8A8A8A', font=('arial 10 bold'))

        #combobox para o status do pagamento
        self.pagamento_way = ctk.CTkComboBox(self.f_filtros_busca,values=['Pendente', 'Concluído', 'Ambos']) 

        #label entrega
        self.entrega = Label(self.f_filtros_busca, text='Entrega', bg='#8A8A8A', font=('arial 10 bold'))

        #combobox para filtrar o status da entrega
        self.entrega_way = ctk.CTkComboBox(self.f_filtros_busca, values=['Entregue', 'Pendente', 'Ambos'])                                            


        #metodo bind para atualizar a data assim que for selecionada
        self.calendario_inicio.bind("<<DateEntrySelected>>", self.atualizar_label_data_inicio)
        self.calendario_fim.bind("<<DateEntrySelected>>", self.atualizar_label_data_fim)

        # aqui coloca os widgets no frame
        self.calendario_fim.place(relx=0.62, rely=0.55, relheight=0.3, relwidth=.010)
        self.calendario_inicio.place(relx=0.5, rely=0.55, relheight=0.3, relwidth=.010)
        self.title_data_inicio.place(relx=.42, rely=0)
        self.title_data_fim.place(relx=.55, rely=0)
        self.data_inicio.place(relx=.42, rely=0.50)
        self.data_fim.place(relx=.54, rely=.5)
        self.pagamentos.place(relx=.66, rely=0)
        self.pagamento_way.place(relx=.66, rely=.5, relwidth=.07)
        self.entrega.place(relx=.76,rely=0)
        self.entrega_way.place(relx=.76, rely=.5, relwidth=.07)



    def atualizar_label_data_inicio(self, event):
        nova_data = self.calendario_inicio.get_date()
        nova_data_formatada = nova_data.strftime('%d/%m/%Y')
        self.data_inicio.config(text=nova_data_formatada)
    def atualizar_label_data_fim(self, event):
        nova_data = self.calendario_fim.get_date()
        nova_data_formatada = nova_data.strftime('%d/%m/%Y')
        self.data_fim.config(text=nova_data_formatada)

    def on_enter_compra(self,event):
        pass