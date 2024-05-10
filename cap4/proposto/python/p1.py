records:int = 30
vLido:list = [0] * (records)
vResult:list = [0] * (records)

for i in range(0, records):
    vLido[i] = int(input(f"entre com termo número n {i+1}\n"))
    vResult[i] = ((vLido[i] * 2) if i % 2 == 0 else (vLido[i] * 3))

print(vResult)