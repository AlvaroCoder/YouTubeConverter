import tkinter as tk
from services.validate_entry import * 
from tkinter import messagebox

PANEL_LOGO_YT = "./assets/LogoYoutu.ico"
FONT_TITLE = ("Helvetica, 20 bold")
FONT_TEXT = ("Helvetica, 10")
BG_COLOR ="#343637"

class Frame_Buttons(tk.Frame):
    def __init__(self,w=tk.Tk):
        super().__init__()
        self.master = w
        self.entry_url = tk.Entry(self,font=FONT_TEXT,borderwidth=12,relief=tk.FLAT,width=55)
        self.type_video = ["mp4","mp3"]
        self.configure(background=BG_COLOR)
        self.__create_widgets()

    def convert(self):
        ob = validate_entry_url(self.url)    
        if not ob:
            url = self.entry_url.get()
        else:
            messagebox.showwarning('Error en url', ob['message'])
    def __create_widgets(self):
        variable = tk.StringVar()
        variable.set(self.type_video[0])
        self.entry_url.pack(side=tk.LEFT)
        tk.OptionMenu(self,variable,*self.type_video).pack(side=tk.LEFT)
        tk.Button(self,width=20,height=2,text="Convertir",font=("Helvetica, 10 bold"),background="red",foreground="white",command=self.convert,relief=tk.FLAT).pack(side=tk.LEFT)

    @property
    def url(self):
        return self.entry_url.get()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x300")
        self.iconbitmap(PANEL_LOGO_YT)
        self.configure(background='#343637')
        self.__create_widgets()
        
    def destroy(self):
        return super().quit()

    def __create_widgets(self):
        fr = Frame_Buttons(self)
        tk.Label(self,text="CONVERTIDOR DE YOUTUBE!",font=FONT_TITLE,padx=20,pady=20,foreground='white',background=BG_COLOR).pack(anchor=tk.CENTER,pady=15)
        fr.pack()
        tk.Label(self,text='Asegúrese de ingresar una URL de YouTube válida',font=("Helvetica, 12"),background=BG_COLOR,foreground='white').pack(anchor=tk.CENTER)
