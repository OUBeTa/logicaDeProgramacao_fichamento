records:int = 10
inputV:list = [0] * (records)

for i in range(0, records, 1): inputV[i] = int(input(f"valor número : {i + 1}"))

menor:int = inputV[0]
maior:int = inputV[0]

for i in range(0, records - 2 + 1, 1):
    if inputV[i + 1] < menor: menor = inputV[i + 1]
    if inputV[i + 1] > maior: maior = inputV[i + 1]

print(f"O maior valor do conjunto dado é : {maior}")
print(f"O menor valor do conjunto dado é : {menor}")
