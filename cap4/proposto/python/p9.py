def fixDecimal(value, digits): return "%.*f" % (digits, value)

def orderList(v):
    isOrdered = False
    aux = 0
    while not isOrdered:
        isOrdered = True
        for i in range(0, len(v) - 2 + 1, 1):
            if v[i] > v[i + 1]:
                aux = v[i]
                v[i] = v[i + 1]
                v[i + 1] = aux
                isOrdered = False

records:int = 10
altura:list = [0] * (records)

counter:int = 1
maiorSeq:int = 1
media:float = 0.0
soma:float = 0.0
dp:float = 0.0

for i in range(0, records, 1):
    print("Entre com altura n" + str(i + 1))
    altura[i] = float(input())
    media = media + altura[i]

orderList(altura)

media = media / records

for i in range(0, records, 1): soma = soma + aabs((altura[i] - media) * (altura[i] - media) / records)

dp = soma**0.5

current = altura[0]

for i in range(0, records - 1, 1):
    if altura[i + 1] == current: counter = counter + 1
    else:
        if maiorSeq < counter:
            mo = current
            maiorSeq = counter

        current = altura[i + 1]
        counter = 1

print(f"Média das alturas : {fixDecimal(media,3)}")
print(f"Desvio padrão entre as alturas : {fixDecimal(dp,3)}")
print(f"moda entre as alturas : [{mo}] occorência{'' if maiorSeq == 1 else 's'} -> {maiorSeq}")
print(f"Mediana entre as alturas : {fixDecimal((altura[float(len(altura)) / 2] + altura[float(len(altura)) / 2] - 1) / 2,2)}")
