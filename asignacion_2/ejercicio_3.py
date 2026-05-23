""""
3. Conversor de Estatura: Dado que el facilitador mide 1.80 metros, pide al alumno
su estatura y calcula la diferencia en centímetros respecto a la del profesor.

"""

# declaramos las variables
ESTATURA_PROFESOR = 1.80
estatura_padawan = float(input("Ingresar la estatura en metros (ej 1.70): "))

# calcular la diferencia en centímetros
diferencia_cm = (ESTATURA_PROFESOR - estatura_padawan) * 100
print(f"La diferencia en centímetros es: {diferencia_cm:.2f} cm") 