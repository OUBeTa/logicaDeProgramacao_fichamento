records:int = 5
vMat:list = [0] * (records)
vCurso:list = [""] * (records)
vName:list = [""] * (records)

search = "0"
i:int

for i in range(0, records):
    vName[i] = input(f"Entra com nome do aluno n{i + 1}")
    vMat[i] = int(input(f"Entra número da matrícula do aluno n{i + 1}"))
    vCurso[i] = input(f"Entra com curso do aluno n{i + 1}")

print("//======= Começando expedição =======//")
search = input("Entre com nome do curso em questão\n")
while search != "0":
    for i in range(0, records):
        if search == vCurso[i]:
            print(f"[nome] : {vName[i]}")
            print(f"[curso] : {vCurso[i]}")
            print(f"[Número de matrícula] : {vMat[i]}")
            print("")
    print("//======= Próxima busca =======//")
    search = input()
print("//======= fim expedição =======//")