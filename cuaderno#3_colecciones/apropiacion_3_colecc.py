# Apropiación #3 Colecciones
import os

# * 3- Cree una aplicación que presente un menú con las siguientes opciones:

# Aplicaciones con Listas

# 1. Ingresar lista nueva
# 2. Ordenar lista
# 3. Promedio lista
# 4. Buscar elemento
# 5. Salir
def ingresar_lista():
    lista = []
    cantidad = int(input("Digite la cantidad de elementos que desea ingresar a la lista."))
    for i in range(cantidad):
        elemento = input(f"Digita el elemento {i + 1} que deseas agregar a la lista: ")
        lista.append(elemento)
    return lista

def ordenar_lista(lista_valor):
    lista_valor.sort()
    return lista_valor

def promedio_lista(lista_valor):
    valor_sum = 0
    for i in range (len(lista_valor)):
        valor_sum = lista_valor[i] + valor_sum
    return valor_sum


lista_valor = []
valor_sum = 0

while True:
    #os.system ("cls")
    print("\nMenú:")
    print("1. Ingresar lista nueva")
    print("2. Ordenar lista")
    print("3. Promedio lista")
    print("4. Buscar elemento")
    print("5. Salir")

    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        lista_valor = ingresar_lista()
        print("valores ingresados a la lista", lista_valor)
    elif opcion == "2":
        if not lista_valor:
            print("La lista está vacía. Ingrese una lista primero.")
        else:
            lista_ordenada = ordenar_lista(lista_valor)
            print(f"lista ordenada: {lista_ordenada}")
    elif opcion == "3":
        if not lista_valor:
            print("La lista está vacía. Ingrese una lista primero para poder calcular su promedio")
        else:
            promediar_lista = promedio_lista(lista_valor)
            print(f"El valor del promedio de la lista es : {promediar_lista}")
    elif opcion == "4":
        print(f"buscar elemento")
        if not lista_valor:
            print("La lista está vacia, ingrese un elemento para poder utilizar esta opción")
        else:
            elemento_buscar = input("Digite el elemento que desea buscar en la lista.")
            if elemento_buscar in lista_valor:
                print(f"El elemento {elemento_buscar} se encuentra en la lista.")
                print(lista_valor)
                
    elif opcion == "5":
        print("Bye")
        break
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")
    