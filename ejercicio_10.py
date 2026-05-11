"""
  10 Promedio del Semestre: Solicita las notas de los 4 cortes (25% cada uno). Calcula la nota final acumulada y determina si el estudiante exime la defensa final  
  (promedio superior a 12) o no (promedio inferior a 10).

"""
# declaración de variables 
suma_notas = 0
promedio = suma_notas / 4

# ciclo for para solicitar las notas de los 4 cortes
for i in range(1, 5):
    nota = float(input("Ingrese las notas de la clase: "))
    suma_notas += nota
    print(f"Nota de la clase {i}: {nota}")

# calcular el promedio
promedio = suma_notas / 4


# condicional if
if promedio > 12:
    print("Promedio superior a 12. Estudiante exime la defensa final.")
else:
    print("Promedio inferior a 10. No exime la defensa final.")