records:int = 5
vLido:list = [0] * (records * records)

i:int
j:int

def printMatrix(M):
    for i in range(0, records, 1):
        for j in range(0, records, 1):
            if j == records - 1: print(" | - | ") if M[i * records + j] == 0 else print(f" | {M[i * records + j]} | ")
            else: print(" | - | ", end='', flush=True) if M[i * records + j] == 0 else print(f" | {M[i * records + j]} | ", end='', flush=True)

for i in range(records):
    for j in range(records): vLido[i * records + j] = int(input(f"Entre com [{i}][{j}]: "))

print("Matrix inicial")
printMatrix(vLido)

for j in range(records):
    aux = vLido[j * records + 1]
    vLido[j * records + 1] = vLido[j * records + 4]
    vLido[j * records + 4] = aux

print("\nSwapping 2nd coll and 5th coll")
printMatrix(vLido)

for i in range(records):
    aux = vLido[i * records + i]
    vLido[i * records + i] = vLido[i * records + (records - i - 1)]
    vLido[i * records + (records - i - 1)] = aux

print("\nSwapping diagonal principal e diagonal secundária")
printMatrix(vLido)

