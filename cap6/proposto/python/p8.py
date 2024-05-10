a:int = int(input("Entrar com número inteiro"))
aa:int = a
x:int = a
b:int = int(input("Entrar com número inteiro"))
bb:int = b
y:int = b

while y != 0:
    aux = y
    y = a % y
    a = aux

print(f"máximo múltiplo comum entre {aa} e {bb} é : {(aa * bb) // a}")
