# Librería básica para la manipulación de archivos csv
# import csv

# Lectura de las filas del archivo csv
# with open("4_SeccionSemiAvanzada\\Archivos\\informacion_personas.csv") as archivo_csv:
    # reader = csv.reader(archivo_csv)
    # for fila in reader:
        # print(fila)

# -------------------------------- PANDAS ------------------------------------ #
# Importar librería y referenciarla
import pandas as pd

# Abrir un data frame
df = pd.read_csv("4_SeccionSemiAvanzada\\Archivos\\informacion_personas.csv", 
                          names=["name", "lastname", "age", "nationality"])
                        
# Ordenar el data frame según un encabezado
# Ordenado ascendente (predeterminado)
df_ordenado_uno = df.sort_values("age")
# Ordenado descendente
df_ordenado_dos = df.sort_values("age", ascending=False)

# Concatenar dataframes
df_concatenado = pd.concat([df_ordenado_uno, df_ordenado_dos])

# Visualizar el contenido por filas
# Primeras tres filas
primeras_filas = df_ordenado_uno.head(3)
# Últimas tres filas
ultimas_filas = df_ordenado_uno.tail(3)

# Saber la cantidad total de filas y columnas del data frame.
filas_totales, columanas_totales = df.shape

# Información estadística de un data frame.
df_informacion = df.describe()

# Acceder a datos concretos del data frame.
# Accediendo a un dato específico utilizando la propiedad .loc
dato_especifico_loc = df.loc[2, "name"]
# Accediendo a un dato específico utilizando la propiedad .iloc
dato_especifico_iloc = df.iloc[3, 3]
# Accediando a todas las filas de una columna (slicing) utilizando las dos propiedades.
edades = df.loc[:, "age"]
apellidos = df.iloc[:, 1]
# Accediendo a todos los datos de una fila utilizando las dos propiedades.
exequiel = df.loc[0, :]
akane = df.iloc[4, :]
# Acceder a datos según una condición
mayores_de_30 = df.loc[df["age"] > 30, :]
