from tkinter import *

raiz = Tk()
raiz.title("Practica 0")
miFrame = Frame(raiz, width=500, height=400)
miFrame.pack()

Label1 = Label(miFrame, text="c=", font=("Comc Sans MS",18))
Label1.place(x=150,y=200)

Label2 = Label(miFrame, text="Archivo", font=("Comc Sans MS",18))
Label2.place(x=120,y=240)

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