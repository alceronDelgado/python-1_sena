import random

# ? De esta forma nosotros hemos modificado el código, podemos aplicarle otras mejoras y tratar de innovar el ejercicio


# Variables globales
palabras = []
intentos_permitidos = 6

#Agrega la palabra a la variable llamada lista
def agregar_palabra():

    while True:
        ##Posiblemente agregar un while para poder agregar Más palabras.
        palabra = input("Ingresa una palabra para agregar al juego: ").lower()
        palabras.append(palabra)
        print(f'La palabra "{palabra}" ha sido agregada.')
        print("====================================")
        print(f"la lista modificada es {palabras}")
        validar = input("¿Deseas agregar una palabra adicional? S/N ").lower()
        print("====================================")
        if validar == 'n':
            break
    return

#Definimos cantidad de intentos.
def configurar_intentos():
    global intentos_permitidos
    try:
        intentos = int(input("Ingresa el Número de intentos permitidos, por defecto 6."))
        if intentos > 0:
            intentos_permitidos = intentos
        else:
            print("El Número de intentos debe ser mayor a cero.")
    except ValueError:
            print("Ingresa un número válido")

#Seleccionamos la palabra aleatoria de la lista.
def seleccionar_palabra():
    #return print(random.choices(palabras))
    return random.choices(palabras)

#Muestra la cantidad de caracteres en líneas bajas de la palabra
def inicializar_palabra_oculta(palabra):
    return print(['_'] * len(palabra))

def mostrar_palabra_oculta(palabra_oculta):
    return ' '.join(palabra_oculta)

#Aca se inicia el juego.
def jugar():
    #Guardamos en una variable la función seleccionar palabra, esta nos da una palabra aleatoria
    palabra = seleccionar_palabra()
    #Transforma la palabra en espacios en guiones para no saber la palabra.
    palabra_oculta = inicializar_palabra_oculta(palabra)
    # asignamos el valor de intentos_permitidos que es una variable global a la variable oportunidades.
    oportunidades = intentos_permitidos

    print("Comencemos a jugar!")
    print(f"Palabra: {mostrar_palabra_oculta(palabra_oculta)}")

    while True:
        letra = input("Adivina una letra: ").lower()
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
            print(f"Palabra: {mostrar_palabra_oculta(palabra_oculta)}")
            #Valida si no hay guiones bajos en la palabra oculta
            if '_' not in palabra_oculta:
                print("¡Has ganado! La palabra era:", palabra)
                break
        else:
            oportunidades -= 1
            print(f"Letra incorrecta. Te quedan {oportunidades} oportunidades.")

        if oportunidades == 0:
            print("¡Has perdido! La palabra era:", palabra)
            break

#Menu del juego
def main():
        
    while True:
        print("\nMenú:")
        print("1. Agregar Palabra")
        print("2. Configurar Intentos Permitidos")
        print("3. Jugar")
        print("4. Salir") 
        opcion = input("Elige una opción: ")
        try:
            #Arreglarlo, podemos usar un try except para esto.
            if opcion == '1':
                agregar_palabra()
            elif opcion == '2':
                configurar_intentos()
            elif opcion == '3':
                if len(palabras) == 0:
                    print("Debes agregar palabras antes de jugar.")
                else:
                    jugar()
            elif opcion == '4':
                print("¡Adiós!")
                break
            else:
                print("Opción no válida. Por favor, elige una opción del menú.")
        except ValueError:
            print("Opción no válida Fuera de value")
if __name__ == "__main__":
    main()