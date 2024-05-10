records:int = 50
vLido:list = [0] * (records)
currentSeq:int = 1
maiorSeq:int = 1
maiorSeqV:int = 0

for i in range(0, records, 1): vLido[i] = int(input((f"Entre com número n {i+1}\n")))
print(f"Dentro da lista : {vLido}", end='', flush=True)

for i in range(0, records - 2 + 1, 1):
    if vLido[i + 1] > vLido[i]: currentSeq = currentSeq + 1
    else:
        if currentSeq > maiorSeq:
            maiorSeq = currentSeq
            currentSeq = 1
            ''
if currentSeq > maiorSeq:
    maiorSeq = currentSeq
    currentSeq = 1

print(f"a maior sequência de números em ordem crescente tem : {maiorSeq}{'' if maiorSeq == 1 else 's'}")
