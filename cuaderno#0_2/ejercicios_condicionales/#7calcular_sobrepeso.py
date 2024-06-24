# calcular si una persona tiene sobre peso

estatura = int(input("Digite la estatura en centimetros "))

if estatura < 100:
    print("La estatura no debe ser negativa")
else:
    peso_actual = int(input("Digite su peso actual "))
    
    total = estatura - 100
    
    print(total)

    if total > peso_actual:
        print("Tienes sobre peso")
    else:
        print("No tienes sobre peso")