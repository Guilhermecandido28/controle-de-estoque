from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from tkinter import ttk
from bancodedados.banco_dados import *
from tkinter import messagebox


class EditarFornecedor():
    def __init__(self, frame, id) -> None:
        self.f_editar_fornecedor = frame        
        self.id = id
        self.banco_fornecedor = BancoDeDados('controle_estoque.db')
        self.make_listbox()
        self.entrys()
        self.titulos()
        self.botoes()

    def entrys(self): 
        self.ed_id = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)       
        self.ed_nome = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        placeholder_nome(self.ed_nome)
        #CATEGORIA

        self.ed_categoria = ttk.Combobox(self.f_editar_fornecedor, background=cor4, font=('arial 12'), state='readonly')
        self.ed_categoria['values'] = list(self.ed_categoria['values']) + self.ler_categoria_do_arquivo()
        self.img_adicionar = PhotoImage(file='imagens/adicionar.png')
        
       
        self.ed_cnpj = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        placeholder_cnpj(self.ed_cnpj)
        self.ed_email = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_telefone = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        placeholder_celular(self.ed_telefone)
        self.ed_obs = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_cep = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        placeholder_cep(self.ed_cep)
        self.ed_rua = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        placeholder_nome(self.ed_rua)
        self.ed_numero = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_bairro = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        placeholder_nome(self.ed_bairro)
        self.ed_cidade = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        placeholder_nome(self.ed_cidade)
        self.ed_estados = ttk.Combobox(self.f_editar_fornecedor, font=('arial 12'), takefocus=True, state='readonly')
        self.ed_estados['values'] = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
        self.ed_estados.current(24)  # Pré-seleciona o estado de São Paulo 
  
        
        
        #----------------------------------------------------------------------------------#
        
        self.ed_id.place(relx=.05, rely=.2, relwidth=.2, relheight=0.04) 
        self.ed_nome.place(relx=.05, rely=.3, relwidth=.2, relheight=0.04)
        self.ed_categoria.place(relx=.05, rely=.4, relwidth=.2, relheight=0.04)
        self.ed_cnpj.place(relx=.05, rely=.5, relwidth=.2, relheight=0.04)
        self.ed_email.place(relx=.05, rely=.60, relwidth=.2, relheight=0.04)
        self.ed_telefone.place(relx=.05, rely=.7, relwidth=.2, relheight=0.04)
        self.ed_obs.place(relx=.4, rely=.2, relwidth=.2, relheight=0.04)
        self.ed_cep.place(relx=.4, rely=.3, relwidth=.2, relheight=0.04)
        self.ed_rua.place(relx=.4, rely=.4, relwidth=.2, relheight=0.04)
        self.ed_numero.place(relx=.4, rely=.5, relwidth=.2, relheight=0.04)
        self.ed_bairro.place(relx=.4, rely=.6, relwidth=.2, relheight=0.04)
        self.ed_cidade.place(relx=.4, rely=.7, relwidth=.2, relheight=0.04)
        self.ed_estados.place(relx=.4, rely=.8, relwidth=.2, relheight=0.04)
    
    def titulos(self):
        self.linha = Frame(self.f_editar_fornecedor, bg=cor5)
        self.linha.place(relx=0.01, rely=0.1, relwidth=0.605, relheight=0.004)
        self.titulo_geral = Label(self.f_editar_fornecedor, text="Editor de Fornecedor", font=('arial 18'), bg='white')
        self.titulo_geral.place(relx=0.01, rely=0.05)
        self.t_ed_id = Label(self.f_editar_fornecedor, text='ID:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_nome = Label(self.f_editar_fornecedor, text='NOME:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_categoria = Label(self.f_editar_fornecedor, text='CATEGORIA:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_cnpj = Label(self.f_editar_fornecedor, text='CNPJ:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_email = Label(self.f_editar_fornecedor, text='EMAIL:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_telefone = Label(self.f_editar_fornecedor, text='TELEFONE:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_obs = Label(self.f_editar_fornecedor, text='OBS:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_cep = Label(self.f_editar_fornecedor, text='CEP:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_cep = Label(self.f_editar_fornecedor, text='CEP:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_rua= Label(self.f_editar_fornecedor, text='RUA:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_numero= Label(self.f_editar_fornecedor, text='NUMERO:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_bairro= Label(self.f_editar_fornecedor, text='BAIRRO:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_cidade= Label(self.f_editar_fornecedor, text='CIDADE:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_estado= Label(self.f_editar_fornecedor, text='ESTADO:', font=('arial 14'), foreground=cor4, bg='white')
        
        
        #-------------------------------------------#
        self.t_ed_id.place(relx=0.05, rely=.15,  relheight=0.04)
        self.t_ed_nome.place(relx=0.05, rely=.25,  relheight=0.04)
        self.t_ed_categoria.place(relx=0.05, rely=.35,  relheight=0.04)
        self.t_ed_cnpj.place(relx=0.05, rely=.45,  relheight=0.04)
        self.t_ed_email.place(relx=0.05, rely=.55,  relheight=0.04)
        self.t_ed_telefone.place(relx=0.05, rely=.65,  relheight=0.04)
        self.t_ed_obs.place(relx=0.4, rely=.15,  relheight=0.04)
        self.t_ed_cep.place(relx=0.4, rely=.25,  relheight=0.04)
        self.t_ed_rua.place(relx=0.4, rely=.35,  relheight=0.04)
        self.t_ed_numero.place(relx=0.4, rely=.45,  relheight=0.04)
        self.t_ed_bairro.place(relx=0.4, rely=.55,  relheight=0.04)
        self.t_ed_cidade.place(relx=0.4, rely=.65,  relheight=0.04)
        self.t_ed_estado.place(relx=0.4, rely=.75,  relheight=0.04)
        

     
        
    def botoes(self):
        self.btn_add_categoria = Button(self.f_editar_fornecedor, image=self.img_adicionar, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.categoria, cursor='hand2')
        self.img_salvar = PhotoImage(file='imagens/salvar.png')
        self.btn_salvar = Button(self.f_editar_fornecedor, text='Salvar', image=self.img_salvar, compound=LEFT, bg=cor6, font=('arial 22 bold'), cursor='hand2', foreground='white', command=self.salvar_fornecedor)
        self.btn_salvar.place(relx=.32, rely=.90, relwidth=.18)
        self.btn_add_categoria.place(relx=.251, rely=.4, relheight=0.04, relwidth=0.02) 

    def make_listbox(self):
        self.scrollbar_list = Scrollbar(self.f_editar_fornecedor, orient=VERTICAL)
        self.scrollbar_list_fornecedor = Scrollbar(self.f_editar_fornecedor, orient=VERTICAL)               
        self.seta_cima = PhotoImage(file='imagens/seta_simples_cima.png')
        self.seta_baixo = PhotoImage(file='imagens/seta_simples_baixo.png')
        self.title_lista = Label(self.f_editar_fornecedor, text='LISTA DE PRODUTOS:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_lista.place(relx=0.71, rely=0.15)        
        self.e_lista = Listbox(self.f_editar_fornecedor, font=('arial 12'), yscrollcommand=self.scrollbar_list.set, selectmode=MULTIPLE) 
        self.e_lista.place(relx=0.71, rely=0.20, relwidth=0.20, relheight=0.3)
        self.para_baixo = Button(self.f_editar_fornecedor, image=self.seta_baixo, command=self.mover_baixo_listbox)
        self.para_baixo.place(relx=0.94, rely=.3, relwidth=.03, relheight=.1)
        self.para_cima = Button(self.f_editar_fornecedor, image=self.seta_cima, command=self.mover_cima_listbox)
        self.para_cima.place(relx=0.94, rely=.7, relwidth=.03, relheight=.1)
        self.title_lista_fornecedor = Label(self.f_editar_fornecedor, text='PRODUTOS QUE O FORNECEDOR VENDE:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_lista_fornecedor.place(relx=0.71, rely=0.55)        
        self.e_lista_fornecedor = Listbox(self.f_editar_fornecedor, font=('arial 12'), yscrollcommand=self.scrollbar_list_fornecedor.set, selectmode=(MULTIPLE)) 
        self.e_lista_fornecedor.place(relx=0.71, rely=0.60, relwidth=0.20, relheight=0.3)
        self.scrollbar_list.config(command=self.e_lista.yview)
        self.scrollbar_list.place(relx=.91, rely=.2, relheight=.3)
        self.scrollbar_list_fornecedor.config(command=self.e_lista_fornecedor.yview)
        self.scrollbar_list_fornecedor.place(relx=.91, rely=.6, relheight=.3)


    def mover_baixo_listbox(self):
        selected_indices = self.e_lista.curselection()

        for item in selected_indices:
            produto = self.e_lista.get(item)

            # Verifica se o produto já existe na lista antes de inseri-lo
            if produto not in self.e_lista_fornecedor.get(0, tk.END):
                self.e_lista_fornecedor.insert(tk.END, produto)
            else:
                messagebox.showinfo('Erro', 'O produto já está na lista de produtos vendidos pelo fornecedor, escolha outro produto.')

        for index in reversed(selected_indices):
            self.e_lista.delete(index)


    def mover_cima_listbox(self):
        selected_indices = self.e_lista_fornecedor.curselection()

        for item in selected_indices:
            produto = self.e_lista_fornecedor.get(item)

            # Verifica se o produto já existe na lista antes de inseri-lo
            if produto not in self.e_lista.get(0, tk.END):
                self.e_lista.insert(0, produto)
            else:
                pass

        for index in reversed(selected_indices):
            self.e_lista_fornecedor.delete(index)
    
    def salvar_fornecedor(self):            
        modify_id = self.ed_id.get()
        modify_nome = self.ed_nome.get().strip()
        modify_categoria = self.ed_categoria.get()
        modify_cnpj = self.ed_cnpj.get()
        modify_email = self.ed_email.get()
        modify_telefone = self.ed_telefone.get()
        modify_obs = self.ed_obs.get()
        modify_cep = self.ed_cep.get()
        modify_rua = self.ed_rua.get()
        modify_numero = self.ed_numero.get()
        modify_bairro = self.ed_bairro.get()
        modify_cidade = self.ed_cidade.get()
        modify_estado = self.ed_estados.get()
        lista_formatada_produtos = [str(tupla).replace('(', '').replace(')', '').replace("'", "") for tupla in self.e_lista_fornecedor.get(0, END)]
        value_e_lista_fornecedor = '; '.join(lista_formatada_produtos)
        query = f"UPDATE fornecedor SET id = ?, nome = ?, categoria = ?, cnpj = ?, email = ?, telefone = ?, OBS = ?, CEP = ?, rua = ?, numero = ?, bairro = ?, cidade = ?, estado = ?, lista_produtos = ? WHERE id = {self.id}"
        params = (modify_id, modify_nome, modify_categoria, modify_cnpj, modify_email, modify_telefone, modify_obs, modify_cep, modify_rua, modify_numero, modify_bairro, modify_cidade, modify_estado, value_e_lista_fornecedor)
        self.banco_fornecedor.dml(query, params)
        print('fornecedor foi salvo')

    def ler_categoria_do_arquivo(self):
            categorias = []
            try:
                with open('fornecedor/categoria.txt', 'r') as file:
                    for line in file:
                        categoria = line.strip().upper()  # Cada marca lida do arquivo
                        if categoria:  # Verifica se a linha não está vazia
                            categorias.append(categoria)
            except FileNotFoundError:
                print('Arquivo categoria.txt não encontrado.')

            return categorias
    


    def categoria(self):
        self.img_excluir = PhotoImage(file='imagens/excluir.png')
        self.img_ok = PhotoImage(file='imagens/ok.png')
        self.ed_categoria.configure(state='normal')
        self.btn_add_categoria.place_forget()
        self.btn_exc_categoria = Button(self.f_editar_fornecedor, image=self.img_excluir, background='dark green', relief='flat', highlightthickness=0, bd=0, command=lambda: self.ed_categoria.set(""), cursor='hand2')
        self.btn_exc_categoria.place(relx=0.251, rely=0.40, relheight=0.04, relwidth=0.02)
        self.btn_ok_categoria = Button(self.f_editar_fornecedor, image=self.img_ok, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.salvar_categoria, cursor='hand2')
        self.btn_ok_categoria.place(relx=0.272, rely=0.40, relheight=0.04, relwidth=0.02)

    def salvar_categoria(self):
            nova_categoria = self.ed_categoria.get().upper()  # Obtém a nova categoria digitada e a converte para maiúsculas

            # Lê as categorias existentes
            categoria_existentes = []
            try:
                with open('fornecedor/categoria.txt', 'r') as file:
                    categoria_existentes = [linha.strip() for linha in file]
            except FileNotFoundError:
                print('Arquivo categoria.txt não encontrado.')

            # Verifica se a nova categoria já existe (insensível a maiúsculas/minúsculas)
            if nova_categoria.upper() in (categoria.upper() for categoria in categoria_existentes):
                messagebox.showinfo('Erro',f'A categoria {nova_categoria} já existe.')
                return

            # Adiciona a nova categoria à lista de categorias existentes
            categoria_existentes.append(nova_categoria)
            self.ed_categoria['values'] = list(self.ed_categoria['values']) + [nova_categoria]
            self.ed_categoria.set(nova_categoria)

            # Ordena as categorias em ordem alfabética (insensível a maiúsculas/minúsculas)
            categoria_existentes.sort(key=lambda x: x.lower())

            # Salva todas as categorias, uma por linha
            try:
                with open('fornecedor/categoria.txt', 'w') as file:
                    for categoria in categoria_existentes:
                        file.write(categoria + '\n')
            except FileNotFoundError:
                print('Arquivo categoria.txt não encontrado.')

            self.btn_exc_categoria.place_forget()
            self.btn_ok_categoria.place_forget()
            self.btn_add_categoria.place(relx=.251, rely=.4, relheight=0.04, relwidth=0.02)