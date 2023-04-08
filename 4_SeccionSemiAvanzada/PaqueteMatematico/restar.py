def restar(*numeros):
    resultado = 0
    for i, numero in enumerate(numeros):
        if i == 0:
            resultado = numero
        else:
            resultado -= numero
    return resultado