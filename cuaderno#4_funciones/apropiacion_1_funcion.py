# Apropiación #1 Funciones

# * 1- Realiza una función que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.

# * salida en pantalla: Números pares: [2, 4, 6, 8] Números impares: [1, 3, 5, 9]

def pedir_valor():
    lista = []
    valor = int(input("Digite el valor que deseas agregar: "))
    lista.append(valor)
    while True:
        print(f"último valor agregado: {lista}")
        respuesta = int(input("Deseas agregar otro valor? 1 o 0: "))
        if respuesta == 1:
            valor = int(input("Digite un número para agregarlo a la lista: "))
            lista.append(valor)
        else:
            break
    print(f"Estos son los valores agregados: {lista}")
    return lista
#Para agregar valores.
lista = pedir_valor()
#lista = [12,50,20,52,46,12,17,15]

def recibir_lista(lista):
    listaPar = []
    listaImpar = []
    for i in range(len(lista)):
        print(lista[i])
        if (lista[i] % 2) == 0:
            listaPar.append(lista[i])
            listaPar.sort()
        else:
            listaImpar.append(lista[i])
            listaImpar.sort()

    print(f"Es par: {listaPar}")
    print(f"Es impar: {listaImpar}")



if len(lista) == 0:
    print(f"Lista vacia. {len(lista)}")
else:
    #print(f"Longitud de la lista actual: {lista}")
    recibir_lista(lista)