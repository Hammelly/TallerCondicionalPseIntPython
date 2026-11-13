print("¿Cuántos estudiantes son?: ")
number = int(input())
android = 0
ios = 0
for contador in range(1, number + 1):
    respuesta = input("Voto " + str(contador) + " (android/ios): ")
    if respuesta == "android":
        android = android + 1
    else:
        if respuesta == "ios":
            ios = ios + 1
        else:
            print("Respuesta no valida")
print("Android:", android)
print("iOS:", ios)

if android > ios:
    print("Gana Android")
else:
    if ios > android:
        print("Gana iOS")
    else:
        print("Empate")