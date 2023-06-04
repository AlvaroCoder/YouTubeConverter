from pytube import YouTube
from urllib3 import request
from PIL import ImageTk
import pprint
# https://www.youtube.com/watch?v=FoCG-WNsZio

dest_download = 'music'

def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")

yt = YouTube("http://youtube.com/watch?v=2lAe1cqCOXo",use_oauth=True, allow_oauth_cache=False)
print(yt.thumbnail_url)
print(yt.use_oauth)
print(yt.title)

# yout = yt.streams.filter(file_extension='mp4',progressive=True).order_by('resolution').desc().get_by_resolution("720p").download(dest_download)
# print('Download finished ! ')

