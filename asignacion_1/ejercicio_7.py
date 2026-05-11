"""
{
    
 7. Clasificador de Datos: Pide al usuario que ingrese un valor y determina si es un número entero, un decimal o una cadena de texto (String). 
    
}    
"""
# declaración de variables
entrada = input("Ingrese un Valor: ")
# bloque try except para manejar errores
try:
    if "," in entrada:
        print("Es un número decimal con coma (Flotante)")
    elif "." in entrada:
        print("Es un número decimal sin coma (Flotante)")
    elif entrada.isdigit():
        print("Es un número entero")
    else:
        print("Es una cadena de texto")
except ValueError:
    print("Error: El valor ingresado no es válido")