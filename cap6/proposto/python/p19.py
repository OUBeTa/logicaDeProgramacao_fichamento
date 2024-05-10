def inCode(num):
    oldNum = num
    reverse = 0
    while num != 0:
        dig = num % 10
        reverse *= (10 + dig)
        num = (num // 10)
    newNum = oldNum + reverse
    soma = (newNum % 10) * 6 + ((newNum // 10) % 10) * 5 + ((newNum // 100) % 10) * 4 + ((newNum // 1000) % 10) * 3 + ((newNum // 10000) % 10) * 2 + (newNum // 100000) % 10
    soma = soma % 10
    
    return soma

def func_print(arqStr, arqFlt):
    records = int(len(arqStr) / 2)
    for i in range(0, records):
        print(f"[Nome] -> {arqStr[i * 2]}")
        print(f"[Agência] -> {arqStr[i * 2 + 1]}")
        print(f"[Número do cheque] -> {arqFlt[i * 4]}")
        print(f"[Número da conta corrente] -> {arqFlt[i * 4 + 1]}")
        print(f"[Valor do cheque] -> {arqFlt[i * 4 + 2]}")
        print(f"[Dígito verificador] -> {arqFlt[i * 4 + 3]}")
        print("")

def sumCheq(accountNum, arqFlt):
    soma = 0
    for i in range(0, len(arqFlt), 4): soma += arqFlt[i + 2] if arqFlt[i + 1] == accountNum else 0
    return soma

records:int = 5
arqStr:list = [""] * (records * 2)
arqFlt:list = [0] * (records * 4)

print("//====== INÍCIO REGISTROS ======//\n")

for i in range(0, records):
    arqStr[i * 2] = input(f"Entrar com nome [{i + 1}]")
    arqStr[i * 2 + 1] = input(f"Entrar com agência [{i + 1}]")
    arqFlt[i * 4] = float(input(f"Entrar com número do cheque [{i + 1}]"))
    arqFlt[i * 4 + 1] = float(input(f"Entrar com número da conta corrente [{i + 1}]"))

    while not (10000 <= arqFlt[i * 4 + 1] <= 99999): arqFlt[i * 4 + 1] = float(input("O número da conta corrente deve ter exatamente cinco dígitos. Tente novamente"))

    arqFlt[i * 4 + 2] = float(input(f"Entrar com valor do cheque [{i + 1}]"))
    arqFlt[i * 4 + 3] = inCode(arqFlt[i * 4 + 1])

print("")
func_print(arqStr, arqFlt)
print("")

account = None
while account != 0:
    account = int(input("Entre com número de conta para exibir valor total dos cheques"))
    print(f"[Valor total dos cheques ({account})] -> {sumCheq(account, arqFlt)}")
