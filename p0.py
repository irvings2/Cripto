from tkinter import *

raiz = Tk()
raiz.title("Practica 0")

label1 = Label(raiz, text="c=", font=("Comic Sans MS",18)).grid(row=2, pady=4, sticky="e", padx=4)
archivo = Label(raiz, text="Archivo", font=("Comic Sans MS",18)).grid(row=3, pady=4, sticky="e", padx=4)

e1 = Entry(raiz)
e2 = Entry(raiz)

e1.grid(row=2, column=1, padx=10, pady=10)
e2.grid(row=3, column=1, padx=10, pady=10)

boton1 = Button(raiz, text='Cifrar', width=10, height=2, font=("Comic Sans MS",10)).grid(row=0, column=0, pady=4)
boton2 = Button(raiz, text='Descifrar', width=10, height=2, font=("Comic Sans MS",10)).grid(row=1, column=0, pady=4)


with open("cancion.txt") as file_object:
    leer = file_object.read()
    CadenaLimpia=""
    for i in range(len(leer)):
        if leer[i]!="\n" and leer[i]!=" " and leer[i]!="'" and leer[i]!="," and leer[i]!="?" and leer[i]!="(" and leer[i]!=")" and leer[i]!="-" and leer[i]!="!":
            CadenaLimpia+=leer[i]
    file_object.close()

with open("cancion.txt") as file_object:
    leer = file_object.read()
    c=5
    if c>25:
        print("Ingrese un numero entre 1 y 25")
        exit(1)
    else:
        CadenaFinal=""
        for i in range(len(CadenaLimpia)):
            if ord(CadenaLimpia[i])+c>122:
                 aux=122-ord(CadenaLimpia[i])
                 CadenaFinal+=chr(96+c-aux)
            else:     
                CadenaFinal+=chr(ord(CadenaLimpia[i])+c)
        cifrado=""
        for i in range(len(CadenaFinal)):
            cifrado+=chr(ord(CadenaFinal[i])-32)
    file_object.close()

with open("cancion_c.txt", "w") as file_object:
        file_object.write(cifrado)
        file_object.close()

raiz.mainloop()