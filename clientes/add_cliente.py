from tkinter import *
from styles.cores import *
import tkinter as tk
from tkinter import filedialog
from formations import *
from tkinter import ttk
from PIL import Image, ImageTk
from limpar import limpar



class AddCliente():
    def __init__(self,frame_pai) -> None: 
        self.img = Image.open('imagens/pessoa.png')               
        self.principal = frame_pai
        self.add_client()
        self.hist_client()        
        self.tvw_hist()       
                      
        
    def add_client(self):
        #título 
        self.titulo = Label(self.principal, text='Ficha de Cadastro de Clientes', bg='white', font=('arial 16 bold'))
        self.linha = Frame(self.principal, bg=cor5)
        self.linha.place(relx=0.146, rely=0.17, relwidth=0.525, relheight=0.004)
        self.titulo.place(relx=0., rely=0.1, relwidth=0.5, relheight=0.1)
        #imagem
        self.my_canvas = Canvas(self.principal, bd=0, highlightthickness=0, relief='ridge')
        self.my_canvas.place(relx=0, rely=0.1, relheight=.34, relwidth=.14)
              
        self.my_canvas.bind('<Configure>', self.resizer)
        botao_upload = tk.Button(self.principal, command= self.upload , text="Upload de foto", font=('arial 12 bold'), background='green', foreground='white', cursor='hand2')
        botao_upload.place(relx=0, rely=0.44, relwidth=.14, relheight=0.04)
        # Entrys
            #nome
        self.title_nome = Label(self.principal, text='NOME:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_nome.place(relx=0.148, rely=0.195)
        self.e_nome = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
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
        self.title_email = Label(self.principal, text="EMAIL:", font=('arial 12'), foreground=cor4, bg='white')
        self.title_email.place(relx= 0.49 , rely=0.295) 
        self.e_email = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_email.place(relx=0.49, rely=0.34, relwidth=0.18, relheight=0.04)
        placeholder_email(self.e_email)
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
            #CIDADE
        self.title_cidade = Label(self.principal, text="CIDADE:", font=('arial 14'), foreground=cor4, bg='white')
        self.title_cidade.place(relx=.24, rely= .705 )
        self.e_cidade = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_cidade.place(relx=0.24, rely=0.75, relwidth=0.263, relheight=0.04)
            #ESTADO
        estados = ttk.Combobox(self.principal, font=('arial 12'), takefocus=True, state='readonly')
        estados['values'] = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
        estados.current(24)  # Pré-seleciona o estado de São Paulo
        estados.place(relx=0.545, rely=0.75, relwidth=0.124, relheight=0.04)      
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
        self.btn_salvar = Button(self.principal, text='Salvar', image=self.img_salvar, compound=LEFT, bg=cor6, font=('arial 22 bold'), cursor='hand2', foreground='white')
        self.btn_salvar.place(relx=.25, rely=.91, relwidth=.18)
        

    def hist_client(self):
        self.hist_titulo = Label(self.principal, text='Clientes Cadastrados', bg='white', font=('arial 16 bold'), foreground=cor5)
        self.hist_linha = Frame(self.principal, bg=cor5)
        self.hist_linha.place(relx=0.689, rely=0.17, relwidth=0.30, relheight=0.004)
        self.hist_titulo.place(relx=.51, rely=0.1, relwidth=0.5, relheight=0.1)

    def tvw_hist(self):               
        self.tvw_hist = ttk.Treeview(self.principal, columns=("Data", "Nome", "Valor Gasto"))
        self.tvw_hist.column("#0", width=25, minwidth=25)        
        self.tvw_hist.column("Data", anchor=W, width=120)
        self.tvw_hist.column("Nome", anchor=W, width=200, minwidth=120)
        self.tvw_hist.column("Valor Gasto", anchor=CENTER, width=80, minwidth=25)
        self.tvw_hist.place(relx=0.689, rely=0.21, relheight=.7, relwidth=.3)
        self.tvw_hist.heading("#0", text="ID", anchor=CENTER)
        self.tvw_hist.heading("#1", text="DATA", anchor=CENTER)
        self.tvw_hist.heading("#2", text="NOME", anchor=CENTER)
        self.tvw_hist.heading("#3", text="VALOR GASTO", anchor=CENTER)

    def resizer(self,e):
        global resized_img, new_img       
        resized_img = self.img.resize((e.width, e.height))        
        new_img = ImageTk.PhotoImage(resized_img)
        self.my_canvas.create_image(0,0, image=new_img, anchor='nw')

    def upload(self):        
        self.filename = filedialog.askopenfilename(title="Selecione uma foto", filetypes=[("Imagens", "*.jpg *.png *.bmp")])        
        self.img = Image.open(self.filename)
        largura = self.my_canvas.winfo_width()
        altura = self.my_canvas.winfo_height()
        resized_img2 = self.img.resize((largura, altura))
        self.img_tk = ImageTk.PhotoImage(resized_img2)
        self.my_canvas.create_image(0,0, image=self.img_tk, anchor='nw') 