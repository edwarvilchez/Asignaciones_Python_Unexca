"""
1. Calculadora de UC: Crea un programa que reciba la cantidad de materias inscritas
y multiplique cada una por las 5 Unidades de Crédito (UC) de la materia para dar el
total de carga académica.
"""
# constante para la cantidad de materias inscritas
UC_POR_MATERIA = 5

materias = int(input("Ingrese la cantidad de Materias: "))
total_uc = materias * UC_POR_MATERIA

# imprimir el resultado
print(f"EL Total de Unidades de Crédito (UC) es: {total_uc}")