import tkinter as tk

class Application:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Botão Selecionado")
        
        self.cor4 = "blue"  # Defina sua cor de fundo padrão
        self.var_botao = tk.IntVar()  # Variável de controle para o Checkbutton
        
        self.buttons()
        
    def buttons(self):
        self.img_cliente = tk.PhotoImage(file='imagens/cliente.png')
        self.checkbtn_clientes = tk.Checkbutton(
            self.janela,
            text='Clientes',
            image=self.img_cliente,
            compound=tk.LEFT,
            bg=self.cor4,
            bd=0,
            font=('arial', 12, 'bold'),
            variable=self.var_botao,  # Associe a variável de controle ao Checkbutton
            command=self.toggle_cor_fundo  # A função a ser chamada quando o estado mudar
        )
        self.checkbtn_clientes.place(relx=0, rely=0, relwidth=0.14, relheight=1)
    
    def toggle_cor_fundo(self):
        if self.var_botao.get() == 1:  # Verifica se o Checkbutton está marcado (clicado)
            self.checkbtn_clientes.configure(bg='red')  # Define a cor de fundo quando selecionado
        else:
            self.checkbtn_clientes.configure(bg=self.cor4)  # Volta para a cor de fundo padrão

if __name__ == "__main__":
    janela = tk.Tk()
    app = Application(janela)
    janela.mainloop()
