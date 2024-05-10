a:int = int(input("Selecione o valor desejado para a"))
b:int = int(input("Selecione o valor desejado para b"))
c:int = int(input("Selecione o valor desejado para b"))

if a == b or b == c: print("Dentre os três, existem números iguais")
else:
    if a > b and a > c: print(f"Os números escolhidos em ordem decrescente: a : {a} | b : {b} | c : {c}") if b > c else print(f"Os números escolhidos em ordem decrescente: a : {a} | c : {c} | b : {b}")
    else:
        if b > a and b > c: print(f"Os números escolhidos em ordem decrescente: b : {b} | a : {a} | c : {c}") if a > c else print(f"Os números escolhidos em ordem decrescente: b : {b} | c : {c} | a : {a}")
        else:
            if c > b and c > a: print(f"Os números escolhidos em ordem decrescente: c : {c} | a : {a} | b : {b}") if a > b else print(f"Os números escolhidos em ordem decrescente: c : {c} | b : {b} | a : {a}")
