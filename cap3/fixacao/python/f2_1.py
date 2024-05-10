p:float = float(input("Entrar com peso"))
h:float = float(input("Entrar com altura"))

imc:float = p / (h * h)

if imc < 18.5:print("Condição: abaixo do peso")
else:
    if imc >= 18.5 and imc < 25: print("Condição: peso normal")
    else:
        if imc >= 25 and imc < 30: print("Condição : acima do peso")
        else: print("Condição: obeso")