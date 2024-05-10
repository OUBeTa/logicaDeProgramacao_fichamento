records:int = 6
vReal:list = [0] * records
vWeight:list = [0] * records

soma:int = 0
den:int = 0

for i in range(0, records - 1 + 1, 1):
    vReal[i] = float(input(f"Entre com valor número {i+1}\n"))
    vWeight[i] = i + 1
    den = den + i + 1
for i in range(0, records - 1 + 1, 1): soma = soma + vWeight[i] * vReal[i]

print("Média ponderada : " + str(soma / den))
