from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

ws=Tk()
ws.geometry("600x120")
ws.resizable(False,False)
ws.title("Descarga$Video$YouTube")
ws.config(bg="#940404")


#Pantalla:
etiq_link= Label(ws, text="Link YouTube  :", bg="#FFBF00")
etiq_link.grid(row=1, column=0, padx=5, pady=5)

link_video=StringVar()
entry_link=Entry(ws, width=55,textvariable=link_video)
entry_link.grid(row=1, column=1, pady=5, padx=5, columnspan=2)



ws.mainloop()
