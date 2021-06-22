from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

ws=Tk()
ws.geometry("470x110")
ws.resizable(False,False)
ws.title("Descarga$Video$YouTube")
ws.config(bg="#940404")

#Logica
def Buscar():
    directorio_descargar= filedialog.askdirectory(initialdir="RUTA DE DIRECTORIO")
    ruta_descarga.set(directorio_descargar)

def Descargar():
    link_Youtube= link_video_ingresado.get()
    carpeta_descarga= ruta_descarga.get()
    toma_video= YouTube(link_Youtube)
    stream_video=toma_video.streams.first()
    stream_video.download(carpeta_descarga)

    messagebox.showinfo("COMPLETADO", f"DESCARGADO Y GUARDADO EN {carpeta_descarga}")


#Pantalla:
etiq_link= Label(ws, text="Link YouTube  :", bg="#FFBF00")
etiq_link.grid(row=1, column=0, padx=5, pady=5)

link_video_ingresado=StringVar()
entry_link=Entry(ws, width=55,textvariable=link_video_ingresado)
entry_link.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

etiq_destino= Label(ws, text="Carpeta Destino  :", bg="#FFBF00")
etiq_destino.grid(row=2, column=0, padx=5, pady=5)

ruta_descarga=StringVar()
entry_destino=Entry(ws, width=40, textvariable=ruta_descarga)
entry_destino.grid(row=2, column=1, padx=5, pady=5)

boton_busqueda= Button (ws, text="Buscar", width=10, bg="#D8D8D8", command=Buscar)
boton_busqueda.grid(row=2, column=2, pady=1, padx=1)

boton_descargar= Button(ws, text="Descargar", width=20, bg="#D8D8D8", command=Descargar)
boton_descargar.grid(row=3, column=1, padx=3, pady=3)

ws.mainloop()