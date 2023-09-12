import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def redimensionar_imagem(imagem, largura, altura):
    imagem_redimensionada = imagem.resize((largura, altura), Image.ANTIALIAS if 'ANTIALIAS' in dir(Image) else Image.LANCZOS)
    return ImageTk.PhotoImage(imagem_redimensionada)

def carregar_imagem(label_cliente):
    
    # Abre a janela de seleção de arquivos
    filename = filedialog.askopenfilename(title="Selecione uma foto", filetypes=[("Imagens", "*.jpg *.png *.bmp")])

    # Se o usuário selecionou um arquivo, carrega a foto e atualiza o Label
    if filename:
        imagem_original = Image.open(filename)        
        imagem_redimensionada = redimensionar_imagem(imagem_original, 150, 150)
        

        # Atualize o Label da imagem com a nova imagem
        label_cliente.configure(image=imagem_redimensionada)
        label_cliente.image = imagem_redimensionada