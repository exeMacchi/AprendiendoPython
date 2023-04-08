# Declaración de una lista de elementos (mutable)
lista_persona = ["Exequiel Lautaro Macchi", 23, 1.74, True]
print(lista_persona[0])

# Declaración de una tupla de elementos (inmutable)
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupla_numeros[4])

# Declaracion de un conjunto de elementos (set)
conjunto_mixto = {42, "Manzana", 32.78, 'C', "Manzana"} 
# La palabra "Manzana" duplicada no se imprimirá
print(conjunto_mixto)

# Declaración de un diccionario (dict)
diccionario_personas = {
    "Juan": 45,
    "Maria": 37,
    "Pedro": 28
}
print(diccionario_personas["Maria"])