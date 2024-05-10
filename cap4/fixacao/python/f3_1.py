class RegCheque:
	valor:float = None
	dia:int = None
	mes:int = None
	ano:int = None
	nominal:str = None
	cidade:str = None

	def regData(self,attrName,value): setattr(self,attrName,value) if (hasattr(self,attrName)) else 0;


a = RegCheque()

a.regData("valor",3503.5)
a.regData("dia",13)
a.regData("mes",6)
a.regData("ano",1997)
a.regData("nominal","Carlos Antônio")
a.regData("cidade","São Bernardo")