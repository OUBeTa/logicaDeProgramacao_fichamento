records:int = 20
vLido:list = [0] * (records)
n:int = 0
ordered:bool = False

i:int

for i in range(0, records, 1): vLido[i] = int(input(f"Entrar com termo número {i+1} da lista\n"))

while not ordered:
    ordered = True
    n = n + 1
    print("iteração : " + str(n))
    for i in range(0, records - 1, 1):
        if vLido[i + 1] > vLido[i]:
            aux = vLido[i]
            vLido[i] = vLido[i + 1]
            vLido[i + 1] = aux
            ordered = False
print("")
print("Lista ordenada : ")
for i in range(0, records, 1): print(vLido[i])
