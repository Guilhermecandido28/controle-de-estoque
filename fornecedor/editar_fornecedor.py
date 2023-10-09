from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from estoque.banco_dados_estoque import *
import io


class EditarFornecedor():
    def __init__(self, frame, img, id) -> None:
        self.f_editar_fornecedor = frame        
        self.id = id
        self.img = img
        self.entrys()
        self.titulos()
        self.foto()
        self.botoes()

    def entrys(self): 
        self.ed_id = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)       
        self.ed_nome = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_categoria = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_cnpj = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_email = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_telefone = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_obs = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_cep = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_rua = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_numero = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_bairro = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
        self.ed_cidade = tk.Entry(self.f_editar_fornecedor, bg=cor4, font=('arial 12'), bd=0)
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
        


    def foto(self):
        self.my_canvas = Canvas(self.f_editar_fornecedor, bd=0, highlightthickness=0, relief='ridge')
        self.my_canvas.place(relx=0.65, rely=0.1, relheight=.7, relwidth=.32)
        self.my_canvas.bind('<Configure>', self.resizer)        
        
    def botoes(self):
        # self.botao_upload = tk.Button(self.f_editar_cliente, text="Upload", font=('arial 12 bold'), background='green', foreground='white', cursor='hand2', command=self.upload)
        self.img_salvar = PhotoImage(file='imagens/salvar.png')
        self.btn_salvar = Button(self.f_editar_fornecedor, text='Salvar', image=self.img_salvar, compound=LEFT, bg=cor6, font=('arial 22 bold'), cursor='hand2', foreground='white', command=self.salvar_fornecedor)
        self.btn_salvar.place(relx=.72, rely=.87, relwidth=.18)
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
    
    def salvar_fornecedor(self):                

        modify_barcode = self.ed_barcode.get()
        
        modify_descricao = self.ed_descricao.get().strip()
        modify_categoria = self.ed_categoria.get()
        modify_marca = self.ed_marca.get()
        modify_estoque_min = self.ed_estoque_min.get()
        modify_quantidade = self.ed_quantidade.get()
        modify_obs = self.ed_obs.get()
        modify_tamanho = self.ed_tamanho.get()
        modify_cor = self.ed_cor.get()
        modify_preco_custo = self.ed_preco_custo.get()
        modify_preco_venda = self.ed_preco_venda.get()
        
        query = f"UPDATE estoque SET id = ?, descricao = ?, categoria = ?, marca = ?, estoque_minimo = ?, quantidade = ?, observacoes = ?, tamanho = ?, cor = ?, custo = ?, venda = ? WHERE id = {self.id}"
        params = (modify_barcode, modify_descricao, modify_categoria, modify_marca, modify_estoque_min, modify_quantidade, modify_obs, modify_tamanho, modify_cor, modify_preco_custo, modify_preco_venda)
        dml(query, params)
        print('produto foi salvo')
        