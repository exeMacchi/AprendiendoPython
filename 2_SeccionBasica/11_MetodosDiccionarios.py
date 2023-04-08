diccionario = {
    'nombre': "Exequiel",
    'apellido': "Macchi",
    'edad': 23,
    'pais': "Argentina"
}

# Devolver todas las claves de un diccionario. El método devuelve dict_items.
claves = diccionario.keys()
print(claves)

# Obtener un valor a patir de su clave. El método evita que se lance una excepción
# en caso de no encontrar el valor asociado a la clave especificada.
valor = diccionario.get('edad')
print(valor)

# Obtener un diccionario iterable.
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

# Eliminar un elemento del diccionario.
diccionario.pop('pais')
print(diccionario)

# Eliminar todos los elementos (keys & values) de un diccionario.
diccionario.clear()
print(diccionario)
