from tkinter import *
from tkinter import filedialog as fd
from services.render_video import Render
import asyncio

PANEL_LOGO_YT = "./assets/LogoYoutu.ico"
FONT_TITLE = ("Helvetica, 20 bold")
FONT_TEXT = ("Helvetica, 10")
BG_COLOR ="#343637"

class AppVideo(Tk):
    def __init__(self, url):
        super().__init__()
        self.geometry("600x300")
        self.iconbitmap(PANEL_LOGO_YT)
        self.configure(background='#343637')
        self.url = url
        self.__create_widgets()
        
    def __create_widgets(self):
        render = Render(self.url)
        img = render.image
        fr1 = Frame(self, background=BG_COLOR,width=200,height=200)
        fr2 = Frame(self, background=BG_COLOR, width=300).pack(side=RIGHT)
        lbl = Label(fr1, image=img)
        lbl.pack(anchor=CENTER)
        fr1.pack(side=LEFT)
        return
