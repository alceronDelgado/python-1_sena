# Apropiación #2 Colecciones

# * 2- Solicite al usuario dos frases y devuelva una lista con todas las letras que se repiten en la misma posición de ambas listas

# Objetivo: lista con las letras que se repitan en las frases.

#frase_uno = input("Digite una frase #1: ")
#frase_dos = input("Digite una frase #2: ")


frase_uno = "memento mori"
frase_dos = "love or die"

def frases(frase_uno,frase_dos):
    lista_uno = []
    lista_dos = []
    
    #Aplico el proceso con la frase #1
    #Corto el espaciado de la cadena de texto, devuelve una lista
    frase_uno = frase_uno.split(" ")
    
    #Como ya es una lista, uno los 2 elementos y queda una sola frase junta.
    frase_uno = "".join(frase_uno)
    
    # Itinero cada letra para agregarlo a una lista1
    for i in range(len(frase_uno)):
        letra_1 = frase_uno[i]
        lista_uno.append(letra_1)

    #Aplico el proceso con la frase #2
    frase_dos = frase_dos.split(" ")
    frase_dos = "".join(frase_dos)
    
    # Itinero cada letra para agregarlo a la lista2
    for k in range(len(frase_dos)):
        letra_2 = frase_dos[k]
        lista_dos.append(letra_2)
    
    
    # Defino una lista
    letras_repetidas = []
    # Itinero la primera y segunda lista para saber su rango. 
    for j in lista_uno:
        for o in lista_dos:
            if j == o:
                letras_repetidas.append(j)
    #print(f"cantidad de palabras repetidas :{len(letras_repetidas)}")
    print(f"{letras_repetidas}")

frases(frase_uno, frase_dos)
        