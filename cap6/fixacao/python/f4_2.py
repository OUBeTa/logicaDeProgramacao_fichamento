num:int = int(input("Entrar com número inteiro"))
reverse:int = 0
sign:int


sign = -1 if num < 0 else 1
num = abs(num)

while num != 0:
    dig = num % 10
    reverse = reverse * 10 + dig
    num //= 10

print(reverse * sign)
