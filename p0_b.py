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
    
boton1 = Button(raiz, text='Cifrar', width=10, height=2, font=("Comic Sans MS",10)).grid(row=0, column=1, pady=15 ,sticky="w")
boton2 = Button(raiz, text='Descifrar', width=10, height=2, font=("Comic Sans MS",10)).grid(row=1, column=1, pady=15, sticky="w")

img = cv2.imread("img.bmp")
b,g,r = cv2.split(img)

img[:,:,0] = 255
img[:,:,1] = 255
img[:,:,2] = 199
cv2.imshow('prueba',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
raiz.mainloop()