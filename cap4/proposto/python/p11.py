records:int = 10
vLido:list = [0] * (records * records)
menor:list = [0] * (records * records)
i:int
j:int

for i in range(0, records, 1):
    for j in range(0, records, 1):
        vLido[i * records + j] = int(input(f"Entre com [{i}][{j}]\n"))
        menor[j * records + i] = vLido[i * records + j]

for i in range(0, records, 1):
    for j in range(0, records, 1): print(" | " + str(vLido[i * records + j]) + " | ") if j == records - 1 else print(" | " + str(vLido[i * records + j]) + " | ", end='', flush=True)

for i in range(0, records, 1):
    print(f"Linha n {i + 1} (maior até o menor) : ", end='', flush=True)
    isOrdered = False
    while not isOrdered:
        isOrdered = True
        for j in range(0, records - 1, 1):
            aux = vLido[i * records + j]
            if aux < vLido[i * records + (j + 1)]:
                vLido[i * records + j] = vLido[i * records + (j + 1)]
                vLido[i * records + (j + 1)] = aux
                isOrdered = False

    for j in range(0, records, 1): print(" | " + str(vLido[i * records + j]) + " | ") if j == records - 1 else print(" | " + str(vLido[i * records + j]) + " | ", end='', flush=True)

for i in range(0, records, 1):
    print(f"coluna n {i} (menor até o maior) : ", end='', flush=True)
    isOrdered = False
    while not isOrdered:
        isOrdered = True
        for j in range(0, records - 1, 1):
            aux = menor[i * records + j]
            if aux < menor[i * records + (j + 1)]:
                menor[i * records + j] = menor[i * records + (j + 1)]
                menor[i * records + (j + 1)] = aux
                isOrdered = False

    for j in range(0, records, 1): print(" | " + str(menor[i * records + j]) + " | ") if j == records - 1 else print(" | " + str(menor[i * records + j]) + " | ", end='', flush=True)
