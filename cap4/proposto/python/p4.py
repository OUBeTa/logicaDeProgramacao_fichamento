def fixDecimal(value, digits): return "%.*f" % (digits, value)

records:int = 50
vLido:list = [0] * (records)
porcentagem:list = [0] * (records)
below:int = 0
above:int = 0
media:float = 0.0


for i in range(0, records, 1):
    porcentagem[i] = 0
    vLido[i] = float(input("Entrar com nota n°{i+1}"))
    media = media + vLido[i]

media = media / records

for i in range(0, records, 1):
    if vLido[i] == media: print(f"Nota n°{i + 1}) (vLido[i]) na média (media)")
    else: porcentagem[i] = abs(((vLido[i] - media) / records) * 100)

    if vLido[i] < media:
        print(f"Nota n°{i + 1} ({vLido[i]}) : {fixDecimal(porcentagem[i],2)}% abaixo da média ({media})")
        below = below + 1

    if vLido[i] > media:
        print(f"Nota n°{i + 1} ({vLido[i]}) : {fixDecimal(porcentagem[i],2)}% abaixo da média ({media})")
        above = above + 1

print(f"Alunos pelo menos 10% acima da média : {above}")
print(f"Alunos pelo menos 10% abaixo da média : {below}")

