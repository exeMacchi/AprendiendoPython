# 1) Crear un conjunto utilizando la función set()
conjunto = set(["dato1", "dato2"])

print(f"1) {conjunto}\n")

# 2) Crear un conjunto con otro conjunto (inmutable)
conjunto_uno = frozenset({"dato3", "dato4"})
conjunto_dos = {"dato5", conjunto_uno}

print(f"2) {conjunto_dos}\n")

# 3) Teoría de conjuntos
conjunto_A = {1, 3, 7, 12, 22}
conjunto_B = {1, 7, 3}
print("3) Teoria de conjuntos")
print(f"Conjunto A: {conjunto_A}")
print(f"Conjunto B: {conjunto_B}\n")

# a) Subconjunto
respuesta = conjunto_A.issubset(conjunto_B)
print(f"a) ¿Es el conjunto A un subconjunto del conjunto B?   --> {respuesta}")

# b) Subconjunto
respuesta = conjunto_B <= conjunto_A
print(f"b) ¿Es el conjunto B un subconjunto del conjunto A?   --> {respuesta}")

# c) Superconjunto
respuesta = conjunto_A.issuperset(conjunto_B)
print(f"c) ¿Es el conjunto A un superconjunto del conjunto B? --> {respuesta}")

# d) Superconjunto
respuesta = conjunto_B > conjunto_A
print(f"d) ¿Es el conjunto B un superconjunto del conjunto A? --> {respuesta}")

# e) ¿Tienen elementos en común?
respuesta = conjunto_A.isdisjoint(conjunto_B)
print(f"e) ¿Los conjuntos tienen elementos diferentes? ---> {respuesta}")

# f) Unión
print(f"f) Unión de los conjuntos: {conjunto_A | conjunto_B}")

# g) Intersección
print(f"g) Intersección de los conjuntos: {conjunto_A & conjunto_B}")

# h) Diferencia
print(f"h) Diferencia de los conjuntos: {conjunto_A - conjunto_B}")

# i) Diferencia simétrica
print(f"i) Diferencia simétrica entre los conjuntos: {conjunto_A ^ conjunto_B}")
