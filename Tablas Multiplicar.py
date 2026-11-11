tabla = int(input("¿Qué tabla quieres repasar del 1 al 10?: "))
puntos = 0
for contador in range(1, 11):
    respuesta = int(input(f"¿Cuánto es {tabla} x {contador}?: "))
    if respuesta == tabla * contador:
        print("¡Felicitaciones!")
        puntos = puntos + 1
    else:
        print("Incorrecto. La respuesta es", tabla * contador)
print("Aciertos:", puntos, "de 10")
if puntos <= 5:
    print("Insuficiente")
else:
    if puntos == 6 or puntos == 7:
        print("Aceptable")
    else:
        if puntos == 8 or puntos == 9:
            print("Sobresaliente")
        else:
            print("Valoración: Excelente")