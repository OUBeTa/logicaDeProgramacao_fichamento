class Nomes:
    def __init__(self):
        self.mName = []  
        self.fName = []  

    def isrtMname(self, nome):
        self.mName.append(nome)

    def isrtDelMname(self, nome):
        if nome in self.mName:
            self.mName.remove(nome)
            print(f"Nome '{nome}' excluído.")

        else:
            self.mName.append(nome)
            print(f"Nome '{nome}' incluído.")

    def insrtName(self, nome, sexo):
        if sexo == "homem":

            self.mName.append(nome)
            print(f"Nome '{nome}' incluído.")

        elif sexo == "mulher":

            self.fName.append(nome)
            print(f"Nome '{nome}' incluído.")

        else: print("Sexo não identificado. Insira 'homem' ou 'mulher'.")

    def delName(self, nome, sexo):
        if sexo == "homem":
            if nome in self.mName:
                self.mName.remove(nome)
                print(f"Nome '{nome}' excluído.")

            else: print(f"Nome '{nome}' não encontrado.")

        elif sexo == "mulher":
            if nome in self.fName:
                self.fName.remove(nome)
                print(f"Nome '{nome}' excluído.")

            else: print(f"Nome '{nome}' não encontrado.")
        else: print("Sexo não identificado. Insira 'homem' ou 'mulher'.")

    def findChangeName(self, nome_atual, sexo_atual, novo_nome, novo_sexo):
        if sexo_atual == "homem":
            if nome_atual in self.mName:
                index = self.mName.index(nome_atual)
                print(f"Nome alterado de '{nome_atual}' para '{novo_nome}'.")
                
                if novo_sexo == "mulher":
                    self.mName.pop(index)
                    self.fName.append(novo_nome)
                    print(f"Nome '{novo_nome}' movido para a lista de mulheres.")
                
            else: print(f"Nome '{nome_atual}' não encontrado.")
        elif sexo_atual == "mulher":
            if nome_atual in self.fName:
                index = self.fName.index(nome_atual)
                print(f"Nome alterado de '{nome_atual}' para '{novo_nome}'.")
                
                if novo_sexo == "homem":
                    self.fName.pop(index)
                    self.mName.append(novo_nome)
                    print(f"Nome '{novo_nome}' movido para a lista de homens.")
                
            else: print(f"Nome '{nome_atual}' não encontrado.")
        else: print("Sexo não identificado. Insira 'homem' ou 'mulher'.")


nomes = Nomes()

nomes.isrtMname("João")
nomes.isrtDelMname("Carlos")
nomes.isrtDelMname("Carlos")
nomes.insrtName("Maria", "mulher")
nomes.delName("Maria", "mulher")
nomes.findChangeName("João", "homem", "João Paulo", "homem")
nomes.findChangeName("João Paulo", "homem", "Joana", "mulher")

name:str = ''
sexo:str

print("\n//====== COMEÇO REGISTRO ======//\n")

while True:
    name = input("Entre com o nome para incluir (ou 'X' para sair):\n")
    
    if name.upper() == 'X': break
    
    sexo = input(f"Entre com o sexo associado ao nome '{name}' ('homem' ou 'mulher'):\n").lower()
    
    if sexo == "homem":
        nomes.isrtMname(name)
        print(f"Nome '{name}' incluído na lista de homens.")

    elif sexo == "mulher":

        nomes.insrtName(name, sexo)
        print(f"Nome '{name}' incluído na lista de mulheres.")
    else: print("Sexo não identificado. Por favor, insira 'homem' ou 'mulher'.")

print("\n//====== FIM REGISTRO ======//\n")

print("//===== Lista M =====//\n")
for i in nomes.mName: print(i)

print("\n//===== Lista F =====//\n")
for i in nomes.fName: print(i)