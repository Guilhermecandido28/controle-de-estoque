from tkinter import *
from styles.cores import *
import tkinter as tk
from formations import *
from PIL import Image
from limpar import limpar
from PIL import Image, ImageTk



class Home():
    def __init__(self, frame):
        self.home = tk.Canvas(frame, bd=0, highlightthickness=0)
    
    def frame_home(self):
        self.layout_home = Image.open('imagens/layout_home.png')       
        self.home.place(relx=0.2, rely=.27, relheight=.6, relwidth=.6)        
        self.layout_home_tk = PhotoImage(self.layout_home)
        self.home.bind('<Configure>', self.resize_layout)


    def resize_layout(self, event):
        self.nova_layout = self.layout_home.resize((event.width, event.height))
        self.nova_layout_tk = ImageTk.PhotoImage(self.nova_layout)
        self.home.create_image(0,0, anchor = NW, image = self.nova_layout_tk)
        self.home.image = self.nova_layout_tk