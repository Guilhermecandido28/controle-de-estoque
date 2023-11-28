from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from limpar import limpar
from tkinter import ttk
from tkinter import messagebox
import io
from fornecedor.add_fornecedor import AddFornecedor
from fornecedor.editar_fornecedor import EditarFornecedor
from bancodedados.banco_dados import *
from bancodedados.banco_dados import *
from PIL import Image, ImageTk
import subprocess
import os

class Fornecedor():
    def __init__(self, frame):
        self.principal = tk.Frame(frame, bg= 'white')
        self.f_editar_fornecedor = tk.Frame(frame, bg='white')
        self.f_add_fornecedor = tk.Frame(frame, bg= 'white')
        self.location_est = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.banco_fornecedor = BancoDeDados('fornecedores.db')
        self.banco_estoque = BancoDeDados('estoques.db')
        self.buscar_fornecedor_est()
        self.tree_fornecedor()
        self.fornecedor_na_treeview()
        
    def editar_fornecedor(self):        
        if self.fornecedor_treeview.selection() == ():
            messagebox.showerror('Erro', "Selecione um fornecedor primeiro! ")
        else:
            self.f_editar_fornecedor.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.72)
            items_selecionado = []
            for item in self.fornecedor_treeview.selection():
                item_values = self.fornecedor_treeview .item(item, 'values')
                items_selecionado.append(item_values)            
            self.fornecedor_tree_scroll.place_forget()        
            self.limpar_treeview() 
                                  
            self.ed_fornecedor = EditarFornecedor(self.f_editar_fornecedor, id=items_selecionado[0][0])
            lista_entrys = [ self.ed_fornecedor.ed_id, self.ed_fornecedor.ed_nome, self.ed_fornecedor.ed_categoria, self.ed_fornecedor.ed_cnpj, self.ed_fornecedor.ed_email, self.ed_fornecedor.ed_telefone, self.ed_fornecedor.ed_obs, self.ed_fornecedor.ed_cep, self.ed_fornecedor.ed_rua, self.ed_fornecedor.ed_numero, self.ed_fornecedor.ed_bairro, self.ed_fornecedor.ed_cidade, self.ed_fornecedor.ed_estados]        
            limpar(lista_entrys)            
            query =f"SELECT id, nome, categoria, cnpj, email, telefone, OBS, CEP, rua, numero, bairro, cidade, estado FROM fornecedor WHERE id = {items_selecionado[0][0]}"           
            query_listbox = f"SELECT lista_produtos FROM fornecedor WHERE id = {items_selecionado[0][0]}"
            dados_listbox = self.banco_fornecedor.dql(query_listbox)
            dados_listbox = str(dados_listbox).split('; ')
            dados = self.banco_fornecedor.dql(query)            
            count=0
            for campo in lista_entrys:
                campo.insert(0, dados[0][count])
                count+=1
            for dado in dados_listbox:
                dado = dado.replace("'", '').replace('[(', '').replace(')]', '').replace(',', '')
                self.ed_fornecedor.e_lista_fornecedor.insert(0, dado)
            self.preencher_listbox()   
    def preencher_listbox(self):
        produtos = "SELECT descricao, categoria, marca FROM estoque"
        query = self.banco_estoque.dql(produtos)               
        for produto in query:
            descricao = produto[0]
            categoria = produto[1]
            marca = produto[2]             
            texto_formatado = f"{descricao} - {categoria} - {marca}"
            self.ed_fornecedor.e_lista.insert(END, texto_formatado)      
    def add_fornecedor(self):
        self.adicionar_fornecedor = AddFornecedor(self.f_add_fornecedor)
        self.f_add_fornecedor.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.72)

    def fornecedores(self):
        self.location_est.place(relx=0, rely=0.14, relwidth=1, relheight=0.09)        
        self.img_location_est = Image.open('imagens/location.png')
        self.img_location_est_tk = ImageTk.PhotoImage(self.img_location_est)
        self.location_est.create_text(100,30, text='FORNECEDOR', anchor=NW, font=('arial 18 bold underline'))
        self.location_est.bind('<Configure>', self.resize_image)
        self.principal.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.72)        
        #Botão_adicionar_estoque        
        self.btn_addfornecedor = Button(self.principal, text='ADICIONAR\n Fornecedor', bg='light gray', compound='center',bd=0, font=('arial 14 bold'), foreground='black', cursor='hand2', command=self.add_fornecedor)
        self.btn_addfornecedor.place(relx=0.9, rely=0, relheight=0.1, relwidth=0.1)
        #botão de editar estoque
        self.btn_edtfornecedor = Button(self.principal, text='EDITAR\n Fornecedor', bg='dark gray', compound='center',bd=0, font=('arial 14 bold'), foreground='black', cursor='hand2', command=self.editar_fornecedor)
        self.btn_edtfornecedor.place(relx=0.8, rely=0, relheight=0.1, relwidth=0.1)
        #excluir estoque        
        self.btn_exclfornecedor = Button(self.principal, text='EXCLUIR\n Fornecedor', bg='gray', compound='center',bd=0, font=('arial 14 bold'), foreground='black', cursor='hand2', command=self.excluir_estoque)
        self.btn_exclfornecedor.place(relx=0.7, rely=0, relheight=0.1, relwidth=0.1)
        #botão voltar
        self.img_voltar = PhotoImage(file='imagens/voltar.png')
        self.btn_voltar_editar = Button(self.f_editar_fornecedor, image=self.img_voltar, bg='white', cursor='hand2', command=self.voltar, relief='flat')
        self.btn_voltar_editar.place(relx=0.962, rely=0.0)
        #botão voltar do addfornecedor      
        
        self.btn_voltar_add = Button(self.f_add_fornecedor, image=self.img_voltar, bg='white', cursor='hand2', command=self.voltar, relief='flat')
        self.btn_voltar_add.place(relx=0.962, rely=0)
        

    def voltar(self):
        self.f_editar_fornecedor.place_forget()
        self.f_add_fornecedor.place_forget()
        self.fornecedor_na_treeview()

    def resize_image(self, event):
        self.nova_imagem_est = self.img_location_est.resize((event.width, event.height))
        self.nova_imagem_est_tk = ImageTk.PhotoImage(self.nova_imagem_est)
        self.location_est.create_image(0,0, anchor = NW, image = self.nova_imagem_est_tk)
        self.location_est.image = self.nova_imagem_est_tk

    def buscar_fornecedor_est(self):
        self.search_est = Entry(self.principal, font=('arial 14'), bg="#8A8A8A", bd=0)
        self.search_est.insert(0, "Procure por fornecedor...")
        self.search_est.bind("<FocusIn>", lambda event: self.search_est.delete(0, "end"))
        self.search_est.place(relx=0, rely=0, relheight=0.1, relwidth=0.7)
        #botão_pesquisar
        self.img_search_est = PhotoImage(file='imagens/search.png')
        self.btn_search_est = Button(self.principal, image=self.img_search_est, bg="#8A8A8A", bd=0, cursor='hand2', command=self.fornecedor_buscado)
        self.btn_search_est.place(relx=0.6, rely=0, relheight=0.1, relwidth=0.05)
        self.search_est.bind('<Return>', self.on_enter_est)
        #Botão_imprimir
        self.img_print_est = PhotoImage(file='imagens/impressora.png')
        self.btn_print_est = Button(self.principal, image=self.img_print_est, bg="#8A8A8A", bd=0, cursor='hand2')
        self.btn_print_est.place(relx=0.65, rely=0, relheight=0.1, relwidth=0.05)

    def tree_fornecedor(self):        
        self.fornecedor_tree_scroll = Scrollbar(self.principal)
        self.fornecedor_tree_scroll.place(relx=0.985, rely=0.1, relheight=.9, relwidth=.015)
        self.fornecedor_treeview = ttk.Treeview(self.principal, yscrollcommand=self.fornecedor_tree_scroll.set, show="headings")
        style = ttk.Style(self.fornecedor_treeview)
        style.configure("Treeview", font= ('arial 15 normal'),
                        rowheight= 40,
                        )
        style.configure("Treeview.Heading", font= ('arial 15 normal'), foreground='gray', padding=0 
                        )
        self.fornecedor_tree_scroll.config(command=self.fornecedor_treeview.yview)
        self.fornecedor_treeview['columns'] = ('ID', 'NOME','CNPJ','EMAIL','TELEFONE')
        self.fornecedor_treeview.heading('#1', text='ID', anchor=W)        
        self.fornecedor_treeview.heading('#2', text='NOME')
        self.fornecedor_treeview.heading('#3', text='CNPJ')
        self.fornecedor_treeview.heading('#4', text='EMAIL')
        self.fornecedor_treeview.heading('#5', text='TELEFONE')
        self.fornecedor_treeview.place(relx=0, rely=.1, relheight=.9, relwidth=.985)
        self.fornecedor_treeview.column("ID",width=50, stretch=FALSE, anchor='w')        
        self.fornecedor_treeview.column("NOME", width=200, minwidth=250, stretch=TRUE, anchor='center')
        self.fornecedor_treeview.column("CNPJ", width=150, minwidth=150, stretch=TRUE, anchor='center')
        self.fornecedor_treeview.column("EMAIL", width=100, minwidth=100, stretch=TRUE, anchor='center')
        self.fornecedor_treeview.column("TELEFONE", width=200, minwidth=250, stretch=TRUE, anchor='center')       


    def fornecedor_na_treeview(self):
        self.fornecedor_treeview.tag_configure('oddrow', background='white')
        self.fornecedor_treeview.tag_configure('evenrow', background='light gray') 
        if self.fornecedor_treeview:
            self.fornecedor_treeview.delete(*self.fornecedor_treeview.get_children())       
        query ="SELECT ID, nome, categoria, cnpj, email, telefone FROM fornecedor order by ID"
        linhas= self.banco_fornecedor.dql(query)
        count=0
        
        for i in linhas:
            if count % 2 == 0:    
                self.fornecedor_treeview.insert("", "end",values=i, tags=('oddrow',))             
                
                
            else:
                self.fornecedor_treeview.insert("", "end",values=i, tags=('evenrow',))
            count+=1 

    def excluir_estoque(self):
        items_selecionados = []
        item_id=[]        
        if self.fornecedor_treeview.selection() == ():
            messagebox.showerror('Erro', "Selecione um ou mais produto(s) primeiro! ")
        else:
            for item in self.fornecedor_treeview.selection():
                item_values = self.fornecedor_treeview.item(item, 'values')
                items_selecionados.append(item_values)
            for i, item in enumerate(items_selecionados):
                ids = items_selecionados[i][0]
                item_id.append(ids)
            for produto in item_id:
                query = "DELETE FROM fornecedor WHERE id=?"
                self.banco_fornecedor.dml(query, (produto,))
            self.fornecedor_na_treeview()
            print('produto excluido')

    def fornecedor_buscado(self):        
        self.e_buscado = self.search_est.get()
        if self.e_buscado == 'Procure por fornecedor...':
            pass
        else:
            consulta = f"SELECT id, nome, categoria, cnpj, email, telefone FROM fornecedor " \
            f"WHERE id LIKE '%{self.e_buscado}%' " \
            f"OR nome LIKE '%{self.e_buscado}%' " \
            f"OR categoria LIKE '%{self.e_buscado}%' " \
            f"OR cnpj LIKE '%{self.e_buscado}%' " \
            f"OR email LIKE '%{self.e_buscado}%' " \
            f"OR telefone LIKE '%{self.e_buscado}%' " \
            
            linhas = self.banco_fornecedor.dql(consulta)
            count=0
            for item in self.fornecedor_treeview.get_children():
                self.fornecedor_treeview.delete(item)        
            for i in linhas:
                if count % 2 == 0:            
                    self.fornecedor_treeview.insert("", "end", values=i, tags=('oddrow',))
                else:
                    self.fornecedor_treeview.insert("", "end", values=i, tags=('evenrow',))
                count+=1
    def on_enter_est(self,event):
        self.fornecedor_buscado()

    def limpar_treeview(self):
        if self.fornecedor_treeview:
            self.fornecedor_treeview.delete(*self.fornecedor_treeview.get_children())
