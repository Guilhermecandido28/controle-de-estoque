import tkinter as tk

def limpar(campos):
    for campo in campos:
        campo.delete(0,tk.END)

