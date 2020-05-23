import pytube

link = 'https://www.youtube.com/watch?v=sEhOY55CSng&list=RDMM&index=23'
caminho = 'C:/Users/Lucas/Downloads/API_teste'

resolution = "720p"

youtubeAll = pytube.YouTube(link).streams.filter()
youtube = pytube
data = pytube.YouTube(link).streams
for video in data.itag_index.items():
    if video[1].resolution == '720p' or '1080p':
        youtube = video
        break
    else:
        print(f"Resolução: {video[1].resolution}")
youtube.download(caminho)
