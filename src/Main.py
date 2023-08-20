import os
import requests
import json
import MyPytube
import CONSTANTES


class VideoData:
    def __init__(self, linkVideo, typeFile):
        self.linkVideo = linkVideo
        self.typeFile = typeFile


def getTypeFile():
    videoOrAudio = str(input("Qual tipo de Arquivo deseja baixar? [mp3/mp4/playlist]: "))
    link_videos = str(input("URL do Audio,Video ou Playlist: "))
    pathDownload = str(input("Informe o caminho para o Download: Default será na (Downloads/API_DOWNLOAD)"))
    return VideoData(link_videos, videoOrAudio)


def getPlaylits():
    print(MyPytube.download_playlist(videoData.linkVideo))

def getMP3():
    print(MyPytube.download_audio(videoData.linkVideo))

def getMP4():
    resolution = str(input("Qual Resolção Deseja? [144p/240p/360p/720p/1080p]: "))
    print(MyPytube.download_video(videoData.linkVideo, resolution))


videoData = getTypeFile()

if videoData.typeFile in CONSTANTES.TYPE_FILES:
    if videoData.typeFile.lower() == CONSTANTES.MP3:
        getMP3()

    elif videoData.typeFile.lower() == CONSTANTES.MP4:
        getMP4()

    else:
        getPlaylits()

else:
    videoData = getTypeFile()


