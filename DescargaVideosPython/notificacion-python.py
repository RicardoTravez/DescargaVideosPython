from pytube import YouTube
from hurry.filesize import size
from plyer import notification
import datetime
import time
import os

link = input("Ingersa el link: ")
yt = YouTube(link)

strm = yt.streams.get_highest_resolution()
print("Titulo: ", yt.title)
print("Descripcion: ", yt.description)
print("Autor: ", yt.author)
print("Fecha de publicacion: ", yt.publish_date.strftime("%Y-%m-%d"))
print("Duracion del video: ", str(datetime.timedelta(seconds=yt.length)), "seconds")
print("Resolucion del video: ", strm.resolution)
print("Tamaño del video: ", size(strm.filesize))
print("Iniciando descarga del video: ")
strm.download(os.path.expanduser("Descarga"))
print("Video descargado con exito.")
notification.notify(
    title = "Descargador de video Python.",
    message = "Tu video se descargo Correctamente.\nRevisa en tu carpeta Descarga",
    app_icon = "python.ico",
    timeout = 20
    )
