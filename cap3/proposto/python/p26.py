result:int = 0
i:int

for i in range(1, 11, 1):
    term = i / (i * i)
    if i % 2 == 0: term = term * -1
    result = result + term
print("S = 1/ 1 - 2/4 + 3/9 - 4/ 16 + 5/25 - 6/36 ... - 10/ 100")
print("S = " + str(result))