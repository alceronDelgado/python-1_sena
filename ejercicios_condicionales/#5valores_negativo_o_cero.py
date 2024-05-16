#calcular si la suma de 2 valores es positiva, negativa o cero

num1 = int(input("Digita el número 1"))
num2 = int(input("Digita el número 2"))

total = num1 + num2

if total > 0:
    print(f"el resultado es positivo")
elif total == 0:
    print(f"el resultado es cero")
else:
    print(f"el resultado es negativo")