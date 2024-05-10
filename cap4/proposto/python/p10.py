records:int = 5
matrix = [([0] * records) for i in range(records)]
sRow = [0] * (records)
sColl = [0] * (records)

sOdd = 0
for i in range(0, records, 1):
    for j in range(0, records, 1):
        print("Entrar com [" + str(i) + "][" + str(j) + "]")
        matrix[i][j] = int(input())
for i in range(0,records,1): print(matrix[i])

for i in range(0, records, 1):
    for j in range(0, records, 1):
        sColl[i] += matrix[j][i]
        if matrix[i][j] % 2 == 1: sOdd += matrix[i][j]

        sRow[i] += matrix[i][j]

for i in range(0, records, 1): print(f"Soma da coluna n° {i + 1} : {sColl[i]}")
for i in range(0, records, 1): print(f"Soma da linha n° {i + 1} : {sRow[i]}")

print("Soma de todos os números ímpares : " + str(sOdd))
