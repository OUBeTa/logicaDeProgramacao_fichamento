a:int = int(input("Entrar com número inteiro"))
aa:int = a
b:int = int(input("Entrar com número inteiro"))
bb:int = b

while b != 0:
    aux = b
    b = a % b
    a = aux

print(f"Máximo dívisor comum entre {aa} e {bb} é : {a}")
