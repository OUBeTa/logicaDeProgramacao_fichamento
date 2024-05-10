x:int = int(input("Entra com primeiro operando"))
s:str = input("Entrar com operador")
y:int = int(input("Entrar com segundo operando"))

if s == "+":
    r = x + y
    print("A soma resulta em : " + str(r))
else:
    if s == "-":
        r = x - y
        print("A subtração resulta em : " + str(r))
    else:
        if s == "*":
            r = x * y
            print("A multiplicação resulta em : " + str(r))
        else:
            if s == "/":
                if y == 0:
                    print("Denominador nulo!")
                else:
                    r = float(x) / y
                    print("A divisão resulta em : " + str(r))
            else: print("Operação inexistente!")
