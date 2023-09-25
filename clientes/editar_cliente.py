from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from clientes.banco_dados_cliente import *
import io


class EditarCliente():
    def __init__(self, frame, img, id) -> None:
        self.f_editar_cliente = frame
        self.img = img
        self.id = id
        
        self.entrys()
        self.titulos()
        self.foto()
        self.botoes()

    def entrys(self):
        self.ed_id = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_nome = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_sobrenome = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_cpf = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_celular = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_instagram = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_comment = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_cep = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_rua = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_numero = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_bairro = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_cidade = tk.Entry(self.f_editar_cliente, bg=cor4, font=('arial 12'), bd=0)
        self.ed_estados = ttk.Combobox(self.f_editar_cliente, font=('arial 12'), takefocus=True, state='readonly')
        self.ed_estados['values'] = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
        self.ed_estados.current(24)  # Pré-seleciona o estado de São Paulo
        
        placeholder_nome(self.ed_nome)
        placeholder_sobrenome(self.ed_sobrenome)
        placeholder_celular(self.ed_celular)
        placeholder_cpf(self.ed_cpf)
        placeholder_instagram(self.ed_instagram)
        placeholder_cep(self.ed_cep)
        #----------------------------------------------------------------------------------#
        self.ed_id.place(relx=.05, rely=.2, relwidth=.05, relheight=0.04) 
        self.ed_nome.place(relx=.05, rely=.3, relwidth=.2, relheight=0.04)
        self.ed_sobrenome.place(relx=.05, rely=.4, relwidth=.2, relheight=0.04)
        self.ed_cpf.place(relx=.05, rely=.5, relwidth=.2, relheight=0.04)
        self.ed_celular.place(relx=.05, rely=.60, relwidth=.2, relheight=0.04)
        self.ed_instagram.place(relx=.05, rely=.7, relwidth=.2, relheight=0.04)
        self.ed_comment.place(relx=.4, rely=.2, relwidth=.2, relheight=0.04)
        self.ed_cep.place(relx=.4, rely=.3, relwidth=.2, relheight=0.04)
        self.ed_rua.place(relx=.4, rely=.4, relwidth=.2, relheight=0.04)
        self.ed_numero.place(relx=.4, rely=.5, relwidth=.2, relheight=0.04)
        self.ed_bairro.place(relx=.4, rely=.6, relwidth=.2, relheight=0.04)
        self.ed_cidade.place(relx=.4, rely=.7, relwidth=.2, relheight=0.04)
        self.ed_estados.place(relx=.4, rely=0.8, relwidth=0.124, relheight=0.04)
    
    def titulos(self):
        self.linha = Frame(self.f_editar_cliente, bg=cor5)
        self.linha.place(relx=0.01, rely=0.1, relwidth=0.605, relheight=0.004)
        self.titulo_geral = Label(self.f_editar_cliente, text="Editor de Clientes", font=('arial 18'), bg='white')
        self.titulo_geral.place(relx=0.01, rely=0.05)
        self.t_ed_id = Label(self.f_editar_cliente, text='ID:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_nome = Label(self.f_editar_cliente, text='NOME:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_sobrenome = Label(self.f_editar_cliente, text='SOBRENOME:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_cpf = Label(self.f_editar_cliente, text='CPF:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_celular = Label(self.f_editar_cliente, text='CELULAR:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_instagram = Label(self.f_editar_cliente, text='INSTAGRAM:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_comment = Label(self.f_editar_cliente, text='OBS:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_cep = Label(self.f_editar_cliente, text='CEP:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_rua = Label(self.f_editar_cliente, text='RUA:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_numero = Label(self.f_editar_cliente, text='NUMERO:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_bairro = Label(self.f_editar_cliente, text='BAIRRO:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_cidade = Label(self.f_editar_cliente, text='CIDADE:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_estado = Label(self.f_editar_cliente, text='ESTADO:', font=('arial 14'), foreground=cor4, bg='white')
        
        #-------------------------------------------#
        self.t_ed_id.place(relx=0.05, rely=.15,  relheight=0.04)
        self.t_ed_nome.place(relx=0.05, rely=.25,  relheight=0.04)
        self.t_ed_sobrenome.place(relx=0.05, rely=.35,  relheight=0.04)
        self.t_ed_cpf.place(relx=0.05, rely=.45,  relheight=0.04)
        self.t_ed_celular.place(relx=0.05, rely=.55,  relheight=0.04)
        self.t_ed_instagram.place(relx=0.05, rely=.65,  relheight=0.04)
        self.t_ed_comment.place(relx=0.4, rely=.15,  relheight=0.04)
        self.t_ed_cep.place(relx=0.4, rely=.25,  relheight=0.04)
        self.t_ed_rua.place(relx=0.4, rely=.35,  relheight=0.04)
        self.t_ed_numero.place(relx=0.4, rely=.45,  relheight=0.04)
        self.t_ed_bairro.place(relx=0.4, rely=.55,  relheight=0.04)
        self.t_ed_cidade.place(relx=0.4, rely=.65,  relheight=0.04)
        self.t_ed_estado.place(relx=0.4, rely=.75,  relheight=0.04)

    def foto(self):
        self.my_canvas = Canvas(self.f_editar_cliente, bd=0, highlightthickness=0, relief='ridge')
        self.my_canvas.place(relx=0.65, rely=0.1, relheight=.7, relwidth=.32)
        self.my_canvas.bind('<Configure>', self.resizer)        
        
    def botoes(self):
        # self.botao_upload = tk.Button(self.f_editar_cliente, text="Upload", font=('arial 12 bold'), background='green', foreground='white', cursor='hand2', command=self.upload)
        self.img_salvar = PhotoImage(file='imagens/salvar.png')
        self.btn_salvar = Button(self.f_editar_cliente, text='Salvar', image=self.img_salvar, compound=LEFT, bg=cor6, font=('arial 22 bold'), cursor='hand2', foreground='white', command=self.salvar_cliente)
        self.btn_salvar.place(relx=.25, rely=.91, relwidth=.18)
        # self.botao_upload.place(relx=0.65, rely=0.80, relwidth=.32, relheight=0.08)

    def resizer(self,e):
        global resized_img, new_img       
        resized_img = self.img.resize((e.width, e.height))        
        new_img = ImageTk.PhotoImage(resized_img)        
        self.img_id_resizer = self.my_canvas.create_image(0,0, image=new_img, anchor='nw')
        return self.img_id_resizer

    # def upload(self):                
    #     self.filename = filedialog.askopenfilename(title="Selecione uma foto", filetypes=[("Imagens", "*.jpg *.png *.bmp")])               
    #     self.img = Image.open(self.filename)
    #     largura = self.my_canvas.winfo_width()
    #     altura = self.my_canvas.winfo_height()
    #     resized_img2 = self.img.resize((largura, altura))
    #     self.img_tk = ImageTk.PhotoImage(resized_img2)
    #     self.img_id = self.my_canvas.create_image(0,0, image=self.img_tk, anchor='nw')
    #     return self.img_id 
    
    def salvar_cliente(self):                

        modify_id = self.ed_id.get()
        
        modify_nome = self.ed_nome.get()
        modify_sobrenome = self.ed_sobrenome.get()
        modify_celular = self.ed_celular.get()
        modify_cpf = self.ed_cpf.get()
        modify_instagram = self.ed_instagram.get()
        modify_obs = self.ed_comment.get()
        modify_cep = self.ed_cep.get()
        modify_rua = self.ed_rua.get()
        modify_numero = self.ed_numero.get()
        modify_bairro = self.ed_bairro.get()
        modify_cidade = self.ed_cidade.get()
        modify_estados = self.ed_estados.get()

        query = f"UPDATE clientes SET id = ?, nome = ?, sobrenome = ?, celular = ?, cpf = ?, instagram = ?, OBS = ?, CEP = ?, rua = ?, numero = ?, bairro = ?, cidade = ?, estado = ? WHERE id = {self.id}"
        params = (modify_id, modify_nome, modify_sobrenome, modify_celular, modify_cpf, modify_instagram, modify_obs, modify_cep, modify_rua, modify_numero, modify_bairro, modify_cidade, modify_estados)
        dml(query, params)
        print('cliente foi salvo')
        




