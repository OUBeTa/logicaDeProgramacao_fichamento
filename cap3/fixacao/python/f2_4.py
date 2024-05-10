s:str = input("Defina o sexo do indivíduo (M/F)")
h:float = float(input("Defina a altura do indivíduo"))

p:float = (72.7 * h - 58) if s == "M" or s == "m" else (62.1 * h - 44.7)

print(f"O peso recomendado para um indivíduo deste sexo é: {p}")
