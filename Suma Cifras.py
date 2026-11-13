number = int(input("Escriba un número: "))
if number > 0:
    copiaNumero = number
    contadorCifras = 0
    sumaCifra = 0
    while copiaNumero > 0:
        cifra = copiaNumero % 10
        copiaNumero = copiaNumero // 10
        sumaCifra = sumaCifra + cifra
        contadorCifras = contadorCifras + 1
    print("La cantidad de cifras de:", number)
    print("Son:", contadorCifras)
    print("La sumatoria es:", sumaCifra)
else:
    print("No es un número positivo")