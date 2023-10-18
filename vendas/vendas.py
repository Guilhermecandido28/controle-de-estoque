from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image, ImageTk
import threading 

class Vendas():
    def __init__(self, frame) -> None:
        self.principal = tk.Frame(frame, background='white')
        self.location_venda = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.should_continue = True
        self.onde_estou()
        self.nova_compra()

    def onde_estou(self):
        #aqui coloca o frame de localização usando o metodo place
        self.location_venda.place(relx=0, rely=0.14, relwidth=1, relheight=0.09)

            # coloca o nome da localização: COMPRA
        self.location_venda.create_text(100,30, text='VENDAS', anchor=NW, font=('arial 18 bold underline'))

            # coloca a imagem de fundo e a torna responsiva
        self.img_location_compra = Image.open('imagens/location.png')
        self.img_location_compra_tk = ImageTk.PhotoImage(self.img_location_compra)
        self.location_venda.bind('<Configure>', self.resize_image)
    def resize_image(self, event):
        self.nova_imagem_venda = self.img_location_compra.resize((event.width, event.height))
        self.nova_imagem_venda_tk = ImageTk.PhotoImage(self.nova_imagem_venda)
        self.location_venda.create_image(0,0, anchor = NW, image = self.nova_imagem_venda_tk)
        self.location_venda.image = self.nova_imagem_venda_tk

    def nova_compra(self):
        #aqui coloca o frame responsavel pela lista
        self.principal.place(relx=0.01, rely=0.32, relwidth=0.98, relheight=0.65)
        Button(self.principal, text='iniciar venda', command=self.leitor_codigo).pack()
        Button(self.principal, text='finalizar venda', command=self.stop_loop).pack()

        

    def leitor_codigo(self):        
        # Simula a leitura do código de barras
        self.codigo = Entry(self.principal).pack()
                
        
    def stop_loop(self):
        self.should_continue = False 