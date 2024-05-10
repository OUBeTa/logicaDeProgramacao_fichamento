records:int = 5
vLido:list = [0] * (records * records)
vResult:list = [0] * (records * records)

i:int
j:int

def printMatrix(M):
    for i in range(0, records, 1):
        for j in range(0, records, 1):
            if j == records - 1: print(" | - | ") if M[i * records + j] == 0 else print(f" | {M[i * records + j]} | ")
            else: print(" | - | ", end='', flush=True) if M[i * records + j] == 0 else print(f" | {M[i * records + j]} | ", end='', flush=True)

for i in range(0, records, 1):
    for j in range(0, records, 1):
        vLido[i * records + j] = int(input(f"Entrar com [{i}][{j}]"))
        vResult[j * records + i] = vLido[i * records + j]

print("Matriz inicial")
printMatrix(vLido)

print("Matriz rotacionada 90 graus")
printMatrix(vResult)