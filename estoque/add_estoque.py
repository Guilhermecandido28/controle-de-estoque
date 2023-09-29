from tkinter import *
from styles.cores import *
import tkinter as tk
from tkinter import filedialog
from formations import *
from tkinter import ttk
from PIL import Image, ImageTk
from limpar import limpar
from clientes.banco_dados_cliente import *
import sqlite3
from clientes.foto_instagram import *
from tkinter import messagebox
from datetime import datetime


class AddEstoque():
    def __init__(self, frame):
        self.principal = frame
        self.add_estoque()

    def add_estoque(self):
        self.titulo_est = Label(self.principal, text='Ficha de Cadastro de Produto', bg='white', font=('arial 36 bold'))
        self.linha_est = Frame(self.principal, bg=cor5)
        self.linha_est.place(relx=0.01, rely=0.11, relwidth=0.98, relheight=0.004)
        self.titulo_est.place(relx=0.01, rely=0.0)
        #imagem
        self.my_canvas = Canvas(self.principal, bd=0, highlightthickness=0, relief='ridge')
        self.my_canvas.place(relx=0.01, rely=0.15, relheight=.39, relwidth=.14)
        # self.my_canvas.bind('<Configure>', self.resizer)
        #upload
        botao_upload = tk.Button(self.principal, text="Upload", font=('arial 12 bold'), background='green', foreground='white', cursor='hand2')
        botao_upload.place(relx=0.01, rely=0.50, relwidth=.14, relheight=0.04)
         # Entrys
            #DESCRIÇÃO
        self.title_descricao = Label(self.principal, text='DESCRIÇÃO:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_descricao.place(relx=0.158, rely=0.15)
        self.e_descricao = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_descricao.place(relx=0.160, rely=0.20, relwidth=0.45, relheight=0.04)
        placeholder_nome(self.e_descricao)
            #CATEGORIA
        self.title_categoria = Label(self.principal, text='CATEGORIA:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_categoria.place(relx=0.158, rely=0.25)
        self.e_categoria = ttk.Combobox(self.principal, background=cor4, font=('arial 12'), state='readonly')
        self.e_categoria['values'] = list(self.e_categoria['values']) + self.ler_categoria_do_arquivo()
        self.e_categoria.place(relx=0.160, rely=0.30, relwidth=0.19, relheight=0.04)
        self.img_adicionar = PhotoImage(file='imagens/adicionar.png')
        self.btn_add_categoria = Button(self.principal, image=self.img_adicionar, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.categoria, cursor='hand2')
        self.btn_add_categoria.place(relx=0.351, rely=0.30, relheight=0.04, relwidth=0.02)
        placeholder_nome(self.e_categoria)
        
            #MARCA
        self.title_marca = Label(self.principal, text='MARCA:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_marca.place(relx=0.40, rely=0.25)
        self.e_marca = ttk.Combobox(self.principal, background=cor4, font=('arial 12'), state='readonly')
        self.e_marca['values'] = list(self.e_marca['values']) + self.ler_marcas_do_arquivo()
        self.e_marca.place(relx=0.400, rely=0.30, relwidth=0.19, relheight=0.04)
        self.btn_add_marca = Button(self.principal, image=self.img_adicionar, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.marca)
        self.btn_add_marca.place(relx=0.591, rely=0.30, relheight=0.04, relwidth=0.02)
        placeholder_nome(self.e_marca)
            #ESTOQUE MÍNIMO
        self.title_estoque_min = Label(self.principal, text='ESTOQUE MÍNIMO:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_estoque_min.place(relx=0.158, rely=0.35)
        self.e_estoque_min = Spinbox(self.principal, from_=1, to=100, background=cor4, font=('arial 12'), bd=0, highlightthickness=0, buttonbackground=cor4)
        self.e_estoque_min.place(relx=0.160, rely=0.40, relwidth=0.21, relheight=0.04)     

        placeholder_estoque(self.e_estoque_min)
            #ESTOQUE MAXIMO
        self.title_estoque_max = Label(self.principal, text='ESTOQUE MÁXIMO:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_estoque_max.place(relx=0.40, rely=0.35)
        self.e_estoque_max = Spinbox(self.principal, from_=1, to=100, background=cor4, font=('arial 12'), bd=0, highlightthickness=0, buttonbackground=cor4)
        self.e_estoque_max.place(relx=0.400, rely=0.40, relwidth=0.21, relheight=0.04)        
        placeholder_estoque(self.e_estoque_max)
            #Observação
        self.title_obs = Label(self.principal, text='OBSERVAÇÃO:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_obs.place(relx=0.158, rely=0.45)
        self.e_obs = Entry(self.principal, bg=cor4, font=('arial 12'), bd=0)
        self.e_obs.place(relx=0.160, rely=0.50, relwidth=0.21, relheight=0.04)
            # Tamanho
        self.title_tamanho = Label(self.principal, text='TAMANHO:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_tamanho.place(relx=0.400, rely=0.45)
        self.e_tamanho = ttk.Combobox(self.principal, background=cor4, font=('arial 12'), state='readonly')
        self.e_tamanho['values'] = list(self.e_tamanho['values']) + self.ler_tamanhos_do_arquivo()
        
        self.e_tamanho.place(relx=0.400, rely=0.50, relwidth=0.08, relheight=0.04)
        self.btn_add_tamanho = Button(self.principal, image=self.img_adicionar, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.tamanho, cursor='hand2')
        self.btn_add_tamanho.place(relx=0.482, rely=0.50, relheight=0.04, relwidth=0.02)
            # COR
        self.title_cor = Label(self.principal, text='COR:', font=('arial 12'), foreground= cor4, bg='white')
        self.title_cor.place(relx=0.530, rely=0.45)
        self.e_cor = ttk.Combobox(self.principal, background=cor4, font=('arial 12'), state='readonly')
        self.e_cor.place(relx=0.530, rely=0.50, relwidth=0.06, relheight=0.04)
        self.e_cor['values'] = list(self.e_cor['values']) + self.ler_cores_do_arquivo()
        self.btn_add_cor = Button(self.principal, image=self.img_adicionar, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.cor, cursor='hand2')
        self.btn_add_cor.place(relx=0.592, rely=0.50, relheight=0.04, relwidth=0.02)

        #botão voltar
        self.img_voltar = PhotoImage(file='imagens/voltar.png')
        self.btn_voltar = Button(self.principal, image=self.img_voltar, bg='white', cursor='hand2', command=self.voltar, relief='flat')
        self.btn_voltar.place(relx=0.962, rely=0)

    def ler_cores_do_arquivo(self):
        self.cores = []
        try:
            with open('estoque/cores.txt', 'r') as file:
                for line in file:
                    cor = line.strip().upper()
                    if cor:  # Verifica se a linha não está vazia
                        self.cores.append(cor)
        except FileNotFoundError:
            print('arquivo cores.txt não encontrado.')

        return self.cores
    
    def ler_tamanhos_do_arquivo(self):
        tamanhos = []
        try:
            with open('estoque/tamanho.txt', 'r') as file:
                for line in file:
                    tamanho = line.strip().upper()
                    if tamanho:  # Verifica se a linha não está vazia
                        tamanhos.append(tamanho)
        except FileNotFoundError:
            print('arquivo tamanho.txt não encontrado.')

        return tamanhos
    
    def ler_marcas_do_arquivo(self):
        marcas = []
        try:
            with open('estoque/marcas.txt', 'r') as file:
                for line in file:
                    marca = line.strip().upper()  # Cada marca lida do arquivo
                    if marca:  # Verifica se a linha não está vazia
                        marcas.append(marca)
        except FileNotFoundError:
            print('Arquivo marcas.txt não encontrado.')

        return marcas
    
    def ler_categoria_do_arquivo(self):
        categorias = []
        try:
            with open('estoque/categoria.txt', 'r') as file:
                for line in file:
                    categoria = line.strip().upper()  # Cada marca lida do arquivo
                    if categoria:  # Verifica se a linha não está vazia
                        categorias.append(categoria)
        except FileNotFoundError:
            print('Arquivo categoria.txt não encontrado.')

        return categorias
    
    def marca(self):
        self.img_excluir_marca = PhotoImage(file='imagens/excluir.png')
        self.img_ok_marca = PhotoImage(file='imagens/ok.png')
        self.e_marca.configure(state='normal')
        self.btn_add_marca.place_forget()
        self.btn_exc_marca = Button(self.principal, image=self.img_excluir_marca, background='dark green', relief='flat', highlightthickness=0, bd=0, command=lambda: self.e_marca.set(""), cursor='hand2')
        self.btn_exc_marca.place(relx=0.591, rely=0.30, relheight=0.04, relwidth=0.02)
        self.btn_ok_marca = Button(self.principal, image=self.img_ok_marca, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.salvar_marca, cursor='hand2')
        self.btn_ok_marca.place(relx=0.612, rely=0.30, relheight=0.04, relwidth=0.02)

    def categoria(self):
        self.img_excluir = PhotoImage(file='imagens/excluir.png')
        self.img_ok = PhotoImage(file='imagens/ok.png')
        self.e_categoria.configure(state='normal')
        self.btn_add_categoria.place_forget()
        self.btn_exc_categoria = Button(self.principal, image=self.img_excluir, background='dark green', relief='flat', highlightthickness=0, bd=0, command=lambda: self.e_categoria.set(""), cursor='hand2')
        self.btn_exc_categoria.place(relx=0.351, rely=0.30, relheight=0.04, relwidth=0.02)
        self.btn_ok_categoria = Button(self.principal, image=self.img_ok, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.salvar_categoria, cursor='hand2')
        self.btn_ok_categoria.place(relx=0.372, rely=0.30, relheight=0.04, relwidth=0.02)

    def cor(self):
        self.img_excluir = PhotoImage(file='imagens/excluir.png')
        self.img_ok = PhotoImage(file='imagens/ok.png')
        self.e_cor.configure(state='normal')
        self.btn_add_cor.place_forget()
        self.btn_exc_cor = Button(self.principal, image=self.img_excluir, background='dark green', relief='flat', highlightthickness=0, bd=0, command=lambda: self.e_cor.set(""), cursor='hand2')
        self.btn_exc_cor.place(relx=0.591, rely=0.50, relheight=0.04, relwidth=0.02)
        self.btn_ok_cor = Button(self.principal, image=self.img_ok, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.salvar_cor, cursor='hand2')
        self.btn_ok_cor.place(relx=0.612, rely=0.50, relheight=0.04, relwidth=0.02)

    def tamanho(self):
        self.img_excluir = PhotoImage(file='imagens/excluir.png')
        self.img_ok = PhotoImage(file='imagens/ok.png')
        self.e_tamanho.configure(state='normal')
        self.btn_add_tamanho.place_forget()
        self.btn_exc_tamanho = Button(self.principal, image=self.img_excluir, background='dark green', relief='flat', highlightthickness=0, bd=0, command=lambda: self.e_tamanho.set(""), cursor='hand2')
        self.btn_exc_tamanho.place(relx=0.482, rely=0.50, relheight=0.04, relwidth=0.02)
        self.btn_ok_tamanho = Button(self.principal, image=self.img_ok, background='dark green', relief='flat', highlightthickness=0, bd=0, command=self.salvar_tamanho, cursor='hand2')
        self.btn_ok_tamanho.place(relx=0.503, rely=0.50, relheight=0.04, relwidth=0.02)

    def salvar_marca(self):
        nova_marca = self.e_marca.get().upper()  # Obtém a nova marca digitada e a converte para maiúsculas

        # Lê as marcas existentes
        marcas_existentes = []
        try:
            with open('estoque/marcas.txt', 'r') as file:
                marcas_existentes = [linha.strip() for linha in file]
        except FileNotFoundError:
            print('Arquivo marcas.txt não encontrado.')

        # Verifica se a nova marca já existe (insensível a maiúsculas/minúsculas)
        if nova_marca.upper() in (marca.upper() for marca in marcas_existentes):
            print(f'A marca {nova_marca} já existe.')
            return

        # Adiciona a nova marca à lista de marcas existentes
        marcas_existentes.append(nova_marca)

        # Ordena as marcas em ordem alfabética (insensível a maiúsculas/minúsculas)
        marcas_existentes.sort(key=lambda x: x.lower())
        self.e_marca['values'] = list(self.e_marca['values']) + [nova_marca]
        self.e_marca.set(nova_marca)

        # Salva todas as marcas, uma por linha
        try:
            with open('estoque/marcas.txt', 'w') as file:
                for marca in marcas_existentes:
                    file.write(marca + '\n')
        except FileNotFoundError:
            print('Arquivo marcas.txt não encontrado.')

        self.btn_exc_marca.place_forget()
        self.btn_ok_marca.place_forget()
        self.btn_add_marca.place(relx=0.591, rely=0.30, relheight=0.04, relwidth=0.02)

    def salvar_categoria(self):
        nova_categoria = self.e_categoria.get().upper()  # Obtém a nova categoria digitada e a converte para maiúsculas

        # Lê as categorias existentes
        categoria_existentes = []
        try:
            with open('estoque/categoria.txt', 'r') as file:
                categoria_existentes = [linha.strip() for linha in file]
        except FileNotFoundError:
            print('Arquivo categoria.txt não encontrado.')

        # Verifica se a nova categoria já existe (insensível a maiúsculas/minúsculas)
        if nova_categoria.upper() in (categoria.upper() for categoria in categoria_existentes):
            messagebox.showinfo('Erro',f'A categoria {nova_categoria} já existe.')
            return

        # Adiciona a nova categoria à lista de categorias existentes
        categoria_existentes.append(nova_categoria)
        self.e_categoria['values'] = list(self.e_categoria['values']) + [nova_categoria]
        self.e_categoria.set(nova_categoria)

        # Ordena as categorias em ordem alfabética (insensível a maiúsculas/minúsculas)
        categoria_existentes.sort(key=lambda x: x.lower())

        # Salva todas as categorias, uma por linha
        try:
            with open('estoque/categoria.txt', 'w') as file:
                for categoria in categoria_existentes:
                    file.write(categoria + '\n')
        except FileNotFoundError:
            print('Arquivo categoria.txt não encontrado.')

        self.btn_exc_categoria.place_forget()
        self.btn_ok_categoria.place_forget()
        self.btn_add_categoria.place(relx=0.351, rely=0.30, relheight=0.04, relwidth=0.02)

    def salvar_cor(self):
        nova_cor = self.e_cor.get().upper()  # Obtém a nova cor digitada e a converte para maiúsculas

        # Lê as cores existentes
        cor_existentes = []
        try:
            with open('estoque/cores.txt', 'r') as file:
                cor_existentes = [linha.strip() for linha in file]
        except FileNotFoundError:
            print('Arquivo cores.txt não encontrado.')

        # Verifica se a nova cor já existe (insensível a maiúsculas/minúsculas)
        if nova_cor.upper() in (cor.upper() for cor in cor_existentes):
            messagebox.showinfo('Erro', f'A cor {nova_cor} já existe.')
            return

        # Adiciona a nova cor à lista de cores existentes
        cor_existentes.append(nova_cor)


        # Ordena as cores em ordem alfabética (insensível a maiúsculas/minúsculas)
        cor_existentes.sort(key=lambda x: x.lower())
        self.e_cor['values'] = list(self.e_cor['values']) + [nova_cor]
        self.e_cor.set(nova_cor)

        # Salva todas as cores, uma por linha
        try:
            with open('estoque/cores.txt', 'w') as file:
                for cor in cor_existentes:
                    file.write(cor + '\n')
        except FileNotFoundError:
            print('Arquivo cores.txt não encontrado.')

        self.btn_exc_cor.place_forget()
        self.btn_ok_cor.place_forget()
        self.btn_add_cor.place(relx=0.351, rely=0.30, relheight=0.04, relwidth=0.02)

    def salvar_tamanho(self):
        nova_tamanho = self.e_tamanho.get().upper()  # Obtém o novo tamanho digitado e o converte para maiúsculas

        # Lê os tamanhos existentes
        tamanho_existentes = []
        try:
            with open('estoque/tamanho.txt', 'r') as file:
                tamanho_existentes = [linha.strip() for linha in file]
        except FileNotFoundError:
            print('Arquivo tamanho.txt não encontrado.')

        # Verifica se o novo tamanho já existe
        if nova_tamanho in tamanho_existentes:
            messagebox.showinfo('Erro', f'O tamanho {nova_tamanho} já existe.')
            return

        # Adiciona o novo tamanho à lista de tamanhos existentes
        tamanho_existentes.append(nova_tamanho)

        # Ordena os tamanhos em ordem do menor para o maior
        tamanho_existentes.sort(key=lambda x: x.lower())
        tamanho_existentes.sort(key=lambda x: int(x) if x.isdigit() else float('inf'))
        self.e_tamanho['values'] = list(self.e_tamanho['values']) + [nova_tamanho]
        self.e_tamanho.set(nova_tamanho)

        # Salva todos os tamanhos, um por linha
        try:
            with open('estoque/tamanho.txt', 'w') as file:
                for tamanho in tamanho_existentes:
                    file.write(tamanho + '\n')
        except FileNotFoundError:
            print('Arquivo tamanho.txt não encontrado.')

        self.btn_exc_tamanho.place_forget()
        self.btn_ok_tamanho.place_forget()
        self.btn_add_tamanho.place(relx=0.482, rely=0.50, relheight=0.04, relwidth=0.02)

    # def excluir_linha_e_reorganizar_arquivo(self,caminho_arquivo, linha_para_excluir):
    #     # Ler o conteúdo do arquivo e remover a linha desejada
    #     linhas = []
    #     with open(caminho_arquivo, 'r') as file:
    #         linhas = file.readlines()
        
    #     # Remover a linha desejada (se existir)
    #     linhas = [linha for linha in linhas if linha.strip() != linha_para_excluir]

    #     # Escrever o conteúdo atualizado de volta ao arquivo
    #     with open(caminho_arquivo, 'w') as file:
    #         file.writelines(linhas)

    #     messagebox.showinfo('Sucesso!', 'Item excluído com sucesso!')
    
    def voltar(self):
        self.principal.place_forget()