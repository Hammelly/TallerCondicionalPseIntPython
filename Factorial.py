number = int(input("Ingrese un número: "))
if number < 0:
    print("Los negativos no tienen factorial")
else:
    factor = 1
    for contador in range(1, number + 1):
        factor = factor * contador
    print(number, "! =", factor)