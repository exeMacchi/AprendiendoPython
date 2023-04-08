# Módulo básico con el cual se trabajan las expresiones regulares
import re

texto_largo = """\
Este es un texto de prueba relativamente largo para la búsqueda de coincidencias 
partir del uso de expresiones regulares en Python.
Esta sería la línea número tres (3) del texto.
Tanto los perros como los gatos son animales domésticos muy populares. Además,
en la naturaleza existen muchas razas de perros y gatos.
Boca Juniors se fundó el 3 de abril de 1905.
Esta sería la línea número seis (6) del Texto.
"""

texto_corto = """\
Este es un texto corto de dos (2) líneas para buscar coincidencias.
Esta sería la segunda línea.
"""

# ---------------------------------------------------------------------------- #
# 1) Buscar una coincidencia simple en el texto.
coincidencia = re.search("Python", texto_largo)
if coincidencia:
    print(f"1) Se encontró la palabra '{coincidencia.group()}' en el texto " +
          f"(índice {coincidencia.start()})\n")
# ---------------------------------------------------------------------------- #
# 2) Buscar concidencias simples en el texto.
coincidencias = re.findall("Perros", texto_largo, flags = re.IGNORECASE)
if coincidencias:
    print(f"2) Se encontraron {len(coincidencias)} coincidencias de la palabra " + 
          f"'perros' en el texto: {coincidencias}\n")
# ---------------------------------------------------------------------------- #
# 3) 
print("3)")
# a) Búsqueda de dígitos numéricos en el texto (ahora sí usando expresiones regulares)
coincidencias = re.findall(r"\d", texto_largo)
if coincidencias:
    print(f"a) Se encontraron {len(coincidencias)} dígitos numéricos en el texto: {coincidencias}")
else:
    print("a) No se encontraron dígitos numéricos en el texto.")

# b) También se podría buscar todo menos dígitos numéricos de la siguiente forma:
coincidencias = re.findall(r"\D", texto_corto)
if coincidencias:
    print(f"b) Se encontraron {len(coincidencias)} caracteres no numéricos en el texto: {coincidencias}\n")
else:
    print("b) Solo se encontraron dígitos numéricos en el texto.\n")
# ---------------------------------------------------------------------------- #
# 4) 
print("4)")
# a) Búsqueda de caracteres alfanuméricos en el texto (a-z, A-Z, 0-9, _)
coincidencias = re.findall(r"\w", texto_corto)
if coincidencias:
    print(f"a) Se encontraron {len(coincidencias)} caracteres alfanuméricos " +
          f"en el texto: {coincidencias}")
else:
    print("a) No se encontraron caracteres alfanuméricos en el texto.")

# b) Búsqueda de caracteres no alfanuméricos.
coincidencias = re.findall(r"\W", texto_corto)
if coincidencias:
    print(f"b) Se encontraron {len(coincidencias)} caracteres no alfanuméricos " +
          f"en el texto: {coincidencias}\n")
else:
    print("b) No se encontraron caracteres no alfanuméricos en el texto.\n")
# ---------------------------------------------------------------------------- #
# 5) 
print("5)")
# a) Búsqueda de espacios en blanco (espacios, tabulaciones y nuevas líneas)
coincidencias = re.findall(r"\s", texto_largo)
if coincidencias:
    print(f"a) Se encontraron {len(coincidencias)} espacios en blanco en el texto: {coincidencias}")
else:
    print("a) No se encontraron espacios en blanco en el texto.")

# b) Búsqueda de todo, menos espacios en blanco.
coincidencias = re.findall(r"\S", texto_corto)
if coincidencias:
    print(f"b) Se encontraron {len(coincidencias)} caracteres en el texto que no son " +
          f"espacios en blanco: {coincidencias}\n")
else:
    print("b) En el texto solo hay espacios en blanco.\n")
# ---------------------------------------------------------------------------- #
# 6)
print("6)")
# a) Búsqueda de saltos de línea
coincidencias = re.findall(r"\n", texto_largo)
if coincidencias:
    print(f"a) Se encontraron {len(coincidencias)} saltos de línea en el texto: {coincidencias}")
else:
    print("a) No se encontraron saltos de línea en el texto.")

# b) Búsqueda de todo, menos saltos de línea.
coincidencias = re.findall(r".", texto_corto)
if coincidencias:
    print(f"b) Se encontraron {len(coincidencias)} caracteres en el texto menos " +
          f"saltos de línea: {coincidencias}\n")
else:
    print("b) Solo se encontraron saltos de línea en el texto.\n")
# ---------------------------------------------------------------------------- #
# 7) Búsqueda de un caracter especial, en este caso, el punto.
coincidencias = re.findall(r"\.", texto_largo)
if coincidencias:
    print(f"7) Se encontraron {len(coincidencias)} puntos '.' en el texto: {coincidencias}\n")
else:
    print("7) No se encontraron puntos '.' en el texto", end="\n\n")
# ---------------------------------------------------------------------------- #
# 8) Buscar una cadena en el texto. En este caso, se busca un dígito rodeado por
# paréntesis.
coincidencias = re.findall(r"\(\d\)", texto_largo)
if coincidencias:
    print(f"8) Se encontraron {len(coincidencias)} coincidencias en el texto de la " +
          f"búsqueda deseada: {coincidencias}\n")
# ---------------------------------------------------------------------------- #
# 9) Búsqueda de un patrón en el inicio de cada nueva línea del texto.
coincidencias = re.findall(r'^Esta', texto_largo, flags = re.MULTILINE)
if coincidencias:
    print(f"9) Se encontraron {len(coincidencias)} coincidencias en el texto de la " +
          f"búsqueda deseada: {coincidencias}\n")
# ---------------------------------------------------------------------------- #
# 10) Búsqueda de un patrón al final de cada línea del texto.
coincidencias = re.findall(r'texto.$', texto_largo, flags = re.MULTILINE | re.IGNORECASE)
if coincidencias:
    print(f"10) Se encontraron {len(coincidencias)} coincidencias en el texto de la " +
          f"búsqueda deseada: {coincidencias}\n")
# ---------------------------------------------------------------------------- #
# 11) 
print("11)")
# a) Buscar n cantidad de veces un patrón. En este caso, buscar cuatro dígitos seguidos.
coincidencias = re.findall(r"\d{4}", texto_largo)
if coincidencias:
    print(f"a) Se encontraron {len(coincidencias)} coincidencias en el texto de la " +
          f"búsqueda deseada: {coincidencias}")
    
# b) Buscar de n a m cantidad de veces un patrón. En este caso, un rango de dígitos.
coincidencias = re.findall(r"\d{1,4}", texto_largo)
if coincidencias:
    print(f"b) Se encontraron {len(coincidencias)} coincidencias en el texto de la " +
          f"búsqueda deseada: {coincidencias}\n")
# ---------------------------------------------------------------------------- #
# 12) Buscar una expresión u otra (puede devolver ambas).
coincidencias = re.findall(r'perros|gatos|\d{2}', texto_largo, flags=re.IGNORECASE)
if coincidencias:
    print(f"12) Se encontró {len(coincidencias)} coincidencias en el texto de la " +
          f"búsqueda deseada: {coincidencias}")
