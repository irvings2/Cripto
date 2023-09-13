with open("prueba.txt") as file_object:
    leer = file_object.read()
    print(leer)

with open("prueba_c.txt", "w") as file_object:
    file_object.write("Prueba1")