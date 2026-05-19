"""
2. Registro de Asistencia: Solicita el nombre del estudiante y el día de la semana
(Martes, Miércoles o Viernes). Si el día es correcto, imprime un mensaje de
"Bienvenido a la sesión presencial"
"""

def validar_asistencia():
    DIAS_PERMITIDOS = ["Martes", "Miércoles", "Miercoles", "Viernes"]
    
    nombre = input("Ingresa tu Nombre de Aprendiz Padawan: ")
    dia_ingresado = input("Ingresa el día de la semana: ").strip().capitalize()
    
    # condicional if
    if dia_ingresado in DIAS_PERMITIDOS:
        print(f"Bienvenido a la sesión presencial, { nombre }!")
    else: 
        print(f"Día no válido para la sesión presencial, { nombre }!")
    
if __name__ == "__main__":
    validar_asistencia() 