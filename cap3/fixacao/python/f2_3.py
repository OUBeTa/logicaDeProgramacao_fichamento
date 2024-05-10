a:float = float(input("Digite o valor desejado para a"))
b:float = float(input("Digite o valor desejado para b"))
c:float = float(input("Digite o valor desejado para c"))

d:float = b * b - 4 * a * c

x1:float
x2:float

if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print("As raizes são: [" + str(x1) + "," + str(x2) + "]")
else:
    if d == 0:
        x1 = -b / (2 * a)
        print("Apenas uma raiz é real!")
        print("raiz : " + str(x1))
    else:
        print("Ambas as raizes são imaginárias!")
