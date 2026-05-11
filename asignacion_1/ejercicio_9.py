""""
9. Simulador de Intentos de Login: Crea un sistema que pida una clave de acceso al proyecto Nominus. El usuario tiene solo 3 intentos antes de que el programa se bloquee.
"""

# declaración de variables
clave_correcta = "Nominus2026"
intentos = 3

# condicional while
while intentos > 0:
    password = input("Ingrese la clave de acceso: ")
    if password == clave_correcta:
        print("Acceso concedido. Bienvenido a Nominus.")
        break
    else:
        intentos -= 1
        print("Acceso denegado. Intentos restantes:", intentos)       

if intentos == 0:
    print("Acceso bloqueado. Se ha agotado el número máximo de intentos.")