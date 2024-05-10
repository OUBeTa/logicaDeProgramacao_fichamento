records:int = 2
soma:int = 0
arquivoStr:list = [""] * (records * 3)
arquivoInt:list = [0] * (records * 3)

print("//====== INICIANDO REGISTRO EM ARQUIVOS ======//\n\n")

for i in range(0, records):
    arquivoStr[i * 3] = input(f"Entrar com nome do sócio [{i + 1}]")
    arquivoInt[i * 3] = int(input(f"Entrar com n° do sócio [{i + 1}]"))
    arquivoInt[i * 3 + 1] = int(input(f"Entrar com número de dependentes do sócio [{i + 1}]"))
    arquivoStr[i * 3 + 1] = input(f"Entrar com endereço do sócio [{i + 1}]")
    arquivoStr[i * 3 + 2] = input(f"Entrar com data de associação do sócio [{i + 1}]")
    arquivoInt[i * 3 + 2] = int(input(f"Entrar com valor da mensalidade do sócio [{i + 1}]\n\n"))

print("//====== FIM REGISTRO EM ARQUIVOS ======//\n\n")

for i in range(0, records): soma += (1 + arquivoInt[i * 3 + 1])

print(f"Número total de possíveis frequentadores do clube : {soma}")

