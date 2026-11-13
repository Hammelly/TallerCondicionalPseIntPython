cantidadEstudiantes = int(input("La cantidad de estudiantes: "))
sumaNota = 0
aprobados = 0
reprobados = 0
contadorEstudiantes = 0
while contadorEstudiantes < cantidadEstudiantes:
    nota = float(input("Ingrese la nota: "))
    if nota >= 3.0:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1
    sumaNota = sumaNota + nota
    contadorEstudiantes = contadorEstudiantes + 1
promedio = sumaNota / cantidadEstudiantes
print("La cantidad que aprobaron:", aprobados)
print("La cantidad que reprobaron:", reprobados)
print("El promedio es:", promedio)