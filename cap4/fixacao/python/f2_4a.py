records:int = 4
i:int
matrix:list = [([0] * records) for i in range(records)]


for i in range(0, records):
    for j in range(0, records): matrix[i][j] = ((0) if i == j else (int(input(f"Entrar com valor para [{i}][{j}]\n"))))

li = int(input("Entre com localidade I\n"))
lj = int(input("Entre com localidade J\n"))

while li != lj:
    print(f"Distância entre a localidade : {matrix[li][lj]}")
    li = int(input("Entre com localidade I\n"))
    lj = int(input("Entre com localidade J\n"))

for i in range(0,records): print(matrix[i])