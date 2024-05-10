records:int = 4
matrix:list = [([0] * records) for i in range(records)]
somaA:int
somaB:int
opt1:int
opt2:int
origem:int
destino:int

for i in range(0, records):
    for j in range(0, records): matrix[i][j] = int(input(f"Entrar com valor para [{i}][{j}]\n"))

opt1 = int(input("Entrar com parada n1\n"))
opt2 = int(input("Entrar com parada n2\n"))
origem = int(input("Entrar com localidade inicial\n"))
destino = int(input("entrar com destino final\n"))


somaA = matrix[origem][opt1] + matrix[opt1][destino]
somaB = matrix[origem][opt2] + matrix[opt2][destino]

if somaA > somaB: print(f"Melhor opção : {origem} , {opt1} , {destino}")
else: print(f"Melhor opção : {origem} , {opt2} , {destino}") if somaA < somaB else print("As duas opçoes consomem o mesmo tempo")

for i in range(0,records): print(matrix[i])
