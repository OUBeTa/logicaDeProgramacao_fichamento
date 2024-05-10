valorInicial:float = float(input("entrar com valor da prestação\n"))
acrs:float = valorInicial + (valorInicial * 0.1)
valorFinal:float = acrs - (acrs * 0.1)
prejuizo = abs(valorInicial - valorFinal)

print(f"{valorInicial}/{acrs}/{valorFinal}/{prejuizo}")
print(f"valor com desconto de 10% sob acréscimo de 10%: R$ {valorFinal}")
print(f"prejuizo do comerciante : R$ {prejuizo}")
