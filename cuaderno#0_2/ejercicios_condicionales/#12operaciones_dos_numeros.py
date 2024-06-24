num1 = int(input("Digite el valor #1 "))
num2 = int(input("Digite el valor #2 "))

if num1 < 0 or num2 < 0:
    print("No es posible hacer la operación")
else:
    suma_total = num1 + num2
    resta_total = num1 - num2
    multi_total = num1 * num2
    divi_total = num1 / num2
    potencia_num1 = num1**2
    potencia_num2 = num2**2

    print(f"el total de la suma es {suma_total}")
    print(f"el total de la resta es {resta_total}")
    print(f"el total de la multiplicación es {multi_total}")
    print(f"el total de la división es {divi_total}")
    print(f"el total de la Potencia de {num1} es: {potencia_num1} y la potencia de {num2} es : {potencia_num2}")