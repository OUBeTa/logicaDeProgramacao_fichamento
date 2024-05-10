records:int = 10
codigo:list = [""] * (records)
porte:list = [""] * (records)
funcionarios:list = [0] * (records)

gr:int = 0
me:int = 0
pe:int = 0
mi:int = 0

i:int

for i in range(0, records, 1):
    porte[i] = input(f"Entrar com porte da empresa número {i + 1} (grande[gr] média[me] pequena[pe] micro[mi])\n")
    codigo[i] = input(f"Entrar com código da empresa número {i+1}\n")
    funcionarios[i] = int(input(f"Entrar com número de funcionários da empresa número {i+1}\n"))

    if (porte[i] == "gr") and (funcionarios[i] > gr):
        grCode = codigo[i]
        gr = funcionarios[i]
    else:
        if (porte[i] == "me") and (funcionarios[i] > me):
            meCode = codigo[i]
            me = funcionarios[i]
        else:
            if (porte[i] == "pe") and (funcionarios[i] > pe):
                peCode = codigo[i]
                pe = funcionarios[i]
            else:
                if (porte[i] == "mi") and (funcionarios[i] > mi):
                    miCode = codigo[i]
                    mi = funcionarios[i]


print(f"maior empresa de grande porte : {grCode} x {gr}")
print(f"maior empresa de medio porte : {meCode} x {me}")
print(f"maior empresa de pequeno porte : {peCode} x {pe}")
print(f"maior empresa de micro porte : {miCode} x {mi}")
