records:int = 20
nNotas:int = 2
maxIntegrantes:int = 5
maxEquipes:int = 4
vNotas:list = [0] * (records * nNotas)
meEquipes:list = [0] * (maxEquipes)
notaEquipes:list = [0] * (maxIntegrantes * maxEquipes)
vName:list = [""] * (records)
medias:list = [0] * (records)
integrantes:list = [0] * (maxIntegrantes)

for i in range(0, records, 1):
    vName[i] = input(f"Entrar com nome do aluno n{i + 1}")
    group = int(input(f"Entrar com número do grupo em que o aluno n{i + 1} está (1 - {maxEquipes})"))

    if not group <= maxEquipes:
        while not group <= maxEquipes:
            group = int(input(f"Não existe grupo n{i}. tente outro grupo (1 - {maxEquipes})"))
            if group < maxEquipes:
                while not integrantes[group - 1] < maxIntegrantes:
                    if not(group > maxEquipes): group = int(input(f"O grupo {group} está cheio. Entre com outro grupo (1 - 8 != [{group}])"))
    else:
        while not integrantes[group - 1] < maxIntegrantes:
            if not(group > maxEquipes): group = int(input(f"O grupo {group} está cheio. Entre com outro grupo (1 - 8 != [{group}])"))

    for j in range(0, nNotas, 1):
        vNotas[i * nNotas + j] = float(input(f"Entrar com nota n{j + 1} do aluno n{i + 1}"))
        medias[i] += vNotas[i * nNotas + j]

    medias[i] /= nNotas
    notaEquipes[(group - 1) * maxIntegrantes + integrantes[group - 1]] = medias[i]
    integrantes[group - 1] = integrantes[group - 1] + 1
    
for i in range(0, maxEquipes, 1):
    for j in range(0, maxIntegrantes, 1): meEquipes[i] = i * nNotas + j

    meEquipes[i] = meEquipes[i] / maxIntegrantes
    print(f"Média da equipe n{i + 1} : {meEquipes[i]}")