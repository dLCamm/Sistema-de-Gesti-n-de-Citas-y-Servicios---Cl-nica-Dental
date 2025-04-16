import tkinter
from tkinter import *
from PIL import ImageTk, Image

ventanainicio = tkinter.Tk()

ventanainicio.geometry('1920x1000')#Tamaño de la ventanainicio
ventanainicio.iconbitmap("elicono.ico")
ventanainicio.configure(bg="lavender")

contenedor1 = tkinter.Frame(ventanainicio, bg="lavender")
contenedor1.pack(expand=True)  # expand True para centrar verticalmente
contenedor1.place(relx=0.85, rely=0.5, anchor="e")

etiqueta = tkinter.Label(ventanainicio, text = "Clinica Dental")
etiqueta.config(fg="steel blue", bg="lavender",font=("Arial", 35, "bold"))
etiqueta.pack()

def abrir_ventana():
    nueva_ventana = tkinter.Toplevel()
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("300x200")
    etiqueta = tkinter.Label(nueva_ventana, text="¡Hola! Esta es otra ventana.")
    etiqueta.pack(pady=20)

#BOTONOES
botonagenda = tkinter.Button(contenedor1, text="AGENDA")
botonagenda.config(fg="white", bg="thistle", font=("Arial", 50, "bold"), command=abrir_ventana)
botonagenda.pack(pady="25")

botonpacientes = tkinter.Button(contenedor1, text="PACIENTE")
botonpacientes.config(fg="white", bg="thistle", font=("Arial", 45, "bold"))
botonpacientes.pack(pady="25")

botonfinanzas = tkinter.Button(contenedor1, text="FINANZAS")
botonfinanzas.config(fg="white", bg="thistle", font=("Arial", 45, "bold"))
botonfinanzas.pack(pady="25")

logo = Image.open("imag/logo.png")
logo  = logo.resize((600,600), Image.Resampling.LANCZOS)

log = ImageTk.PhotoImage(logo)
etiqlogo = Label(ventanainicio, image=log)
etiqlogo.place(x=150, y=125)






ventanainicio.mainloop()
