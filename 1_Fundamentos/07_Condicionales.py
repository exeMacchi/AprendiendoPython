edad = 17
if edad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")

# Mismo ejemplo, pero utilizando el operador ternario.
print("Sos mayor de edad" if edad > 17 else "Sos menor de edad", end="\n\n")

# ------------------------- #

password_DB = "AprendiendoPython"
password_Usuario = "AprendiendoPython"

if password_DB == password_Usuario:
    print("Iniciando sesión...\n")
else:
    print("Error: la contraseña ingresada no es correcta.\n")

# ------------------------- #

cantidad_de_productos = 20

if cantidad_de_productos >= 50:
    print("Descuento del 50%\n")
elif cantidad_de_productos >= 20:
    print("Descuento del 20%\n")
else:
    print("No hay descuento\n")

# ------------------------- #
# If anidados
salario_minimo = 10000
ingreso_mensual = 15000
gasto_mensual = 15001

if ingreso_mensual >= salario_minimo:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en déficit.\n") 
    elif ingreso_mensual - gasto_mensual > 5000:
        print("Estás bien económicamente.\n")
    else:
        print("Aunque no estás en déficit, estás gastando más de lo que deberías.\n")

else:
    print("Estás ganando menos que el salario mínimo.\n")

# ------------------------- #
# Cadena de comparadores
edad = 64
# En vez de poner 'edad > 17 and edad < 60', la comparación se puede resumir en:
if 17 < edad < 60:
    print("Puedes entrar en la atracción.")
else:
    print("No puedes entrar en la atracción.")
