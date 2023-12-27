from tkinter import *
from styles.cores import *
import tkinter as tk
from tkinter import filedialog
from formations import *
from tkinter import ttk
from PIL import Image, ImageTk
from limpar import limpar
from bancodedados.banco_dados import *
import sqlite3
from clientes.foto_instagram import *
from tkinter import messagebox
from datetime import datetime


  




class AddCliente():
    def __init__(self,frame) -> None: 
        self.img = Image.open('imagens/pessoa.png')               
        self.principal = frame
        self.filename = None
        self.banco = BancoDeDados('clientes.db')
        self.add_client()               
        self.tvw_hist()
        self.inserir_na_treeview()             

    def add_client(self):
        
        #título 
        self.titulo = Label(
            self.principal,
            text='Ficha de Cadastro de Clientes',
            bg='white',
            font=('arial 36 bold'))
        self.titulo.place(relx=0.146, rely=0.07, relheight=0.1)

        Frame(
            self.principal,
            bg=cor5
            ).place(relx=0.146, rely=0.17, relwidth=0.525, relheight=0.004)
        
        #imagem
        self.my_canvas = Canvas(
            self.principal,
            bd=0,
            highlightthickness=0,
            relief='ridge')
        self.my_canvas.place(relx=0, rely=0.1, relheight=.34, relwidth=.14)
        self.my_canvas.bind('<Configure>', self.resizer) 
               
        botao_upload = tk.Button(
            self.principal,
            command= self.upload,
            text="Upload",
            font=('arial 12 bold'),
            background='green',
            foreground='white',
            cursor='hand2')        
        botao_upload.place(relx=0, rely=0.44, relwidth=.14, relheight=0.04)

        botao_upload_instagram = tk.Button(
            self.principal,
            command= self.upload_instagram,
            text="Mostre foto perfil instagram ",
            font=('arial 12 bold'),
            background='green',
            foreground='white',
            cursor='hand2')
        botao_upload_instagram.place(relx=0.49, rely=0.38, relwidth=.18, relheight=0.04)

        # Entrys
            #nome
        self.title_nome = Label(
            self.principal,
            text='NOME:',
            font=('arial 12'),
            foreground= cor4,
            bg='white')
        self.title_nome.place(relx=0.148, rely=0.195)

        self.e_nome = Entry(
            self.principal,
            bg=cor4,
            font=('arial 12'),
            bd=0)
        self.e_nome.place(relx=0.150, rely=0.24, relwidth=0.25, relheight=0.04)
        placeholder_nome(self.e_nome)
        
            #sobrenome
        self.title_sobrenome = Label(self.principal, text='SOBRENOME:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_sobrenome.place(relx=0.416, rely=0.195)
        self.e_sobrenome = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_sobrenome.place(relx=0.42, rely=0.24, relwidth=0.25, relheight=0.04)
        placeholder_sobrenome(self.e_sobrenome)
            #CPF
        self.title_cpf = Label(self.principal, text='CPF:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_cpf.place(relx=0.148, rely=0.295)
        self.e_cpf = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_cpf.place(relx=0.150, rely=0.34, relwidth=0.15, relheight=0.04)
        placeholder_cpf(self.e_cpf)
            #celular
        self.title_celular = Label(self.principal, text="CELULAR:", font=('arial 12'), foreground=cor4, bg='white')
        self.title_celular.place(relx= 0.316 , rely=0.295)
        self.e_celular = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_celular.place(relx=0.32, rely=0.34, relwidth=0.15, relheight=0.04)
        placeholder_celular(self.e_celular)
            #email
        self.title_instagram = Label(self.principal, text="INSTAGRAM:", font=('arial 12'), foreground=cor4, bg='white')
        self.title_instagram.place(relx= 0.49 , rely=0.295) 
        self.e_instagram = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_instagram.place(relx=0.49, rely=0.34, relwidth=0.18, relheight=0.04)
        placeholder_instagram(self.e_instagram)
            #cometário
        self.title_comment = Label(self.principal, text="OBS:", font=('arial 12'), foreground=cor4, bg='white')
        self.title_comment.place(relx=0.148, rely=0.395)
        self.e_comment = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_comment.place(relx=0.150, rely=0.44, relwidth=0.52, relheight=0.04)
        # endereço
        self.linha2 = Frame(self.principal, bg=cor5)
        self.linha2.place(relx=0.01, rely=0.56, relwidth=0.66, relheight=0.004)
        self.titulo_endereco = Label(self.principal, text="ENDEREÇO", font=('arial 14'), foreground=cor4, bg='white')
        self.titulo_endereco.place(relx=0.01, rely=0.51)
            #CEP
        self.title_cep = Label(self.principal, text="CEP:", font=('arial 12'), foreground=cor4, bg='white')
        self.title_cep.place(relx=0.01, rely=0.605)
        self.e_cep = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_cep.place(relx=0.01, rely=0.65, relwidth=0.08, relheight=0.04)  
        placeholder_cep(self.e_cep)
            #RUA
        self.title_rua = Label(self.principal, text="RUA:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_rua.place(relx=.125, rely= .605 )
        self.e_rua = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_rua.place(relx=0.125, rely=0.65, relwidth=0.38, relheight=0.04)
        placeholder_endereco(self.e_rua)
            #N°
        self.title_numero = Label(self.principal, text="NÚMERO:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_numero.place(relx=.545, rely= .605 )
        self.e_numero = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_numero.place(relx=0.545, rely=0.65, relwidth=0.124, relheight=0.04)
            #BAIRRO
        self.title_bairro = Label(self.principal, text="BAIRRO:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_bairro.place(relx=.01, rely= .705 )
        self.e_bairro = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_bairro.place(relx=0.01, rely=0.75, relwidth=0.20, relheight=0.04)
        placeholder_endereco(self.e_bairro) 
            #CIDADE
        self.title_cidade = Label(self.principal, text="CIDADE:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_cidade.place(relx=.24, rely= .705 )
        self.e_cidade = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_cidade.place(relx=0.24, rely=0.75, relwidth=0.263, relheight=0.04)
        placeholder_endereco(self.e_cidade)
            #ESTADO
        self.e_estados = ttk.Combobox(self.principal, font=('arial 12'), takefocus=True, state='readonly')
        self.e_estados['values'] = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
        self.e_estados.current(24)  # Pré-seleciona o estado de São Paulo
        self.e_estados.place(relx=0.545, rely=0.75, relwidth=0.124, relheight=0.04)      
        self.title_estado = Label(self.principal, text="ESTADO:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_estado.place(relx=.545, rely= .705 )
        #botão limpar
        self.img_limpar = PhotoImage(file='imagens/vassoura.png')
        self.btn_limpar_endereco = Button(self.principal, text=' Limpar', image=self.img_limpar, compound=LEFT, bg=cor4, font=('arial 12 bold'), command=lambda: limpar([self.e_cidade, self.e_bairro, self.e_numero, self.e_rua, self.e_cep]), cursor='hand2')
        self.btn_limpar_endereco.place(relx=.600, rely=.810, relheight=0.05, relwidth= 0.07)        
        self.btn_limpar_cadastro = Button(self.principal, text=' Limpar', image=self.img_limpar, compound=LEFT, bg=cor4, font=('arial 12 bold'), command= lambda:limpar([self.e_nome, self.e_sobrenome, self.e_cpf, self.e_celular, self.e_email, self.e_comment]), cursor='hand2')
        self.btn_limpar_cadastro.place(relx=.600, rely=.505, relheight=0.05, relwidth= 0.07)
        #botão salvar
        self.img_salvar = PhotoImage(file='imagens/salvar.png')
        self.btn_salvar = Button(self.principal, text='Salvar', image=self.img_salvar, compound=LEFT, bg=cor6, font=('arial 22 bold'), cursor='hand2', foreground='white', command=self.salvar_cliente)
        self.btn_salvar.place(relx=.25, rely=.91, relwidth=.18)
        #botão voltar
        self.img_voltar = PhotoImage(file='imagens/voltar.png')
        self.btn_voltar = Button(self.principal, image=self.img_voltar, bg='white', cursor='hand2', command=self.voltar, relief='flat')
        self.btn_voltar.place(relx=0.962, rely=0)
        
    def voltar(self):
        self.principal.place_forget()
        
        

    def tvw_hist(self):
        self.hist_titulo = Label(self.principal, text='Histórico Clientes', bg='white', font=('arial 16 bold'), foreground=cor5)
        self.hist_linha = Frame(self.principal, bg=cor5)
        self.hist_linha.place(relx=0.689, rely=0.17, relwidth=0.30, relheight=0.004)
        self.hist_titulo.place(relx=.689, rely=0.125) 
        self.hist_scroll = Scrollbar(self.principal)
        self.hist_scroll.place(relx=0.985, rely=0.2, relheight=.798, relwidth=.015)              
        self.tvw_hist = ttk.Treeview(self.principal, yscrollcommand=self.hist_scroll.set, columns=("Data", "Nome", "Valor"), show="headings")
        self.hist_scroll.config(command=self.tvw_hist.yview)       
        self.tvw_hist.column("Data", anchor=W, width=30, minwidth=20)
        self.tvw_hist.column("Nome", anchor=W, width=70, minwidth=120)
        self.tvw_hist.column("Valor", anchor=CENTER, width=70, minwidth=25)
        self.tvw_hist.place(relx=0.689, rely=0.20, relheight=.795, relwidth=.297)
        
        self.tvw_hist.heading("#1", text="DATA", anchor=CENTER)
        self.tvw_hist.heading("#2", text="NOME", anchor=CENTER)
        self.tvw_hist.heading("#3", text="VALOR", anchor=CENTER)

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
    
    def salvar_cliente(self):
        if self.filename is not None:
            with open(self.filename, 'rb') as img_file:
                self.byte_img = img_file.read()
        else:
            self.img_padrao = Image.open('imagens/pessoa.png')
            with open('imagens/pessoa.png', 'rb') as img_file:
                self.byte_img = img_file.read()
        value_imagem = self.byte_img
        value_nome = self.e_nome.get().strip()
        value_sobrenome = self.e_sobrenome.get()
        if len(self.e_celular.get()) < 13:
            messagebox.showerror('Erro', 'Numero de telefone inválido.')
        else:
            value_celular = self.e_celular.get()
        if len(self.e_cpf.get()) < 14:
            messagebox.showerror('Erro', 'Numero de cpf inválido.')
        else:
            value_cpf = self.e_cpf.get()
        value_instagram = self.e_instagram.get()
        value_obs = self.e_comment.get()
        value_cep = self.e_cep.get()
        if len(self.e_cep.get()) < 9:
            messagebox.showerror('Erro', 'Numero de cep inválido.')
        else:
            value_cpf = self.e_cep.get()
        value_rua = self.e_rua.get()
        value_numero = self.e_numero.get()
        value_bairro = self.e_bairro.get()
        value_cidade = self.e_cidade.get()
        value_estados = self.e_estados.get()
        
        query = "INSERT INTO clientes (imagem, nome, sobrenome, celular, cpf, instagram, OBS, CEP, rua, numero, bairro, cidade, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        params = (sqlite3.Binary(value_imagem), value_nome, value_sobrenome, value_celular, value_cpf, value_instagram, value_obs, value_cep, value_rua, value_numero, value_bairro, value_cidade, value_estados)
        self.banco.dml(query, params)
        print('cliente foi salvo')
        self.e_nome.delete(0, "end")
        placeholder_nome(self.e_nome)
        self.e_sobrenome.delete(0, "end")
        placeholder_sobrenome(self.e_sobrenome)
        self.e_cpf.delete(0, "end")
        placeholder_cpf(self.e_cpf)
        self.e_celular.delete(0, "end")
        placeholder_celular(self.e_celular)
        self.e_cep.delete(0, "end")
        placeholder_cep(self.e_cep)
        self.e_instagram.delete(0, "end")
        placeholder_instagram(self.e_instagram)
        self.e_comment.delete(0, 'end')        
        self.my_canvas.delete(self.img_id_resizer)
        self.img_id_resizer = None
        self.img_id = None        
        self.img = Image.open('imagens/pessoa.png')
        self.e_rua.delete(0, 'end')
        self.e_numero.delete(0,'end')
        self.e_bairro.delete(0,'end')
        self.e_cidade.delete(0,'end')
                                           
        messagebox.showinfo("Sucesso", "Operação realizada com sucesso!")
        
    def upload_instagram(self):
        usuario_instagram = self.e_instagram.get()
        try:
            url_foto_perfil = obter_url_foto_perfil(usuario_instagram)
        except:
            messagebox.showerror('Erro', 'Usuário de instagram não encontrado')
            
        if url_foto_perfil:
            caminho_foto_perfil = baixar_foto_perfil(url_foto_perfil, usuario_instagram)
            if caminho_foto_perfil:
                print('Foto de perfil baixada com sucesso:', caminho_foto_perfil)
            else:
                print('Não foi possível baixar a foto de perfil')
        else:
            print('Não foi possível obter a URL da foto de perfil')
        
        self.filename = f'imagens/{self.e_instagram.get()}.jpg'        
        self.img = Image.open(self.filename)
        largura = self.my_canvas.winfo_width()
        altura = self.my_canvas.winfo_height()
        resized_img2 = self.img.resize((largura, altura))
        self.img_tk = ImageTk.PhotoImage(resized_img2)
        self.img_id = self.my_canvas.create_image(0,0, image=self.img_tk, anchor='nw')
        return self.img_id
        
    def inserir_na_treeview(self):
        self.tvw_hist.tag_configure('oddrow', background='white')
        self.tvw_hist.tag_configure('evenrow', background='light gray') 
        if self.tvw_hist:
            self.tvw_hist.delete(*self.tvw_hist.get_children())       
        query ="SELECT nome, valor_gasto FROM clientes order by id"
        linhas= self.banco.dql(query)
        count=0
        data_atual = datetime.now().strftime('%d/%m/%Y')
        for i in linhas:
            values_with_date = (data_atual,) + i
            if count % 2 == 0:    
               self.tvw_hist.insert("", "end",values=values_with_date, tags=('oddrow',))             

            else:
                self.tvw_hist.insert("", "end",values=values_with_date, tags=('evenrow',))
            count+=1 