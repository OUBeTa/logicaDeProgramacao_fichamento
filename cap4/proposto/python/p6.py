def orderList(v):
    isOrdered = False
    aux = 0
    while not isOrdered:
        isOrdered = True
        for i in range(0, len(v) - 1, 1):
            if v[i] > v[i + 1]:
                aux = v[i]
                v[i] = v[i + 1]
                v[i + 1] = aux
                isOrdered = False

records:int = 20
v1:list = [0] * (records)
v2:list = [0] * (records)

current:int = 0
result:str = ""

i:int

for i in range(0, records, 1): v1[i] = int(input(f"Entre com v1[{i}]"))
for i in range(0, records, 1): v2[i] = int(input(f"Entre com v2[{i}]"))

orderList(v1)
orderList(v2)

for i in range(0, records, 1):
    for j in range(0, records, 1):

        if v1[i] == v2[j] and v1[i] != current:
            if j == 0: result = result + "["
            if j < records - 1: result = result + str(v1[i]) + ","
            if j == records - 1: result = result + str(v1[i]) + "]"

            current = v1[i]

print(f"A -> {v1}\n")    
print(f"B -> {v2}\n")    
print(f"Repetidos : {result}")
