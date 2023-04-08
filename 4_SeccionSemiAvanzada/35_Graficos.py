# Importando las librerías necesarias.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Obteniendo los datos a mostrar.
df_contagios = pd.read_csv("4_SeccionSemiAvanzada\\Archivos\\informacion_contagios.csv")
df_habilidad = pd.read_csv("4_SeccionSemiAvanzada\\Archivos\\informacion_habilidad.csv")
df_categorias = pd.read_csv("4_SeccionSemiAvanzada\\Archivos\\informacion_categorias.csv")

# Creando un gráfico lineal y un marcador para el máximo (manualmente)
    # sns.lineplot(x = 'Fechas', y = 'Contagios', data = df_contagios)
    # plt.plot('01-08', 54, 'o')

# Creando un gráfico de barras agregándole a la esquina superior derecha el total de
# contagios.
    # total_contagios = df_contagios['Contagios'].sum()
    # sns.barplot(x = 'Fechas', y = 'Contagios', data = df_contagios)
    # plt.text(len(df_contagios) - 1, max(df_contagios['Contagios']), 
            # f"Total de contagios: {total_contagios}", ha='right', va='top')

# Creando un gráfico de dispersión.
# sns.scatterplot(x = 'Tiempo', y = 'Habilidad', data = df_habilidad)

# Creando un gráfico de cajas.
sns.boxplot(x = 'Categoria', y = 'Valor', data = df_categorias)

# Mostrando el gráfico lineal.
plt.show()
