from tkinter import *
from styles.cores import *
import tkinter as tk


janela = Tk()


class Applicantion():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.buttons()        
        janela.mainloop()
    def tela(self):
        self.janela.title('Controle fincanceiro')
        self.janela.geometry('1500x1000')
        self.janela.configure(background= cor5)
    
    def frames(self):
        self.menu = tk.Frame(self.janela, bg=cor4)
        self.menu.place(relx=0, rely=0, relwidth=0.1, relheight=1)

    def buttons(self):
        imagem_venda= PhotoImage(file='imagens/vendas.png', master=self.menu)        
        img_venda = Label(self.menu, text='VENDAS', image=imagem_venda)
        img_venda.image = imagem_venda
        self.venda = tk.Button(self.menu, text='VENDAS', image=imagem_venda, bd=0, highlightthickness=0, bg=cor4)
        self.venda.place(relx=0,rely=0, relwidth=1, relheight=0.1)
        
Applicantion()

        
          

    