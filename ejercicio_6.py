"""
6. Descuento en Inscripción: Si un estudiante tiene un promedio superior a 18, aplica un 15% de descuento a su matrícula. Muestra el monto final a pagar.    
"""

matricula = float(input("Ingrese el monto de la Matrícula:"))
promedio_padawan = float(input("Ingrese el promedio del Padawan: "))

# condicional if
if promedio_padawan > 18:
    descuento = matricula * 0.15
    print(f"El monto final a pagar es de: {matricula - descuento:.2f} ")
else:
    print("No aplica descuento")
