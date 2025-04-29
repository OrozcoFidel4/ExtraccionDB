import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\panda\Dataframes\practica4\temperaturas.csv') #r fuerza la ruta a usarla

print("------IMPRIMIR 10 FILAS-------")
print(df.head(10))

print("\n------VERIFICAR VALORES NULOS-------")
print(df.isnull())

#Eliminar valores nulos
df = df.dropna()

print("\n------RECUENTO DE FILAS-------")
print(f"Filas despues de limpieza: {df.shape[0]}")

print("\n------TEMP PROMEDIO DE CIUDADES-------")
tempPromCiudades = df.groupby('Ciudad')['Temperatura'].mean()
print(tempPromCiudades)

print("\n------CIUDAD CON LA TEMP MAS ALTA-------")
CiudadTempMax = df.loc[df['Temperatura'].idxmax(), 'Ciudad']
print("\n",CiudadTempMax)

print("\n------CIUDADES CON TEMP MAYORES A 30-------")
dfMayor30= df[df["Temperatura"] > 30]
print(dfMayor30) 

#Crear lista Ciudad para X
filtro = df["Ciudad"]
listCiudades = []

for i in filtro:
    listCiudades.append(i)

#Crear lista TempProm para Y
listTempProm = []

for i in tempPromCiudades:
    listTempProm.append(i)

#Crear Grafica Barras
plt.bar(listCiudades, listTempProm)
plt.xlabel('Ciudades')
plt.ylabel('Temperatura Promedio')
plt.title("Temperatura Promedio De Ciudades")
plt.grid(True)
plt.show()

dfGrafica = df[['Ciudad', 'Temperatura']]


#Crear Grafica de Variacion
dfGrafica.plot.line(x='Ciudad', y='Temperatura', marker="o")
plt.xlabel('Ciudades')
plt.ylabel('Temperatura Promedio')
plt.title("Variaciones En Temperatura De Ciudades")
plt.show() 


#Nuevo Archivo
NuevoArchivo = df['Temperatura'][df['Temperatura'] >= 30]
NuevoArchivo.to_csv('NuevoArchivo.csv')

