isPrime:bool = True
a:int = int(input("Entre com primeiro número\n"))
b:int = int(input("Entre com segundo número\n"))
count:int = 0

for a in range(a + 1, b - 1 + 1, 1):
    isPrime = True
    for i in range(2, a * a + 1, 1):
        if not(i == a):
            if a % i == 0: isPrime = False
    if isPrime:
        count = count + 1
        print(a)

print(f"{count} número{'' if count == 1 else 's'} primo{'' if count == 1 else 's'} no total!")
