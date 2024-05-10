base:int = int(input("Entre com base"))
result:int = base
exp:int = int(input("Entre com expoente"))

i:int

for i in range(1, exp, 1): result *= result

print(f"{base} ^ {exp} = {result}")