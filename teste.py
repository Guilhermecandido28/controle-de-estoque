from tkinter import ttk
import tkinter as tk

root = tk.Tk()

# Criando Treeview
tree = ttk.Treeview(root)
tree["columns"] = ("ID", "Nome")

# Definindo os estilos para cada coluna e dado
tree.tag_configure("ID1", foreground="green")
tree.tag_configure("ID2", foreground="red")
tree.tag_configure("ID3", foreground="blue")
tree.tag_configure("Nome", foreground="black")

# Adicionando colunas na Treeview
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")

# Adicionando dados na Treeview
tree.insert("", "end", text="Item 1", values=("1", "Alice"), tags=("ID1", "Nome"))
tree.insert("", "end", text="Item 2", values=("2", "Bob"), tags=("ID2", "Nome"))
tree.insert("", "end", text="Item 3", values=("3", "Charlie"), tags=("ID3", "Nome"))

# Exibindo a Treeview
tree.pack()

root.mainloop()