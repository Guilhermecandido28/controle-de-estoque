import tkinter as tk
from tkinter import ttk

class SuaClasse:
    def __init__(self, principal):
        self.principal = principal
        self.inserir_dados()

    def inserir_dados(self):
        self.treeview = ttk.Treeview(self.principal)
        self.treeview['columns'] = ('ID', 'NOME', 'ACAO')

        self.treeview.heading('#1', text='ID')
        self.treeview.heading('#2', text='NOME')
        self.treeview.heading('#3', text='AÇÃO')

        self.treeview.pack()

        # Adicionando alguns itens de exemplo
        self.treeview.insert(parent='', index='end', iid=0, text='Item 1', values=('1', 'Guilherme', ''))
        self.treeview.insert(parent='', index='end', iid=1, text='Item 2', values=('2', 'João', ''))

        for item_id in range(2):  # Adapte conforme o número de itens
            self.treeview.insert('', 'end', text=f'Item {item_id+1}', values=(item_id+1, f'Nome {item_id+1}', 'Clique'), tags=('button',))
            self.treeview.tag_configure('button', foreground='blue')
        
        self.treeview.bind('<ButtonRelease-1>', self.on_item_click)

    def on_item_click(self, event):
        item = self.treeview.selection()[0]
        col = self.treeview.identify_column(event.x)
        if col == '#3':  # Clique na coluna de ação
            item_values = self.treeview.item(item, 'values')
            print(f'Botão clicado para o item com ID {item_values[0]}')

# Exemplo de uso
root = tk.Tk()
root.title("Exemplo de Treeview com Botões Simulados")
app = SuaClasse(root)
root.mainloop()
