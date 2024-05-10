c:int = 0
numOld:int

num = abs(int(input("Entrar com número\n")))
numOld = num

while num != 0:
    c = c + 1
    num //= 10

print(f"O dígito {numOld} possui {c} dígito{'' if c == 1 else 's'}")
