from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from limpar import limpar
from tkinter import ttk
from tkinter import messagebox
import io
from estoque.add_estoque import AddEstoque
from estoque.editar_estoque import EditarEstoque
from estoque.banco_dados_estoque import *
from PIL import Image, ImageTk
import subprocess
import os

class Estoque(EditarEstoque):
    def __init__(self, frame):
        self.principal = tk.Frame(frame, bg= 'white')
        self.f_editar_estoque = tk.Frame(frame, bg='white')
        self.f_add_estoque = tk.Frame(frame, bg= 'white')
        self.location_est = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.buscar_estoque_est()
        self.tree_estoque()
        self.estoque_na_treeview()
        
    def editar_estoque(self):        
        if self.estoque_treeview.selection() == ():
            messagebox.showerror('Erro', "Selecione um produto primeiro! ")
        else:
            self.f_editar_estoque.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.72)
            items_selecionado = []
            for item in self.estoque_treeview .selection():
                item_values = self.estoque_treeview .item(item, 'values')
                items_selecionado.append(item_values)            
            self.estoque_tree_scroll.place_forget()        
            self.limpar_treeview() 
            query_img = f"SELECT imagem FROM estoque WHERE id = {items_selecionado[0][0]}"
            img_em_bytes = dql(query_img)                       
            img = Image.open(io.BytesIO(img_em_bytes[0][0]))                                   
            self.ed_estoque = EditarEstoque(self.f_editar_estoque, img, id=items_selecionado[0][0])
            lista_entrys = [self.ed_estoque.ed_barcode, self.ed_estoque.ed_descricao, self.ed_estoque.ed_categoria, self.ed_estoque.ed_marca, self.ed_estoque.ed_estoque_min, self.ed_estoque.ed_quantidade, self.ed_estoque.ed_obs, self.ed_estoque.ed_tamanho, self.ed_estoque.ed_cor, self.ed_estoque.ed_preco_custo, self.ed_estoque.ed_preco_venda]        
            limpar(lista_entrys)            
            query =f"SELECT id, descricao, categoria, marca, estoque_minimo, quantidade, observacoes, tamanho, cor, custo, venda FROM estoque WHERE id = {items_selecionado[0][0]}"           

            dados = dql(query)            
            count=0
            for campo in lista_entrys:
                campo.insert(0, dados[0][count])
                count+=1

    def add_estoque(self):
        self.adicionar_estoque = AddEstoque(self.f_add_estoque)
        self.f_add_estoque.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.72)

    def estoques(self):
        self.location_est.place(relx=0, rely=0.14, relwidth=1, relheight=0.09)        
        self.img_location_est = Image.open('imagens/location.png')
        self.img_location_est_tk = ImageTk.PhotoImage(self.img_location_est)
        self.location_est.create_text(100,30, text='ESTOQUE', anchor=NW, font=('arial 18 bold underline'))
        self.location_est.bind('<Configure>', self.resize_image)
        self.principal.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.72)        
        #Botão_adicionar_estoque        
        self.btn_addestoque = Button(self.principal, text='ADICIONAR\n Estoque', bg='light gray', compound='center',bd=0, font=('arial 14 bold'), foreground='black', cursor='hand2', command=self.add_estoque)
        self.btn_addestoque.place(relx=0.9, rely=0, relheight=0.1, relwidth=0.1)
        #botão de editar estoque
        self.btn_edtestoque = Button(self.principal, text='EDITAR\n Estoque', bg='dark gray', compound='center',bd=0, font=('arial 14 bold'), foreground='black', cursor='hand2', command=self.editar_estoque)
        self.btn_edtestoque.place(relx=0.8, rely=0, relheight=0.1, relwidth=0.1)
        #excluir estoque        
        self.btn_exclestoque = Button(self.principal, text='EXCLUIR\n Estoque', bg='gray', compound='center',bd=0, font=('arial 14 bold'), foreground='black', cursor='hand2', command=self.excluir_estoque)
        self.btn_exclestoque.place(relx=0.7, rely=0, relheight=0.1, relwidth=0.1)
        #botão voltar
        self.img_voltar = PhotoImage(file='imagens/voltar.png')
        self.btn_voltar_editar = Button(self.f_editar_estoque, image=self.img_voltar, bg='white', cursor='hand2', command=self.voltar, relief='flat')
        self.btn_voltar_editar.place(relx=0.962, rely=0.0)
        #botão voltar        
        self.btn_voltar_add = Button(self.f_add_estoque, image=self.img_voltar, bg='white', cursor='hand2', command=self.voltar, relief='flat')
        self.btn_voltar_add.place(relx=0.962, rely=0)

    def voltar(self):
        self.f_editar_estoque.place_forget()
        self.f_add_estoque.place_forget()
        self.estoque_na_treeview()

    def resize_image(self, event):
        self.nova_imagem_est = self.img_location_est.resize((event.width, event.height))
        self.nova_imagem_est_tk = ImageTk.PhotoImage(self.nova_imagem_est)
        self.location_est.create_image(0,0, anchor = NW, image = self.nova_imagem_est_tk)
        self.location_est.image = self.nova_imagem_est_tk

    def buscar_estoque_est(self):
        self.search_est = Entry(self.principal, font=('arial 14'), bg="#8A8A8A", bd=0)
        self.search_est.insert(0, "Procure por produto...")
        self.search_est.bind("<FocusIn>", lambda event: self.search_est.delete(0, "end"))
        self.search_est.place(relx=0, rely=0, relheight=0.1, relwidth=0.7)
        #botão_pesquisar
        self.img_search_est = PhotoImage(file='imagens/search.png')
        self.btn_search_est = Button(self.principal, image=self.img_search_est, bg="#8A8A8A", bd=0, cursor='hand2', command=self.estoque_buscado)
        self.btn_search_est.place(relx=0.6, rely=0, relheight=0.1, relwidth=0.05)
        self.search_est.bind('<Return>', self.on_enter_est)
        #Botão_imprimir
        self.img_print_est = PhotoImage(file='imagens/impressora.png')
        self.btn_print_est = Button(self.principal, image=self.img_print_est, bg="#8A8A8A", bd=0, cursor='hand2')
        self.btn_print_est.place(relx=0.65, rely=0, relheight=0.1, relwidth=0.05)

    def tree_estoque(self):        
        self.estoque_tree_scroll = Scrollbar(self.principal)
        self.estoque_tree_scroll.place(relx=0.985, rely=0.1, relheight=.9, relwidth=.015)
        self.estoque_treeview = ttk.Treeview(self.principal, yscrollcommand=self.estoque_tree_scroll.set, show="headings")
        style = ttk.Style(self.estoque_treeview)
        style.configure("Treeview", font= ('arial 15 normal'),
                        rowheight= 40,
                        )
        style.configure("Treeview.Heading", font= ('arial 15 normal'), foreground='gray', padding=0 
                        )
        self.estoque_tree_scroll.config(command=self.estoque_treeview.yview)
        self.estoque_treeview['columns'] = ('CÓD. BARRAS', 'DESCRIÇÃO','CATEGORIA','MARCA','COR','FORNECEDOR', 'QUANTIDADE','TAMANHO', 'VENDA')
        self.estoque_treeview.heading('#1', text='CÓD. BARRAS', anchor=W)        
        self.estoque_treeview.heading('#2', text='DESCRIÇÃO')
        self.estoque_treeview.heading('#3', text='CATEGORIA')
        self.estoque_treeview.heading('#4', text='MARCA')
        self.estoque_treeview.heading('#5', text='COR')
        self.estoque_treeview.heading('#6', text='FORNECEDOR')
        self.estoque_treeview.heading('#7', text='QTD un.')
        self.estoque_treeview.heading('#8', text='TAM' )
        self.estoque_treeview.heading('#9', text='VENDA R$' )
        self.estoque_treeview.place(relx=0, rely=.1, relheight=.9, relwidth=.985)
        self.estoque_treeview.column("CÓD. BARRAS",width=160, stretch=FALSE, anchor='w')        
        self.estoque_treeview.column("DESCRIÇÃO", width=200, minwidth=250, stretch=TRUE, anchor='center')
        self.estoque_treeview.column("CATEGORIA", width=150, minwidth=150, stretch=TRUE, anchor='center')
        self.estoque_treeview.column("MARCA", width=100, minwidth=100, stretch=TRUE, anchor='center')
        self.estoque_treeview.column("COR", width=200, minwidth=250, stretch=TRUE, anchor='center')
        self.estoque_treeview.column("FORNECEDOR", width=100, minwidth=100, stretch=TRUE, anchor='center')
        self.estoque_treeview.column("QUANTIDADE",minwidth=50, stretch=TRUE, anchor='center')
        self.estoque_treeview.column("TAMANHO", minwidth=100, stretch=TRUE, anchor='center')        
        self.estoque_treeview.column("VENDA", minwidth=100, stretch=TRUE, anchor='center')


    def estoque_na_treeview(self):
        self.estoque_treeview.tag_configure('oddrow', background='white')
        self.estoque_treeview.tag_configure('evenrow', background='light gray') 
        if self.estoque_treeview:
            self.estoque_treeview.delete(*self.estoque_treeview.get_children())       
        query ="SELECT ID, descricao, categoria, marca, cor, fornecedor, quantidade, tamanho, venda FROM estoque order by ID"
        linhas= dql(query)
        count=0
        
        for i in linhas:
            if count % 2 == 0:    
                self.estoque_treeview.insert("", "end",values=i, tags=('oddrow',))             
                
                
            else:
                self.estoque_treeview.insert("", "end",values=i, tags=('evenrow',))
            count+=1 

    def excluir_estoque(self):
        items_selecionados = []
        item_id=[]        
        if self.estoque_treeview.selection() == ():
            messagebox.showerror('Erro', "Selecione um ou mais produto(s) primeiro! ")
        else:
            for item in self.estoque_treeview.selection():
                item_values = self.estoque_treeview.item(item, 'values')
                items_selecionados.append(item_values)
            for i, item in enumerate(items_selecionados):
                ids = items_selecionados[i][0]
                item_id.append(ids)
            for produto in item_id:
                query = "DELETE FROM estoque WHERE id=?"
                dml(query, (produto,))
            self.estoque_na_treeview()
            print('produto excluido')

    def estoque_buscado(self):        
        self.e_buscado = self.search_est.get()
        consulta = f"SELECT id, descricao, categoria, marca, cor, fornecedor, quantidade, tamanho, venda FROM estoque " \
        f"WHERE id LIKE '%{self.e_buscado}%' " \
        f"OR descricao LIKE '%{self.e_buscado}%' " \
        f"OR categoria LIKE '%{self.e_buscado}%' " \
        f"OR marca LIKE '%{self.e_buscado}%' " \
        f"OR cor LIKE '%{self.e_buscado}%' " \
        f"OR fornecedor LIKE '%{self.e_buscado}%' " \
        f"OR quantidade LIKE '%{self.e_buscado}%' " \
        f"OR tamanho LIKE '%{self.e_buscado}%' " \
        f"OR venda LIKE '%{self.e_buscado}%'"
        linhas = dql(consulta)
        count=0
        for item in self.estoque_treeview.get_children():
            self.estoque_treeview.delete(item)        
        for i in linhas:
            if count % 2 == 0:            
                self.estoque_treeview.insert("", "end", values=i, tags=('oddrow',))
            else:
                self.estoque_treeview.insert("", "end", values=i, tags=('evenrow',))
            count+=1
    def on_enter_est(self,event):
        self.estoque_buscado()

    def limpar_treeview(self):
        if self.estoque_treeview:
            self.estoque_treeview.delete(*self.estoque_treeview.get_children())
