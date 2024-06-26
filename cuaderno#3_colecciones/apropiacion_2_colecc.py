# Apropiación #2 Colecciones

# * 2- Solicite al usuario dos frases y devuelva una lista con todas las letras que se repiten en la misma posición de ambas listas

# Objetivo: lista con las letras que se repitan en las frases.

#frase_uno = input("Digite una frase #1: ")
#frase_dos = input("Digite una frase #2: ")
frase_dos = "i Never Stop"
frase_uno = "Circles"

frase_uno = frase_uno.lower()
frase_dos = frase_dos.lower()

min_letra = min(len(frase_uno), len(frase_dos))

frase_uno = frase_uno[:min_letra]
frase_dos = frase_dos[:min_letra]

frase_uno = list(frase_uno)
frase_dos = list(frase_dos)

def frases(frase_uno,frase_dos):

    letras_repetidas = []
    for i in range(len(frase_uno)):
        print(frase_uno)
        if frase_uno[i] == frase_dos[i]:
            letras_repetidas.append(frase_uno[i])
    print(f"Las letras repetidas son : {letras_repetidas}")
        
frases(frase_uno, frase_dos)