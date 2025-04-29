import pandas as pd

df =pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\panda\Dataframes\practica2\Ventas.csv') #r fuerza la ruta a usarla

print("Primeras filas del DataFrame")
print(df.head(12))

print("\n------------------")
suma_ventas = df['Ventas'].sum()
print(f"Suma total de las ventas: {suma_ventas}")

print("\n------------------")
promedio_ventas = df['Ventas'].mean()
print(f"Promedio de las ventas: {promedio_ventas}")

print("\n------------------")
mes_max_ventas = df.loc[df['Ventas'].idxmax(), 'Mes']
print(f"Mes con mayor numero de ventas: {mes_max_ventas}")

