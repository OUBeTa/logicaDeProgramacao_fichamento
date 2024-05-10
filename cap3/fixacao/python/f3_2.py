n:int = int(input("Entre com valor inteiro"))
r:int = 0
while True:
    r = r + 1
    if r * r > n: break
r = r - 1
print(f"O inteiro aproximado da raiz de {n} é {r}")