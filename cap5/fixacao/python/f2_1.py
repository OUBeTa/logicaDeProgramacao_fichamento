records:int = 5
nNotas:int = 4
search:int = 1
mediaTotal:int = 0
vNotas:list = [0] * (records * 4)
vName:list = [""] * (records)
vNum:list = [0] * (records)
medias:list = [0] * (records)

i:int
j:int

for i in range(0, records, 1):
    vName[i] = input(f"Entrar com nome do aluno n°{i+1}")
    vNum[i] = int(input(f"Entrar com número do aluno n°{i+1}"))

    for j in range(0, nNotas, 1):
        vNotas[i * records + j] = float(input(f"Entrar com nota n°{j+1} do aluno {i+1}"))
        medias[i] += vNotas[i * records + j]

for i in range(0, records, 1): medias[i] /= nNotas

while search != 0:
    find = False
    print("Número do aluno em questão : ")
    search = int(input())
    for i in range(0, records, 1):
        if search == vNum[i]:
            find = True
            print(f"[Nome] : {vName[i]}")
            print(f"[Notas] : [{vNotas[i * records + 0]},{vNotas[i * records + 1]},{vNotas[i * records + 2]},{vNotas[i * records + 3]}]")
            print(f"[Média] : {medias[i]}")
            print(f"[status] : ", end='', flush=True)
            if medias[i] >= 7: print("Aprovado")
            else: print("Recuperação")if medias[i] < 7 and medias[i] >= 5 else print("Reprovado")
    print("//============//")
    if not find: print(f"Nenhum aluno referente ao número [{search}] foi encontrado")
print("Expedição encerrada")
