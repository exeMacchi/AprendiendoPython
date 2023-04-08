# Ejercicio: pedirle una palabra o frase al usuario y verificar que esta sea o
# palíndroma.

def es_palindromo(texto_original):
    texto_formateado = formatear_texto(texto_original)
    i = len(texto_formateado) - 1
    for char in texto_formateado:
        if char != texto_formateado[i]:
            return False
        i -= 1
    return True


def formatear_texto(texto):
    palabras = texto.split()
    texto_formateado = str()
    for palabra in palabras:
        texto_formateado += palabra
    return texto_formateado


palabra_usuario = input("Escriba una palabra: ").strip()
print(f"¿La palabra '{palabra_usuario}' es palíndroma? ---> " +
      f"{es_palindromo(palabra_usuario.lower())}")
