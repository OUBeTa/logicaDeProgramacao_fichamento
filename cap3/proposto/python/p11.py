records = 3
paises = [""] * records

mO:list = [0] * records
mP:list = [0] * records
mB:list = [0] * records

for i in range(0, records, 1):
    paises[i] = input("Entrar com país número " + str(i + 1))
    mO[i]:int = int(input(f"Medalhas de ouro do país : | {paises[i]}  |"))
    mP[i]:int = int(input(f"Medalhas de Prata do país : | {paises[i]}  |"))
    mB[i]:int = int(input(f"Medalhas de bronze do país : | {paises[i]}  |"))

for i in range(0, records, 1):
    print(f"País : {paises[i]}")
    print(f"ouro : {mO[i]}")
    print(f"prata : {mP[i]}")
    print(f"bronze : {mB[i]}")
    print(f"TOTAL | {paises[i]} | {mO[i] * 3 + mP[i] * 2 + mB[i]}")
