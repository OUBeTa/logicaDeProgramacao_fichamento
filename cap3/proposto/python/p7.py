meses:list = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]

mes:int = int(input("entre com número referente a um mês (1-12)"))

print(f"o mês número {mes} é o mês de {meses[mes - 1]}") if mes >= 1 and mes <= 12 else print("mês inválido")
