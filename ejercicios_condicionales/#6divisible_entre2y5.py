#calcular si un Número es divisible por 2 o 5

# Algoritmo para calcular si el número es divisible por 14.
divisible_uno = int(input("Digite el numero para saber si es divisible por 2 "))
divisible_dos = int(input("Digite el numero para saber si es divisible por 5 "))

total1 = divisible_uno % 5 
total2 = divisible_dos % 5 

if total1 == 0 and total2 == 0:
    print(f"El divisible {divisible_uno} y {divisible_dos} es divisible por 2 y por 5")
else:
    print(f"El Número {divisible_uno} y {divisible_uno} no es divisible por 2 y por 5")