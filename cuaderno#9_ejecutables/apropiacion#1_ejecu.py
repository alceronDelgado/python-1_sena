# Apropiación 1 Distribuibles y ejecutables
from random import randint
import package.random_number.numero_aleatorio as rm_number
import package.intentos.intentos as itn
import emoji
# !PREVIO A LA APROPIACIÓN DEBEMOS DE TENER REALIZADO EL DIST DE ALGÚN EJERCICIO.

#Realice el juego de adivine el número en el que el usuario tiene 3 oportunidades para #adivinar un número entre 0 y 10 generado aleatoriamente. El juego termina cuando el #usuario adivina el número usando sus tres oportunidades (el usuario gana) o cuando se #usan las tres oportunidades sin adivinar el número (el computador gana).
#
#Cree un ejecutable .exe del programa
#
#Ejecute el programa desde cualquier equipo (incluso si no tiene python instalado)

# ?Lo que necesito 
# función random que devuelva un número aleatorio
# numero de intentos por el usuario
#usuario gana si adivina antes de los 3 intentos
#computador gana si el usuario no adivina con los 3 intentos.

def main():
    aleatorio_computadora = rm_number.valor_elatorio(random_entero=randint(0,10))
    intentos_usuario = itn.intentos_usuario()

    # TODO: mejorar el try y except de esta sección del código.
    while True:
        try:
            print(f"Intento #: {intentos_usuario}")
            numero = int(input(emoji.emojize('Digita el número que deseas adivinar \N{face without mouth} : ')))
            if numero == aleatorio_computadora:
                intentos_usuario = intentos_usuario - 1
                print("ganaste \N{face with rolling eyes}")
                break
            else:
                intentos_usuario = intentos_usuario - 1
            if intentos_usuario == 0:
                print("Perdiste \N{smiling face with sunglasses}")
                break
        except KeyboardInterrupt:
            print("\nSales del programa por fuerza mayor.")
            break
    
    
    # TODO: Colocar un try y except 
    try:
        repetir = input('Deseas repetir este programa? S/N')
        if repetir == 'S':
            main()
        else:
            print("Presiona ENTER para salir del programa.")
            input()
    except KeyboardInterrupt:
        print("\nSaliste del programa de forma externa")
    
    
main()

#input()