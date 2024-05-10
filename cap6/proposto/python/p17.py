a:int = int(input("Entre com a quantia de termos fibonacci a serem exibidos"))
tAnterior:int
tAtual:int

if not a == 0:
    tAnterior = 1
    tAtual = 1

    print("f" + str(a) + " -> [", end='', flush=True)

    if a == 1: print("1", end='', flush=True)
    else:
        if a == 2: print("1,1", end='', flush=True)
        else:
            if a >= 2: print("1,1,", end='', flush=True)
    i = 2

    while i < a:
        pTermo = tAnterior + tAtual
        if i + 1 == a: print(pTermo, end='', flush=True)
        else: print(str(pTermo) + ",", end='', flush=True)

        tAnterior = tAtual
        tAtual = pTermo
        i +=  1
else:
    print("[", end='', flush=True)
print("]")

