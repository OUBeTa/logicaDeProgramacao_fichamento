records:int = 5
vLido:list = [0] * (records)

i:int
aux:int

for i in range(0, records, 1): vLido[i] = int(input(f"Entrar com item número {i+1}\n"))

aux = vLido[records - 1]

for i in range(records - 1, 0, -1): vLido[i] = vLido[i - 1]

vLido[0] = aux

print(vLido)