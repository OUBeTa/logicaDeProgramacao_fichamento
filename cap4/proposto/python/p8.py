def getNumberId(v):
    result = 0
    for i in range(0, len(v) - 1, 1):
        if v[result] < v[i + 1]: result = i + 1
    
    return result

records:int = 200
vNota:list = [0] * (records)
vNome:list = [""] * (records)
i:int

for i in range(0, records, 1):
    vNome[i] = input(f"Entre com nome de aluno n°{i+1}")
    vNota[i] = int(input(f"Entre com nota de aluno n°{i+1}"))

for i in range(0, records, 1):
    if vNota[getNumberId(vNota)] > 70:
        print(f"n°{i + 1} : {vNome[getNumberId(vNota)]} | {vNota[getNumberId(vNota)]}Pts")
        vNota[getNumberId(vNota)] = 0
