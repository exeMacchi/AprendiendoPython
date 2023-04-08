# 1) Declarar y definir una función simple.
def saludo_general():
    print("Hola, buenos días\n")

# 2) Declarar y definir un funcion con parámetros.
def saludo_personalizado(nombre):
    print(f"Hola, {nombre}, ¿cómo estás?\n")

# 3) Declarar y definir una función con valor de retorno (en este caso una tupla de dos valores)
def crear_password(num):
    caracteres = "abcdefghij"
    primer_digito = int( str(num)[0] )
    c1 = primer_digito
    c2 = primer_digito - 1
    c3 = primer_digito - 2
    password = f"{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}{num ** 2}"
    return password, primer_digito

def pedir_numero():
    return int( input("3) Escriba un número: ") )

# 4) Declarar y definir una función con un número variable de argumentos.
def sumar_numeros(*numeros):
    return sum(numeros)

# 5) Declarar y definir una función con parámetros opcionales.
def multiplicar_numero(numero, producto = 2):
    return numero * producto

# 6) Llamar a una función pasándole argumentos en distinto orden.
def saludar_usuario(nombre, apellido, dia_tarde_noche):
    return f"Hola, {nombre} {apellido}, {dia_tarde_noche}."

# 7) Declarar y definir una función que acepta un número variable de argumentos
# de palabras clave (key-value pairs) en forma de un diccionario.
def informacion_producto(**info):
    nombre = info.get("nombre", "NN")
    precio = info.get("precio", 0.0)
    cantidad = info.get("cantidad", 1)
    
    print("--------------------------------")
    print(nombre, precio, cantidad, sep="\n")

# ---------------------------------------------------------------------------- #
# Función simple
print("1) ", end="")
saludo_general()

# Función con parámetros
print("2) ", end="")
saludo_personalizado("Exequiel")

# Función con valor de retorno (dos en este caso)
password, digito = crear_password(pedir_numero())
print(f"Tu nueva contraseña es: {password}")
print(f"Se utilizo el dígito {digito} como referencia.\n")

# Función con número variable de argumentos.
print(f"4) Suma total: {sumar_numeros(1,5,6,7,2,3,465,1,5,7,8)}\n")

# Función con parámetros opcionales (el producto será 2, ya que no se pasa el segundo argumento)
print(f"5) Multiplicacion: {multiplicar_numero(4)}\n")

# Llamada a la función con argumentos en distinto orden.
frase = saludar_usuario(dia_tarde_noche = "buenos dias", apellido = "Macchi", 
                        nombre = "Exequiel")
print(f"6) {frase}\n")

# Llamada a la función que acepta un número variable de key-value pairs.
print("7) Información de productos:")
informacion_producto(nombre='Terrabusi', precio="417", cantidad=2)
informacion_producto(precio=756)
