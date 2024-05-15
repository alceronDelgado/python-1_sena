# calcular si el numero es par o impar
numero = int(input("Digite el número para determinar si es un número par o impar "))

total = numero % 2

print(total)
if total == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
