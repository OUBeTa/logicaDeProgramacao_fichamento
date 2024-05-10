n:int = int(input("Entre com inteiro"))
if n == 0: print(f"{n}! : 0")
else:
    f = 1
    for v in range(1, n + 1, 1): f = f * v
    print(f"{n}! : {f}")
