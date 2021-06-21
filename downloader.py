from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

rt = Tk()
rt.title("Downloader")
rt.geometry("350x400")
rt.columnconfigure(0, weight=1)


etiq_yt=Label(rt, text="Introduce la URL del video", font=("jost", 15))
etiq_yt.grid()

variable_entrada= StringVar()
yt_variable=Entry(rt, width=40, textvariable=variable_entrada)
yt_variable.grid()

yt_salvar= Label(rt, text="Salvar El Archivo", font=("jost", 15, "bold"))
yt_salvar.grid()

salvar_archivo= Button(rt, width=10, text="Elige la Ruta", bg="red", fg="white")
salvar_archivo.grid()







rt.mainloop()