def calc(n1, operator, n2):
    if operator == "+": num = n1 + n2
    else:
        if operator == "-": num = n1 - n2
        else:
            if operator == "/": num = float(n1) / n2
            else:
                if operator == "*": num = n1 * n2
                else:
                    invalidOperator = 1
                    num = 0
    
    return num

records:int = 5
v1:list = [0] * (records)
v2:list = [0] * (records)
vOper:list = [""] * (records)

i:int

for i in range(0, records, 1):
    v1[i] = int(input(f"entre com primeiro operando inteiro [{i + 1}]\n"))
    vOper[i] = input(f"entre com operador [{i + 1}] (+  -  *  /)\n")
    v2[i] = int(input(f"entre com segundo operando inteiro [{i + 1}]\n"))

for i in range(0, records, 1): print(f"Operação [{i + 1}] ({v1[i]} {vOper[i]} {v2[i]}) : {calc(v1[i], vOper[i], v2[i])}")
