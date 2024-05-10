print("Animais possíveis: leão, cavalo, humano, macaco, morcego, baleia, avestruz, pinguim, pato, águia, tartaruga, crcodilo e cobra")
mamifero = input("è mamifero? (0-1)")
if mamifero:
    quadrupede = bool(input("é quadrupede?"))
    if quadrupede:
        carnivoro = bool(input("é carnívoro?"))
        if carnivoro: finalAnimal = "leão"
        else: finalAnimal = "Cavalo"
    else:
        bipede = bool(input("é bípede?"))
        if bipede:
            onivoro = bool(input("é onívoro?"))
            if onivoro: finalAnimal = "Humano"
            else: finalAnimal = "Macaco"
        else:
            voador = bool(input("é voador?"))
            if voador: finalAnimal = "Morcego"
            else: finalAnimal = "Baleia"
else:
    ave = bool(input("é uma ave?"))
    if ave:
        voador = bool(input("é voadora?"))
        if voador:
            nadador = bool(input("é nadador?"))
            if nadador: finalAnimal = "Pato"
            else: finalAnimal = "Águia"
        else:
            tropical = bool(input("é tropical?"))
            if tropical: finalAnimal = "Avestruz"
            else: finalAnimal = "pinguim"
    else:
        cCasco = bool(input("Possui casco?"))
        if cCasco: finalAnimal = "Tartaruga"
        else:
            carnivoro = bool(input("é carnivoro?"))
            if carnivoro: finalAnimal = "Crododilo"
            else: finalAnimal = "Cobra"

print(f"O animal é : {finalAnimal}")
