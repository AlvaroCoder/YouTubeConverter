from pytube import YouTube
import urllib.request
from PIL import ImageTk

class Render():
    def __init__(self, url='') -> None:
        self.yt = YouTube(url,use_oauth=True,allow_oauth_cache=False)
        self.__image = self.yt.thumbnail_url
        self.__video = self.yt.streams.filter(file_extension='mp4',progressive=True).desc().get_highest_resolution()
        self.__title = self.yt.title
        self.__author = self.yt.author

    def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        pct_completed = bytes_downloaded / total_size * 100
        print(f"Status: {round(pct_completed, 2)} %")
    
    @property
    def image(self):
        req = urllib.request.urlopen(self.__image)
        raw_data = req.read()
        req.close()
        return ImageTk.PhotoImage(data=raw_data)
    @property
    def thumbnail(self):
        return self.__image
    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    def download(self):
        self.__video.download()
    
