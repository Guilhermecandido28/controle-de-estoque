from tkinter import *
from styles.cores import *
import tkinter as tk
from tkinter import filedialog
from formations import *
from tkinter import ttk
from PIL import Image, ImageTk
from limpar import limpar
from bancodedados.banco_dados import *
from tkinter import messagebox
from estoque.barcode import *



class AddFornecedor():
    def __init__(self, frame):
        self.principal = frame
        self.banco_estoque = BancoDeDados('estoques.db')
        self.banco_fornecedor = BancoDeDados('fornecedores.db')
        self.add_fornecedor()
        self.make_listbox()
        self.preencher_listbox()
        self.img = Image.open('imagens/pessoa.png')
        self.filename = None
        

    def add_fornecedor(self):
        self.titulo_est = Label(self.principal, text='Ficha de Cadastro de Fornecedor', bg='white', font=('arial 36 bold'))
        self.linha_est = Frame(self.principal, bg=cor5)
        self.linha_est.place(relx=0.01, rely=0.11, relwidth=0.98, relheight=0.004)
        self.titulo_est.place(relx=0.01, rely=0.0)
        #imagem
        self.my_canvas = Canvas(self.principal, bd=0, highlightthickness=0, relief='ridge')
        self.my_canvas.place(relx=0.01, rely=0.15, relheight=.39, relwidth=.14)
        self.my_canvas.bind('<Configure>', self.resizer)
        #upload
        botao_upload = tk.Button(self.principal, text="Upload", font=('arial 12 bold'), background='green', foreground='white', cursor='hand2', command=self.upload)
        botao_upload.place(relx=0.01, rely=0.50, relwidth=.14, relheight=0.04)
         # Entrys

            #NOME
        self.title_descricao = Label(self.principal, text='NOME:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_descricao.place(relx=0.158, rely=0.15)
        self.e_nome = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_nome.place(relx=0.160, rely=0.20, relwidth=0.45, relheight=0.04)
        placeholder_nome(self.e_nome)
            #CATEGORIA
        self.title_categoria = Label(self.principal, text='CATEGORIA:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_categoria.place(relx=0.158, rely=0.25)
        self.e_categoria = ttk.Combobox(self.principal, background=cor4, font=('arial 12'), state='readonly')
        self.e_categoria['values'] = list(self.e_categoria['values']) + self.ler_categoria_do_arquivo()
        self.e_categoria.place(relx=0.160, rely=0.30, relwidth=0.19, relheight=0.04)
        self.img_adicionar = PhotoImage(file='imagens/adicionar.png')
        self.btn_add_categoria = Button(self.principal, image=self.img_adicionar, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.categoria, cursor='hand2')
        self.btn_add_categoria.place(relx=0.351, rely=0.30, relheight=0.04, relwidth=0.02)
        placeholder_nome(self.e_categoria)
        
            #CNPJ
        self.title_cnpj = Label(self.principal, text='CNPJ:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_cnpj.place(relx=0.40, rely=0.25)
        self.e_cnpj = Entry(self.principal, background=cor4, font=('arial 12'), bd=0)        
        self.e_cnpj.place(relx=0.400, rely=0.30, relwidth=0.21, relheight=0.04)
        
        placeholder_cnpj(self.e_cnpj)
            #email
        self.title_email = Label(self.principal, text='EMAIL:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_email.place(relx=0.158, rely=0.35)
        self.e_email = Entry(self.principal, background=cor4, font=('arial 12'), bd=0, highlightthickness=0)
        self.e_email.place(relx=0.160, rely=0.40, relwidth=0.21, relheight=0.04)     

        
            #telefone
        self.title_celular = Label(self.principal, text='TELEFONE:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_celular.place(relx=0.40, rely=0.35)
        self.e_celular = Entry(self.principal, background=cor4, font=('arial 12'), bd=0, highlightthickness=0)
        self.e_celular.place(relx=0.400, rely=0.40, relwidth=0.21, relheight=0.04)        
        placeholder_celular(self.e_celular)
            #Observação
        self.title_obs = Label(self.principal, text='OBSERVAÇÃO:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_obs.place(relx=0.158, rely=0.45)
        self.e_obs = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_obs.place(relx=0.160, rely=0.50, relwidth=0.45, relheight=0.04)
         
        # endereço
        self.linha2 = Frame(self.principal, bg=cor5)
        self.linha2.place(relx=0.01, rely=0.56+0.04, relwidth=0.60, relheight=0.004)
        self.titulo_endereco = Label(self.principal, text="ENDEREÇO", font=('arial 14'), foreground=cor4, bg='white')
        self.titulo_endereco.place(relx=0.01, rely=0.51+0.04)
            #CEP
        self.title_cep = Label(self.principal, text="CEP:", font=('arial 12'), foreground=cor4, bg='white')
        self.title_cep.place(relx=0.01, rely=0.605+0.04)
        self.e_cep = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_cep.place(relx=0.01, rely=0.65+0.04, relwidth=0.08, relheight=0.04)  
        placeholder_cep(self.e_cep)
            #RUA
        self.title_rua = Label(self.principal, text="RUA:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_rua.place(relx=.125, rely= .605+0.04 )
        self.e_rua = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_rua.place(relx=0.125, rely=0.65+0.04, relwidth=0.38, relheight=0.04)
        placeholder_endereco(self.e_rua)
            #N°
        self.title_numero = Label(self.principal, text="NÚMERO:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_numero.place(relx=.545, rely= .605+0.04 )
        self.e_numero = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_numero.place(relx=0.545, rely=0.65+0.04, relwidth=0.065, relheight=0.04)
            #BAIRRO
        self.title_bairro = Label(self.principal, text="BAIRRO:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_bairro.place(relx=.01, rely= .705+0.04 )
        self.e_bairro = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_bairro.place(relx=0.01, rely=0.75+0.04, relwidth=0.20, relheight=0.04)
        placeholder_endereco(self.e_bairro) 
            #CIDADE
        self.title_cidade = Label(self.principal, text="CIDADE:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_cidade.place(relx=.24, rely= .705+0.04 )
        self.e_cidade = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_cidade.place(relx=0.24, rely=0.75+0.04, relwidth=0.20, relheight=0.04)
        placeholder_endereco(self.e_cidade)
            #ESTADO
        self.e_estados = ttk.Combobox(self.principal, font=('arial 12'), takefocus=True, state='readonly')
        self.e_estados['values'] = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
        self.e_estados.current(24)  # Pré-seleciona o estado de São Paulo
        self.e_estados.place(relx=0.486, rely=0.75+0.04, relwidth=0.124, relheight=0.04)      
        self.title_estado = Label(self.principal, text="ESTADO:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_estado.place(relx=.486, rely= .705+0.04 )
        
        #botão salvar
        self.img_salvar = PhotoImage(file='imagens/salvar.png')
        self.btn_salvar = Button(self.principal, text='Salvar', image=self.img_salvar, compound=LEFT, bg=cor6, font=('arial 22 bold'), cursor='hand2', foreground='white', command=self.salvar_fornecedor)
        self.btn_salvar.place(relx=.25, rely=.91, relwidth=.18)        
        
        
    def make_listbox(self):
        self.scrollbar_list = Scrollbar(self.principal, orient=VERTICAL)
        self.scrollbar_list_fornecedor = Scrollbar(self.principal, orient=VERTICAL)               
        self.seta_cima = PhotoImage(file='imagens/seta_simples_cima.png')
        self.seta_baixo = PhotoImage(file='imagens/seta_simples_baixo.png')
        self.title_lista = Label(self.principal, text='LISTA DE PRODUTOS:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_lista.place(relx=0.71, rely=0.15)        
        self.e_lista = Listbox(self.principal, font=('arial 12'), yscrollcommand=self.scrollbar_list.set, selectmode=MULTIPLE) 
        self.e_lista.place(relx=0.71, rely=0.20, relwidth=0.20, relheight=0.3)
        self.para_baixo = Button(self.principal, image=self.seta_baixo, command=self.mover_baixo_listbox)
        self.para_baixo.place(relx=0.94, rely=.3, relwidth=.03, relheight=.1)
        self.para_cima = Button(self.principal, image=self.seta_cima, command=self.mover_cima_listbox)
        self.para_cima.place(relx=0.94, rely=.7, relwidth=.03, relheight=.1)
        self.title_lista_fornecedor = Label(self.principal, text='PRODUTOS QUE O FORNECEDOR VENDE:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_lista_fornecedor.place(relx=0.71, rely=0.55)        
        self.e_lista_fornecedor = Listbox(self.principal, font=('arial 12'), yscrollcommand=self.scrollbar_list_fornecedor.set, selectmode=(MULTIPLE)) 
        self.e_lista_fornecedor.place(relx=0.71, rely=0.60, relwidth=0.20, relheight=0.3)
        self.scrollbar_list.config(command=self.e_lista.yview)
        self.scrollbar_list.place(relx=.91, rely=.2, relheight=.3)
        self.scrollbar_list_fornecedor.config(command=self.e_lista_fornecedor.yview)
        self.scrollbar_list_fornecedor.place(relx=.91, rely=.6, relheight=.3)        

    def salvar_fornecedor(self):
        lista = [self.e_nome, self.e_categoria, self.e_cnpj, self.e_email, self.e_celular, self.e_obs, self.e_cep, self.e_rua, self.e_numero, self.e_bairro, self.e_cidade, self.e_estados, self.e_lista_fornecedor]
        for entry in lista:
            if entry == self.e_lista_fornecedor:
                if entry.get(0, END) == '':
                    messagebox.showerror('Erro', 'Preencha todos os campos.')
                    return                    
            else:
                if entry.get() == "":
                    messagebox.showerror('Erro', 'Preencha todos os campos.')
                    return

        if self.filename is not None:
            with open(self.filename, 'rb') as img_file:
                self.byte_img = img_file.read()
        else:
            self.img_padrao = Image.open('imagens/pessoa.png')
            with open('imagens/pessoa.png', 'rb') as img_file:
                self.byte_img = img_file.read()
        value_imagem = self.byte_img                
        value_nome = self.e_nome.get().strip()
        value_categoria = self.e_categoria.get()
        value_cnpj = self.e_cnpj.get()
        value_email = self.e_email.get()
        value_celular = self.e_celular.get()
        value_obs = self.e_obs.get()
        value_cep = self.e_cep.get()
        value_rua = self.e_rua.get()
        value_numero = self.e_numero.get()
        value_bairro = self.e_bairro.get()
        value_cidade = self.e_cidade.get()
        value_estado = self.e_estados.get()
        lista_formatada_produtos = [str(tupla).replace('(', '').replace(')', '').replace("'", "") for tupla in self.e_lista_fornecedor.get(0, END)]
        value_e_lista_fornecedor = '; '.join(lista_formatada_produtos)
        
        

        query = "INSERT INTO fornecedor (nome, categoria, cnpj, email, telefone, OBS, CEP, rua, numero, bairro, cidade, estado, lista_produtos, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        params = (value_nome, value_categoria, value_cnpj, value_email, value_celular, value_obs, value_cep, value_rua, value_numero, value_bairro, value_cidade, value_estado, value_e_lista_fornecedor, value_imagem)
        self.banco_fornecedor.dml(query, params)
        print('fornecedor foi salvo')           
                                        
        messagebox.showinfo("Sucesso", "Operação realizada com sucesso!")   

    def preencher_listbox(self):
        produtos = "SELECT descricao, categoria, marca, tamanho, cor FROM estoque"
        query = self.banco_estoque.dql(produtos)               
        for produto in query:
            descricao = produto[0]
            categoria = produto[1]
            marca = produto[2]
            tamanho = produto[3]
            cor = produto[4]             
            texto_formatado = f"{descricao} - {categoria} - {marca} - {tamanho} - {cor}"
            self.e_lista.insert(END, texto_formatado)
        
        
      
    def mover_baixo_listbox(self):
        selected_indices = self.e_lista.curselection()        
        for item in selected_indices:
            produto = self.e_lista.get(item)       
            self.e_lista_fornecedor.insert(0, produto)
        for index in reversed(selected_indices):
            self.e_lista.delete(index) 

    def mover_cima_listbox(self):
        selected_indices = self.e_lista_fornecedor.curselection()        
        for item in selected_indices:
            produto = self.e_lista_fornecedor.get(item)       
            self.e_lista.insert(0, produto)
        for index in reversed(selected_indices):
            self.e_lista_fornecedor.delete(index)        
            

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
        self.e_categoria.configure(state='normal')
        self.btn_add_categoria.place_forget()
        self.btn_exc_categoria = Button(self.principal, image=self.img_excluir, background='dark green', relief='flat', highlightthickness=0, bd=0, command=lambda: self.e_categoria.set(""), cursor='hand2')
        self.btn_exc_categoria.place(relx=0.351, rely=0.30, relheight=0.04, relwidth=0.02)
        self.btn_ok_categoria = Button(self.principal, image=self.img_ok, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.salvar_categoria, cursor='hand2')
        self.btn_ok_categoria.place(relx=0.372, rely=0.30, relheight=0.04, relwidth=0.02)

    
   

    def salvar_categoria(self):
        nova_categoria = self.e_categoria.get().upper()  # Obtém a nova categoria digitada e a converte para maiúsculas

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
        self.e_categoria['values'] = list(self.e_categoria['values']) + [nova_categoria]
        self.e_categoria.set(nova_categoria)

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
        self.btn_add_categoria.place(relx=0.351, rely=0.30, relheight=0.04, relwidth=0.02)

    



    def resizer(self,e):
        global resized_img, new_img       
        resized_img = self.img.resize((e.width, e.height))        
        new_img = ImageTk.PhotoImage(resized_img)
        self.img_id_resizer = self.my_canvas.create_image(0,0, image=new_img, anchor='nw')
        return self.img_id_resizer
    
    def upload(self):                
        self.filename = filedialog.askopenfilename(title="Selecione uma foto", filetypes=[("Imagens", "*.jpg *.png *.bmp")])        
        self.img = Image.open(self.filename)
        largura = self.my_canvas.winfo_width()
        altura = self.my_canvas.winfo_height()
        resized_img2 = self.img.resize((largura, altura))
        self.img_tk = ImageTk.PhotoImage(resized_img2)
        self.img_id = self.my_canvas.create_image(0,0, image=self.img_tk, anchor='nw')
        return self.img_id 