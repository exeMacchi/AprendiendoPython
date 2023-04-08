# Ejercicios CSV:
# 1) Cambiar el tipo de dato de una columna.
# 2) Reemplazar el valor de una columna.
# 3) Eliminar filas con datos faltantes.
# 4) Eliminar filas con datos repetidos.
# 5) Crear un nuevo data frame con todas las modificaciones.

import pandas as pd
ruta_archivo_csv_original = "4_SeccionSemiAvanzada\\Archivos\\ejercicio_practico_07_original.csv"
data_frame = pd.read_csv(ruta_archivo_csv_original, 
                         names=["nombre", "apellido", "edad", "nacionalidad"], 
                         encoding="UTF-8")
print("Data frame original: ")
print(data_frame, end="\n\n")

# 1) Conviritendo el tipo de dato entero de las edades a un tipo string.
data_frame['edad'] = data_frame['edad'].astype(str)

# 2) Reemplazando el apellido "Munoz" por "Muñoz".
data_frame["apellido"].replace("Munoz", "Muñoz", inplace=True)

# 3) Eliminado las filas con datos vacíos o faltantes.
data_frame = data_frame.dropna()

# 4) Eliminando las filas con datos repetidos.
data_frame = data_frame.drop_duplicates()

# 5) Creando un nuevo data frame con todas las modificaciones.
ruta_archivo_csv_modificado = "4_SeccionSemiAvanzada\\Archivos\\ejercicio_practico_07_modificado.csv"
data_frame.to_csv(ruta_archivo_csv_modificado)
