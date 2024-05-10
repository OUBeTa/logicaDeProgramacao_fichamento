idade:int = int(input("Entrar com idade"))
if idade <= 15: print("não votante")
else: print("voto obrigatório") if idade >= 16 and idade <= 65 else print("voto opcional")