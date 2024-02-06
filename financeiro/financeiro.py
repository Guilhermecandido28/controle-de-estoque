from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image, ImageTk
from functions.functions import OndeEstou
import os

class Financeiro:
    def __init__(self, frame):
        self.principal = tk.Frame(frame, background='light gray')
        self.location_financeiro = tk.Canvas(frame, bd=0, highlightthickness=0)
        self.onde_estou()

    def onde_estou(self):
        local = OndeEstou(self.location_financeiro, 'FINANCEIRO', os.path.dirname(__file__))
        local.localizador()

        # coloca o nome da localização: FINANCEIRO
        self.location_financeiro.create_text(
            100, 30, text='FINANCEIRO', anchor=NW, font=('arial 18 bold underline'))

        # coloca a imagem de fundo e a torna responsiva
        self.img_location_financeiro = Image.open('imagens/location.png')
        self.img_location_financeiro_tk = ImageTk.PhotoImage(
            self.img_location_financeiro)
        self.location_financeiro.bind('<Configure>', self.resize_image)

    def resize_image(self, event):
        self.nova_imagem_financeiro = self.img_location_financeiro.resize(
            (event.width, event.height))
        self.nova_imagem_financeiro_tk = ImageTk.PhotoImage(self.nova_imagem_financeiro)
        self.location_financeiro.create_image(
            0, 0, anchor=NW, image=self.nova_imagem_financeiro_tk)
        self.location_financeiro.image = self.nova_imagem_financeiro_tk

    def financeiro(self):
        self.principal.place(relx=0.01, rely=0.25, relwidth=0.98, relheight=0.72)
        Label(self.principal,
              text='EM BREVE!',
              font=('arial 28 bold'),
              bg='light gray').pack(pady=(60, 0), padx=10)
