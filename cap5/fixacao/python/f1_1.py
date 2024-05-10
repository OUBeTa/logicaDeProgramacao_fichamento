records:int = 10
vName:int = [""] * (records)
vAutor:int = [""] * (records)
vAssunto:int = [""] * (records)
vDoado:int = [False] * (records)
vCode:int = [0] * (records)
vPag:int = [0] * (records)
i:int

for i in range(0, records, 1):
    vCode[i] = int(input(f"Entre com código do livro n°{i+1}"))
    vDoado[i] = (input(f"Entre com (Doado?) n°{i+1}"))
    vAssunto[i] = input(f"Entre com assunto do livro n°{i+1}")
    vAutor[i] = input(f"Entre com nome do autor de livro n°{i+1}")
    vName[i] = input(f"Entre com nome do livro n°{i+1}")
    vPag[i] = int(input(f"Entre com número de páginas de livro n°{i+1}"))

desire = input("Qual assunto você procura dentre os livros da biblioteca?")
print("Lista de livros deste assunto disponíveis")
print("//====================//")
for i in range(0, records - 1 + 1, 1):
    if vAssunto[i] == desire:
        print(f"[nome] : {vName[i]}")
        print(f"[Autor] : {vAutor[i]}")
        print(f"[Assunto] : {vAssunto[i]}")
        print(f"[n/Paginas] : {vPag[i]}")
        print("[doado] : sim") if vDoado[i] else print("[doado] : não")
        print(f"[código] : {vCode[i]}")
        print("//====================//")