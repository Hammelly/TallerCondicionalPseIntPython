cantidadNumeros = int(input("Ingrese la cantidad de números: "))
while cantidadNumeros < 0:
    cantidadNumeros = int(input("Ingrese una cantidad positiva: "))
for number in range(1, cantidadNumeros + 1):
    print(number, number * number, number + number * number)