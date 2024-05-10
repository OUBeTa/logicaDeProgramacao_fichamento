p:float = float(input("Insira o valor do produto\n"))
cod:int = int(input("Insira a condição de pagamento\n"))

if cod == 1:
    np = p * 0.9
    print(f"Preço à vista com desconto : {np}")
else:
    if cod == 2:
        np = p * 0.95
        print(f"Preço no cartão com desconto : {np}")
    else:
        if cod == 3:
            np = p / 2
            print(f"Duas parcelas de : {np}")
        else:
            if cod == 4:
                np = p * 1.1 / 3
                print(f"Três parcelas de : {np}")
            else: print("Código inexistente")
