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

def dividir(x, y = 2):
    res = x/y
    print(res)
#primera ejecución
dividir(3, y = 4)
dividir(8)