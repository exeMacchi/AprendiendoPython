# Ejercicio: mostrar una cantidad específica de números de la serie Fibonacci.
def pedir_cantidad_numeros():
    return int( input("Escriba la cantidad de números de la serie Fibonacci: ") )

def serie_fibonacci(cantidad_numeros):
    r1 = 0
    r2 = 1
    r3 = 0
    for i in range(cantidad_numeros):
        if i == cantidad_numeros - 1:
            print(r1, end=".\n")
        else:
           print(r1, end=", ")
           r3 = r1 + r2
           r1 = r2
           r2 = r3

# Main()
cantidad_fibonacci = pedir_cantidad_numeros()
serie_fibonacci(cantidad_fibonacci)