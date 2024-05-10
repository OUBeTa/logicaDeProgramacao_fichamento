dataValida = True
dia:str = int(input("entre com dia (1-31)"))
mes:str = int(input("entre com mês (1-12)"))
ano:str = int(input("entre com ano"))

if not (dia <= 0 or dia > 31 or (mes <= 0 or mes > 12) or ano <= 0):
    if mes == 2:
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            if not(dia >= 1 and dia <= 29): dataValida = False
        else:
            if not(dia >= 1 and dia <= 28): dataValida = False
    else:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if not(dia >= 1 and dia <= 30): dataValida = False
        else:
            if not(dia >= 1 and dia <= 31): dataValida = False
            
else: dataValida = False

print("Data " + str(dia) + "/" + str(mes) + "/" + str(ano) + " é válida") if dataValida else print("Data " + str(dia) + "/" + str(mes) + "/" + str(ano) + " é inválida")
