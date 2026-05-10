"""Calculadora de UC: Crea un programa que reciba la cantidad de materias inscritas y multiplique cada una por las 5 Unidades de Crédito (UC) de la materia para dar el total de carga académica."""
materias = int(input("Ingrese la cantidad de Materias Inscritas: ")) 
uc_por_materia = 5
carga_academica_total = materias * uc_por_materia
print("La carga academica total es de: ", carga_academica_total, "UC") 