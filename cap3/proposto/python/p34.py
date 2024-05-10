records:int = 10
maiorIdade:list = [0] * (5)
idade:list = [0] * (records)
nota:list = [0] * (records)
notaCount:list = [0] * (records)
porcentual:list = [0] * (records)
maiorIruim:int = 0
maiorIotimo:int = 0

i:int
diferenca:int

for i in range(0,5, 1): notaCount[i],porcentual[i],maiorIdade[i] = 0,0,0

for i in range(0, records, 1):
    idade[i] = int(input(f"Entrar com idade do indivíduo n{i+1}"))
    nota[i] = int(input(f"Entrar com nota dada pelo indivíduo n{i+1} (1-5)"))
    notaCount[nota[i] - 1] = notaCount[nota[i] - 1] + 1

    if maiorIdade[nota[i] - 1] < idade[i]: maiorIdade[nota[i] - 1] = idade[i]

porcentual[0] = float(notaCount[4]) / records * 100
porcentual[1] = float(notaCount[3]) / records * 100
porcentual[2] = float(notaCount[2]) / records * 100
porcentual[3] = float(notaCount[1]) / records * 100
porcentual[4] = float(notaCount[0]) / records * 100

diferenca = abs(porcentual[1] / 100 * records - porcentual[2] / 100 * records) / records * 100
print(f"Notas A ({notaCount[4]}/{records}) : {porcentual[0]}%")
print(f"Diferença porcentual entre respostas boas ({notaCount[3]}/{records}) e respostas regulares ({notaCount[2]}/{records}) : {diferenca}%")
print(f"Respostas péssimas ({notaCount[0]}/{records}) : {porcentual[4]}%")
print(f"Maior idade de resposta péssima : {maiorIdade[0]}")
print(f"A diferença de idade entre a maior idade que respondeu Otimo ({maiorIdade[4]}) e a maior idade que respondeu Ruim ({maiorIdade[1]}) : {abs(maiorIdade[4] - maiorIdade[1])}")