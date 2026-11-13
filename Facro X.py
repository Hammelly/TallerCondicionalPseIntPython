valorX = int(input("Ingrese el mínimo valor para X: "))
while valorX < 0:
    valorX = int(input("Ingrese un número positivo: "))
for x in range(0, valorX + 1, 2):
    function = x**3 + x**2 - 5
    print("Para x =", x, ", f(x) =", function)