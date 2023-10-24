

# # import tkinter as tk

# # def manter_foco(event):
# #     entry.focus_set()

# # root = tk.Tk()
# # root.title("Manter Foco na Entry")

# # # Função chamada quando o foco é alterado
# # root.bind("<FocusOut>", manter_foco)

# # entry = tk.Entry(root)
# # entry.pack(pady=20)

# # root.mainloop()

# import tkinter as tk

# root = tk.Tk()
# root.geometry("200x200")

# # Crie uma variável do tipo StringVar e atribua o texto inicial que você deseja
# texto_inicial = tk.StringVar(value="Texto inicial na Entry")

# # Crie a Entry e associe a variável de texto a ela
# entry = tk.Entry(root, textvariable=texto_inicial)
# entry.config(state='readonly')
# print(entry.get())
# entry.pack(pady=20)

# root.mainloop()

        

# def voltar(self):        
#         self.f_add_compra.place_forget()  
#         self.nova_compra()
#         self.lista_compras()
#         self.filtros_busca()
#         self.onde_estou()

import tkinter as tk
from tkinter import ttk

def exibir_tooltip(widget, texto):
    tooltip = ttk.Label(root, text=texto, background='lightyellow', padding=(5, 2))
    tooltip.place(x=root.winfo_pointerx() + 10, y=root.winfo_pointery() + 10)
    root.after(3000, tooltip.destroy)  # Exibe o tooltip por 3 segundos

root = tk.Tk()
root.title("Tooltip em Label")

label = ttk.Label(root, text="Passe o mouse aqui")
label.pack(pady=20)

label.bind("<Enter>", lambda event: exibir_tooltip(label, "Isso é uma dica de ferramenta."))

root.mainloop()