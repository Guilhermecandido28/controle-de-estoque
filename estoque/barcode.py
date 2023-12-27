from random import randint
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import subprocess
import os
#import pyautogui
import win32print
import win32api


def gerar_numero_aleatorio():
    # Gera um número aleatório de 12 dígitos
    numero_aleatorio = randint(10**11, (10**12) - 1)
    
    # Formata o número para uma string de 12 dígitos
    numero_aleatorio_formatado = "{:012d}".format(numero_aleatorio)
    
    return numero_aleatorio_formatado

def gerar_barcode(entry, texto):
    numero = gerar_numero_aleatorio()
    entry.set(numero)
    codigo_barra = EAN13(numero, writer=ImageWriter())
    codigo_barra.save(f'estoque/codigos_barras/{numero}')
    imagem = Image.open(f'estoque/codigos_barras/{numero}.png')
    # draw = ImageDraw.Draw(imagem)
    # font = ImageFont.truetype('arial.ttf', size=40)
    # draw.text((200, 240), f"{texto}", font=font, fill='black')
    # imagem.save(f'estoque/codigos_barras/{numero}.png')  
    # imagem_path = os.path.abspath(f'estoque/codigos_barras/{numero}.png')
    imprimir_barcode(numero=numero)

def imprimir_barcode(numero):
    lista_impressoras = win32print.EnumPrinters(2)
    impressora = lista_impressoras[2]
    win32print.SetDefaultPrinter(impressora[2])
    caminho_imagem = os.path.abspath(f'estoque/codigos_barras/{numero}.png')
    
    # Verifica se o arquivo existe antes de tentar imprimir
    if os.path.exists(caminho_imagem):
        win32api.ShellExecute(0, "print", caminho_imagem, None, ".", 0)
    else:
        print(f"O arquivo {caminho_imagem} não foi encontrado.")



    


    

