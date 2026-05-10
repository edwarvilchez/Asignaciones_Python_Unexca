"""
Conversor de Estatura: Dado que el facilitador mide 1.80 metros, pide al alumno su estatura y calcula la diferencia en centímetros respecto a la del profesor.
"""
estatura_del_profesor = 1.80  # en metros
estatura_del_padawan = float(input("Ingrese su estatura en metros (ej 1.70): "))
diferencias = abs(estatura_del_profesor - estatura_del_padawan) * 100
print(f"La diferencia con respecto al profesor es de: {diferencias:.2f} cm") 