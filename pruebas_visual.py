from cProfile import label
from gettext import install
from tkinter import *

import tkinter
from turtle import bgcolor
from isort import file
from matplotlib.animation import PillowWriter

import pip
from sklearn.feature_extraction import image

ventana = tkinter.Tk()
ventana.geometry("700x500")
ventana = 

cajatexto = tkinter.Entry(ventana)
cajatexto.pack(side= tkinter.TOP)

boton1 = tkinter.Button(ventana, text = "Buscar mi Nahual", bg = "blue")
boton1.pack(side= tkinter.TOP)

image = PhotoImage(file=r"C:\Users\manue\OneDrive\Escritorio\Python\proyecto_grupo\Nahual-885x500.png")
label = Label(ventana, image=image)
label.pack()

ventana.mainloop()



