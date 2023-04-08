# Formas de crear una tupla

# 1) Tupla vacía usando la función tuple()
tupla = tuple()
print(f"1) {tupla}\n")

# 2) Creando una tupla usando la función tuple()
print("2)")
# a) Con elementos de una lista
tupla = tuple(["dato1", "dato2", "dato3"])
print(f"  a) {tupla}")
# b) Con elementos de una tupla
tupla = tuple(("dato3", "dato4", "dato5"))
print(f"  b) {tupla}\n")

# 3) Creando una tupla sin paréntesis
print("3)")
# a) Con múltiples datos
tupla = "dato6", "dato7"
print(f"  a) {tupla}")
# b) Con un solo dato
tupla = "dato8",
print(f"  b) {tupla}\n")