from random import randint
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import subprocess
import os
import pyautogui
import win32print
import win32api
from time import sleep
from random import randint

def gerar_numero_aleatorio():
    # Gera um número aleatório de 12 dígitos
    numero_aleatorio = randint(10**11, (10**12) - 1)
    numero_aleatorio_str = str(numero_aleatorio)  # Convertendo para string
    soma_pares = sum(int(numero_aleatorio_str[i]) for i in range(0, 12, 2))
    soma_impares = sum(int(numero_aleatorio_str[i]) for i in range(1, 12, 2))
    soma_impares *= 3
    total_soma = soma_pares + soma_impares
    proximo_multiplo_10 = (total_soma // 10 + 1) * 10
    digito_verificador = proximo_multiplo_10 - total_soma

    if digito_verificador == 10:
        digito_verificador = 0
    
    # Formata o número para uma string de 13 dígitos
    numero_aleatorio_formatado = f"{numero_aleatorio:012d}{digito_verificador}"
    
    return numero_aleatorio_formatado


def gerar_barcode(entry, texto):
    numero = gerar_numero_aleatorio()    
    entry.set(numero)
    

    codigo_barra = EAN13(numero, writer=ImageWriter())    

    codigo_barra.save(f'estoque/codigos_barras/{numero}')

    # Abre a imagem e redimensiona conforme necessário
    imagem = Image.open(f'estoque/codigos_barras/{numero}.png')
    nova_dimensao = (550, 450)  # Ajuste conforme necessário
    imagem_redimensionada = imagem.resize(nova_dimensao)

    draw = ImageDraw.Draw(imagem_redimensionada)

    # Ajuste a posição e o tamanho do texto conforme necessário
    text_position = (70, 390)
    font_size = 45
    font = ImageFont.truetype('arial.ttf', size=font_size)
    draw.text(text_position, f"{texto}", font=font, fill='black')

    imagem_redimensionada.save(f'estoque/codigos_barras/{numero}.png')
    imagem_path = os.path.abspath(f'estoque/codigos_barras/{numero}.png')
    imprimir_barcode(numero=numero)
    sleep(1)
    # pyautogui.press('enter')

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



    


    

