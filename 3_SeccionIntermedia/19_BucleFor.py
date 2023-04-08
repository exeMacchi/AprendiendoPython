# 1) Iterar un número específico de veces.
print("1) ", end="")
for i in range(10):
    if i == 9:
        print(i, end = ".\n")
    else:
        print(i, end = ", ")


# 2) Iterar un rango específico de veces.
print("\n2) ", end="")
for i in range(-5, 6):
    if i == 5:
        print(i, end = ".\n")
    else:
        print(i, end = ", ")


# 3) Iterar una lista de animales (se utiliza enumerate() para formatear el texto de salida)
animales = ['Perro', 'Gato', 'Loro', 'Colibrí', 'Conejo']
print("\n3) ", end="")
for indice, animal in enumerate(animales):
    if indice == len(animales) - 1:
        print(animal, end=".\n")
    else:
        print(animal, end=", ")


# 4) Iterar dos listas la mismo tiempo (se utiliza enumareate() para formatear el texto de salida)
letras = list("ABCD") 
numeros = [1, 2, 3, 4]
print("\n4) ", end="")
for i, (letra, numero) in enumerate(zip(letras, numeros)):
    if i == len(numeros) - 1:
        print(f"{letra}-{numero}", end=".\n")
    else:
        print(f"{letra}-{numero}", end=", ")


# 5) For-Else: realizar una acción luego de que el bucle haya finalizado correctamente.
print("\n5) ", end="")
for numero in enumerate(numeros):
    if numero[0] == len(numeros) - 1:
        print(numero[1], end = ".\n")
    else:
        print(numero[1], end = ", ")
else:
    print("Bucle finalizado correctamente.")


# 6) Recorrer un diccionario utilizando el método items(), el cual devuelve una tupla con
#    las claves y valores asociados.
diccionario = {'nombre': "Exequiel", 'apellido': "Macchi", 'edad': 23}
print("\n6) Recorriendo el diccionario: ")
for clave, valor in diccionario.items():
    print(f"Clave: {clave}; Valor: {valor}")
    
# for clave_valor in diccionario.items():
    # clave = clave_valor[0]
    # valor = clave_valor[1]
    # print(f"Clave: {clave}; Valor: {valor}")


# 7) Saltearse una iteración según una condición.
lista_frutas = ["Manzana", "Banana", "Kiwi", "Durazno", "Frutilla"]
print("\n7) Lista de fruta: ", end = "")
for i, fruta in enumerate(lista_frutas):
    if fruta == "Kiwi":
        continue
    if i == len(lista_frutas) - 1:
        print(fruta, end = ".\n")
    else:
        print(fruta, end = ", ")


# 8) Finalizar un bucle antes de tiempo.
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n8) ", end="")
for numero in lista_numeros:
    if numero == 6:
        break
    print(numero, end=", ")
else:
    print("Este texto nunca aparecerá en la consola.")
print("\nBucle finalizado antes de tiempo.")


# 9) Recorrer una cadena de caracteres
print("\n9) ", end="")
cadena = "Texto de prueba"
for i, caracter in enumerate(cadena):
    if i == len(cadena) - 1:
        print(caracter, end=".\n")
    else:
        print(caracter, end =", ")


# 10) Bucle for en una línea de código.
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_numeros_duplicados = [n * 2 for n in lista_numeros]
print(f"\n10) {lista_numeros_duplicados}\n")

# 11) Practica: dibujando un triángulo rectángulo
print("11) Triángulo rectángulo:")
for i in range(11):
    if i != 0:
        print("* " * i)
