# Definir el area de un cuadrado, rectángulo, triángulo

figura = int(input("Elija la figura que desea calcular su area siendo el cuadrado=1, rectángulo=2 y triángulo=3 "))

def calcular(figura):
    #cuadrado
    if figura == 1:
        lado1 = int(input("Digite el lado del cuadrado"))
        resultado = lado1 * lado1
        print("el area del cuadrado es",resultado)
    #rectángulo
    elif figura == 2:
        largo = int(input("Digite el largo: "))
        ancho = int(input("Digite el ancho: "))
        resultado = largo * ancho
        print("El area del rectangulo es: ",resultado)
    #triángulo
    elif figura ==3:
        base = int(input("Digite la base del triángulo "))
        altura = int(input("Digite la altura del triángulo "))

        resultado_area = (base * altura) / 2
        print("El area del triángulo es:",resultado_area)
    else:
        print("ninguno de los Números corresponde con las figuras acordadas.")

calcular(figura)