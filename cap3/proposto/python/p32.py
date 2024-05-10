ana:int = 150
fel:int = 110
ano:int = 0

while True:
    print("Altura de Anacleto : {ana}cm")
    print("Altura de Felisberto : {fel}cm")
    ano = ano + 1
    ana = ana + 2
    fel = fel + 3
    if fel > ana: break

print("")
print(f"em {ano} ano{'' if ano == 1 else 's'}, Felisberto estará com {fel} cm de altura, superando Anacleto, que no mesmo ano terá : {ana} cm de altura")
