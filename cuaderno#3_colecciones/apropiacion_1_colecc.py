# Apropiación #1 Colecciones

# * 1- Pregunte al usuario cuántos elementos desea ingresar en una lista, luego solicite cada uno de ellos y presente el contenido de la lista y su contenido invertido.


cantidad_elementos = int(input("Digite la cantidad de elementos: "))

def agregar_elementos(cantidad_elementos):
    lista = []
    for i in range(cantidad_elementos):
        elemento = input(f"Digita el elemento #{i + 1}: ")
        lista.append(elemento)
        
    lista.sort()
    print(f"Lista ordenada{lista}")
    lista.reverse()
    print(f"Lista desordenada{lista}")
    

agregar_elementos(cantidad_elementos)