a:int = int(input("Entrar com número inteiro\n"))
i:int

print("Os divisores de " + str(a) + " são : [", end='', flush=True)

for i in range(1, a + 1, 1):
    if a % i == 0: print(str(i) + "]") if i == a else print(str(i) + ",", end='', flush=True)

