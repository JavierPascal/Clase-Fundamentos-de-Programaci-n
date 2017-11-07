vidas=3
print("Tienes tres vidas")
while vidas==3:

    puntos=0
    if respuesta==1:
        puntos+=100
    else:
        puntos-=50
        vidas-=1
print("Perdiste")

