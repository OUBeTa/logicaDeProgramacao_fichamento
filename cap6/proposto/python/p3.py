count:int = 0
a:int = int(input("Entrar com divisor"))
b:int = int(input("Entrar com dividendo"))

while a >= b:
    a -= b
    count += 1

print(f"Divisão inteira : {count}")