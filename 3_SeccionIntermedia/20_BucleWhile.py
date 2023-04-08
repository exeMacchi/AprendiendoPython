# 1) Crear un contador del 1 al 10 usando bucle while
contador = 1
print("1) ", end="")
while contador <= 10:
    if contador == 10:
        print(contador, end=".\n")
    else:
        print(contador, end=", ")
    contador += 1
    
# 2) Replicar el comportamiento de un bucle do-while en Python
texto = str()
while True:
    texto = input("\n2) Escriba una palabra de más de 8 letras: ")
    if not len(texto) <= 8:
        break
print(texto)