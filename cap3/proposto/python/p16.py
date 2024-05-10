base:int = int(input("Entrar com denominador"))
exp:int = int(input("entrar com expoente"))

result:int = base

for control in range(1, exp, 1): result = result * result

print(f"{base} ^ {exp} = {result}")