cantidadTerminos = int(input("Ingrese un número: "))
termino = 1
contadorNumeros = 0
while contadorNumeros < cantidadTerminos - 1:
    print(termino, end=", ")
    termino = termino + 2
    contadorNumeros = contadorNumeros + 1
print(termino)