n:int = int(input("Entre com número inteiro"))

p:bool = True

for v in range(n - 1, 2 - 1, -1):
    if n % v == 0: p = False

print(f"o número {n} é primo") if p else print(f"o número {n} não é primo")