def suma(*args):
    resultado = sum(args)
    return resultado

def multiplicar(*args):
    resultado = 1
    for i in args:
        #Primera forma = resultado *= i
        resultado = i * resultado #Segunda forma
    
    return resultado
def resta(num_uno,num_dos):
    resultado_resta = num_uno - num_dos
    return resultado_resta

def division(num_uno,num_dos):
    resultado = num_uno / num_dos
    return resultado

def operacion(valor_uno,valor_dos,signo):
    if signo == "+":
        resultado = valor_uno + valor_dos
        return resultado
    elif signo == "-":
        resultado = valor_uno - valor_dos
        return resultado
    elif signo == "*":
        resultado = valor_uno * valor_dos
        return resultado
    elif signo == "/":
        if valor_dos == 0:
            return print(f"Número divisible por 0")
        else:
            resultado = valor_uno / valor_dos
            return resultado