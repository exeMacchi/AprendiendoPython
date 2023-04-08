# Definición de variables enteras
a = 5
b = 10
c = a + b
print(c)

# Definición de variables strings
nombre = "Exequiel"
bienvenida = f"Hola, {nombre}, ¿cómo estás?"
del nombre # Se elimina la variable nombre
print(bienvenida)

# Uso de operadores de pertenencia (in / not in)
print("¿Aparece 'Exequiel' en el saludo de bienvenida? ---> ", end = "")
print("Exequiel" in bienvenida)

print("¿No aparece 'Exequiel' en el saludo de bienvenida? ---> ", end = "")
print("Exequiel" not in bienvenida)