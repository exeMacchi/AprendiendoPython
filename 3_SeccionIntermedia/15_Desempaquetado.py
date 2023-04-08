# Desempaquetando una tupla
tupla_persona = ("Exequiel", "Macchi", 23)
nombre, apellido, edad = tupla_persona

print("Desempaquetando una tupla:")
print(nombre)
print(apellido)
print(edad)
print("--------------------------")

# Desempaquetando una lista
lista = [1, 2, 3]
a, b, c, *d = lista # En este ejemplo, d es una lista vacía.

print("Desempaquetando una lista:")
print(a)
print(b)
print(c)
print(d)
print("--------------------------")

# Desempaquetando una cadena de caracteres
p, r, *u = "Prueba"

print("Desempaquetando una cadena de caracteres:")
print(p)
print(r)
print(u)
print("--------------------------")

# Desempaquetando un diccionario
diccionario_persona = {
    'nombre': "Exequiel",
    'apellido': "Macchi",
    'edad': 23,
    'altura': 1.75
}

key_nombre, key_apellido, key_edad, key_altura = diccionario_persona.keys()
value_nombre, value_apellido, value_edad, value_altura = diccionario_persona.values()

print("Desempaquetando un diccionario:")
print(f"Claves: {key_nombre}, {key_apellido}, {key_edad}, {key_altura}")
print(f"Valores: {value_nombre}, {value_apellido}, {value_edad}, {value_altura}")
print("--------------------------")