num:int = int(input("Entre com número inteiro"))
i:int = num
bb:str = ""

if num <= 2: bb = (f"{num} não é primo")
else:
    bb = (f"{num} é primo")
    for i in range(2, int(num ** 0.5) + 1, 1): bb = (f"{num} não é primo") if num % i == 0 else bb

print(bb)
