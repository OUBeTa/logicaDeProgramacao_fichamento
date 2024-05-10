ano:str = int(input("Insira o ano atual"))

a:int = int(input("Qual o ano de nascimento do indivíduo?"))
i:int = abs(ano - a)

if i >= 18: print("Você já pode prestar habilitação")
else: print("Você já pode fzer seu título de eleitor") if i >= 16 else print("Você ainda é menor de idade")
