

# import tkinter as tk

# def manter_foco(event):
#     entry.focus_set()

# root = tk.Tk()
# root.title("Manter Foco na Entry")

# # Função chamada quando o foco é alterado
# root.bind("<FocusOut>", manter_foco)

# entry = tk.Entry(root)
# entry.pack(pady=20)

# root.mainloop()

import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

# Crie uma variável do tipo StringVar e atribua o texto inicial que você deseja
texto_inicial = tk.StringVar(value="Texto inicial na Entry")

# Crie a Entry e associe a variável de texto a ela
entry = tk.Entry(root, textvariable=texto_inicial)
entry.config(state='readonly')
print(entry.get())
entry.pack(pady=20)

root.mainloop()