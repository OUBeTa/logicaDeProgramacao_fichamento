def fixDecimal(value, digits): return "%.*f" % (digits, value)

records:int = 4
vName:list = [""] * (records)
vCusto:list = [0] * (records)
vPreco:list = [0] * (records)
vPorcentagem:list = [0] * (records)

for i in range(0, records, 1):
    vName[i] = input("Entra com nome do produto n" + str(i + 1))
    vCusto[i] = float(input("Entra com custo do produto n" + str(i + 1)))
    vPreco[i] = float(input("Entrar com preço do procuto n" + str(i + 1)))
    vPorcentagem[i] = abs(((vCusto[i] - vPreco[i]) / vCusto[i]) * 100)

for i in range(0, records, 1):
    if vPreco[i] == vCusto[i]: print(f"[{vName[i]}] : (preço/custo) " + str(vCusto[i]) + "/" + str(vPreco[i]) + ") -> 0% de lucro")
    else: print(f"[{vName[i]}] : (preço/custo) ({vCusto[i]}/{vPreco[i]}) -> {fixDecimal(vPorcentagem[i],2)}% de {'prejuízo' if vPreco[i] < vCusto[i] else 'lucro'}")

print("\nLucro < 10%")
for i in range(0, records, 1): print(f"[{vName[i]}] : {vPorcentagem[i]})%") if vCusto[i] < vPreco[i] and vPorcentagem[i] < 10 else print("")

print("\nLucro > 10% < 30%")
for i in range(0, records, 1): print(f"[{vName[i]}] : {vPorcentagem[i]})%") if if vCusto[i] < vPreco[i] and (vPorcentagem[i] > 10 and vPorcentagem[i] < 30) else print("")

print("\nLucro > 30%")
for i in range(0, records, 1): print(f"[{vName[i]}] : {vPorcentagem[i]})%") if vCusto[i] < vPreco[i] and vPorcentagem[i] > 30 else print("")
