import pytube
import  os
def download_video(link_video = str, caminho = 'C:/Users/Lucas/Downloads/API_DOWNLOAD'):
    try:
        youtube = pytube.YouTube(link_video).streams.filter(file_extension='mp4',progressive=True).order_by('resolution').first()
        if not os.path.exists(caminho):
            os.mkdir(caminho)
    except:
        return 'URL invalida!'
    youtube.download(caminho)
