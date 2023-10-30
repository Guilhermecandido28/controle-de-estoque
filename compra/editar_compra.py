from tkinter import *
from tkcalendar import DateEntry
from tkinter import ttk
from compra.bancodedadoscompra import*
from estoque.banco_dados_estoque import dql_args
class EditarCompra():
    def __init__(self,  id):
        self.janela = Tk()
        self.janela.title("Editar Compra")
        self.janela.geometry('500x800')
        self.id = id
        self.label_frames()
        self.labels()
        self.entrys()
        
       
    def data_compra(self):
        query = f'SELECT data_compra FROM compras WHERE id = ?' 
        data = compra_dql_args(query, self.id)
        return data[0][0]
    
    
    def data_entrega(self):
        query = f'SELECT data_entrega FROM compras WHERE id = ?' 
        data = compra_dql_args(query, self.id)
        return data[0][0]
    
    
    def data_vencimento(self):
        query = f'SELECT vencimento FROM compras WHERE id = ?' 
        data = compra_dql_args(query, self.id)
        return data[0][0]
    
    def info_cod_barras(self):
        query = f'SELECT codigo_de_barras FROM compras WHERE id = ?' 
        cod = compra_dql_args(query, self.id)
        return cod
    
    def info_fornecedor(self):
        query = f'SELECT fornecedor FROM compras WHERE id = ?'
        fornecedor = compra_dql_args(query, self.id)
        return fornecedor[0][0]
        
    def info_quantidade(self):
        query = f'SELECT quantidade FROM compras WHERE id = ?'
        quantidade = compra_dql_args(query, self.id)
        return quantidade[0][0]
        
    def info_frete(self):
        query = f'SELECT frete FROM compras WHERE id = ?'
        frete = compra_dql_args(query, self.id)
        return frete[0][0]

    def info_desconto(self):
        query = f'SELECT desconto FROM compras WHERE id = ?'
        desconto = compra_dql_args(query, self.id)
        return desconto[0][0]
    
    def info_status(self):
        query = 'SELECT status FROM compras WHERE id = ?'
        status = compra_dql_args(query, self.id)
        if status == 'Concluído':
            return 0
        else:
            return 1

    def info_produto(self, event):
        query = 'SELECT descricao, categoria, marca, tamanho, cor FROM estoque WHERE ID = ?'
        cod_barras = self.cod_barras.get()
        produto = dql_args(query, (cod_barras,))
        Label(
            self.frame_produtos,
            text=produto[0][0] + ' ' + produto[0][1] + ' ' + produto[0][2] + ' ' + produto[0][3] + ' ' + produto[0][4],
            font=('arial 12')
        ).place(relx=.25, rely=.275)

    def label_frames(self):
        self.frame_datas = LabelFrame(
            self.janela,
            text='Datas',
            font=('arial 14 bold')
        )
        self.frame_datas.place(relx=0.05, rely=0, relheight=.275, relwidth=.90)

        self.frame_produtos = LabelFrame(
            self.janela,
            text='Produtos',
            font=('arial 14 bold')
        )

        self.frame_produtos.place( relx=0.05, rely=.35, relheight=.275, relwidth=.9)

        self.frame_pagamento = LabelFrame(
            self.janela,
            text='Pagamento e Recebimento',
            font=('arial 14 bold')
            )
        self.frame_pagamento.place(relx=0.05, rely=.7, relheight=.275, relwidth=.9)
    
    def info_total(self):
        query = 'SELECT total FROM compras WHERE id = ?'
        total = compra_dql_args(query, self.id)
        return total
    
    def info_forma_pagamento(self):
        query = 'SELECT forma_de_pagamento FROM compras WHERE id = ?'
        pagto = compra_dql_args(query, self.id) 
        return pagto       
       
    def transformar_pagamento(self):
        pagamento = self.info_forma_pagamento()
        pagamento = pagamento[0][0]
        if pagamento == 'Crédito':
            return 0   
                 
        elif pagamento == 'Débito':            
            return 1
        
        elif pagamento == 'PIX':             
            return 2
        
        elif pagamento == 'Dinheiro':
            return 3
        
        else:
            return 4
    
    def labels(self):
        Label(
            self.frame_datas,
            text='Data da Compra:',
            font=('arial 12')
        ).place(relx=.03, rely=0.03)

        Label(
            self.frame_datas,
            text='Data da Entrega:',
            font=('arial 12')
        ).place(relx=0.03, rely=.35)

        Label(
            self.frame_datas,
            text='Vencimento:',
            font=('arial 12')
        ).place(relx=0.03, rely=.67)

        Label(
            self.frame_produtos,
            text='Cód. Barras:',
            font=('arial 12')
        ).place(relx=.03, rely=0.03)

        Label(
            self.frame_produtos,
            text='Produto:',
            font=('arial 12')
        ).place(relx=0.03, rely=.275)

        Label(
            self.frame_produtos,
            text='Quantidade:',
            font=('arial 12')
        ).place(relx=.03, rely=.52)

        self.label_fornecedor = Label(
            self.frame_produtos,
            text=f'Fornecedor:   {self.info_fornecedor()}',
            font=('arial 12')
        )
        self.label_fornecedor.place(relx=0.03, rely=.765)

        Label(
            self.frame_pagamento,
            text='Total:',
            font=('arial 12')
        ).place(relx=0.03, rely=0.03)

        Label(
            self.frame_pagamento,
            text='Forma de Pagamento:',
            font=('arial 12')
        ).place(relx=0.03, rely=.275)

        Label(
            self.frame_pagamento,
            text='Frete:',
            font=('arial 12')
        ).place(relx=0.03, rely=.52)

        Label(
            self.frame_pagamento,
            text='Desconto:',
            font=('arial 12')
        ).place(relx=.5, rely=.52)
        
        Label(
            self.frame_pagamento,
            text='Status:',
            font=('arial 12')
        ).place(relx=.03, rely=.765)

    def entrys(self):
        self.datacompra = DateEntry(
            self.frame_datas
        )
        self.datacompra.place(relx=0.35, rely=0.03)
        self.datacompra.set_date(self.data_compra())

        self.dataentrega = DateEntry(
            self.frame_datas
        )
        self.dataentrega.place(relx=0.35, rely=0.35)
        self.dataentrega.set_date(self.data_entrega())

        self.datavencimento = DateEntry(
            self.frame_datas,

        )
        self.datavencimento.place(relx=0.35, rely=.67),
        self.datavencimento.set_date(self.data_vencimento())

        self.cod_barras = ttk.Combobox(
            self.frame_produtos,
            state='readonly'
        )
        self.cod_barras.place(relx=0.35, rely=.03, relwidth=.6)
        self.cod_barras['values'] = self.info_cod_barras()
        self.cod_barras.bind('<<ComboboxSelected>>', lambda event: self.info_produto(event))


        self.quantidade = Spinbox(
            self.frame_produtos,
            from_=self.info_quantidade(),
            to= 999
                        
        )

        self.total = Entry(
            self.frame_pagamento,

        )
        self.total.place(relx=0.15, rely=.03)
        self.total.insert(0, self.info_total()[0][0])


        self.quantidade.place(relx=0.35, rely=.52, relwidth=.1)

        self.forma_pagamento = ttk.Combobox(
            self.frame_pagamento,
            values=(['Crédito', 'Débito', 'PIX', 'Dinheiro', 'Boleto'])
        )
        self.forma_pagamento.place(relx=.45, rely=.275, relwidth=.5)
        self.forma_pagamento.current(self.transformar_pagamento())

        self.frete = Entry(
            self.frame_pagamento
        )
        self.frete.place(relx=.15, rely=.52, relwidth=.25)
        self.frete.insert(0, self.info_frete())

        self.desconto = Entry(
            self.frame_pagamento
        )
        self.desconto.place(relx=.72, rely=.52, relwidth=.25)
        self.desconto.insert(0, self.info_desconto())

        self.status = ttk.Combobox(
            self.frame_pagamento,
            values=(['Concluído', 'Pendente']),
            state='readonly'
        )
        self.status.place(relx=0.175, rely=.765)
        self.status.current(self.info_status())