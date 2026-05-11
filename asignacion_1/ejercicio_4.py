
    
"""
# Nivel Intermedio        
4. Sistema de Notas (Corte 2): Un programa que reciba la nota de la Evaluación Diagnóstica y el Taller (ambos de 0 a 20). Calcula el promedio y muestra "Aprobado" si es mayor a 10. 
         
"""
nota_diagnostica = float(input("Ingrese la nota de la Evaluación Diagnóstica (0-20): "))
nota_taller = float(input("Ingrese la nota del Taller (0-20): "))
promedio = (nota_diagnostica + nota_taller) / 2
    # si el promedio es mayor a 10, muestra "Aprobado"
if promedio >= 10:
        print("Aprobado")
else:
        print("Reprobado")
        
    