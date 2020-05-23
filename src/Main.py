import os
import MyPytube
link_videos = str(input("URL do Video ou Playlist: "))
resoluçao_video = str(input("Qual Resolção Deseja? [144p/240p/360p/720p/1080p]"))
print("Video será baixado na pasta Downloads/API_DOWNLOAD")

print(MyPytube.download_video(link_videos,resoluçao_video))

