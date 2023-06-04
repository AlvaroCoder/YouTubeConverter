from pytube import YouTube

URL_YOUTUBE = 'https://www.youtube.com/watch?v=fCgsUDHaieQ'
youtube_video = YouTube(url=URL_YOUTUBE, use_oauth=True, allow_oauth_cache=False)

stream = youtube_video.streams
high_res = stream.filter(file_extension='mp4', progressive=True).desc().get_highest_resolution()
destination = './music'
high_res.download(output_path=destination)

print('Descarga completada')
