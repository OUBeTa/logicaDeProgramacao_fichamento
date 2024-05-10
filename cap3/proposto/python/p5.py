meses:list = [31,28,31,30,31,30,31,31,30,31,30,31]

d1 = int(input("Entrar com dia de nascimento (1-31)\n"))
d2 = int(input("Entrar com dia atual\n"))
m1 = int(input("Entrar com mês de nascimento (1-12)\n"))
m2 = int(input("Entrar com mês mês atual (1-12)\n"))
y1 = int(input("Entre com ano de nascimento\n"))
y2 = int(input("Entre com ano de nascimento\n"))

dd = 0
md = 0

yd = abs(y1 - y2)
if m2 < m1 or m2 == m1 and d2 < d1:
    yd = yd - 1
    m2 = m2 + 12
if d2 < d1:
    m2 = m2 - 1
    if m2 < 0:
        m2 = m2 + 12
        yd = yd - 1
    if y2 % 4 == 0 and (y2 % 100 != 0 or y2 % 400 == 0): meses[1] = 29

    d2 = d2 + meses[m2 - 1]

dd = abs(d2 - d1)
md = abs(m2 - m1)

print(f"anos : {yd}")
print(f"Meses : {md}")
print(f"Dias : {dd}")
