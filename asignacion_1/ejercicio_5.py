"""
5. Validador de Laboratorio: El programa debe preguntar el número de laboratorio. Si el usuario ingresa "LF6-LAB", permite el acceso; de lo contrario, indica "Aula incorrecta".
"""
# declaración de variables
aula = input("Ingrese el número del laboratorio: ").upper()  
# Convertir a mayúsculas para evitar problemas de comparación
# condicional if
if aula == "LF6-LAB":
    print("Acceso permitido")
else:
    print("Aula Incorrecta")
