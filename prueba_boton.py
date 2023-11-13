from tkinter import *
import tkinter as TK
ventana = Tk()
class Mi_fondo:
    def __init__(self):
        self.fondo = PhotoImage(file="fondos/fondov6.png")
        self.etiqueta_fondo = Label(ventana,image=self.fondo,border=0)
    def mostrar_fondo(self):
        self.etiqueta_fondo.place(x=0,y=0)

class Botones_partida:
    def __init__(self):
        self.boton_off = PhotoImage(file="boton_noactivo.png")
        self.boton_on = PhotoImage(file="boton_activo.png")
        self.boton = Button(ventana,height=182,width=524,image=self.boton_off)
        self.boton.place(x=399,y=269)
    def boton_activo(self,event):
        self.boton.configure(image=self.boton_on)
    def boton_no_activo(self,event):
        self.boton.configure(image=self.boton_off)


fondo = Mi_fondo()
Boton = Botones_partida()

Boton.boton.bind("<Enter>",Boton.boton_activo)
Boton.boton.bind("<Leave>",Boton.boton_no_activo)




ventana.geometry("1280x720")

fondo.mostrar_fondo()

ventana.mainloop()