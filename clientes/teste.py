import tkinter as tk

class Clientes(tk.Frame):

    def __init__(self, master):
        super().__init__(master)

        self.clientes = []

        self.frame = tk.Frame(self)
        self.frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.frame)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.create_window((0, 0), window=self.clientes, anchor="nw")

        self.clientes.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_cliente(self, cliente):
        self.clientes.append(cliente)
        self.canvas.create_window((0, 0), window=cliente, anchor="nw")

root = tk.Tk()
clientes = Clientes(root)
clientes.pack(fill="both", expand=True)

for i in range(100):
    clientes.add_cliente(tk.Label(clientes, text=f"Cliente {i}"))

root.mainloop()