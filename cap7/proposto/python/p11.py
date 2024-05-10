class Vinho:
    def __init__(self, produto, casca, safra):
        self.produto = produto
        self.casca = casca
        self.safra = safra
    
    def __repr__(self): return f"[{self.produto}] : casca [{self.casca}] | safra[{self.safra}])"

class Adega:
    def __init__(self): self.adega = []

    def insert(self, vinho): self.adega.append(vinho)

    def chooseWine(self): return self.adega.pop() if self.adega else None

    def oldWines(self): return self.adega

adega = Adega()
adega.insert(Vinho(produto="Vinho Tinto", casca="Vermelha", safra="2020"))
adega.insert(Vinho(produto="Vinho Branco", casca="Amarela", safra="2019"))
adega.insert(Vinho(produto="Vinho Rosé", casca="Rosada", safra="2021"))
adega.insert(Vinho(produto="Vinho Espumante", casca="Branca", safra="2022"))
adega.insert(Vinho(produto="Vinho Tinto Reserva", casca="Vermelha", safra="2018"))

name:str = ''
casca:str
safra:str

print("\n//====== COMEÇO REGISTRO ======//\n")

while name.upper() != "X":

    name:str = (input("Entre com nome do novo vinho (X to exit)\n"))

    if name.upper() != "X":

    	casca = input(f"Entra com casca de [{name}]\n") 
    	safra = input(f"\nEntra com safra refente a [{name}]\n")

    	adega.insert(Vinho(produto=name,casca=casca,safra=safra))

    	print(f"Vinho {name} registrado com sucesso!\n")


print("\n//====== FIM REGISTRO ======//\n")

print("//== AQUISIÇÕES DAS MENOS AS MAIS ANTIGAS ===//\n")

for i in adega.oldWines(): print(i,"\n")

print("\n//=== VINHO PARA OCASIÃO ESPECIAL ===//: \n")
chooseWine = adega.chooseWine()
print(chooseWine,"\n\n")

print("//=== LISTA APÓS ABRIR VINHO ESPECIAL ===//\n")
for i in adega.oldWines(): print(i,"\n")
