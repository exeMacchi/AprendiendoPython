# Ejercicio: mostrar en consola números primos entre 1 y el número máximo especificado 
# por el usuario.

def pedir_numero_maximo():
    return int(input("Ingrese el número tope: "))

def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def mostrar_numeros_primos_hasta_x(num_max):
    numeros_primos = list()
    for numero in range(1, num_max + 1):
        if es_primo(numero):
            numeros_primos.append(numero)
    print(numeros_primos)

# Main()
num_max = pedir_numero_maximo()
print("Listado de números primos: ", end="")
mostrar_numeros_primos_hasta_x(num_max)