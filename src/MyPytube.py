import pytube
import  os
caminho = 'C:/Users/Lucas/Downloads/API_DOWNLOAD'

def download_video(link_video = str, resolução='720p'):
    try:
        youtube = pytube.YouTube(link_video).streams
        if resolução == '720p' or '1080p' or '1080' or '720':
            youtube = high_resolution(youtube,resolução)
        if not os.path.exists(caminho):
            os.mkdir(caminho)
    except:
        return 'URL invalida!'
    else:
        make_download(youtube)
        return "Download Finalizado!"

    #youtube.filter(file_extension='mp4', progressive=True).order_by('resolution').first().download(caminho)


def make_download(obj_video = pytube.YouTube):
    obj_video.download(caminho)


def high_resolution(obj_video = pytube.YouTube,resolucao = str):
    data = obj_video
    if resolucao == '1080' or resolucao == '720':
        resolucao = (f"{resolucao}p")
    for video in data.itag_index.items():
        if video[1].resolution == resolucao:
            return video