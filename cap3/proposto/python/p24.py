records:int = 10
alturaV:list = [0] * (records)
pesoV:list = [0] * (records)
sexoV:list = [""] * (records)
mCount:int = 0
fCount:int = 0
alturaFsum:int = 0
menor:int
i:int

for i in range(0, records, 1):
    sexoV[i] = input(f"Entre com o sexo do indivíduo número {i + 1} (m - f)\n")
    pesoV[i] = float(input(f"Entre com o peso do indivíduo número {i + 1}\n"))
    alturaV[i] = float(input(f"Entre com a altura do indivíduo número {i + 1}\n"))

menor = alturaV[0]

for i in range(0, records - 1, 1):
    if alturaV[i + 1] < menor: menor = alturaV[i + 1]

for i in range(0, records, 1):
    if sexoV[i] == "f":
        fCount = fCount + 1
        alturaFsum = alturaFsum + alturaV[i]
    else: mCount = mCount + 1

print(f"menor altura do grupo : {menor}cm")
print(f"Altura média dos indivíduos de sexo feminino : {alturaFsum / fCount}")
print(f"sexo masculino ({mCount}): {mCount / (mCount + fCount) * 100}")
print(f"sexo feminino ({fCount}): {fCount / (mCount + fCount) * 100}")
