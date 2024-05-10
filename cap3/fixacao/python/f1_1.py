def fixDecimal(value, digits): return "%.*f" % (digits, value)

a:float = float(input("Entre com número a"))
b:float = float(input("Entre com número b"))
c:float = float(input("Entre com número c"))

d:float = b * b - 4 * a * c

if d <= 0:
    if d == 0: print("Raiz única : " + str(-b / (2 * a)))
    else:
        parteReal = -b / (2 * a)
        parteImaginaria = sqrt(-d) / (2 * a)
        print("Raiz 1 : " + str(parteReal) + " + " + fixDecimal(parteImaginaria,2) + "i")
        print("Raiz 2 : " + str(parteReal) + " - " + fixDecimal(parteImaginaria,2) + "i")
else:
    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
    print("Raiz 1 : " + str(x1))
    print("Raiz 2 : " + str(x2))
