from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


nombre_archivo=""

def abrir_directorio():
    global nombre_archivo
    nombre_archivo = filedialog.askdirectory()

    if (len(nombre_archivo) > 1):
        error_ruta.config(text=nombre_archivo, fg="green")

    else:
        error_ruta.config(text="Por favor elige una carpeta!!", fg="red")
        


def descarga_video():
    eleccion = calidades_vd.get()
    url=variable_vd.get()

    if(len(url)>1):
        error_vd.config(text="")
        vd = YouTube(url)

        if (eleccion==calidades[0]):
            seleciona= vd.streams.filter(progressive=True).first()

        elif (eleccion==calidades[1]):
            seleciona=vd.streams.filter(progressive=True,file_extension="mp4").last()

        elif (eleccion==calidades[2]):
            seleciona=vd.streams.filter(only_audio=True).first()

        else:
            error_vd.config(text="Copia el link de nuevo", fg="red")

    seleciona.download(nombre_archivo)
    error_vd.config(text="Descarga Completa")


rt = Tk()
rt.title("Downloader")
rt.geometry("350x400")
rt.columnconfigure(0, weight=1)


etiq_vd=Label(rt, text="Introduce la URL del video", font=("jost", 15))
etiq_vd.grid()

variable_entrada= StringVar()
variable_vd=Entry(rt, width=40, textvariable=variable_entrada)
variable_vd.grid()

error_vd= Label(rt, text="Error de URL", fg="red", font=("jost",10))
error_vd.grid()

salvar_vd= Label(rt, text="Salvar El Archivo", font=("jost", 15, "bold"))
salvar_vd.grid()

salvar_archivo= Button(rt, width=10, text="Elige la Ruta", bg="red", fg="white", command=abrir_directorio)
salvar_archivo.grid()

error_ruta= Label(rt, text="Error de ruta seleccioanda", fg="red", font=("jost", 10))
error_ruta.grid()

calidad_vd= Label(rt, text="Selecciona la Calidad", font=("jost",15))
calidad_vd.grid()

calidades=["720p", "144p", "Audio"]
calidades_vd= ttk.Combobox(rt, values=calidades)
calidades_vd.grid()

boton_descargar = Button(rt, text="Descargar", width=10, bg="red", fg="white", command=descarga_video)
boton_descargar.grid()

rt.mainloop()