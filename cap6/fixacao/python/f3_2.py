records:int = 2
arq:list = [""] * (records * 5)

for i in range(0, records):
    arq[i * 5] = input(f"Entre com número de identidade [{i + 1}]")
    arq[i * 5 + 1] = input(f"Entre com nome [{i + 1}]")
    arq[i * 5 + 2] = input(f"Entre com altura [{i + 1}]")
    arq[i * 5 + 3] = input(f"Entre com sexo (m/f)[{i + 1}]")
    arq[i * 5 + 4] = input(f"Entre com idade [{i + 1}]")

print("\n//====== COMEÇO EXPEDIÇÂO =======//\n")

searchA = int(input(f"Escolha um registro (1 - {records}) : "))

if not (searchA <= records and searchA >= 0):
    while not (searchA <= records and searchA > 0): searchA = int(input(f"Entrada [{i + 1}] inválida, tente novamente."))

searchB = int(input(f"Escolha um segundo registro (1 - {records}) : "))
if not (searchB <= records and searchB >= 0):
    while not (searchB <= records and searchB > 0): searchB = int(input(f"Entrada [{i + 1}] inválida, tente novamente."))

print("")

while searchA != 0 and searchB != 0:
    if arq[(searchA - 1) * 5] == arq[(searchB - 1) * 5]: print(f"[Número de identidade] : {arq[(searchA - 1) * 5]} == {arq[(searchB - 1) * 5]}")
    if arq[(searchA - 1) * 5 + 1] == arq[(searchB - 1) * 5 + 1]: print(f"[Nome] : {arq[(searchA - 1) * 5 + 1]} == {arq[(searchB - 1) * 5 + 1]}")
    if arq[(searchA - 1) * 5 + 2] == arq[(searchB - 1) * 5 + 2]: print(f"[Altura] : {arq[(searchA - 1) * 5 + 2]} == {arq[(searchB - 1) * 5 + 2]}")
    if arq[(searchA - 1) * 5 + 3] == arq[(searchB - 1) * 5 + 3]: print(f"[Sexo] : {arq[(searchA - 1) * 5 + 3]} == {arq[(searchB - 1) * 5 + 3]}")
    if arq[(searchA - 1) * 5 + 4] == arq[(searchB - 1) * 5 + 4]: print(f"[Idade] : {arq[(searchA - 1) * 5 + 4]} == {arq[(searchB - 1) * 5 + 4]}")

    print("")

    searchA = int(input(f"Escolha um registro (1 - {records}) : "))

    if not (searchA <= records and searchA >= 0):
        while not (searchA <= records and searchA > 0): searchA = int(input(f"Entrada [{i + 1}] inválida, tente novamente."))

    searchB = int(input(f"Escolha um segundo registro (1 - {records}) : "))

    if not (searchB <= records and searchB >= 0):
        while not (searchB <= records and searchB > 0): searchB = int(input(f"Entrada [{i + 1}] inválida, tente novamente."))

print("\n\n//====== FIM EXPEDIÇÂO ======//")
