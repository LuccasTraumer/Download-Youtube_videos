import pytube

link = 'https://www.youtube.com/watch?v=sEhOY55CSng&list=RDMM&index=23'
caminho = 'C:/Users/Lucas/Downloads/API_teste'

resolution = "720p"


youtubeAll = pytube.YouTube(link).streams.filter(res=resolution).first().download(caminho)
print(type(youtubeAll))
youtube = pytube.YouTube(link).streams
print(type(youtube))
