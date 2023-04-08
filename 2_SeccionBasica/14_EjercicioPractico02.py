pro_palabras_personas_por_segundo = 2
pro_palabras_profesor_por_segundo = pro_palabras_personas_por_segundo * 1.30
texto_usuario = input("Escriba lo que quiere decir: ")

# 1) Pedirle al usuario un texto y:
    # a) Calcular cuánto tardaría en decir esa frase.
    # b) ¿Cuántas palabras dijo?
# 2) Si se tarda más de un minuto, decirle al usuario: "Pará, flaco, tampoco te 
#    pedí un testamento."
# 3) El profesor habla un 30% más rápido. ¿Cuánto tardaría en decir el texto del
#    usuario.

lista_palabras = texto_usuario.split()
cant_palabras = len(lista_palabras)
tiempo_frase_usuario = cant_palabras / pro_palabras_personas_por_segundo
tiempo_frase_profesor = cant_palabras / pro_palabras_profesor_por_segundo

# Punto 1 (a y b) y 2
print(f"Usted diría en {tiempo_frase_usuario} segundos {cant_palabras} palabras.")

# Punto 2
if tiempo_frase_usuario > 60:
    print("Pará, flaco, tampoco te pedí un testamento.")

# Punto 3
print(f"El profesor diría dichas palabras en {round(tiempo_frase_profesor, 2)} segundos.")