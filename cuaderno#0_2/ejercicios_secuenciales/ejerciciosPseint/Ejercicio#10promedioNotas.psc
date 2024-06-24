Proceso promedioDeNotas
	Definir nota1,nota2,nota3 Como Real
	Escribir "Escriba el nombre del alumno"
	leer alumno
	Escribir "Digite las 3 notas del alumno: ",alumno
	leer nota1,nota2,nota3
	promedio_notas = (nota1+nota2+nota3) / 3
	Escribir "La nota promedio de ",alumno, " es de:",promedio_notas
FinProceso
