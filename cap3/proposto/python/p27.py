result:int = 0
denominador:int = 500
i:int

for i in range(2, 12, 1):

	result = (result + 2 / denominador) if i % 2 == 0 else (result - 5 / denominador)

    denominador = denominador - 50

print("S = 2/500 - 5/450 + 2/400 - 5/350 + ...")
print(f"S = {result}")
