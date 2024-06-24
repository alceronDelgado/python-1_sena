lado_pentagono = int(input("Digite lado del pentágono: "))
apotema = int(input("Digite el apotema del pentágono: "))

perimetro_pentagono = lado_pentagono * 5
area_pentagono = (perimetro_pentagono * apotema) / 2

print("El perímetro del pentágono es:",perimetro_pentagono)
print("El area del pentágono es:",area_pentagono)