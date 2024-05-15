# Calcular cual número es mayor.

#forma 1
def num_mayor_forma1():

    num1 = int(input("Digite el número #1 "))
    num2 = int(input("Digite el número #2 "))
    num3 = int(input("Digite el número #3 "))
    num4 = int(input("Digite el número #4 "))
    mayor = max(num1,num2,num3,num4)

    if mayor > 0:
        print(f"El número mayor de la forma#1 es: {mayor}")
    else:
        print("Solo se trabajan con Numeros positivos.")

num_mayor_forma1()

#forma 2
def num_mayor_forma2():

    num1 = int(input("Digite el número #1 "))
    num2 = int(input("Digite el número #2 "))
    num3 = int(input("Digite el número #3 "))
    num4 = int(input("Digite el número #4 "))
    mayor = max(num1,num2,num3,num4)

    if num1 > num2 and num1 > num3 and num1 > num4:
        print("El número mayor de la forma#2 es",num1)
    elif num2 > num1 and num2 > num3 and num2 > num4:
        print("El número mayor de la forma#2 es",num2)
    elif num3 > num1 and num3 > num2 and num3 > num4:
        print("El número mayor de la forma#2 es",num3)
    elif num4 > num1 and num4 > num2 and num4 > num3:
        print("El número mayor de la forma#2 es",num4)
    else:
        print("Error!")

num_mayor_forma2()