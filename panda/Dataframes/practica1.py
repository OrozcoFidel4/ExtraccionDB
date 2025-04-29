import pandas as pd 

#crear un df
data = {'Nombre': ['Ana', 'Luis', 'Pedro', 'Maria'],
        'Edad' : [23, 45, 35, 22],
        'Ciudad': ['Morelia', 'CDMX', 'Cd. Juarez', 'Hermosillo']}

df = pd.DataFrame(data)
print(df)

print('\n-------------------------')
#filtrar edades
edades = df['Edad']
print(edades)

print('\n-------------------------')
#filtrar personas con edad mayor a 30
filtro = df[df['Edad'] > 30]
print(filtro)

print('\n-------------------------')
#Agrupar por ciudad y calcular el promedio
grupo = df.groupby('Ciudad')['Edad'].mean()
print(grupo)

print('\n-------------------------')
#estadisticas basicas
estadisticas = df.describe()
print(estadisticas)