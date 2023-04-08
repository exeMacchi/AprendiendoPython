# Declaración de una función anónima asignada a un identificador
multiplicar_por_dos = lambda x: x * 2
print(multiplicar_por_dos(6))

# Utilizando una función lambda como argumento de la función filter()
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list( filter(lambda n: n % 2 == 0, lista_numeros) )
print(f"Números pares de la lista: {numeros_pares}")