# Apropiación 2 Paquetes

# * 2- Dado el siguiente código, cree la estructura de paquetes y módulos para que las importaciones y llamado a funciones trabajen correctamente. Complemente el código de ser necesario.

import mi_paquete.greetings.saludar as one
import mi_paquete.greetings.despedir as hi
import mi_paquete.ropa.uniforme.camisa as uni
import mi_paquete.calculadora.operaciones as ca

one.saludo()
one.hi()
hi.despedir()
uni.camisa()
print(ca.sumar(10,303,501,500))
