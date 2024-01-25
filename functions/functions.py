from PIL import Image, ImageTk
from tkinter.constants import NW
import os



class Redimensionamento:
    def __init__(self, imagem) -> None:
        self.imagem = imagem    
    
    def resize(self, frame, event):
        nova_imagem = self.imagem.resize((event.width, event.height)) # ajusta a imagem confome necessário
        nova_imagem_tk = ImageTk.PhotoImage(nova_imagem) # transforma em um formato que o tkinter aceita
        frame.create_image(0, 0, anchor=NW, image=nova_imagem_tk) # coloca a imagem no frame
        frame.image = nova_imagem_tk # garante que a imagem permaneça enquando a interface gráfica estiver ativa

class OndeEstou:
    def __init__(self, frame, texto, diretorio) -> None:
        self.frame = frame
        self.texto = texto
        self.diretorio = diretorio

    def localizador(self):
        
        self.frame.place(
            relx=0,
            rely=0.14,
            relwidth=1,
            relheight=0.09) # coloca o frame na interface
        
        self.frame.create_text(
        100,
         30,
         text=f'{self.texto}',
         anchor=NW,
         font=('arial 18 bold underline')) # cria o texto que identifica a localização.
        
        caminho_absoluto = os.path.join(os.path.dirname(__file__), self.diretorio) # caminho da imagem
        imagem = Image.open(f'{caminho_absoluto}') # abre a imagem 

        self.obj = Redimensionamento(imagem) # classe reposavel pelo redimensionamento eventual da imagem
        
        self.frame.bind('<Configure>', lambda event: self.obj.resize(self.frame, event)) # metodo que responsavel por iniciar o processo de redimensionamento.
        


        