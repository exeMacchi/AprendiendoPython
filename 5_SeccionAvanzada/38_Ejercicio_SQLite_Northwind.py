# Ejercicio de rentabilidad utilizando la base de datos Northwind.
# a) Crear un gráfico de barras mostrando los 10 productos más rentables.
# b) Crear un gráfico de barras mostrando los 5 empleados más efectivos en las ventas.
# c) Crear un gráfico de barras mostrando los 5 empleados que más recaudaron.

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

ruta_DB = 'ruta\\Northwind.db'
query_productos_rentables = """\
SELECT P.ProductID AS ID, P.ProductName AS Nombre_Producto, 
       SUM(P.Price * OD.Quantity) AS Rentabilidad
FROM Products AS P, OrderDetails AS OD
WHERE P.ProductID = OD.ProductID
GROUP BY OD.ProductID
ORDER BY Rentabilidad DESC
LIMIT 10;
"""

query_empleados_efectivos = """\
SELECT E.EmployeeID,
	   E.FirstName || ' ' || E.LastName AS Empleado,
	   COUNT(O.OrderID) AS Ordenes_Vendidas
FROM Employees AS E, Orders AS O
WHERE O.EmployeeID = E.EmployeeID
GROUP BY E.EmployeeID
ORDER BY Ordenes_Vendidas DESC
LIMIT 5;
"""

query_empleados_recaudacion = """\
SELECT E.EmployeeID,
       E.FirstName || ' ' || E.LastName AS Empleado,
       SUM(P.Price * OD.Quantity) AS Total_Recaudado
FROM Orders AS O
JOIN Employees AS E ON O.EmployeeID = E.EmployeeID
JOIN OrderDetails AS OD ON O.OrderID = OD.OrderID
JOIN Products AS P ON OD.ProductID = P.ProductID
GROUP BY E.EmployeeID
ORDER BY Total_Recaudado DESC
LIMIT 5;
"""

# a) Los diez productos más rentables.
with sqlite3.connect(ruta_DB) as conn:
    try:
        productos_mas_rentables = pd.read_sql_query(query_productos_rentables, conn)
        productos_mas_rentables.plot(x='Nombre_Producto', y='Rentabilidad', kind='bar', 
                                     figsize=(10,5), title='Top diez productos más rentables',
                                     legend=False)
        plt.xlabel("Productos") 
        plt.ylabel("Rentabilidad")
        plt.xticks(rotation=90)
        plt.show()

    except Exception as e:
        print("Algo ha salido mal.")
        print(f"Error: {e}")

    
# b) Los cinco empleados más efectivos.
with sqlite3.connect(ruta_DB) as conn:
    try:
        empleados_mas_efectivos = pd.read_sql_query(query_empleados_efectivos, conn)
        empleados_mas_efectivos.plot(x = 'Empleado', y = 'Ordenes_Vendidas', kind='bar',
                                     title="Top cinco empleados más efectivos", 
                                     figsize=(10,5), legend=False)
        plt.xlabel("Empleados")
        plt.ylabel("Ordenes vendidas")
        plt.xticks(rotation=45)
        plt.show()

    except Exception as e:
        print("Algo ha salido mal.")
        print(f"Error: {e}")

# c) Los cinco empleados que más recaudaron
with sqlite3.connect(ruta_DB) as conn:
    try:
        empleados_mayor_recaudacion = pd.read_sql_query(query_empleados_recaudacion, conn)
        empleados_mayor_recaudacion.plot(x = 'Empleado', y = 'Total_Recaudado', kind='bar',
                                     title="Top cinco empleados con mayor recaudación", 
                                     figsize=(10,5), legend=False)
        plt.xlabel("Empleados")
        plt.ylabel("Total recaudado")
        plt.xticks(rotation=45)
        plt.show()

    except Exception as e:
        print("Algo ha salido mal.")
        print(f"Error: {e}")
