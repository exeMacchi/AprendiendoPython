# Control de excepciones
def sumar_dos_numeros():
    while True:
        # Código que podría generar excepciones.
        try:
            x = int(input("Inserte el primer número: "))
            y = int(input("Inserte el segundo número: "))
        # Código que se ejecuta si se genera alguna excepción.
        except:
            print("Valor ingresado incorrecto. Inténtelo nuevamente.")
        # Código que se ejecuta si no se genera ninguna excepción.
        else:
            break
        # Código que se ejecutará siempre, se genere o no una excepción.
        finally:
            print("Esta instrucción se imprimirá siempre.")
    return x + y


resultado = sumar_dos_numeros()
print(f"Resultado: {resultado}")

# Lanzar personalmente una excepción, en este caso, si el resultado es mayor a 10.
if resultado > 10:
    raise Exception("El resultado es mayor a 10.") 
else:
    print("Programa finalizado.")
    