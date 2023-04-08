cadena_de_prueba = "   Cadena de prueba 2023   "

# ¿Qué métodos y atributos se pueden aplicar a una cadena?
print(f"Métodos y atributos disponibles: {dir(cadena_de_prueba)}\n")

# Eliminar los espacios en blanco del principio y del final de una cadena.
print(f"Cadena original:{cadena_de_prueba}\n")
print(f"Cadena sin espacios innecesarios: {cadena_de_prueba.strip()}\n")
cadena_de_prueba = cadena_de_prueba.strip()

# Convertir una cadena en mayúsculas
print(f"Cadena en mayúsculas: {cadena_de_prueba.upper()}\n")

# Convertir una cadena en minúsculas
print(f"Cadena en minúsculas: {cadena_de_prueba.lower()}\n")

# Convertir la primera letra de la cadena en mayúsculas.
print(f"Primera letra mayúscula: {cadena_de_prueba.capitalize()}\n")

# Convertir la primera letra de cada palabra de la cadena en mayúsculas.
print(f"Primera letra de cada palabra en mayúsculas: {cadena_de_prueba.title()}\n")

# Índice primera ocurrencia de una subcadena. Devuelve -1 si no la halla.
print(f"Índice primera ocurrencia 'prueba': {cadena_de_prueba.find('prueba')}\n")

# Verifica si existe una subcadena en la cadena dada.
print(f"La fecha '2023' aparece en la cadena ---> {'2023' in cadena_de_prueba}\n")

# Verifica la no existencia de una subcadena en la cadena dada.
print(f"La palabra 'Python' no aparece en la cadena ---> {'Python' not in cadena_de_prueba}\n")

# Indice primera ocurrencia de una subcadena. Devuelve una excepción si no la halla.
print(f"Índice primera ocurrencia 'de': {cadena_de_prueba.index('de')}\n")

# Verificar si una cadena es numérica.
print(f"¿La cadena es numérica? ---> {cadena_de_prueba.isnumeric()}\n")

# Verificar si una cadena es alfabética.
print(f"¿La cadena es alfabética? ---> {cadena_de_prueba.isalpha()}\n")

# Contar cantidad de ocurrencias de una subcadena.
print(f"¿Cuántas veces aparece la letra 'a' en la cadena? ---> {cadena_de_prueba.count('a')}\n")

# Saber cuántos caracteres tiene una cadena.
print(f"¿Cuántos caracteres tiene la cadena? ---> {len(cadena_de_prueba)}\n")

# Verificar si una cadena empieza con una subcadena especificada.
print(f"¿La cadena empieza con 'C'? ---> {cadena_de_prueba.startswith('C')}\n")

# Verificar si una cadena termina con una subcadena especificada.
print(f"¿La cadena termina con 'prueba'? ---> {cadena_de_prueba.endswith('prueba')}\n")

# Reemplazar subcadenas coincidentes de una cadena por otras subcadenas.
print(f"Cadena con reemplazo de la letra 'a' por 'e': {cadena_de_prueba.replace('a', 'e')}\n")

# Dividir una cadena en subcadenas a partir de un delimitador.
# En este ejemplo, se utiliza el delimitador por defecto que es el espacio.
print(f"Lista de subcadenas de la cadena original: {cadena_de_prueba.split()}\n")
