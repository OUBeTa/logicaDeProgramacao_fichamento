records:int = 5
arqStr:list = [""] * (2 * records)
arqInt:list = [0] * (records * 2)

print("//====== INICIO REGISTROS ======//\n\n")

for i in range(0, records):
    arqStr[i * 2] = input(f"Entre com nome do sócio [{i + 1}]")
    arqInt[i * 2] = int(input(f"Entre com número do sócio [{i + 1}]"))
    arqStr[i * 2 + 1] = input(f"Entre com data de nascimento do sócio [{i + 1}]")
    arqInt[i * 2 + 1] = int(input(f"Entre com número de dependentes do sócio [{i + 1}]"))
    print("")
    print("")

print("//====== FIM REGISTROS ======//\n\n")
j = int(input("Deseja alterar ou excluir um registro?(1 - 2)"))

while j != 0:
    while not (j < 3 and j > 0): j = int(input(f"Opção [{j}] inválida. Tente novamente (alterar -> 1 | excluir -> 2)"))

    if j == 1:
        print("")
        print("")
        ji = int(input("Qual campo você deseja atualizar\n[Nome] -> 1\n[Número do sócio] -> 2\n[Número de dependentes] -> 3"))

        while not (ji < 4 and ji > 0): ji = int(input(f"Opção [{ji}] inválida. Tente novamente (nome -> 1 | n° -> 2 | dependentes -> 3)"))

        print("")

        print("Qual registro você deseja alterar?")

        for i in range(0, records):
            if arqStr[i * 2 + 1] != "X": print(f"[{i + 1}] -> n°{arqInt[i * 2]}")

        j = int(input())

        if arqStr[j * 2 + 1] != "X":

            if not (j < records and j > 0):
                while not (j <= records and j > 0): j = int(input(f"Opção [{j}] inválida. Tente novamente (1 - {records})"))

            print("Entre com novo valor de campo")

            if ji == 1: arqStr[(j - 1) * 2] = input()
            else:
                if ji == 2: arqInt[(j - 1) * 2] = int(input())
                else: arqInt[(j - 1) * 2 + 1] = int(input())

            print("")
            print("Novo valor atribuído ao campo com sucesso!")

        else:

            print("Registro excluído!")
            print("Expedição interrompida")
    else:

        j = int(input("Insira o número do registro"))
        found = False
        for i in range(0, records):
            if arqInt[i * 2] == j:
                found = True
                index = i

        if found:

            print(f"Registro de n°{arqInt[index * 2]} foi encontrado com sucesso. Deseja excluir?")
            found = (input().lower() == 'true')
            if found:
                arqInt[index * 2] = 0
                arqInt[index * 2 + 1] = 0
                arqStr[index * 2] = "X"
                arqStr[index * 2 + 1] = "X"
            else:
                print("Expedição interrompida")
        else:
            print("Registro não encontrado!")
            print("Expedição interrompida")

    j = int(input("\n\nDeseja alterar ou excluir um registro?(1 - 2)"))

print("//====== FIM DA EXPEDIÇÃO ======//")
