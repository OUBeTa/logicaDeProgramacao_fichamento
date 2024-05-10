records:int = 30
vLido:list = [0] * (records)
vResult:list = [0] * (records)

for i in range(0, records,1): vLido[i] = int(input(f"Entre com número n {i+1}"))
for i in range(0, records,1): vResult[i] = vLido[records - 1 - i]

print(f"vetor lido {vLido}")
print(f"vetor ordenado inversamente : {vResult}")