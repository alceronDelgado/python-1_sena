# Algoritmo para calcular si el número es divisible por 14.
numero_divisor = int(input("Digite el numero para saber si es divisible por 14 "))

total = 14 % numero_divisor

print(total)

if total == 0:
    print(f"El Número {numero_divisor} es divisible por 14")
else:
    print(f"El Número {numero_divisor} no es divisible por 14")