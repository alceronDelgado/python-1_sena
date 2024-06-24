# Definir el Día de la semana dado un número de día.
numero_dia = int(input("Digite el numero de día siendo 1 Domingo y 7 Sábado"))

dia = ["Domingo","Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

for i in range(0,8):
    if i == 0:
        continue
    elif i == numero_dia: 
        print(dia[i])