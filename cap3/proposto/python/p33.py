def fixDecimal(value, digits): return "%.*f" % (digits, value)

records:int = int(input("Entrar com número de crianças\n"))
sexo:list = [""] * (records)
incubadora:list = [0] * (records)

maiorTempo:int = 0
mCount:int = 0
fCount:int = 0
pCount:int = 0
soma = 0

i:int

for i in range(0, records - 1 + 1, 1):
    sexo[i] = input(f"Entrar com sexo do bebê n{i+1}\n")
    incubadora[i] = int(input(f"Entrar com tempo, em dias, que o bebê n {i + 1} ficou na incubadora, se ficou\n"))

for i in range(0, records - 1, 1): maiorTempo = (incubadora[i+1]) if incubadora[i + 1] > maiorTempo else (maiorTempo)

for i in range(0, records, 1):
    if incubadora[i] > 0:
        soma = soma + incubadora[i]
        pCount = pCount + 1
        if sexo[i] == "f": fCount = fCount + 1
        else: mCount = mCount + 1

print(f"Porcentagem de recem-nascidos prematuros ({pCount})/{records}) : {(fixDecimal(pCount / records) * 100,2)}%")
print(f"Porcentagem de prematuros do sexo masculino ({mCount})/{pCount}) : {(fixDecimal(mCount / pCount) * 100,2)}%")
print(f"Porcentagem de prematuros do sexo feminino ({fCount})/{pCount}) : {(fixDecimal(fCount / pCount) * 100,2)}%")
print(f"Média de dias na incubadora : {soma/records}")
print(f"Maior tempo na incubadora : {maiorTempo}")
