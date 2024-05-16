# Algoritmo para calcular cambio a un cliente
import random

total_recibido = int(input("Digite la cantidad recibida por el cliente "))
total_a_pagar = random.randint(100,100000)

if total_a_pagar > total_recibido:
    print("El valor recibido por el cliente no es suficiente para realizar el pago")
else:
    total_devolver = total_recibido - total_a_pagar
    print("El valor devuelto al cliente es ",total_devolver)
