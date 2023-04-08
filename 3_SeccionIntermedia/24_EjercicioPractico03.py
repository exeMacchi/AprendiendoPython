# Ejercicio: faltó el profesor de una clase y los alumnos decidieron armar la clase ellos
# mismos. Para eso, el alumno con mayor edad será el profesor y el alumno con menor edad 
# su asistente:
# 1) Pedir los nombres y la edad de los compañeros que vinieron a clase.
# 2) Ordenar el listado de alumnos de menor a mayor y mostrarlo.
# 3) Indicar cuál sería el profesor y cuál sería el asistente.

def pedir_informacion_alumnos(cantidad_alumnos):
    listado_alumnos = list()
    for i in range(cantidad_alumnos):
        print(f"------ Información del alumno {i + 1} ------")
        nombre_alumno = input("Nombre del alumno: ")
        edad_alumno = int(input("Edad del alumno: "))
        listado_alumnos.append((nombre_alumno, edad_alumno))
    return listado_alumnos

def ordenar_listado_alumnos(lista_alumnos):
    lista_alumnos.sort(key = lambda x: x[1])

def mostrar_listado_alumnos(lista_alumnos):
    print("\n------ Listado de alumnos ------")
    for i, (alumno, edad) in enumerate(lista_alumnos):
        print(f"{i + 1}. {alumno}, {edad}")

def buscar_profesor_y_asistente(lista_alumnos):
    profesor = str()
    asistente = str()
    for i, alumno in enumerate(lista_alumnos):
        if i == 0:
            asistente = alumno[0]
        elif i == len(lista_alumnos) - 1:
            profesor = alumno[0]
    return asistente, profesor


cantidad_alumnos_clase = 5
print("1) Pedir información de los alumnos.")
lista_alumnos = pedir_informacion_alumnos(cantidad_alumnos_clase)

print("\n2) Ordenar la lista y mostrarla.")
ordenar_listado_alumnos(lista_alumnos)
mostrar_listado_alumnos(lista_alumnos)

print("\n3) ¿Quién es el profesor y el asistente?")
asistente, profesor = buscar_profesor_y_asistente(lista_alumnos)
print(f"El profesor es: {profesor}")
print(f"El asistente es: {asistente}")