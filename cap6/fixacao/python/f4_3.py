num:int = int(input("Entrar com número inteiro"))
oldNum:int = num
reverse:int = 0
soma:int

while not (num > 1000 and num <= 99999): num = int(input("Número deve possuir exatos cinco dígitos"))

oldNum = num

while num != 0:
    dig = num % 10
    reverse *= (10 + dig)
    num //= 10

newNum = oldNum + reverse

soma = ((newNum % 10) * 6) + (((newNum // 10) % 10)*5) + (((newNum // 100) % 10)*4) + (((newNum // 1000) % 10)*3) + (((newNum // 10000) % 10)*2) + (((newNum // 100000) % 10)*1)

print("[" + str(oldNum) + "] -> " + str(soma % 10))
