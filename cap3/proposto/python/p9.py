mes:int = int(input("Entrar com mês de nascimento (1-12)"))
dia:int = int(input("Entrar com dia de nascimento (0-31)"))
signo:str

if mes == 1: signo = "capricórnio" if dia >= 1 and dia <= 19 else "aquário"
else:
    if mes == 2: signo = "aquário" if dia >= 1 and dia <= 18 else "peixes"
    else:
        if mes == 3: signo = "peixes" if dia >= 1 and dia <= 20 else "áries"
        else:
            if mes == 4: signo = "áries" if dia >= 1 and dia <= 20 else "touro"
            else:
                if mes == 5: signo = "touro" if dia >= 1 and dia <= 19 else "gemeos"
                else:
                    if mes == 6: signo = "gêmeos" if dia >= 1 and dia <= 20 else "Câncer"
                    else:
                        if mes == 7: signo = "câncer" if dia >= 1 and dia <= 22 else "leão"
                        else:
                            if mes == 8: signo = "leão" if dia >= 1 and dia <= 22 else "virgem"
                            else:
                                if mes == 9: signo = "virgem" if dia >= 1 and dia <= 22 else "libra"
                                else:
                                    if mes == 10: signo = "libra" if dia >= 1 and dia <= 22 else "escorpião"
                                    else:
                                        if mes == 11: signo = "escorpião" if dia >= 1 and dia <= 21 else "sagitário"
                                        else:
                                            if mes == 12: signo = "sagitário" if dia >= 1 and dia <= 21 else "capricórnio"
                                            else: signo = "inválido"
print(f"signo : {signo}")
