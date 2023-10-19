import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import ImageTk, Image


class ListaCompras(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(master= parent)
        self.pack(expand= True, fill='both')

        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number*item_height

        self.canvas = tk.Canvas(self, scrollregion= (0,0,self.winfo_width(), self.list_height))
        self.canvas.pack(expand= True, fill='both')

        self.frame = ttk.Frame(self)
        
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta/60), "units" ))
        self.bind('<Configure>', self.update_size)
        
    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta/60), "units" ))
            self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
        else:
            height = self.winfo_height()
            self.canvas.unbind_all('<MouseWheel>')
            self.scrollbar.place_forget()
        self.canvas.create_window(
        (0,0),
        window=self.frame,
        anchor='nw',
        width= self.winfo_width(),
        height= self.list_height
        )
        
    def creat_compra(self, index, item):
        frame = ttk.Frame(self.frame)
        image = Image.open('imagens/editar.png')
        tk_image = ctk.CTkImage(image)
                
        ttk.Label(
            frame,
            text=f'{index}',
            font=('Arial', 14)).place(relx=0.025, rely=0.1)
        
        ttk.Label(
            frame,
            text=f'{item[0]}',
            font=('Arial', 14)).place(relx=.08, rely=0.1)
        
        ttk.Label(
            frame,
            text=f'{item[1]}',
            font=('Arial', 14)).place(relx=.43, rely=0.1)
        
        ttk.Label(
            frame,
            text=f'{item[2]}',
            font=('Arial', 14)).place(relx=.59, rely=0.1)
        
        ttk.Label(
            frame,
            text='R$ 48,50',
            font=('Arial', 14, 'bold')).place(relx=.745, rely=0.05)
        
        ttk.Label(
            frame,
            text=f'{item[3]}',
            font='bold',
            foreground='orange').place(relx=.75, rely=0.3)
        
        ctk.CTkButton(frame,
                    text=f'{item[4].upper()}',
                    image=tk_image,
                    compound='right',
                    font=('Arial', 18, 'bold'),
                    text_color="white",
                    hover= True,
                    hover_color= "#454545",
                    height=40,
                    width= 120,
                    border_width=2,
                    corner_radius=10,
                    border_color= "#161616",                     
                    fg_color= "#363636").place(relx=.86, rely=0, relwidth=.1335, relheight=0.5)
        ttk.Separator(frame, orient='horizontal').pack(expand=True, fill='x')

        return frame
    
       
