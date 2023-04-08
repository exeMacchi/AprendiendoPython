# Creando listas con la funcion list()
lista_cadena = list("Cadena")               # ['C', 'a', 'd', 'e', 'n', 'a']
lista_vacia = list()                       # []
lista_persona = list(["Exequiel", 23, 1.74])  # ["Exequiel", 23, 1.74]

# Saber la cantidad de elementos de una lista
cant_elementos_lista_cadena = len(lista_cadena)  # 6
cant_elementos_lista_vacia = len(lista_vacia)   # 0
cant_elementos_lista_persona = len(lista_persona)  # 3

# Saber el índice de un elemento
indiceCadena = lista_cadena.index('n')    # 4
indicePersona = lista_persona.index(1.74)  # 2

# Agregar un elemento al final de la lista
lista_cadena.append(" texto")     # ['C', 'a', 'd', 'e', 'n', 'a', ' Texto']
lista_vacia.append(37)            # [37]
lista_persona.append("Argentina")  # ['Exequiel', 23, 1.74, 'Argentina']


# Agregar un elemento en un índice específico
# ['C', 'a', 'd', 'e', 'n', 'a', ' de', ' Texto']
lista_cadena.insert(len(lista_cadena) - 1, " de")
lista_vacia.insert(0, 27)                          # [27, 37]
# ['Exequiel', 23, 1.74, 'Rio Negro', 'Argentina']
lista_persona.insert(3, "Rio Negro")

# Agregar elementos a una lista
# ['C', 'a', 'd', 'e', 'n', 'a', ' de', ' Texto', ' de prueba']
lista_cadena.extend([" de prueba"])
# ['Exequiel', 23, 1.74, 'Rio Negro', 'Argentina', 27, 37]
lista_persona.extend(lista_vacia)
lista_vacia.extend(lista_vacia)     # [27, 37, 27, 37]

# Eliminar y devolver el último elemento
lista_vacia.pop()  # Devuelve y elimina el 37 ---> [27, 37, 27]

# Eliminar y devolver un elemento en un indice específico (positivo, de inicio a fin)
# Devuelve y elimina el 1.74 ---> ['Exequiel', 23, 'Rio Negro', 'Argentina', 27, 37]
lista_persona.pop(2)

# Eliminar y devolver un elemento en un índice específico (negativo, de fin a inicio)
# Devuelve y elimina ' Texto' ---> ['C', 'a', 'd', 'e', 'n', 'a', ' de', ' de prueba']
lista_cadena.pop(-2)

# Eliminar la primera ocurrencia de un elemento en una lista
lista_vacia.remove(27)  # Elimina el primer 27 ---> [37, 27]

# Eliminar todos los elementos de una lista
lista_vacia.clear()  # []

# Ordenar una lista
lista_numeros = [9, 3, 1, 6, 7, 2, 10, 4, 8, 5]
# Ordenar una lista de forma ascendente (por defecto)
lista_numeros.sort()  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Ordenar una lista de forma descendente
lista_numeros.sort(reverse=True)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Invertir los elementos en una lista
lista_persona.reverse()
# ['Exequiel', 23, 'Rio Negro', 'Argentina', 27, 37] ---> [37, 27, 'Argentina', 'Rio Negro', 23, 'Exequiel]
