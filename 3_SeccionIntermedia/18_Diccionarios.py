# 1) Declaración de un diccionario vacío con la función dict()
diccionario_vacio = dict()
print(f"1) {diccionario_vacio}")

# 2) Declaración de un diccionario con elementos con la función dict()
diccionario_con_elementos = dict(nombre = "Exequiel", apellido = "Macchi", edad = 23)
print(f"2) {diccionario_con_elementos}")

# 3) Declaración de un diccionario con un conjunto inmutable (frozenset)
diccionario_con_conjunto = { frozenset(['A', 'B']): "C" }
print(f"3) {diccionario_con_conjunto}")

# 4) Declaración de un diccionario utilizando el método dict.fromkeys(), con valor por defecto
diccionario_valores_por_defecto = dict.fromkeys(['nombre', 'apellido'], "X")
print(f"4) {diccionario_valores_por_defecto}")

# 5) Declaración de un diccionario utilizando el método dict.fromkeys(), con valor inicial
diccionario_valores_none = dict.fromkeys("ABCDE")
print(f"5) {diccionario_valores_none}")