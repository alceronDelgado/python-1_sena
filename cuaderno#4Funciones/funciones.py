## Funciones integradas
#numeros = [320,12,3,5,10]

## Funcion max y min
#print(f"El número mayor de la lista es {max(numeros)}")
#print(f"El número menor de la lista es {min(numeros)}")


#num = int(input("Ingrese un número: "))

#num_b = bin(num)
#num_o = oct(num)
#num_h = hex(num)

#print(f"El número binario es: {num_b}")
#print(f"El número octal es: {num_o}")
#print(f"El número hexadecimal es: {num_h}")

## Funciones definidas por el usuario.

#Definición de la función
#def tabla_del_5():
#    for i in range(1,11):
#        print(f"10 x {i} es: {10 * i}")


#tabla_del_5()

print("--"*30)


## Funcion definida por el usuario y enviando parámetros.

def mostrar_datos(a,b):
    print(f"{a} {b}")

#mostrar_datos(39,10)

## Funcion definida por el usuario y enviando parámetros. = Mejor forma
#def mostrar_datos2(**keywords):
    #print(type(keywords))
    #print(keywords)

#mostrar_datos2(nombre="Alejandro",apellido="ceron")

#def dividir(x, y = 2):
#    res = x/y
#    print(res)
#primera ejecución
#dividir(3, y = 4)
#dividir(8)

#QUEDE EN NÚMERO DE ARGUMENTOS INDETERMINADOS.


## Cualquier argumento que no se pueda asociar, lo guardamos dentro de la tupla
# * = umpacking
# No se puede mandar como una variable.
# usando args
#def suma (a,b,*args):
#   print(type(args))
#   return sum(args)


#print("la suma de los números es: ", suma(3,10,10,2,15,5))

# usando kwargs
#def mostrar_info(**kwargs):
#    print(type(kwargs))
#    for i in kwargs:
#        print(f"{i} {kwargs[i]}")

#mostrar_info(nombre= "alejandro", apellido = "ceron", edad = "23")


# valores por referencia
# fuera de la función ns tiene un valor de 10, pero dentro es una lista con n cantidad de elementos.
#def doblar_valores(ns):
#    ns[0] = ns [0] * 2    
#    ns[1] = ns [1] * 3    
#    ns[2] = ns [2] * 4    

#    for i in range(len(ns)):
#        print(f"Dentro de la función {ns[i]}")



#ns = [20,30,40]
#doblar_valores(ns)

#ns = 10
#print(ns)


#Cambio de valor dentro de la función
#Las variables pueden cambiar su valor dentro de la función, no van a repercutir fuera de ellos.

#def cambio_valor(x):
#    x = 3
#    print(f"Función cambio valor. {x}")


#x = 100
#print(f"fuera de la funcion {x}")
#cambio_valor(x)

# globalizar variables
#Aca va a valer 3 adentro y fuera de la función.
#def cambio_valor():
#    global x 
#    x = 3
#    print(f"Función cambio valor. {x}")


#x = 8
#cambio_valor()
#print(f"fuera de la funcion {x}")


# Funciones recursivas
#def numero_factorial(num):
#    if num == 1:
#        return 1
#    else:
        #En caso de que el valor ingresado no sea 1 re invoca la función.
#        return num * numero_factorial(num - 1)


#num= int(input("Ingresa un número: "))
#print(f"El factorial de {num} es: {numero_factorial(num)}")

# QUEDE EN APROPIACIÓN