import urllib.request
from PIL import ImageTk
from tkinter import Label, Tk
from services.render_video import Render

url = 'https://i.pinimg.com/564x/52/73/ea/5273eab54abe470af426b06587f4cc52.jpg'
url2 = 'https://www.youtube.com/watch?v=L1FUOpToWh4'
root = Tk()

render = Render(url2)
req = urllib.request.urlopen(render.thumbnail)
raw_data = req.read()
req.close()

photo = ImageTk.PhotoImage(data=raw_data)
lbl = Label(root,image=photo)
lbl.image =  photo

lbl.pack()
root.mainloop()