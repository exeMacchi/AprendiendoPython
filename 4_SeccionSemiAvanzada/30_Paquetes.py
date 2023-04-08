# Importando las funciones desde el paquete
from PaqueteMatematico import sumar 
from PaqueteMatematico import restar
from PaqueteMatematico import multiplicar
from PaqueteMatematico import dividir

# Utilizando las funciones
resultado_suma = sumar.sumar(1, 2, 3, 4, 5)
resultado_resta = restar.restar(1, 2, 3, 4, 5)
restultado_multiplicacion = multiplicar.multiplicar(4, 5, 6)
resultado_division = dividir.dividir(7, 4)

# Mostrando los resultados
print(resultado_suma)
print(resultado_resta)
print(restultado_multiplicacion)
print(resultado_division)