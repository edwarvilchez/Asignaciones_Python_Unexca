"""
Registro de Asistencia: Solicita el nombre del estudiante y el día de la semana (Martes, Miércoles o Viernes). Si el día es correcto, imprime un mensaje de "Bienvenido a la sesión presencial".
"""
nombre = input("Ingrese el Nombre del Estudiante: ")
dia = input("Ingrese el Día de la Semana (Martes, Miércoles o Viernes): ").capitalize()
dias_validos = ["Martes", "Miércoles", "Viernes"]

# ciclo de decisiones if
if dia in dias_validos:
    print("Bienvenido a la sesión presencial, ", nombre)