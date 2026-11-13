cantidadTerminos = int(input("Ingrese la cantidad de términos a generar: "))
termino = 1
for contadorNumeros in range(1, cantidadTerminos):
    print("Termino", termino)
    termino = termino + 2
print("Termino", termino)