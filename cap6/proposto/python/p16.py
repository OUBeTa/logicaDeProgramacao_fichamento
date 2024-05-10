def dp(a):
    soma = 0
    dp = 0
    for i in range(0, len(a), 1): soma += a[i]
    media = soma / len(a)

    for i in range(0, len(a), 1): dp += abs(a[i] - media) * abs(a[i] - media) / len(a)

    print(f"[Desvio padrão] -> {sqrt(abs(dp))}")

def media(a):
    count = 0
    soma = 0

    for i in range(0, len(a), 1):
        soma += a[i]
        count += 1

    print(f"[Media] -> {soma / count}")

def ngtv2zero(a):
    clone = [0] * (len(a))

    for i in range(0, len(a), 1): clone[i] = a[i] if a[i] > 0 else  0

    print(f"[n > 0 -> n == 0] : {clone}")

def func_print(a):
    for i in range(0, len(a), 1): print(f"[{i}] -> " + str(a[i]))

def soma(a):
    soma = 0
    for i in range(0, len(a), 1):
        soma += a[i]

    print(f"[Soma] -> {soma}")

records:int = 5
vLido:list = [0] * (records)
soma:int
i:int

for i in range(0, records, 1):
    print(f"Entrar com valor real para vLido[{i}]")
    vLido[i] = float(input())

print("\n\n//====== Valores ======//\n")
func_print(vLido)

print("\n//====== soma dos valores ======//\n")
soma(vLido)

print("\n//====== média entre dos valores ======//\n")
media(vLido)

print("\n//====== desvio padrão entre valores ======//\n")
dp(vLido)

print("\n//====== valores negativos zerados ======//\n")
ngtv2zero(vLido)