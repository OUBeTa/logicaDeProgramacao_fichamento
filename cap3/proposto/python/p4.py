def fixDecimal(value, digits): return "%.*f" % (digits, value)

capacidadeTotal:float = float(input("entrar com capacidade total do tanque"))
litrosAbastecidos:float = float(input("Entrar com quantia abastecida no total"))
km:float = float(input("entrar com quilometragem percorrida"))

consumo:float = km / litrosAbastecidos
litrosRestantes:float = capacidadeTotal - litrosAbastecidos
auto:float = consumo * litrosRestantes

print(f"consumo total: {fixDecimal(consumo,2)} km/l")
print(f"Autonomia restante : {fixDecimal(auto,2)} km")


