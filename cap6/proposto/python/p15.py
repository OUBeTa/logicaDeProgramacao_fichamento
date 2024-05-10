def round(num, decimalPlaces):

    factor = 10 ** decimalPlaces
    numMulti = num * factor
    numMulti = numMulti + 0.5 if num >= 0 else numMulti - 0.5
    rounded = numMulti // 1
    rounded = rounded / factor
    
    return rounded

a = float(input("Entrar com número real"))
c = int(input("Entrar com número de casa decimais para arredondar"))

print(f"round({a},{c}) = {round(a, c)}")
