a:int = int(input("Entrar com primeiro número"))
b:int = int(input("entrar com segundo número"))

soma:int = 0
div:int = 0

while soma + b <= a:
    soma = soma + b
    div = div + 1
    
print(div)
