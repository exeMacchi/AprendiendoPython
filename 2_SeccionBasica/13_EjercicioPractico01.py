max_hs_cursos_generales = 7     # curso más lento
min_hs_cursos_generales = 2.5   # curso más rápido
pro_hs_cursos_generales = 4     # curso promedio
hs_crudo_generales = 5 # ---> 4

hs_curso_actual = 1.5
hs_crudo_actual = 3.5  # ---> 1.5

# Ejercicios de diferencias entre cursos generales y este curso de Python
# 1) Diferencia en porcentaje entre los cursos
    # a) Entre el actual y el más rápido.
    # b) Entre el actual y el más lento.
    # c) Entre el actual y el promedio.

# 2) Porcentaje de material inservible que se reduce en:
    # a) El promedio de los cursos.
    # b) El curso actual.

# 3) ¿Cuánto equivale ver?
    # a) 10 horas del curso actual en demás cursos.
    # b) 10 horas de los demás cursos en el actual.
    
# 1) 
# a)
print("El curso actual dura un: ")
percent_curso_actual = int((hs_curso_actual * 100) / min_hs_cursos_generales)
percent_diferencia_actual_minimo = 100 - percent_curso_actual
print(f"a) {percent_diferencia_actual_minimo}% menos que el curso más rápido.")

# b)
percent_curso_actual = int((hs_curso_actual * 100) / max_hs_cursos_generales)
percent_diferencia_actual_max = 100 - percent_curso_actual
print(f"b) {percent_diferencia_actual_max}% menos que el curso más lento.")

# c)
percent_curso_actual = int((hs_curso_actual * 100) / pro_hs_cursos_generales)
percent_diferencia_actual_pro = 100 - percent_curso_actual
print(f"c) {percent_diferencia_actual_pro}% menos que el curso promedio.\n")

# 2)
# a)
dif_hs_crudo_general = hs_crudo_generales - pro_hs_cursos_generales
percent_crudo_general = int((dif_hs_crudo_general * 100) / hs_crudo_generales)
print("Porcentaje de material inservible removido de los cursos generales: " +
     f"{percent_crudo_general}%")

#b)
dif_hs_crudo_actual = hs_crudo_actual - hs_curso_actual
percet_crudo_actual = int((dif_hs_crudo_actual * 100) / hs_crudo_actual)
print("Porcentaje de material inservible removido del curso actual: " +
     f"{percet_crudo_actual}%\n")

# 3)
# a)
diez_hs_curso_lento    = (10 * max_hs_cursos_generales) / hs_curso_actual
diez_hs_curso_rapido   = (10 * min_hs_cursos_generales) / hs_curso_actual
diez_hs_curso_promedio = (10 * pro_hs_cursos_generales) / hs_curso_actual

print(f"""Diez horas del curso actual equivaldrían a:
a) {round(diez_hs_curso_rapido, 2)} horas del curso más rápido.
b) {round(diez_hs_curso_lento, 2)} horas del curso más lento.
c) {round(diez_hs_curso_promedio, 2)} horas de cursos promedio.\n""")

# b)
diez_hs_curso_actual_lento = 10 - (10 * (percent_diferencia_actual_max / 100))
diez_hs_curso_actual_rapido = 10 - (10 * (percent_diferencia_actual_minimo / 100))
diez_hs_curso_actual_promedio = 10 - (10 * (percent_diferencia_actual_pro / 100))

print("Diez horas del curso más lento equivalen a " + 
     f"{round(diez_hs_curso_actual_lento, 2)} horas del curso actual.")
print("Diez horas del curso más rápido equivalen a " + 
     f"{round(diez_hs_curso_actual_rapido, 2)} horas del curso actual.")
print("Diez horas de cursos promedio equivalen a " + 
     f"{round(diez_hs_curso_actual_promedio, 2)} horas del curso actual.\n")
