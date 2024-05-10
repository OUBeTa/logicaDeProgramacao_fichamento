a:int = int(input("Entrar com primeiro número inteiro"))
a:int = abs(a)
ac:int = a

b:int = int(input("Entrar com segundo número inteiro"))
b:int = abs(b)
bc:int = b

print(f"O MMC entre {a} e {b} é : ")

while b != 0:
    r = a % b
    a = b
    b = r
    
print((ac * bc) / a)
