# Apropiación #1 Try & Except

# * 1- Finaliza el siguiente código con una gestión completa de sus excepciones. El objetivo del programa es solicitar al usuario una posición de una lista y devolver el valor que se encuentra en dicha posición. Prueba el programa enviando una posición inexistente y enviando una letra como posición. El programa sólo terminará cuando se ejecute correctamente

# TODO: Realizar una mejora a este código con todo lo visto en try y except y los demás cuadernos

#lista = [3,5,6,8]
#pos = int(input("ingrese la posición del elemento que desea obtener:"))
#print(f"El valor en la posicion {pos} es {lista[pos]}")

lista = [3, 5, 6, 8]

while True:
    try:
        pos = int(input("Ingrese la posición del elemento que desea obtener: "))
        valor = lista[pos]
        print(f"El valor en la posición {pos} es {valor}")
        break  # Si todo fue exitoso, salimos del bucle.
    except IndexError:
        print("Error: La posición ingresada está fuera de rango. Intente de nuevo.")
    except ValueError:
        print("Error: Ingrese un número entero como posición. Intente de nuevo.")