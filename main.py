import pytube
import os
import tkinter as tk   
from tkinter import messagebox
from tkinter import ttk

type_video = [
    "mp4",
    "mp3"
]

FONT_PANEL = ("Helvetica, 20 bold")

url_path_prev = './music'

# Panel
PANEL_LOGO_YT = "./assets/LogoYoutu.ico"
BG_COLOR = "#343637"
window = tk.Tk()
window.title("Convertidor de YouTube")
window.geometry("800x300")
window.iconbitmap(PANEL_LOGO_YT)
window.configure(background='#343637')
lbl_convert = tk.Label(window,text="CONVERTIDOR DE YOUTUBE!",font=FONT_PANEL,padx=20,pady=20,foreground='white',background=BG_COLOR)
lbl_convert.pack(anchor=tk.CENTER,pady=15)

fr_convert = tk.Frame(window,background=BG_COLOR)
ent_url = tk.Entry(fr_convert,font=("Helvetica, 10"),borderwidth=12,relief=tk.FLAT,width=55)
ent_url.pack(side=tk.LEFT,padx=0,pady=10)

def download():
    url = str(ent_url.get())

    # yt = pytube.YouTube(url,use_oauth=True)
    # title = yt.title
    # st = yt.streams.get_highest_resolution()
    # st.download(url_path_prev)
    # os.rename(os.path.join(url_path_prev,title+'.mp4'), os.path.join(path_video,title+'.mp4'))

    messagebox.showinfo("Éxito","El video se descargo exitosamente")

# Display menu extensions
variable = tk.StringVar()
variable.set(type_video[0])
opt_type = tk.OptionMenu(fr_convert,variable,*type_video)
opt_type.pack(side=tk.LEFT)
opt_type.configure(background='#123546',foreground='white',font=("Helvetica, 15 "),pady=5)
# Button download
btn_download = tk.Button(fr_convert,width=20,height=2,text="Convertir",font=("Helvetica, 10 bold"),background="red",foreground="white",command=download,relief=tk.FLAT)
btn_download.pack(side=tk.LEFT)
fr_convert.pack()

lbl_url = tk.Label(window, text='Asegúrese de ingresar una URL de YouTube válida',font=("Helvetica, 12"),background=BG_COLOR,foreground='white')
lbl_url.pack(anchor=tk.CENTER)
window.mainloop()


