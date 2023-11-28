from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image, ImageTk

class Troca():
    def __init__(self, frame):
        self.principal = tk.Frame(frame, background='light gray')
        self.location_troca = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.onde_estou()

    def onde_estou(self):
        # aqui coloca o frame de localização usando o metodo place
        self.location_troca.place(
            relx=0, rely=0.14, relwidth=1, relheight=0.09)

        # coloca o nome da localização: FINANCEIRO
        self.location_troca.create_text(
            100, 30, text='TROCAS', anchor=NW, font=('arial 18 bold underline'))

        # coloca a imagem de fundo e a torna responsiva
        self.img_location_troca = Image.open('imagens/location.png')
        self.img_location_troca_tk = ImageTk.PhotoImage(
            self.img_location_troca)
        self.location_troca.bind('<Configure>', self.resize_image)

    def resize_image(self, event):
        self.nova_imagem_troca = self.img_location_troca.resize(
            (event.width, event.height))
        self.nova_imagem_troca_tk = ImageTk.PhotoImage(self.nova_imagem_troca)
        self.location_troca.create_image(
            0, 0, anchor=NW, image=self.nova_imagem_troca_tk)
        self.location_troca.image = self.nova_imagem_troca_tk

    def troca(self):
        self.principal.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.72)
        Label(self.principal,
              text='Entrada:',
              font=('arial 28 bold'),
              bg='light gray').place(relx=.1, rely=.3)
        
        self.entrada = Entry(
            self.principal,
            background= 'white',
            font= ('arial 28')
                    )
        self.entrada.place(relx=.25, rely=.3)

        Label(self.principal,
              text='Saída:',
              font=('arial 28 bold'),
              bg='light gray').place(relx=.1, rely=.5)

        self.saida = Entry(
            self.principal,
            background= 'white',
            font= ('arial 28')
                    )
        self.saida.place(relx=.25, rely=.5)

        Button(
            self.principal,
            text="Confirmar",
            font=('arial 18 bold')
        ).place(relx=.6, rely=.4)


