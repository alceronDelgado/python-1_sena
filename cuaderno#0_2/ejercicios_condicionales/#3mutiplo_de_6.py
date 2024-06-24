# Calcular el multiplo de 6.

valor = int(input("Digite el valor para saber si es multiplo de 6 "))


def multiplo_seis(valor):
    for i in range(0,11):
        total = 6 * i
        if valor == total:
            print(f"{valor} es multiplo de 6")
            break
        else:
            
            continue
    if valor != total:
        print("No es multiplo de 6")

multiplo_seis(valor)