# Apropiación 1 Paquetes

import modulo_calculadora.calculadora as op

# * 1- Cree un programa principal donde importe el módulo calculadora y genere un menú como el siguiente a través del cual se haga uso de las funciones incluídas en el módulo calculadora:

# TODO:: apliar try y except en esta sección, aplicarlo en la función main y de ser posible en el paquete calculadora
#Nota: Todas las funciones deben gestionar correctamente las excepciones.

def menu():
    print("# 1. Sumar")
    print("# 2. Restar")
    print("# 3. Multiplicar")
    print("# 4. Dividir")
    print("# 5. Operación")
    print("# 6. Salir")



def main():
    while True:
        menu()
        opcion = input("selecciona una de las opciones")
        
        if opcion == "1":
            #Con el método split separa cada elemento, por defecto separa las cosas por espacios y devuelve una lista.
            args = input("digite los valores separados por espacios").split()
            args = list(map(int, args))
            resultado = op.suma(*args)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == "2":
            num_uno = int(input("Digita el valor #1"))
            num_dos = int(input("Digita el valor #2"))
            resultado = op.resta(num_uno,num_dos)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == "3":
            args = input("digite los valores que deseas multiplicar, separelos por espacios: ").split()
            args = list(map(int,args))
            resultado = op.multiplicar(*args)
            print(f"El resultado de la multiplicación es : {resultado}")
        elif opcion == "4":
            num_uno = int(input("Digita el valor #1"))
            num_dos = int(input("Digita el valor #2"))
            if num_uno == 0 or num_dos == 0:
                print(f"Error, numero divisible por 0")
            else:
                resultado = op.division(num_uno,num_dos)       
                print(f"El resultado de la división es: {resultado}")
        elif opcion == "5":
            signo = input("digite uno de los signos para realizar su respectiva opieración: ('+','-','*','/')")
            num_uno = int(input("Digita el valor #1"))
            num_dos = int(input("Digita el valor #2"))
            resultado = op.operacion(num_uno,num_dos,signo)
            print(f"El resultado de la operación es: {resultado}")
        elif opcion == "6":
            print("Bye")
            break
main()