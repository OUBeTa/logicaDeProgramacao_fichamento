a:int = int(input("Entrar com divisor"))
c:int = a
b:int = 6

while a >= b: a -= b

print(f"{c} é divisível por 6") if a == 0 else print(f"{c} não é divisível por 6")
