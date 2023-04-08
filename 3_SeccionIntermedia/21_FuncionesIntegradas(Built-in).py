# 1) En una lista de números, encontrar:
#    a) El número máximo.
#    b) El número mínimo.
lista_numeros = [78, 18, 22, 86, 14, 3, 9]
max_numero = max(lista_numeros)
min_numero = min(lista_numeros)
print("1) En la lista de números:")
print(f"  a) El máximo es: {max_numero}")
print(f"  b) El mínimo es: {min_numero}\n")

# 2) Suma acumulada de un interable (solo de números)
suma_acumulada = sum(lista_numeros)
print(f"2) La suma acumulada de la lista de números: {suma_acumulada}\n")

# 3) Redonder un número con decimales.
numero_decimal = 3.141592653589
print(f"3) Pi redondeado a 6 decimales: {round(numero_decimal, 6)}\n")

# 4) Truthy y Falsy values
resultado_verdadero = bool(1)
resultado_falso = bool(0)
print("4) Truthy and Falsy values:")
print(f"  a) bool(1) ---> {resultado_verdadero}")
print(f"  b) bool(0) ---> {resultado_falso}\n")

# 5) Verificar si dentro de un iterable todos los objetos son verdaderos.
resultado_all = all( [43, 24,"Verdadero", True, all([10, 8.8, 0])] )
print(f"5) ¿Todos los elementos del iterable son verdaderos? ---> {resultado_all}")

