from random import randint
from barcode import EAN13
from barcode.writer import ImageWriter

def gerar_numero_aleatorio():
    # Gera um número aleatório de 12 dígitos
    numero_aleatorio = randint(10**11, (10**12) - 1)
    
    # Formata o número para uma string de 12 dígitos
    numero_aleatorio_formatado = "{:012d}".format(numero_aleatorio)
    
    return numero_aleatorio_formatado

def gerar_barcode(entry):
    numero = gerar_numero_aleatorio()
    entry.set(numero)
    codigo_barra = EAN13(numero, writer=ImageWriter())
    codigo_barra.save(f'estoque/codigos_barras/{numero}')