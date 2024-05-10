class RegEmbarque():

	idade:int = None
	numPas:int = None
	nome:str = None
	cidade:str = None
	origem:str = None
	destino:str = None

	def regData(self,attrName,value): setattr(self,attrName,value) if (hasattr(self,attrName)) else 0;

records:int = 10
idadeV:list = [0] * records
vetEmbarque = [RegEmbarque() for _ in range(records)]
media:float
count:int = 0


for i in range(0,records):
	count += 1
	vetEmbarque[i].regData("idade",int(input(f"Entre com idade do indivíduo {i+1}\n")))
	vetEmbarque[i].regData("numPas",int(input(f"Entre com código da viagem do indivíduo {i+1}\n")))
	vetEmbarque[i].regData("nome",input(f"Entre com nome do indivíduo {i+1}\n"))
	vetEmbarque[i].regData("cidade",input(f"Entre com cidade de origem do indivíduo {i+1}\n"))
	vetEmbarque[i].regData("origem",input(f"Entre com origem da viagem do indivíduo {i+1}\n"))
	vetEmbarque[i].regData("destino",input(f"Entre com destino da viagem do indivíduo {i+1}\n"))

for i in range(0,records):idadeV[i] = vetEmbarque[i].idade

print(f"\nA média das idades dos passageiros é : {(sum(idadeV) / count)}")
