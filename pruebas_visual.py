from cProfile import label
from datetime import date
from gettext import install
from importlib.resources import path
from tkinter import *
from tkcalendar import Calendar, DateEntry

import tkinter
from turtle import bgcolor
from isort import file
from matplotlib.animation import PillowWriter
from matplotlib.pyplot import text

import pip
from sklearn.feature_extraction import image
from sklearn.feature_selection import SelectFromModel

import Nahual

#Crear ventana principal
ventana = tkinter.Tk()
ventana.geometry("700x500")

#Crear caja de fecha

cal = DateEntry(ventana, selectmode="day", year = 2020, month = 5,day = 22, date_pattern="dd/mm/yyyy")
cal.pack(pady = 20)

etiqueta = Label(ventana, text="Introduce tu fecha de nacimiento")
etiqueta.pack(side= tkinter.TOP)

#Segunda ventana
def ventana2():
    ventana2 = Toplevel()
    ventana2.geometry("350x250")
    fecha = cal.get_date()
    TuNahual = Nahual.nahual(fecha.day, fecha.month, fecha.year)
    Energia,nahual=TuNahual.split()
    path=rf"C:\Users\manue\OneDrive\Escritorio\Python\proyecto-y-oxlajuj-backtun\Imagenes\{nahual}.png"
    print(nahual)
    etiqueta1 = Label(ventana2, text=f"Tu Nahual es:{TuNahual}")
    etiqueta1.pack()
    if path != "":
        image2 = PhotoImage(file=path)
        label = Label(ventana2, image=image2)
        label.pack()

    ventana2.mainloop()

boton1 = tkinter.Button(ventana, text = "Buscar mi Nahual", bg = "limegreen", command=ventana2)
boton1.pack(side= tkinter.TOP)

image = PhotoImage(file=r"C:\Users\manue\OneDrive\Escritorio\Python\proyecto-y-oxlajuj-backtun\Imagenes\Nahual-885x500.png")
label = Label(ventana, image=image)
label.pack()

ventana.mainloop()



