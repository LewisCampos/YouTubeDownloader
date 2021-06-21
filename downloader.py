from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

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

salvar_archivo= Button(rt, width=10, text="Elige la Ruta", bg="red", fg="white")
salvar_archivo.grid()

error_ruta= Label(rt, text="Error de ruta seleccioanda", fg="red", font=("jost", 10))
error_ruta.grid()

calidad_vd= Label(rt, text="Selecciona la Calidad", font=("jost",15))
calidad_vd.grid()

calidades=["720p", "144p", "Audio"]
calidades_vd= ttk.Combobox(rt, values=calidades)
calidades_vd.grid()

boton_descargar = Button(rt, text="Descargar", width=10, bg="red", fg="white")
boton_descargar.grid()








rt.mainloop()