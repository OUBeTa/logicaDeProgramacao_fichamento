records:int = 5
vMat:list = [0] * (records)
vCurso:list = [0] * (records)
vName:list = [""] * (records)
vSexo:list = [""] * (records)
cursos:list = ["farmácia","ciência da computação","cinema","Artes visuais","Segurança da informação","engenharia civil"]

search:str = "0"
i:int

for i in range(0, records):
    vName[i] = input(f"Entre com nome do aluno n{i + 1}")
    vSexo[i] = input(f"Entre com sexo do aluno n{i + 1}")
    vMat[i] = int(input(f"Entre número da matrícula do aluno n{i + 1}"))
    vCurso[i] = int(input(f"Entre com o código do curso do aluno n{i + 1} (1 - 6)"))

print("//======= Começando expedição =======//")
print("")

for i in range(0, records):
    if vSexo[i].lower() == "m":
        print(f"[nome] : {vName[i]}")
        print(f"[sexo] : {vSexo[i]}")
        print(f"[curso] : {cursos[vCurso[i] - 1]}")
        print(f"[Número de matrícula] : {vMat[i]}")
        print("")
print("//======= Fim expedição =======//")
