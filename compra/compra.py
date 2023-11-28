from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from limpar import limpar
from PIL import Image, ImageTk
from compra.listadecompras import ListaCompras
from compra.add_compra import AddCompra
from bancodedados.banco_dados import *


class Compra():
    def __init__(self, frame) -> None:
        self.principal = tk.Frame(frame, background='black')
        self.f_add_compra = tk.Frame(frame, bg= 'white')
        self.location_compra = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.f_filtros_busca = tk.Frame(frame, bg='#8A8A8A')
        self.titulos = tk.Frame(frame, bg='#8A8A8A')
        self.banco_compra = BancoDeDados('compra.db')
        self.banco_estoque = BancoDeDados('estoques.db')
        self.nova_compra()
        self.lista_compras()
        self.filtros_busca()
        self.onde_estou()
        self.cabecalho()

    def lista_compras(self):
        query = '''SELECT id, fornecedor, data_compra, data_entrega, total, status FROM compras ORDER BY id'''
        self.text_list = self.banco_compra.dql(query)
               
        
        self.lista_compra = ListaCompras(self.principal, self.text_list, 100, self)
        for index, item in enumerate(self.text_list):
            self.lista_compra.creat_compra(self.text_list[index][0], item).pack(expand= True, fill='both', padx=10)
        self.img_voltar = PhotoImage(file='imagens/voltar.png')
        self.btn_voltar_add = Button(
            self.f_add_compra,
            image=self.img_voltar,
            bg='white',
            cursor='hand2',
            command=self.voltar,
            relief='flat')
        self.btn_voltar_add.place(relx=0.962, rely=0)

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
        self.search_compra = Entry(
            self.f_filtros_busca,
            font=('arial 14'),
            bg="#8A8A8A",
            bd=0
            )

            #aqui insere um texto explicativo
        self.search_compra.insert(0, "Procure por compra...")

            #aqui quando o campo é selecionado, deleta o texto explicativo
        self.search_compra.bind("<FocusIn>", lambda event: self.search_compra.delete(0, "end"))

            #aqui coloca o campo buscar no layout
        self.search_compra.place(
            relx=0,
            rely=0,
            relheight=1,
            relwidth=0.4
            )

        #botão_pesquisar
            #coloca a imagem no botão
        self.img_search_compra = PhotoImage(file='imagens/search.png')

        self.btn_search_compra = Button(
            self.f_filtros_busca,
            image=self.img_search_compra,
            bg="#8A8A8A",
            bd=0,
            cursor='hand2',
            command=self.procurar
            )
        self.btn_search_compra.place(
            relx=0.85,
            rely=0.15
            )        
        self.search_compra.bind('<Return>', self.on_enter_compra)

        # #Botão_imprimir
        # self.img_print_compra = PhotoImage(file='imagens/impressora.png')
        # self.btn_print_compra = Button(
        #     self.f_filtros_busca,
        #     image=self.img_print_compra,
        #     bg="#8A8A8A",
        #     bd=0,
        #     cursor='hand2'
        #     )
        # self.btn_print_compra.place(
        #     relx=0.35,
        #     rely=0.15
        #     )
        
        
        # botão de adicionar compra
        self.btn_addcompra = Button(
            self.f_filtros_busca,
            text='ADICIONAR\n Compra',
            bg='light gray',
            compound='center',
            bd=0,
            font=('arial 14 bold'),
            foreground='black',
            cursor='hand2',
            command=self.adicionar_compra
            )
        self.btn_addcompra.place(
            relx=0.9,
            rely=0,
            relheight=1,
            relwidth=0.1
            )
        
    def cabecalho(self):
        # titulo numero
        self.n_compra = Label(
            self.titulos,
            text='N°',
            bg='#8A8A8A',
            font=('arial 10 bold'),
              borderwidth=2,
              relief='solid'
              )
        self.n_compra.place(
            relx=0,
            rely=0,
            relheight=1,
            relwidth=.08
            )

        #titulo fornecedor
        self.fornecedor_compra = Label(
            self.titulos,
            text='Fornecedor',
            bg='#8A8A8A',
            font=('arial 10 bold'),
              borderwidth=2,
              relief='solid'
              ) 
        self.fornecedor_compra.place(
            relx=0.08,
            rely=0,
            relheight=1,
            relwidth=.32
            )           
        

        #titulo data de emissão
        self.data_emissao = Label(
            self.titulos,
            text='DATA COMPRA',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
            )
        self.data_emissao.place(
            relx=.4,
            rely=0,
            relheight=1,
            relwidth=.15
            )
                    

        #titulo data de entrega
        self.data_entrega = Label(
            self.titulos,
            text='DATA ENTREGA',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
              )
        self.data_entrega.place(
            relx=.55,
            rely=0,
            relheight=1,
            relwidth=.15
            )       

        #titulo pagamento
        self.valor_pagamento = Label(
            self.titulos,
            text='PAGAMENTO',
            bg='#8A8A8A',
            font=('arial 10 bold'),
            borderwidth=2,
            relief='solid'
            )           
        self.valor_pagamento.place(
            relx=.7,
            rely=0,
            relheight=1,
            relwidth=.15
            )

        self.editar = Label(
            self.titulos,
            text='EDITAR',
            bg='#8A8A8A',
            font=('arial 10 bold'),
              borderwidth=2,
              relief='solid'
              )        
        self.editar.place(
            relx=.85,
            rely=0,
            relheight=1,
            relwidth=0.15
            )       
        
        
        self.titulos.place(relx=0.01, rely=.3, relwidth=0.98, relheight=.02)
        
        
        
        
        
    def editar_compra(self):
        #aqui é posto o frame para editar a compra
        self.editar.place(
            relx=.85,
            rely=0,
            relheight=1,
            relwidth=.15
            ) 

    def nova_compra(self):
        #aqui coloca o frame responsavel pela lista
        self.principal.place(
            relx=0.01,
            rely=0.32,
            relwidth=0.98,
            relheight=0.65
            )
        

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
        self.f_filtros_busca.place(
            relx=0.01,
            rely=0.23,
            relheight=0.07,
            relwidth=0.98
            )                                      


    def on_enter_compra(self,event):
        pass

    def voltar(self):        
        self.f_add_compra.place_forget()  
        self.nova_compra()        
        self.filtros_busca()
        self.cabecalho()

    def procurar(self):
        palavra_chave = self.search_compra.get().capitalize()
        if palavra_chave == 'Procure por compra...':
            pass     
        else:
            consulta = f"SELECT id, fornecedor, data_compra, data_entrega, total, status FROM compras " \
                        f"WHERE id LIKE '%{palavra_chave}%' " \
                        f"OR fornecedor LIKE '%{palavra_chave}%' " \
                        f"OR data_compra LIKE '%{palavra_chave}%' " \
                        f"OR data_entrega LIKE '%{palavra_chave}%' " \
                        f"OR total LIKE '%{palavra_chave}%' " \
                        f"OR status LIKE '%{palavra_chave}%' " \
            
            linhas = self.banco_compra.dql(consulta)            
            self.lista_compra.clear_frame()
            for index, item in enumerate(linhas):
                self.lista_compra.creat_compra(linhas[index][0], item).pack(expand= True, fill='both', padx=10)