from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from limpar import limpar
from clientes.add_cliente import AddCliente
from tkinter import ttk
from clientes.banco_dados_cliente import *
from tkinter import messagebox



class Cliente(AddCliente):
    def __init__(self, frame) -> None:
        self.principal = tk.Frame(frame, bg= 'white')
        self.inserir_dados()
        self.clientes_na_treeview()              
        

    def novo_cliente(self):
        self.btn_addcliente.configure(state='disabled')
        self.tree_scroll.place_forget()        
        self.limpar_treeview()  # Limpa a TreeView antes de criar um novo cliente
        self.novo_cliente = AddCliente(self.principal)
            
    def clientes(self):
        self.principal.place(relx=0.01, rely=0.23, relwidth=0.98, relheight=0.67)
        #Botão_adicionar_cliente        
        self.btn_addcliente = Button(self.principal, text='ADICIONAR\n Cliente', bg=cor6, compound='center',bd=0, font=('arial 14 bold'), foreground='white', cursor='hand2', command=self.novo_cliente)
        self.btn_addcliente.place(relx=0.9, rely=0, relheight=0.1, relwidth=0.1)
        #botão de editar cliente
        self.btn_edtcliente = Button(self.principal, text='EDITAR\n Cliente', bg='dark red', compound='center',bd=0, font=('arial 14 bold'), foreground='white', cursor='hand2', command=self.editar_cliente)
        self.btn_edtcliente.place(relx=0.8, rely=0, relheight=0.1, relwidth=0.1)
        #excluir cliente
        self.btn_exclcliente = Button(self.principal, text='EXCLUIR\n Cliente', bg='red', compound='center',bd=0, font=('arial 14 bold'), foreground='white', cursor='hand2',command=self.excluir_cliente)
        self.btn_exclcliente.place(relx=0.7, rely=0, relheight=0.1, relwidth=0.1)


    def buscar_cliente(self):
        self.search = Entry(self.principal, font=('arial 14'), bg=cor5, bd=0)
        self.search.insert(0, "Procure por cliente...")
        self.search.bind("<FocusIn>", lambda event: self.search.delete(0, "end"))
        self.search.place(relx=0, rely=0, relheight=0.1, relwidth=0.7)
        #botão_pesquisar
        self.img_search = PhotoImage(file='imagens/search.png')
        self.btn_search = Button(self.principal, image=self.img_search, bg=cor5, bd=0, cursor='hand2', command=self.cliente_buscado)
        self.btn_search.place(relx=0.6, rely=0, relheight=0.1, relwidth=0.05)
        self.search.bind('<Return>', self.on_enter)
        #Botão_imprimir
        self.img_print = PhotoImage(file='imagens/impressora.png')
        self.btn_print = Button(self.principal, image=self.img_print, bg=cor5, bd=0, cursor='hand2')
        self.btn_print.place(relx=0.65, rely=0, relheight=0.1, relwidth=0.05)
        

    def on_enter(self,event):
        self.cliente_buscado()
    def limpar_treeview(self):
        if self.ins_treeview:
            self.ins_treeview.delete(*self.ins_treeview.get_children())
            

    def inserir_dados(self):        
        self.tree_scroll = Scrollbar(self.principal)
        self.tree_scroll.place(relx=0.985, rely=0.1, relheight=.9, relwidth=.015)
        self.ins_treeview = ttk.Treeview(self.principal, yscrollcommand=self.tree_scroll.set, show="headings")
        style = ttk.Style(self.ins_treeview)
        style.configure("Treeview", font= ('arial 15 normal'),
                        rowheight= 40,
                        )
        style.configure("Treeview.Heading", font= ('arial 15 normal'), foreground='gray', padding=0 
                        )
        self.tree_scroll.config(command=self.ins_treeview.yview)
        self.ins_treeview['columns'] = ('ID', 'NOME', 'SOBRENOME','CONTATO', 'VALOR GASTO')
        self.ins_treeview.heading('#1', text='ID', anchor=W)        
        self.ins_treeview.heading('#2', text='NOME')
        self.ins_treeview.heading('#3', text='SOBRENOME')
        self.ins_treeview.heading('#4', text='CONTATO' )
        self.ins_treeview.heading('#5', text='VALOR GASTO' )
        self.ins_treeview.place(relx=0, rely=.1, relheight=.9, relwidth=.985)
        self.ins_treeview.column("ID",width=40, stretch=FALSE, anchor='w')        
        self.ins_treeview.column("NOME", minwidth=250, stretch=TRUE, anchor='center')
        self.ins_treeview.column("SOBRENOME",minwidth=250, stretch=TRUE, anchor='center')
        self.ins_treeview.column("CONTATO", minwidth=240, stretch=TRUE, anchor='center')        
        self.ins_treeview.column("VALOR GASTO", minwidth=240, stretch=TRUE, anchor='center')
  


    def clientes_na_treeview(self):
        self.ins_treeview.tag_configure('oddrow', background='white')
        self.ins_treeview.tag_configure('evenrow', background='light gray') 
        if self.ins_treeview:
            self.ins_treeview.delete(*self.ins_treeview.get_children())       
        query ="SELECT id, nome, sobrenome, celular, valor_gasto FROM clientes order by id"
        linhas= dql(query)
        count=0
        
        for i in linhas:
            if count % 2 == 0:    
               self.ins_treeview.insert("", "end",values=i, tags=('oddrow',))             
                
                
            else:
                self.ins_treeview.insert("", "end",values=i, tags=('evenrow',))
            count+=1 
            

    def editar_cliente(self):
        items_selecionados = []
        for item in self.ins_treeview.selection():
            item_values = self.ins_treeview.item(item, 'values')
            items_selecionados.append(item_values)

    def excluir_cliente(self):
        items_selecionados = []
        item_id=[]        
        if self.ins_treeview.selection() == ():
            messagebox.showerror('Erro', "Selecione um ou mais cliente(s) primeiro! ")
        else:
            for item in self.ins_treeview.selection():
                item_values = self.ins_treeview.item(item, 'values')
                items_selecionados.append(item_values)
            for i, item in enumerate(items_selecionados):
                ids = items_selecionados[i][0]
                item_id.append(ids)
            for cliente in item_id:
                query = "DELETE FROM clientes WHERE id=?"
                dml(query, cliente)
            self.clientes_na_treeview()
            print('cliente excluido')
        
        

    def cliente_buscado(self):        
        self.c_buscado = self.search.get()
        consulta = f"SELECT id, nome, sobrenome, celular, valor_gasto FROM clientes " \
        f"WHERE id LIKE '%{self.c_buscado}%' " \
        f"OR nome LIKE '%{self.c_buscado}%' " \
        f"OR celular LIKE '%{self.c_buscado}%' " \
        f"OR sobrenome LIKE '%{self.c_buscado}%'"
        linhas = dql(consulta)
        count=0
        for item in self.ins_treeview.get_children():
            self.ins_treeview.delete(item)        
        for i in linhas:
            if count % 2 == 0:            
                self.ins_treeview.insert("", "end", values=i, tags=('oddrow',))
            else:
                self.ins_treeview.insert("", "end", values=i, tags=('evenrow',))
            count+=1
        
        
           
        