def fixDecimal(value, digits): return "%.*f" % (digits, value)

records:int = 10
sexo:list = [""] * (records)
olho:list = [""] * (records)
cabelo:list = [""] * (records)
idade:list = [0] * (records)
mCountA:int = 0
fCountA:int = 0
mCountB:int = 0
fCountB:int = 0

maiorIdade:int
i:int

for i in range(0, records - 1 + 1, 1):
    print("Entrar com sexo do indivíduo " + str(i + 1) + " (m/f)")
    sexo[i] = input()
    print("Entrar com cor dos olhos de indivíduo " + str(i + 1) + " (c - > castanho / v -> verde / a -> azul)")
    olho[i] = input()
    print("Entrar com cor do cabelo do indivíduo " + str(i + 1) + " (l -> loiro / c -> castanho / p -> preto)")
    cabelo[i] = input()
    print("Entrar com idade do indivíduo " + str(i + 1))
    idade[i] = int(input())

maiorIdade = idade[0]

for i in range(0, records - 1, 1):
    if idade[i + 1] > maiorIdade: maiorIdade = idade[i + 1]

for i in range(0, records - 1 + 1, 1):
    if sexo[i] == "m":
        mCountA = mCountA + 1
        if idade[i] >= 18 and idade[i] <= 35: mCountB = mCountB + 1
    else:
        fCountA = fCountA + 1
        if idade[i] >= 18 and idade[i] <= 35 and olho[i] == "v" and cabelo[i] == "l": fCountB = fCountB + 1

print(f"Maior idade entre os habitantes : {maiorIdade}")
print(f"Porcentagem entre os indivíduos do sexo masculino, cuja idade está entre 18 e 35 anos ({mCountB}/{mCountA}) : {fixDecimal((mCountB / mCountA) * 100,2)}%")
print(f"Porcentagem do total de indivíduos do sexo feminino entre 18 e 35 anos, e que tenham olhos verdes e cabelos loiros ({fCountB}/{fCountA}) : {fixDecimal((fCountB/(mCountA + fCountA)) * 100,2)}")
