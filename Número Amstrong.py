number = int(input("Ingrese un número: "))
number1 = number
cantidadCifras = 0
suma = 0
while number1 > 0:
    cantidadCifras = cantidadCifras + 1
    number1 = number1 // 10
number1 = number
while number1 > 0:
    digito = number1 % 10
    suma = suma + digito ** cantidadCifras
    number1 = number1 // 10
if suma == number:
    print(number, "SI es Armstrong")
else:
    print(number, "NO es Armstrong")