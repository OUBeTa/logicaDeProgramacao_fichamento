def fixDecimal(value, digits): return "%.*f" % (digits, value)

votos:list = [0] * (6)
porcentual:list = [0] * (6)
i:int

for i in range(0, 4, 1): votos[i] = int(input(f"Entrar com número de votos para o candidato número {i + 1}"))

votos[4] = int(input("entrar com quantia de votos nulos"))
votos[5] = int(input("entrar com quantia de votos em branco"))

soma = sum(votos)

for i in range(0, 6, 1): porcentual[i] = float(votos[i]) / soma * 100

print(f"votos para o primeiro candidato ({votos[0]}/{soma}) : {fixDecimal(porcentual[0],2)}%")
print(f"votos para o segundo candidato ({votos[1]}/{soma}) : {fixDecimal(porcentual[1],2)}%")
print(f"votos para o terceiro candidato ({votos[2]}/{soma}) : {fixDecimal(porcentual[2],2)}%")
print(f"votos para o quarto candidato ({votos[3]}/{soma}) : {fixDecimal(porcentual[3],2)}%")
print(f"votos para o nulos candidato ({votos[4]}/{soma}) : {fixDecimal(porcentual[4],2)}%")
print(f"votos para o branco candidato ({votos[5]}/{soma}) : {fixDecimal(porcentual[5],2)}%")

