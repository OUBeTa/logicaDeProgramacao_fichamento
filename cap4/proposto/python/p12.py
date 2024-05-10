records:int = 5
vLido:list = [0] * (records * records)
target:list = [0] * (records * records)
a:list = [0] * (records * records)
b:list = [0] * (records * records)
c:list = [0] * (records * records)
d:list = [0] * (records * records)
e:list = [0] * (records * records)
f:list = [0] * (records * records)
g:list = [0] * (records * records)
h:list = [0] * (records * records)


i:int
j:int

def printMatrix(M):
    for i in range(0, records, 1):
        for j in range(0, records, 1):
            if j == records - 1: print(" | - | ") if M[i * records + j] == 0 else print(f" | {M[i * records + j]} | ")
            else: print(" | - | ", end='', flush=True) if M[i * records + j] == 0 else print(f" | {M[i * records + j]} | ", end='', flush=True)

for i in range(0, records, 1):
    for j in range(0, records, 1): vLido[i * records + j] = int(input(f"Entre com [{i}][{j}]"))

for i in range(0, records, 1):
    for j in range(0, records, 1):
        a[i * records + j] = vLido[i * records + j] if j == i else  0
        b[i * records + j] = vLido[i * records + j] if j > i else  0
        c[i * records + j] = vLido[i * records + j] if j < i else  0
        d[i * records + j] = vLido[i * records + j] if j != i else  0
        e[i * records + j] = vLido[i * records + j] if j + i == records - 1 else  0
        f[i * records + j] = vLido[i * records + j] if j + i < records - 1 else  0
        g[i * records + j] = vLido[i * records + j] if j + i > records - 1 else  0
        h[i * records + j] = vLido[i * records + j] if j + i != records - 1 else  0

print("Diagonal principal")
printMatrix(a)
print("\nTriângulo superior a diagonal principal")
printMatrix(b)
print("\nTriângulo inferior a diagonal principal")
printMatrix(c)
print("\nTudo exceto a diagonal principal")
printMatrix(d)
print("\nDiagonal secundário")
printMatrix(e)
print("\nTriângulo superior à diagonal secundária")
printMatrix(f)
print("\nTriângulo inferior à diagonal secundária")
printMatrix(g)
print("\nTudo exceto à diagonal secundária")
printMatrix(h)