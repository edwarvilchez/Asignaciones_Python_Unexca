"""
  8. Contador de Semanas: Crea un bucle que imprima los días de clase (Martes, Miércoles, Viernes) por cada semana de Marzo planificada (del 23/03 al 28/03).  
"""
# declaración de variables
dias_clase = ["Martes", "Miércoles", "Viernes"]
# Simulación de la semana
for i in range(1,16): # Podemos ajustar el rango para simular más semanas si es necesario
    print(f"Semana {i}:")
    for dia in dias_clase:
        print(dia)
