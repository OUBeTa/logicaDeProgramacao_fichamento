def factorial(num):
    if not num <= 1:
        i = num * factorial(num - 1)
    else:
        i = 1    
    return i

a:int = int(input("Entre com número total de elementos"))
b:int = int(input("Entra com quantia selecionada de elementos"))

print(f"Número de combinações possíveis entre [{b}] de [{a}] elementos : {factorial(a) // (factorial(b) * factorial(a - b))}")
