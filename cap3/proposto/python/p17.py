termA:int = int(input("Entre com primeiro termo"))
termB:int = int(input("Entre com segundo termo"))
aux:int = 0

print(f"termo 1 : {termA}")
print(f"termo 2 : {termB}")

for i in range(3, 20 + 1, 1):
    aux = termA + termB
    termA = termB
    termB = aux

    print(f"termo {i} : {aux}")
