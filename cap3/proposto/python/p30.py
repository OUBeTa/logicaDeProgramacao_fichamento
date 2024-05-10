records:int = 1
cpf:int = [0] * (records)
dependentes:list = [0] * (records)
rendaB:list = [0] * (records)
imposto:list = [0] * (records)
rendaL:list = [0] * (records)
sm:int = int(input("Entre com salário mínimo"))

i:int

for i in range(0, records - 1 + 1, 1):
    cpf[i] = int(input(f"Entre com cpf do indivíduo número {i + 1}\n"))
    rendaB[i] = int(input("Entre com renda mensal, em reais, do indivíduo\n"))
    dependentes[i] = int(input("Entre com número de dependentes do induvíduo\n"))

for i in range(0, records, 1):
    rendaL[i] = (rendaB[i] - rendaB[i]) / 100 * (5 * dependentes[i])

    if (rendaL[i] // sm) <= 2 or rendaL[i] < sm: imposto[i] = 0
    else:
        if (rendaL[i] // sm) <= 3: imposto[i] = rendaL[i] * 0.05
        else:
            if (rendaL[i] // sm) <= 5: imposto[i] = rendaL[i] * 0.1
            else:
                if (rendaL[i] // sm) <= 7: imposto[i] = rendaL[i] * 0.15
                else: imposto[i] = rendaL[i] * 0.2

for i in range(0, records, 1):
    print(f"||==  INDIVÍDUO N{i+1} ==||")
    print(f"CPF : {cpf[i]}")
    print(f"Renda bruta : R${rendaB[i]}")
    print(f"Desconto por dependentes : {dependentes[i] * 5}% | R${rendaL[i]} |")
    print(f"Imposto de renda : {imposto[i]}\n\n")


