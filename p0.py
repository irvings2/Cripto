with open("cancion.txt") as file_object:
    leer = file_object.read()
    CadenaLimpia=""
    for i in range(len(leer)):
        if leer[i]!="\n" and leer[i]!=" " and leer[i]!="'" and leer[i]!="," and leer[i]!="?" and leer[i]!="(" and leer[i]!=")" and leer[i]!="-" and leer[i]!="!":
            CadenaLimpia+=leer[i]
    c=26
    if c>25:
        print("Ingrese un numero entre 1 y 25")
        exit(1)
    else:
        CadenaFinal=""
        for i in range(len(CadenaLimpia)):
            if ord(CadenaLimpia[i])==120:
                 CadenaFinal+=chr(96+c-2)
            elif ord(CadenaLimpia[i])==121:
                 CadenaFinal+=chr(96+c-1)
            elif ord(CadenaLimpia[i])==122:
                 CadenaFinal+=chr(96+c)
            else: 
                CadenaFinal+=chr(ord(CadenaLimpia[i])+c)
        cifrado=""
        for i in range(len(CadenaFinal)):
            cifrado+=chr(ord(CadenaFinal[i])-32)

with open("cancion_c.txt", "w") as file_object:
        file_object.write(cifrado)
        

