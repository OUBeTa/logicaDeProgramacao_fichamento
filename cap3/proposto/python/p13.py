a:int = int(input("Entrar com primeiro número inteiro"))
b:int = int(input("Entrar com segundo número inteiro"))
print(f"O MDC entre {a} e {b} é : ")
while b != 0:
    r = a % b
    a = b
    b = r
print(a)
