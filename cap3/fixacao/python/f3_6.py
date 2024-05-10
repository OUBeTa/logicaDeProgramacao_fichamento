a:int = 1
b:int = 1
c:int

print("Fibonacci n 1 : 1")
print("Fibonacci n 2 : 1")

for v in range(3, 20 + 1, 1):
    c = a + b
    print(f"Fibonacci n {v} : {c}")
    a = b
    b = c
