import math

cateto1 = int(input("Digite el cateto1 del triángulo: "))
cateto2 = int(input("Digite el cateto2 del triángulo: "))

resultado1 = (cateto1 * cateto1) + (cateto2 * cateto2)

# resultado = resultado1 ** 0.5

print("raiz cuadrada con math: ",math.sqrt(resultado1))
# print("hipotenusa del triángulo rectángulo es: ",resultado)