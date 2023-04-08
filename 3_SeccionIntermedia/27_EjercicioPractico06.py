# Ejercicio: una calculadora interactiva.

print("""Bienvenido a mi calculadora interactiva
. Las operaciones son 'suma', 'resta', 'multi', 'div'.
. Para salir debe escribir 'salir' en la operación a elegir.\n""")

numero_uno = int(input("Ingrese el primer número: "))

while True:
    operacion = input("Ingrese la operación: ")
    if operacion.lower() == "salir":
        break

    numero_dos = int(input("Ingrese el segundo número: "))

    if operacion.lower() == 'suma':
        resultado = numero_uno + numero_dos
    elif operacion.lower() == 'resta':
        resultado = numero_uno - numero_dos
    elif operacion.lower() == 'multi':
        resultado = numero_uno * numero_dos
    elif operacion.lower() == 'div':
        if numero_dos != 0:
            resultado = numero_uno / numero_dos
        else:
            print("El divisor no puede ser 0.")
            continue
    else:
        print("Operación incorrecta.")
        continue

    print(f"El resultado es {resultado}")
    numero_uno = resultado
