import os
import MyPytube
link_videos = str(input("URL do Video ou Playlist: "))
resoluçao_video = str(input("Qual Resolção Deseja? [360p/720p/1080p]"))
caminho_user  = str("Video será baixado na pasta Downloads/API_DOWNLOAD")

MyPytube.download_video(link_videos)

