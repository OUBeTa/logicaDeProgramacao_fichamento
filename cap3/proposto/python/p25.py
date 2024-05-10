result:int = 0
i:int

for i in range(1, 51, 1): result = result + (2 * i - 1) / i

print("H = 1/1 + 3/2 + 5/3 + 7/4 ... + 99/50")
print(f"H = {result}")
