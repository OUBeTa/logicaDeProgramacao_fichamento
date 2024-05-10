num = int(input("Entrar com número inteiro de três dígitos\n"))

while not(100 <= num <= 999): print("Por favor, entre com um número inteiro de três dígitos.\n")

unidade:int = num % 10
dezena:int = (num // 10) % 10
centena:int = num // 100

print(f"Unidades: {unidade}")
print(f"Dezenas: {dezena}")
print(f"Centenas: {centena}")
print(f"Reverso do número: {unidade}{dezena}{centena}")