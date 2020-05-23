import os
import MyPytube
link_videos = str(input("URL do Video ou Playlist: "))
caminho_user  = str("Video será baixado na pasta Downloads/API_DOWNLOAD")

MyPytube.download_video(link_videos)

