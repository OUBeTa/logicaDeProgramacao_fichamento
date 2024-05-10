def fixDecimal(value, digits): return "%.*f" % (digits, value)

a:float = float(input("Entre com valor para a"))
b:float = float(input("Entre com valor para b"))
c:float = float(input("Entre com valor para c"))

d:float = b * b - 4 * a * c

if d <= 0:
    if d == 0: print("Raiz única : " + str(-b / (2 * a)))
    else:
        print("Ambas as raizes são imaginárias\n")
        parteReal = -b / (2 * a)
        parteImaginaria = sqrt(-d) / (2 * a)
        print(f"Raiz 1 : {parteReal} + {fixDecimal(parteImaginaria,2)} i")
        print(f"Raiz 2 : {parteReal} - {fixDecimal(parteImaginaria,2)} i")
else:
    print("Ambas as raizes são reais")
    print(f"Raiz 1 : {(-b + d) / (2 * a)}")
    print(f"Raiz 2 : {(-b - d) / (2 * a)}")