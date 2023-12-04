from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from bancodedados.banco_dados import *




class EditarEstoque():
    def __init__(self, frame, img, id) -> None:
        self.f_editar_estoque = frame 
        self.banco_estoque = BancoDeDados('estoques.db')
        self.banco_fornecedor = BancoDeDados('fornecedores.db')       
        self.id = id
        self.img = img
        self.entrys()
        self.titulos()
        self.foto()
        self.botoes()

    def entrys(self):
        self.ed_barcode = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)
        self.ed_descricao = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)
        self.ed_categoria = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)
        self.ed_marca = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)
        self.ed_estoque_min = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)
        self.ed_quantidade = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)
        self.ed_obs = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)
        self.ed_tamanho = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)
        self.ed_cor = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)
        self.ed_preco_custo = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)
        self.ed_preco_venda = tk.Entry(self.f_editar_estoque, bg=cor4, font=('arial 12'), bd=0)       
        self.e_fornecedor = ttk.Combobox(self.f_editar_estoque, background=cor4, font=('arial 12'), state='readonly')
        query = "SELECT nome FROM fornecedor"
        self.e_fornecedor['values'] = self.banco_fornecedor.dql(query)
        
        #----------------------------------------------------------------------------------#
        self.ed_barcode.place(relx=.05, rely=.2, relwidth=.2, relheight=0.04) 
        self.ed_descricao.place(relx=.05, rely=.3, relwidth=.2, relheight=0.04)
        self.ed_categoria.place(relx=.05, rely=.4, relwidth=.2, relheight=0.04)
        self.ed_marca.place(relx=.05, rely=.5, relwidth=.2, relheight=0.04)
        self.ed_estoque_min.place(relx=.05, rely=.60, relwidth=.2, relheight=0.04)
        self.ed_quantidade.place(relx=.05, rely=.7, relwidth=.2, relheight=0.04)
        self.ed_obs.place(relx=.4, rely=.2, relwidth=.2, relheight=0.04)
        self.ed_tamanho.place(relx=.4, rely=.3, relwidth=.2, relheight=0.04)
        self.ed_cor.place(relx=.4, rely=.4, relwidth=.2, relheight=0.04)
        self.ed_preco_custo.place(relx=.4, rely=.5, relwidth=.2, relheight=0.04)
        self.ed_preco_venda.place(relx=.4, rely=.6, relwidth=.2, relheight=0.04)
        self.e_fornecedor.place(relx=0.4, rely=.7, relwidth=0.20, relheight=0.04)
    
    def titulos(self):
        self.linha = Frame(self.f_editar_estoque, bg=cor5)
        self.linha.place(relx=0.01, rely=0.1, relwidth=0.605, relheight=0.004)
        self.titulo_geral = Label(self.f_editar_estoque, text="Editor de Produtos", font=('arial 18'), bg='white')
        self.titulo_geral.place(relx=0.01, rely=0.05)
        self.t_ed_barcode = Label(self.f_editar_estoque, text='CÓDIGO DE BARRAS:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_descricao = Label(self.f_editar_estoque, text='DESCRIÇÃO:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_categoria = Label(self.f_editar_estoque, text='CATEGORIA:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_marca = Label(self.f_editar_estoque, text='MARCA:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_estoque_min = Label(self.f_editar_estoque, text='ESTOQUE MÍNIMO:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_quantidade = Label(self.f_editar_estoque, text='QUANTIDADE EM ESTOQUE:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_obs = Label(self.f_editar_estoque, text='OBS:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_tamanho = Label(self.f_editar_estoque, text='TAMANHO:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_cor = Label(self.f_editar_estoque, text='COR:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_preco_custo = Label(self.f_editar_estoque, text='CUSTO:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_preco_venda = Label(self.f_editar_estoque, text='VENDA:', font=('arial 14'), foreground=cor4, bg='white')
        self.t_ed_fonecedor = Label(self.f_editar_estoque, text='FORNECEDOR:', font=('arial 12'), foreground= cor4, bg='white')
        
        
        #-------------------------------------------#
        self.t_ed_barcode.place(relx=0.05, rely=.15,  relheight=0.04)
        self.t_ed_descricao.place(relx=0.05, rely=.25,  relheight=0.04)
        self.t_ed_categoria.place(relx=0.05, rely=.35,  relheight=0.04)
        self.t_ed_marca.place(relx=0.05, rely=.45,  relheight=0.04)
        self.t_ed_estoque_min.place(relx=0.05, rely=.55,  relheight=0.04)
        self.t_ed_quantidade.place(relx=0.05, rely=.65,  relheight=0.04)
        self.t_ed_obs.place(relx=0.4, rely=.15,  relheight=0.04)
        self.t_ed_tamanho.place(relx=0.4, rely=.25,  relheight=0.04)
        self.t_ed_cor.place(relx=0.4, rely=.35,  relheight=0.04)
        self.t_ed_preco_custo.place(relx=0.4, rely=.45,  relheight=0.04)
        self.t_ed_preco_venda.place(relx=0.4, rely=.55,  relheight=0.04)
        self.t_ed_fonecedor.place(relx=0.4, rely=.65)


    def foto(self):
        self.my_canvas = Canvas(self.f_editar_estoque, bd=0, highlightthickness=0, relief='ridge')
        self.my_canvas.place(relx=0.65, rely=0.1, relheight=.7, relwidth=.32)
        self.my_canvas.bind('<Configure>', self.resizer)        
        
    def botoes(self):
        # self.botao_upload = tk.Button(self.f_editar_cliente, text="Upload", font=('arial 12 bold'), background='green', foreground='white', cursor='hand2', command=self.upload)
        self.img_salvar = PhotoImage(file='imagens/salvar.png')
        self.btn_salvar = Button(self.f_editar_estoque, text='Salvar', image=self.img_salvar, compound=LEFT, bg=cor6, font=('arial 22 bold'), cursor='hand2', foreground='white', command=self.salvar_estoque)
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
    
    def salvar_estoque(self):                

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
        self.banco_estoque.dml(query, params)
        print('produto foi salvo')
        




