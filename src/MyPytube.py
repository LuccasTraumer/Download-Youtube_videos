import pytube
import  os
import subprocess


caminho = 'C:/Users/Lucas/Downloads/API_DOWNLOAD'
resolucoes = ['144p','240p','360p','480p','720p','1080p','144','240','360','480','720','1080']
def download_video(link_video = str, resolução='360p'):
    try:
        youtube = pytube.YouTube(link_video).streams
        if resolução in resolucoes:
            if resolução == '144' or resolução == '240' or resolução =='360'or resolução =='480'or resolução =='720' or resolução =='1080':
                resolução = (f"{resolução}p")
        if not os.path.exists(caminho):
            os.mkdir(caminho)
    except:
        return 'URL invalida!'
    else:
        youtube.filter(res=resolução).first().download(caminho)
        return "Download Finalizado!"

def download_audio(link_video=str):
    try:
        youtube = pytube.YouTube(link_video).streams.filter(only_audio=True).first().download(caminho)
    except:
        return "Erro ao Baixar Audio!"
    else:
        return "Download finalizado com sucesso!"

def download_playlist(link_playlist = str):
    try:
        playlist = pytube.Playlist(link_playlist)
        print(f"Existem {len(playlist.video_urls)} videos na Playlist!")
        playlist.download_all(caminho+"/playlist")
    except:
        return "Erro ao fazer Download da Playlist"
    else:
        return "Download Exceutado com Sucesso!"