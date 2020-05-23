import os
import MyPytube

video_ou_audio = str(input("Qual tipo de Arquivo deseja baixar? [mp3/mp4/playlist]: "))
link_videos = str(input("URL do Audio,Video ou Playlist: "))
print("Video será baixado na pasta Downloads/API_DOWNLOAD")

if video_ou_audio.lower() == "mp4":
    resoluçao_video = str(input("Qual Resolção Deseja? [144p/240p/360p/720p/1080p]: "))
    print(MyPytube.download_video(link_videos, resoluçao_video))
if video_ou_audio.lower() == "mp3":
    print(MyPytube.download_audio(link_videos))
if video_ou_audio.lower() == "playlist":
    print(MyPytube.download_playlist(link_videos))


