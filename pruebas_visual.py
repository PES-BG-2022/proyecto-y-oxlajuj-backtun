from cProfile import label
from gettext import install
from tkinter import *

import tkinter
from turtle import bgcolor
from isort import file
from matplotlib.animation import PillowWriter
from matplotlib.pyplot import text

import pip
from sklearn.feature_extraction import image

ventana = tkinter.Tk()
ventana.geometry("700x500")

cajatexto = tkinter.Entry(ventana)
cajatexto.pack(side= tkinter.TOP)

def apachar_boton1(event):
    myLabel = Label(ventana2, text="Tu nahual es:", bg="blue")
    myLabel.pack(side= tkinter.BOTTOM)

def ventana2():
    ventana2 = Toplevel()
    ventana2.geometry("350x250")

boton1 = tkinter.Button(ventana, text = "Buscar mi Nahual", bg = "limegreen", command=ventana2)
boton1.pack(side= tkinter.TOP)

image = PhotoImage(file=r"C:\Users\manue\OneDrive\Escritorio\Python\proyecto-y-oxlajuj-backtun\Imagenes\Nahual-885x500.png")
label = Label(ventana, image=image)
label.pack()

ventana.mainloop()


ventana2.mainloop()

