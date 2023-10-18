from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from limpar import limpar
from tkinter import ttk
from tkinter import messagebox
from estoque.banco_dados_estoque import *
from PIL import Image, ImageTk
from fornecedor.banco_dados_fornecedor import fornecedor_dql, fornecedor_dql_arg
from estoque.banco_dados_estoque import dql
import customtkinter as ctk
from tkcalendar import DateEntry
from datetime import date


class AddCompra():
    def __init__(self, frame):
        self.principal = frame
        self.layout_add_compra()
        self.index = 1
        self.rely = 0.02 
        self.lista_preços = []
               
        
    def layout_add_compra(self):
        #-------------------------Cabecalho------------------------------#
        self.principal.place(relx=0.01, rely=.25, relwidth = .98, relheight = .72)
        ttk.Label(self.principal, text='Cadastrar Nova Compra', font=('arial 18 bold'), background='white').place(relx=.05, rely=0.025)  # titulo principal
        ttk.Separator(self.principal, orient='vertical').place(relx=0.05, rely=.07, relwidth=.9) 

        #--------------------------Frames secundários-----------------------------#        
        self.frame_pedido = Frame(self.principal, background='light gray' ,bd=0)        
        self.frame_lista_pedidos = Frame(self.principal, background='light gray')
        self.frame_info = Frame(self.principal, background=cor4, bd=0) 
        self.frame_info.place(relx=0.05, rely=.45, relwidth=.5, relheight=.45)      
        self.frame_pedido.place(relx=0.05, rely=.3, relwidth=.5, relheight=.15)
        self.frame_lista_pedidos.place(relx=.6, rely=.3, relwidth=.39, relheight=.6)
        

        
        #------------------------------Labels -------------------------------------------#
        ttk.Label(self.principal, text='Fornecedor:', font=('arial 14 bold'), foreground=cor4, background='white').place(relx=.35, rely=.1)
        ttk.Label(self.principal, text='Produto:', font=('arial 14 bold'), foreground=cor4, background='white').place(relx=.60, rely=.1)
        ttk.Label(self.principal, text='Valores:', font=('arial 14 bold'), foreground=cor4, background='white').place(relx=.05, rely=.25)
        self.msg_erro = ttk.Label(self.principal, text='Selecione um fornecedor primeiro.', foreground='red', background='white')
        self.msg_erro.place(relx=0.6, rely=.2)
        ttk.Label(self.frame_pedido, text='Cod. Barras:', background='light gray', font=('arial 12 bold')).place(relx=0, rely=0)
        ttk.Label(self.frame_pedido, text='Item:', background='light gray', font=('arial 12 bold')).place(relx=.2, rely=0)
        ttk.Label(self.frame_pedido, text='Tam.:', background='light gray', font=('arial 10 bold')).place(relx=.14, rely=.35)
        ttk.Label(self.frame_pedido, text='Cor:', background='light gray', font=('arial 10 bold')).place(relx=.153, rely=.5)
        ttk.Label(self.frame_pedido, text='QTDE:', background='light gray', font=('arial 12 bold')).place(relx=.4, rely=0)
        ttk.Label(self.frame_pedido, text='Preço:', background='light gray', font=('arial 12 bold')).place(relx=.55, rely=0)
        ttk.Label(self.frame_pedido, text='Total:', background='light gray', font=('arial 12 bold')).place(relx=.7, rely=0)
        ttk.Label(self.principal, text="N°", background='white', font=('arial 12 bold'), foreground=cor4).place(relx=.605, rely=.27)
        ttk.Label(self.principal, text="Produto", background='white', font=('arial 12 bold'), foreground=cor4).place(relx=.65, rely=.27)
        ttk.Label(self.principal, text="QTD", background='white', font=('arial 12 bold'), foreground=cor4).place(relx=.85, rely=.27)
        ttk.Label(self.principal, text="Total", background='white', font=('arial 12 bold'), foreground=cor4).place(relx=.9, rely=.27)
        ttk.Label(self.principal, text="Excluir", background='white', font=('arial 12 bold'), foreground=cor4).place(relx=.95, rely=.27)
        ttk.Label(self.principal, text='PRAZO ENTREGA:', background='white', font=('arial 12 bold'), foreground=cor4).place(relx=0.05, rely=.1)
        ttk.Label(self.principal, text='DATA DA COMPRA', background='white', font=('arial 12 bold'), foreground=cor4).place(relx=.2, rely=.1)
        ttk.Separator(self.principal, orient='vertical').place(relx=.6, rely=.3, relwidth=.39)
        ttk.Label(self.frame_info, text='SubTotal:', background=cor4, font=('arial 12 bold')).place(relx=0, rely=0)
        ttk.Label(self.frame_info, text='Frete:', background=cor4, font=('arial 12 bold')).place(relx=0.15, rely=0)
        ttk.Label(self.frame_info, text='Desconto:', background=cor4, font=('arial 12 bold')).place(relx=0.30, rely=0)
        ttk.Label(self.frame_info, text='Total Final:', background=cor4, font=('arial 12 bold')).place(relx=0.46, rely=0)
        ttk.Label(self.frame_info, text='Valor Pago:', background=cor4, font=('arial 12 bold')).place(relx=0.63, rely=0)
        ttk.Label(self.frame_info, text='Valor Pendente:', background=cor4, font=('arial 12 bold')).place(relx=0.82, rely=0)
        ttk.Label(self.frame_info, text='Forma de Pagamento:', background=cor4, font=('arial 12 bold')).place(relx=0.0, rely=.23)
        ttk.Label(self.frame_info, text='Parcelamento:', background=cor4, font=('arial 12 bold')).place(relx=0.28, rely=.23)
        ttk.Label(self.frame_info, text='Vencimento:', background=cor4, font=('arial 12 bold')).place(relx=0.48, rely=.23)

        

        #------------------------------- Entrys -----------------------------------------#        
        self.fornecedores = ttk.Combobox(self.principal, values=self.obter_fornecedores(), font=('Arial', 14), state='readonly')
        self.fornecedores.place(relx=0.35, rely=.15, relwidth=.20, relheight=.04)
        self.fornecedores.bind('<<ComboboxSelected>>', lambda event: self.obter_produtos(event))
        self.produtos = ttk.Combobox(self.principal, font=('Arial', 12), state='readonly')
        self.produtos.place(relx=0.60, rely=.15, relwidth=.20, relheight=.04)
        self.produtos.bind('<<ComboboxSelected>>', lambda event: self.obter_info_produtos(event))
        self.qtde = Spinbox(self.frame_pedido, background='light gray', font=('arial 12 bold'), bd=0, highlightthickness=0, from_=0, to=1000, command=self.total_relativo)
        self.qtde.bind('<KeyRelease>', lambda event: self.chamar_função(event))
        self.qtde.place(relx=.425, rely=.20, relheight=.25, relwidth=.06)
        self.data_hoje = DateEntry(self.principal, justify= 'center', font=('arial', 12))
        self.data_hoje.set_date(date.today())
        self.data_hoje.place(relx=0.05, rely=.15, relwidth= .11, relheight=.04)
        self.data_entrega = DateEntry(self.principal, justify= 'center', font=('arial', 12))
        self.data_entrega.set_date(date.today())
        self.data_entrega.place(relx=0.2, rely=.15, relwidth= .11, relheight=.04)
        self.desconto = Entry(self.frame_info, bd=0, highlightthickness=0, background='light gray', justify='right', font=('arial 10'))
        self.desconto.place(relx=.3, rely=.1, relheight=.08, relwidth=.11)
        self.frete = Entry(self.frame_info, bd=0, highlightthickness=0, background='light gray', justify='right', font=('arial 10'))
        self.frete.place(relx=.15, rely=.1, relheight=.08, relwidth=.11)
        placeholder_custo(self.frete)        
        self.forma_pag = ttk.Combobox(self.frame_info, font=('Arial', 12), state='readonly')
        self.forma_pag.place(relx=0.0, rely=.33, relwidth=.23, relheight=.08)
        self.parcelamento = ttk.Combobox(self.frame_info, font=('Arial', 12), state='readonly')
        self.parcelamento.place(relx=0.28, rely=.33, relwidth=.15, relheight=.08)
        self.data_vencimento = DateEntry(self.frame_info, justify= 'center', font=('arial', 12))
        self.data_vencimento.set_date(date.today())
        self.data_vencimento.place(relx=0.48, rely=.33, relwidth= .15, relheight=.08)


        #-----------------------------------Botões ----------------------------------------#
        Button(self.frame_pedido, bg='gray', text='Incluir\n Pedido', cursor='hand2', font=('arial 12 bold'), command=self.lista_pedidos).place(relx=.85, rely=0, relwidth=.15, relheight=1)
        Button(self.frame_info, bg='light gray', font=('arial 12 bold'), text='Gerar Contas', cursor='hand2').place(relx=.68, rely=.26, relheight=.15, relwidth=.28)
        
    def chamar_função(self, event):        
        self.total_relativo()
        
    def total_relativo(self):
                
        try:      
            self.preço = info[0][2]
            self.preço = float(self.preço)*int(self.qtde.get())
            self.label_total = ttk.Label(self.frame_pedido, text=f'R${self.preço:.2f}', background='light gray', font=('arial 10 '))
            if self.preço < 100:
                self.label_total.place(relx=0.7, rely=.2,relwidth=.1)
            else: 
                self.label_total.place(relx=0.7, rely=.2)
            
        except:
            pass
        
    def obter_info_produtos(self, event):
        global info, info_produtos
        info_produtos = self.produtos.get()
        info_produtos = info_produtos.split(' - ')        
        query = 'SELECT ID, descricao, custo, tamanho, cor FROM estoque WHERE descricao = ? AND categoria = ? AND marca = ?'
        info = dql_args(query, (info_produtos[0].strip(), info_produtos[1].strip(), info_produtos[2].strip()))
        ttk.Label(self.frame_pedido, text=info[0][0], background='light gray', font=('arial 10 ')).place(relx=0, rely=.2)
        ttk.Label(self.frame_pedido, text=f'{info[0][1]}\n{info[0][3]}\n{info[0][4]}', background='light gray', font=('arial 10 ')).place(relx=0.2, rely=.2)
        ttk.Label(self.frame_pedido, text=f'R${info[0][2]}', background='light gray', font=('arial 10 ')).place(relx=0.55, rely=.2)
        if int(self.qtde.get()) > 0:
            self.label_total = ttk.Label(self.frame_pedido, text=f'R${float(info[0][2])*int(self.qtde.get()):.2f}', background='light gray', font=('arial 10 '))
            self.label_total.place(relx=0.7, rely=.2)

    def obter_fornecedores(self):
        lista_fornecedores = []
        query = "SELECT nome FROM fornecedor"
        fornecedores = fornecedor_dql(query)
        for fornecedor in fornecedores:
            lista_fornecedores.append(fornecedor[0])
        return lista_fornecedores
    
    def obter_produtos(self, event):
        self.msg_erro.place_forget()        
        fornecedor = self.fornecedores.get()
        self.lista_produtos = []
        query = "SELECT lista_produtos FROM fornecedor WHERE nome = ?"
        produtos = fornecedor_dql_arg(query, (fornecedor,))
        produtos = produtos[0][0].split(';')
        for produto in produtos:
            self.lista_produtos.append(produto)
        self.produtos['values'] = self.lista_produtos


    def reorganizar_labels(self):
        rely=.02
        count = 0
        for position in self.frame_lista_pedidos.winfo_children():
            position.place_configure(rely=rely)
            count+=1          
            
            if count == 5:            
                rely+=0.1
                count = 0


    def lista_pedidos(self):
        if self.qtde.get() == '0':
            messagebox.showerror('Erro', "A Quantidade não pode ser 0.")
        else:
            if self.rely > 0.92:
                self.rely-=.1            
                messagebox.showerror('Erro', "No máximo 10 itens por compra.")
            else:
                image = Image.open('imagens/excluir.png')
                tk_image = ImageTk.PhotoImage(image)
                self.lista_preços.append(self.preço)
                index_label = Label(self.frame_lista_pedidos, text=f'{self.index}', font=('arial 12'), background='light gray')
                index_label.place(relx=0.0, rely=self.rely)
                produto_label = Label(self.frame_lista_pedidos, text=f'{info[0][1]} - {info[0][3]} - {info[0][4]}', font=('arial 12'), background='light gray')
                produto_label.place(relx=.125, rely=self.rely)
                qtd_label = Label(self.frame_lista_pedidos, text=f'{self.qtde.get()}', font=('arial 12'), background='light gray')
                qtd_label.place(relx=.65, rely=self.rely)
                preco = tk.StringVar(value=f'R$ {self.preço:.2f}')
                entry_total = Label(self.frame_lista_pedidos, textvariable=preco, font=('arial 12'), bg='light gray')
                entry_total.place(relx=.75, rely=self.rely)
                self.subtotal()
                # Botão "Excluir" com a função de remover a entrada correspondente
                def excluir_item():                             
                    index_label.destroy()
                    produto_label.destroy()
                    qtd_label.destroy()
                    entry_total.destroy()
                    excluir_button.destroy()
                    self.reorganizar_labels()
                    self.rely-=.1
                                           
                      
                    self.subtotal()
                excluir_button = ctk.CTkButton(self.frame_lista_pedidos,
                                            text='',
                                            image=tk_image,
                                            compound='right',
                                            font=('Arial', 18, 'bold'),
                                            text_color="white",
                                            hover=True,
                                            hover_color="#454545",
                                            height=20,
                                            width=40,
                                            border_width=2,
                                            corner_radius=10,
                                            border_color="#161616",
                                            fg_color="#363636",
                                            command=excluir_item)
                excluir_button.place(relx=.9, rely=self.rely)

                self.index += 1
                self.rely += .1
            
    def subtotal(self):                   
        soma_valores = sum(self.lista_preços)
        valor= f'R${soma_valores:.2f}'.replace('.', ',')
        label_valor = ttk.Label(self.frame_info, text=valor, background=cor4, font=('arial 14 bold'), foreground='#3738EB')
        label_valor.place(relx=0, rely=.075)
        
         

               
        




