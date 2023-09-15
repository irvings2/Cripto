from tkinter import *

raiz = Tk()
raiz.title("Practica 0")

label1 = Label(raiz, text="c=", font=("Comic Sans MS",18)).grid(row=2, pady=4, sticky="e", padx=4)
archivo = Label(raiz, text="Archivo", font=("Comic Sans MS",18)).grid(row=3, pady=4, sticky="e", padx=4)

e1 = Entry(raiz)
e2 = Entry(raiz)

e1.grid(row=2, column=1, padx=10, pady=10)
e2.grid(row=3, column=1, padx=10, pady=10)

def cifrar():
    archivo = e2.get()
    with open(archivo, "r") as file_object:
        leer = file_object.read()
        CadenaLimpia=""
        for i in range(len(leer)):
            if leer[i]!="\n" and leer[i]!=" " and leer[i]!="'" and leer[i]!="," and leer[i]!="?" and leer[i]!="(" and leer[i]!=")" and leer[i]!="-" and leer[i]!="!":
                CadenaLimpia+=leer[i]
    file_object.close() 
    c=int(e1.get())
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
        archivoaux=""
        for i in range(len(archivo)):
            if archivo[i]=='.':
                archivoaux+="_c"+archivo[i]
            else:
                archivoaux+=archivo[i]
        with open(archivoaux, "w") as file_object:
            file_object.write(cifrado)
            file_object.close()
            
def descifrar():
    archivo = e2.get()
    with open(archivo, "r") as file_object:
        leer = file_object.read()
        cadena1=""
        for i in range(len(leer)):
                cadena1+=chr(ord(leer[i])+32)
    file_object.close() 
    c=int(e1.get())
    if c>25:
        print("Ingrese un numero entre 1 y 25")
        exit(1)
    else:
        descifrado=""
        for i in range(len(cadena1)):
            if ord(cadena1[i])-c<97:
                aux=122-ord(cadena1[i])
                aux1=ord(cadena1[i])-97
                descifrado+=chr(ord(cadena1[i])+aux-aux1)
            else:         
                descifrado+=chr(ord(cadena1[i])-c)
        archivoaux=""
        for i in range(len(archivo)):
            if archivo[i]=='.':
                archivoaux+="_d"+archivo[i]
            else:
                archivoaux+=archivo[i]
        with open(archivoaux, "w") as file_object:
            file_object.write(descifrado)
            file_object.close()
    
boton1 = Button(raiz, text='Cifrar', width=10, height=2, font=("Comic Sans MS",10),command=cifrar).grid(row=0, column=0, pady=4)
boton2 = Button(raiz, text='Descifrar', width=10, height=2, font=("Comic Sans MS",10), command=descifrar).grid(row=1, column=0, pady=4)

raiz.mainloop()