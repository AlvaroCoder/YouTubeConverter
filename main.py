import pytube
import os
import tkinter as tk   
from tkinter import messagebox
type_video = [
    "mp4",
    "mp3"
]
url_path_prev = './music'
yt_logo_dir = "./assets/LogoYoutu.ico"
window = tk.Tk()
window.title("Convertidor de YouTube")
window.geometry("600x400")
window.iconbitmap(yt_logo_dir)

lbl_convert = tk.Label(window,text="CONVERTIDOR DE YOUTUBE!",font=("Helvetica, 20"),padx=20,pady=20)
lbl_convert.pack(padx=10,pady=10)

fr_path = tk.Frame(window)
lbl_path = tk.Label(fr_path, text="Directorio",font=("Helvetica, 12"),pady=10,padx=20).pack(side=tk.LEFT)
ent_path = tk.Entry(fr_path,font=("Helvetica, 10"),borderwidth=5,relief=tk.FLAT,width=60)
ent_path.pack(side=tk.BOTTOM,pady=10,padx=10)
fr_path.pack()

fr_convert = tk.Frame(window)
lbl_url = tk.Label(fr_convert,text="Url", font=("Helvetica, 12"),padx=20).pack(side=tk.LEFT)

ent_url = tk.Entry(fr_convert,font=("Helvetica, 10"),borderwidth=5,relief=tk.FLAT,width=55)
ent_url.pack(side=tk.LEFT,padx=0,pady=10)



def download():
    url = str(ent_url.get())
    path_video = str(ent_path.get())
    if url == "":
        messagebox.showwarning("Error","Ingrese la URL")
        return
    if path_video == "":
        messagebox.showwarning("Error","Ingrese el directorio")
        return
    if not os.path.isdir(path_video):
        messagebox.showwarning("Error","No existe ese directorio")
        return
    ent_path.delete(0,tk.END)
    ent_path.insert(0,"")

    ent_url.delete(0,tk.END)
    ent_url.insert(0,"")

    yt = pytube.YouTube(url)
    title = yt.streams[0].title
    st = yt.streams.get_highest_resolution()
    st.download(url_path_prev)
    os.rename(os.path.join(url_path_prev,title+'.mp4'), os.path.join(path_video,title+'.mp4'))

    messagebox.showinfo("Éxito","El video se descargo exitosamente")


click = tk.StringVar()
click.set(type_video[0])
opt_type = tk.OptionMenu(fr_convert,click,*type_video)
opt_type.pack(side=tk.LEFT)

fr_convert.pack()

btn_down = tk.Button(window,width=40,height=2,text="Descargar",font=("Helvetica, 10"),background="red",foreground="white",command=download,relief=tk.FLAT)
btn_down.pack(anchor=tk.CENTER)


window.mainloop()


