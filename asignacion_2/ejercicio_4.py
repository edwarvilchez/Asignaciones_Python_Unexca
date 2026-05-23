"""
4. Promedio de notas: Dado que el alumno recibe una nota de 10 en el examen de Diagnóstica y el Taller (ambos de 0 a 20). Calcula el promedio y muestra
"Aprobado" si es mayor a 12.

"""
nota_diagnostica = float(input("Ingresar la Nota de la Prueba Diagonostica: " ))

nota_taller = float(input("Ingresar la Nota del Taller: "))

# promedio es la suma de todas las notas divididad entre la cantidad de notas
promedio = (nota_diagnostica + nota_taller) / 2

# Ciclo if para comparar las notas cargadas con la nota base (12)
if promedio >= 12:
    print(f"La Nota Promedio del Padawan es: {promedio:.2f} que es mayor a 12. Y esta Aprobado")
else: 
    print(f"La Nota Promedio del Padawan {promedio:.2f}  que es menor a 12. Y esta No Aprobado")
