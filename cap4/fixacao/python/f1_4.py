records:int = 20
vLido:list = [0] * (records)

n:int = 0
i:int
ii:int  
menor:int
aux:int

for i in range(0, records, 1): vLido[i] = int(input(f"Entrar com termo número {i+1} da lista\n"))

for i in range(0, records - 1, 1):
    menor = i
    n += 1

    print("Iteração número : " + str(n))

    for ii in range(i + 1, records, 1):
        if vLido[ii] < vLido[menor]: menor = ii

    if menor != i:
        aux = vLido[i]
        vLido[i] = vLido[menor]
        vLido[menor] = aux

print("")
for i in range(0, records, 1): print(vLido[i])
