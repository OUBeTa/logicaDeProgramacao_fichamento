i:int = int(input("Qual a idade do nadador?"))

if i >= 5 and i <= 7: print("Infantil A")
else:
    if i >= 8 and i <= 10: print("Infantil B")
    else:
        if i >= 11 and i <= 13: print("Juvenil A")
        else:
            if i >= 14 and i <= 17: print("Juvenil B")
            else:
                if i >= 18: print("Adulto")
