for con in range(1, 21, 1):
    n = int(input(f"Entrar com n°{con}\n"))
    if con == 1:
        ma = n
        me = n
    if n > ma: ma = n
    else:
        if n < me: me = n

print(f"Maior número : {a}")
print(f"Menor número : {e}")
