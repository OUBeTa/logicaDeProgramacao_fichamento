class Elemento:
    def __init__(self, name):
        self.name = name
        self.proximo = None

class Lista:

    def __init__(self): self.head = None

    def rtnList(self):
        corrente = self.head
        a = ""
        while corrente:
            a += f"{corrente.name}\n"
            corrente = corrente.proximo

        return a

    def insert_name(self, nNome):
        new_Elemento = Elemento(nNome)
        if not(self.head ) or (self.head.name > nNome):
            new_Elemento.proximo = self.head
            self.head = new_Elemento
            return

        corrente = self.head

        while (corrente.proximo) and (corrente.proximo.name < nNome): corrente = corrente.proximo
        new_Elemento.proximo = corrente.proximo
        corrente.proximo = new_Elemento

    def delete_name(self, target_name):
        corrente = self.head
        anterior = None
        while corrente:
            if corrente.name == target_name:
                if anterior:
                    anterior.proximo = corrente.proximo
                else:
                    self.head = corrente.proximo
                return True
            anterior = corrente
            corrente = corrente.proximo
        return False

    def update_name(self, old_name, nNome):
        if self.delete_name(old_name):
            self.insert_name(nNome)
            return True
        return False

nl = Lista()

desire:str
desireName:str
oldName:str
newReg:str = ""

print("\n//====== COMEÇO REGISTRO ======//\n")

while newReg.upper() != "X":

    newReg:str = (input("Registre um novo nome (X to exit)\n"))
    if newReg.upper() != "X":

        nl.insert_name(newReg)
        print(f"\nNome [{newReg}] registrado com sucesso!\n")

print("\n//====== FIM REGISTRO ======//\n")

print("lista antes de qualquer alteração")
print(nl.rtnList())

print("\n//====== COMEÇO EXPEDIÇÃO ======//\n")

desire = int(input("Deseja deletar ou alterar um registro? (1 - 2 [0 to exit])\n"))

while not(desire < 3 and desire >= 0): desire = int(input("Índice inválido! Tente novamente. (deletar -> 0 |  alterar -> 1)\n"))

while desire != 0:

    if desire == 1:
        desireName = input("Qual nome deseja deletar?\n")

        while not(desireName in (nl.rtnList().split("\n"))): desireName = input("Nome não consta na lista, tente novamente\n")

        nl.delete_name(desireName)

    if desire == 2:

        oldName = (input("Qual nome deve ser substituido?\n"))

        while not(oldName in (nl.rtnList().split("\n"))): oldName = input("Nome não consta na lista para ser substituido, tente novamente\n")

        desireName = input("Entre com novo valor para este registro\n")

        nl.update_name(oldName,desireName)

        print(f"[{oldName}] alterado para [{desireName}] com sucesso!")

    desire = int(input("Deseja deletar ou alterar um registro? (1 - 2 [0 to exit])\n"))


print("\n//====== FIM EXPEDIÇÃO ======//\n")

print("lista depois de alterações")
print(nl.rtnList())