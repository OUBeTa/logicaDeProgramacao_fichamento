a:int = int(input("Entre com A"))
b:int = int(input("Entre com B"))
c:int = int(input("Entrar com c"))

print(f"Lista original: [{a}, {b}, {c}]")

if a < c and b < c: print(f"Lista ordenada: [{a}, {b}, {c}]")
if a < c and c < b: print(f"Lista ordenada: [{a}, {c}, {b}]")
if b < a and a < c: print(f"Lista ordenada: [{b}, {a}, {c}]")
if b < c and c < a: print(f"Lista ordenada: [{b}, {c}, {a}]")
if c < a and a < b: print(f"Lista ordenada: [{c}, {a}, {b}]")
if c < b and b < a: print(f"Lista ordenada: [{c}, {b}, {a}]")
