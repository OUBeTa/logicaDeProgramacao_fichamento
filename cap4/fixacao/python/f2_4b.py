records:int = 4
matrix:list = [([0] * records) for i in range(records)]
soma:int = 0

i = int(input("Entrar com localidade inicial\n"))
j:int

while i != 0:
    j = int(input("Entrar com proxima localidade\n"))

    if i != j and j != 0: soma = soma + matrix[i][j]

    i = j
    print(f"Distância do percurso atualmente : {soma}")

print(f"distância total : {soma}")
