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
        self.header = tk.Frame(self.janela, bg=cor3)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.09)
        self.menu = tk.Frame(self.janela, bg=cor4)
        self.menu.place(relx=0, rely=0.09, relwidth=1, relheight=0.05)
        self.location = tk.Frame(self.janela, bg=cor1)
        self.location.place(relx=0, rely=0.14, relwidth=1, relheight=0.09)
        self.search = tk.Frame(self.janela, bg=cor2)
        self.search.place(relx=0, rely=0.23, relwidth=1, relheight=0.05)
        self.principal = tk.Frame(self.janela, bg= 'white')
        self.principal.place(relx=0.01, rely=0.28, relwidth=0.98, relheight=0.67)
        

    def buttons(self):
        self.img_cliente = PhotoImage(file='imagens/cliente.png')
        self.btn_clientes = Button(
            self.menu, 
            text='Clientes', 
            image=self.img_cliente, 
            compound=LEFT, 
            bg=cor4, 
            bd=0,
            font=('arial 12 bold')
            
            )
        self.btn_clientes.place(relx=0, rely=0, relwidth=0.14, relheight=1)
 
Applicantion()

        
          

    