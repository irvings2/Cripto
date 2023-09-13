with open("cancion.txt") as file_object:
    leer = file_object.read()
    CadenaLimpia=""
    for i in range(len(leer)):
        if leer[i]!="\n" and leer[i]!=" " and leer[i]!="'" and leer[i]!="," and leer[i]!="?" and leer[i]!="(" and leer[i]!=")" and leer[i]!="-" and leer[i]!="!":
            CadenaLimpia+=leer[i]
    file_object.close()

with open("cancion.txt") as file_object:
    leer = file_object.read()
    c=25
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
        print(CadenaFinal)
        cifrado=""
        for i in range(len(CadenaFinal)):
            cifrado+=chr(ord(CadenaFinal[i])-32)
    file_object.close()

with open("cancion_c.txt", "w") as file_object:
        file_object.write(cifrado)
        file_object.close()