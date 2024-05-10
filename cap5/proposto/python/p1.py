records:int = 5
arquivo1:list = [""] * (3 * records)
arquivo2:list = ["-"] * (6 * records)
arquivoMerge:list

index:int = 0
indexA:int = 0
indexB:int = 0
count:int = 0

i:int

print("//====== INICIANDO REGISTRO EM ARQUIVOS ======//")

for i in range(0, records):
    arq = int(input(f"Registrar em arquivo (1 - 2): "))
    while not (arq < 3 and arq > 0):
        arq = int(input(f"Arquivo [{arq}] inválido. Tente novamente"))
    
    if arq == 1:
        arquivo1[indexA * 3] = input(f"Entrar com nome [indivíduo n{i + 1}]")
        arquivo1[indexA * 3 + 1] = input(f"Entrar com endereço [indivíduo n{i + 1}]")
        arquivo1[indexA * 3 + 2] = input(f"Entrar com telefone [indivíduo n{i + 1}]")
        indexA += 1

    else:
        arquivo2[indexB * 6] = input(f"Entrar com nome [indivíduo n{i + 1}]")
        arquivo2[indexB * 6 + 1] = input(f"Entrar com endereço [indivíduo n{i + 1}]")
        arquivo2[indexB * 6 + 2] = input(f"Entrar com cidade [indivíduo n{i + 1}]")
        arquivo2[indexB * 6 + 3] = input(f"Entrar com bairro [indivíduo n{i + 1}]")
        arquivo2[indexB * 6 + 4] = input(f"Entrar com CEP [indivíduo n{i + 1}]")
        arquivo2[indexB * 6 + 5] = input(f"Entrar com data de nascimento [indivíduo n{i + 1}]")
        indexB += 1

print("//====== FIM REGISTRO EM ARQUIVOS ======//\n")
print("//====== COMEÇO EXPEDIÇÂO  ======//")

for i in range(0, records):
    count += 1 if arquivo1[i * 3] == arquivo2[i * 6] and arquivo1[i * 3 + 1] == arquivo2[i * 6 + 1] else 0

if count > 0:

    arquivoMerge = [""] * (7 * count)

    for i in range(0, records):
        if arquivo1[i * 3] == arquivo2[i * 6] and arquivo1[i * 3 + 1] == arquivo2[i * 6 + 1]:
            arquivoMerge[index * 7] = arquivo1[i * 3]
            arquivoMerge[index * 7 + 1] = arquivo1[i * 3 + 1]
            arquivoMerge[index * 7 + 2] = arquivo1[i * 3 + 2]
            arquivoMerge[index * 7 + 3] = arquivo2[i * 6 + 2]
            arquivoMerge[index * 7 + 4] = arquivo2[i * 6 + 3]
            arquivoMerge[index * 7 + 5] = arquivo2[i * 6 + 4]
            arquivoMerge[index * 7 + 6] = arquivo2[i * 6 + 5]
            index += 1

    print("Registros correspondentes")
    
    for i in range(0, index):
        print("//===============//")
        print(f"[Registro] : {i + 1}")
        print(f"[Nome] : {arquivoMerge[i * 7]}")
        print(f"[Endereço] : {arquivoMerge[i * 7 + 1]}")
        print(f"[Telefone] : {arquivoMerge[i * 7 + 2]}")
        print(f"[Cidade] : {arquivoMerge[i * 7 + 3]}")
        print(f"[Bairro] : {arquivoMerge[i * 7 + 4]}")
        print(f"[Cep] : {arquivoMerge[i * 7 + 5]}")
        print(f"[Nascimento] : {arquivoMerge[i * 7 + 6]}")
else: print("Nenhum registro correspondente")

print("//====== FIM EXPEDIÇÂO  ======//")