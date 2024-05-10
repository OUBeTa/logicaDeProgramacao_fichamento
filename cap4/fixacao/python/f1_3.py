records:int = 10
vResultado:list = [0] * (records)
v1:list = [0] * (records)
v2:list = [0] * (records)

mid:int = records / 2
left:int = mid - 1
right:int = mid

for i in range(0, records, 1):
    v1[i] = int(input(f"Entre com v1[{i + 1}]\n"))
    v2[i] = int(input(f"Entre com v2[{i + 1}]\n"))

for i in range(0, records, 1): vResultado[i] = 0

for i in range(0, records, 1):
    if v2[i] != 0:
        if i % 2 == 0:
            vResultado[right] = v1[i] * (1 / v2[i])
            right = right + 1
        else:
            vResultado[left] = v1[i] * (1 / v2[i])
            left = left - 1

for i in range(0, records, 1): print(f"n {i + 1} : {vResultado[i]}")
