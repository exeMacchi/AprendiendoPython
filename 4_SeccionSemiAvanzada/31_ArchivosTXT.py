# -------------------------------- APERTURA ---------------------------------- #
# Abrir un archivo de texto (.txt), con encoding utf-8 para la lectura de 
# caracteres y los diacríticos del español.
    # archivo_de_texto = open("4_SeccionSemiAvanzada\\Archivos\\texto_de_prueba.txt", 
    #                         "r", encoding="UTF-8")

# Abrir un archivo de texto (.txt), con encoding utf-8 para la escritura de 
# caracteres y los diacríticos del español.
    # archivo_de_texto = open("4_SeccionSemiAvanzada\\Archivos\\texto_de_prueba.txt", 
    #                         "w", encoding="UTF-8")


# -------------------------------- LECTURA ----------------------------------- #
# Leer y mostrar todo el contenido del archivo.txt
    # todo_el_contenido = archivo_de_texto.read()
    # print(todo_el_contenido)

# Leer y mostrar la primera línea del archivo.txt
    # primera_linea = archivo_de_texto.readline()
    # print(primera_linea)

# Leer y mostrar todas las líneas del archivo.txt. Usar con cuidado, ya que este método
# en archivos muy grandes consume muchos recursos.
    # lineas = archivo_de_texto.readlines()
    # print(lineas)

# ------------------------------- ESCRITURA ---------------------------------- #
# Escribir una cadena completa en el archivo.
    # archivo_texto.write("Linea 1\nLinea 2\nLinea 3\n")

# Escribir varias líneas en el archivo.
    # lineas = ["Linea 1", "Linea 2", "Linea 3"]
    # archivo_texto.writelines(lineas)


# ------------------------------- CLAUSURA ----------------------------------- #
# Cerrar el archivo de texto (importante)
    # archivo_de_texto.close()


# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
# Forma de abrir y leer óptimamente un archivo.txt en Python
with open("4_SeccionSemiAvanzada\\Archivos\\texto_de_prueba.txt", "r",
          encoding="UTF-8") as archivo_texto:
    linea = archivo_texto.readline()
    print(linea)
print("Proceso de lectura exitoso.")

# Forma de abrir y escribir óptimamente en un archivo.txt en Python
with open("4_SeccionSemiAvanzada\\Archivos\\texto_de_prueba.txt", "a",
          encoding="UTF-8") as archivo_texto:
          archivo_texto.write("\nEsta línea de texto fue agregada desde el " +
                              "método write(), pero las siguientes serán " +
                              "agregadas desde el método writelines()\n")

          archivo_texto.writelines([f"Linea {numero}\n" for numero in range(1, 11)])
print("Proceso de escritura exitoso.")
