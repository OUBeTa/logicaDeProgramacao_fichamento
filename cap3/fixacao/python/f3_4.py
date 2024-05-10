h:float = 0
n:int = int(input("Entre com N"))

for v in range(1, n + 1 + 1, 1): h = h + float(1) / v

print(f"O resultado da série : {h}")
