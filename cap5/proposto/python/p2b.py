records:int = 2
arquivoStr:list = [""] * (records * 2)
arquivoInt:int = [0] * (records * 4)
meses:list = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

print("//====== INICIANDO REGISTRO EM ARQUIVOS ======//\n\n")
for i in range(0, records):
    arquivoStr[i * 2] = input(f"Entrar com nome do sócio [{i + 1}]")
    arquivoInt[i * 4] = int(input(f"Entrar com n° do sócio [{i + 1}]"))
    arquivoStr[i * 2 + 1] = input(f"Entrar com endereço do sócio [{i + 1}]")
    arquivoInt[i * 4 + 1] = int(input(f"Entrar com data de nascimento do sócio (ano) [{i + 1}]"))
    arquivoInt[i * 4 + 2] = int(input(f"Entrar com data de nascimento do sócio (mês [1-12]) [{i + 1}]"))

    while not (arquivoInt[i * 4 + 2] < 13 and arquivoInt[i * 4 + 2] > 0):
        arquivoInt[i * 4 + 2] = int(input(f"Mês [{arquivoInt[i * 4 + 2]}] inválido. Tente novamente (1-12)"))

    if arquivoInt[i * 4 + 2] in [1, 3, 5, 7, 8, 10, 12]:diasMes = 31
    elif arquivoInt[i * 4 + 2] == 2:

        if (arquivoInt[i * 4 + 1] % 4 == 0 and arquivoInt[i * 4 + 1] % 100 != 0) or arquivoInt[i * 4 + 1] % 400 == 0: diasMes = 29
        else: diasMes = 28

    else: diasMes = 30

    arquivoInt[i * 4 + 3] = int(input(f"Entrar com data de nascimento do sócio (dia [1-{diasMes}]) [{i + 1}]"))

    while not (arquivoInt[i * 4 + 3] <= diasMes and arquivoInt[i * 4 + 3] > 0): arquivoInt[i * 4 + 3] = int(input(f"Dia [{arquivoInt[i * 4 + 3]}] inválido. Tente novamente (1-{diasMes})"))

    print("\n")

print("//====== FIM REGISTRO EM ARQUIVOS ======//\n\n")

for i in range(0, records): meses[arquivoInt[i * 4 + 2] * 2 + 1] += "+"

for i in range(0, 12): print(f"Sócios nascidos em [{meses[i * 2]}] : {len(meses[i * 2 + 1])}")