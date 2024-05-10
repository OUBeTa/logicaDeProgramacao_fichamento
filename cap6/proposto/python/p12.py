def factorial(num):
    if not num <= 1:
        i = num * factorial(num - 1)
    else:
        i = 1
    return i

num:int = int(input("Entre com número inteiro"))
print(f"n! -> {factorial(num)}")