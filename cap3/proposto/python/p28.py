result:int = 0
i:int

for i in range(1, 11, 1): result = (result - 1 / (i * 2 - 1) ** 3) if i % 2 == 0 else (result + 1 / (i * 2 - 1) ** 3)

print("H = 1/pot(1,3) - 1/pot(3,3) + 1/pot(5,3) - 1/pot(7,3) + 1/pot(9,3) - ...")
print("H = " + str(result))
