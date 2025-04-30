import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


ventanainicio = tkinter.Tk()

ventanainicio.geometry('1920x1000')#Tamaño de la ventanainicio
ventanainicio.iconbitmap("elicono.ico")
ventanainicio.configure(bg="lavender")

contenedor1 = tkinter.Frame(ventanainicio, bg="lavender")
contenedor1.pack(expand=True) 
contenedor1.place(relx=0.85, rely=0.5, anchor="e")

etiqueta = tkinter.Label(ventanainicio, text = "Clinica Dental")
etiqueta.config(fg="turquoise4", bg="lavender",font=("Arial", 35, "bold"))
etiqueta.pack()

def abrir_ventana():
    venagenda = tkinter.Toplevel()
    venagenda.title("AGENDA")
    venagenda.geometry("1920x1000")
    venagenda.configure(bg="lavender")
    etiqueta = tkinter.Label(venagenda, fg="turquoise4", bg="lavender", text="AGENDA", font=("Arial", 35, "bold"))
    etiqueta.pack(pady=20)

    contdatos = tkinter.Frame(venagenda, bg="lavender")
    contdatos.pack(expand=True)  
    contdatos.place(relx=0.05, rely=0.5, anchor="w")

    etiquetaagreg = tkinter.Label(contdatos, text="Cita Nueva", fg="white", bg="lavender", font=("Resist Mono", 25, "bold"))
    etiquetaagreg.pack(pady="10")#espaciado
    etiquetanombre = tkinter.Label(contdatos, text="Fecha de la cita", fg="pale violet red", bg="lavender", font=("Arial", 15, "bold"))
    etiquetanombre.pack(pady="2")
    entradanombre = tkinter.Entry(contdatos, fg="white", bg="thistle", font=("Arial", 15, "bold"))
    entradanombre.pack(pady="10")

    etiqcita = tkinter.Label(contdatos, text="Estado de la cita", fg="pale violet red", bg="lavender", font=("Arial", 15, "bold"))
    etiqcita.pack(pady="2")
    entradaartista = tkinter.Entry(contdatos, fg="white", bg="thistle", font=("Arial", 15, "bold"))
    entradaartista.pack(pady="10")

    etiquetatiempo = tkinter.Label(contdatos, text="Detalles de la cita", fg="pale violet red", bg="lavender", font=("Arial", 15, "bold"))
    etiquetatiempo.pack(pady="2")
    entradatiempo = tkinter.Entry(contdatos, fg="white", bg="thistle", font=("Arial", 15, "bold"))
    entradatiempo.pack(pady="10")

    etiserv = tkinter.Label(contdatos, text="Servicio", fg="pale violet red", bg="lavender", font=("Arial", 15, "bold"))
    etiserv.pack()
    Servicio = tkinter.StringVar()
    comboserv = ttk.Combobox(contdatos, values=["Servicio 1", "Servicio 2", "Servicio 3"], textvariable=Servicio)
    comboserv.pack(pady="10")
    Servicio.set("Servicio 1")


    etisexo = tkinter.Label(contdatos, text="Sexo", fg="pale violet red", bg="lavender", font=("Arial", 15, "bold"))
    etisexo.pack(side="left", padx=5)
    Sexo = tkinter.StringVar()
    combo = ttk.Combobox(contdatos, values=["Femenino", "Masculino"], textvariable=Sexo)
    combo.pack(side="left", padx=5)
    Sexo.set("Masculino")

    etidoc = tkinter.Label(contdatos, text="Doctor", fg="pale violet red", bg="lavender", font=("Arial", 15, "bold"))
    etidoc.pack(side="left", padx=5)
    Doctor = tkinter.StringVar()
    combodoc = ttk.Combobox(contdatos, values=["Tefani Eufemia", "otro"], textvariable=Doctor)
    combodoc.pack(side="right")
    Doctor.set("otro")

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
