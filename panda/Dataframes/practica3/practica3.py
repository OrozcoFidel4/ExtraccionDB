import pandas as pd

df =pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\panda\Dataframes\practica3\calificaciones.csv') #r fuerza la ruta a usarla

print("Primeras filas del DataFrame")
print(df.head())

print("\n------------------")
promedio_calif = df['Calificacion'].mean()
print(f"Promedio de las Calificaciones: {promedio_calif}")

print("\n------------------")
calif_max = df.loc[df['Calificacion'].idxmax(), 'Calificacion']
print(f"Calificacion mas alta: {calif_max}")

print("\n------------------")
calif_baja = df.loc[df['Calificacion'].idxmin(), 'Calificacion']
print(f"Calificacion mas baja: {calif_baja}")\

print("\n------------------")
print("Calificaciones mayores a 80\n")
for i in range(len(df)):
    calif = df.iloc[i]['Calificacion']
    if calif >= 80:
        print(calif)

print("\n------------------")
grupo = df.groupby('Materia')['Calificacion'].mean()
print(grupo)

print("\n------------------")
dfmayor80 = df[df['Calificacion'] >= 80]
print("\nDatos en nuevo CSV")
print(dfmayor80)

dfmayor80.to_csv('califMayor80.csv')
