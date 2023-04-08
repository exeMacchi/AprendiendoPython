# Ejercicio: tenemos dos listas, una con nombres y otra con apellidos. La idea
# es escribir los datos en un archivo de texto de forma óptima con un bucle for

import os

lista_nombres = ["Exequiel", "Ailén", "Eliana", "Darío", "Akane"]
lista_apellidos = ["Macchi", "Muñoz", "Gómez", "Muñoz", "Akono"]

ruta_archivo = "4_SeccionSemiAvanzada\\Archivos\\ejercicio_practico_06.txt"

with open(ruta_archivo, "w", encoding="UTF-8") as txt:
    for i, (nombre, apellido) in enumerate(zip(lista_nombres, lista_apellidos)):
        txt.writelines([f"{i + 1}. {nombre} {apellido}\n"])
    