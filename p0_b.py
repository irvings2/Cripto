from tkinter import *
import cv2
import numpy as np

raiz = Tk()
raiz.title("Practica 0")
raiz.geometry("300x350")

label1 = Label(raiz, text="Desp. R", font=("Comic Sans MS",18)).grid(row=2, column=0, pady=4, sticky="e", padx=4)
label1 = Label(raiz, text="Desp. G", font=("Comic Sans MS",18)).grid(row=3, column=0, pady=4, sticky="e", padx=4)
label1 = Label(raiz, text="Desp. B", font=("Comic Sans MS",18)).grid(row=4, column=0, pady=4, sticky="e", padx=4)
archivo = Label(raiz, text="Archivo", font=("Comic Sans MS",18)).grid(row=5, column=0, pady=4, sticky="e", padx=4)

e1 = Entry(raiz, font=("Comic Sans MS",10))
e2 = Entry(raiz, font=("Comic Sans MS",10))
e3 = Entry(raiz, font=("Comic Sans MS",10))
e4 = Entry(raiz, font=("Comic Sans MS",10))

e1.grid(row=2, column=1, padx=10, pady=10)
e2.grid(row=3, column=1, padx=10, pady=10)
e3.grid(row=4, column=1, padx=10, pady=10)
e4.grid(row=5, column=1, padx=10, pady=10)

def cifrar():
    archivo = e4.get()
    img = cv2.imread(archivo)

    for i in range(396):
        for j in range (317):
            x=i
            y=j
            b = img.item(y, x, 0)
            g = img.item(y, x, 1)
            r = img.item(y, x, 2)
            b1=int(e3.get())
            g1=int(e2.get())
            r1=int(e1.get())
            if b+b1>255:
                img.itemset((y, x, 0), b1-(256-b))
            else:
                img.itemset((y, x, 0), b+b1)
            if g+g1>255:
                img.itemset((y, x, 1), g1-(256-g))
            else:
                img.itemset((y, x, 1), g+g1)
            if r+r1>255:
                img.itemset((y, x, 2), r1-(256-r))
            else:
                img.itemset((y, x, 2), r+r1)
    archivoaux=""
    for i in range(len(archivo)):
        if archivo[i]=='.':
            archivoaux+="_c"+archivo[i]
        else:
            archivoaux+=archivo[i]
    cv2.imwrite(archivoaux, img)

def descifrar():
    archivo = e4.get()
    img = cv2.imread(archivo)
    
    for i in range(396):
        for j in range (317):
            x=i
            y=j
            b = img.item(y, x, 0)
            g = img.item(y, x, 1)
            r = img.item(y, x, 2)
            b1=int(e3.get())
            g1=int(e2.get())
            r1=int(e1.get())
            if b-b1<0:
                img.itemset((y, x, 0), 255-b1+b)
            else:
                img.itemset((y, x, 0), b-b1)
            if g-g1<0:
                img.itemset((y, x, 1), 255-g1+g)
            else:
                img.itemset((y, x, 1), g-g1)
            if r-r1<0:
                img.itemset((y, x, 2), 255-r1+r)
            else:
                img.itemset((y, x, 2), r-r1)
    archivoaux=""
    for i in range(len(archivo)):
        if archivo[i]=='.':
            archivoaux+="_d"+archivo[i]
        else:
            archivoaux+=archivo[i]
    cv2.imwrite(archivoaux, img)
    
boton1 = Button(raiz, text='Cifrar', width=10, height=2, font=("Comic Sans MS",10), command=cifrar).grid(row=0, column=1, pady=15 ,sticky="w")
boton2 = Button(raiz, text='Descifrar', width=10, height=2, font=("Comic Sans MS",10), command=descifrar).grid(row=1, column=1, pady=15, sticky="w")

raiz.mainloop()