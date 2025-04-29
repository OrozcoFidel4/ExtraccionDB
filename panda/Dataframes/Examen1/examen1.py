import pandas as pd

df = pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\panda\Dataframes\examen1\estudiantes.csv') #r fuerza la ruta a usarla

print("-------IMPRIMIR 5 FILAS----------")
print(df.head)

print("\n-------CANTIDAD DE ESTUDIANTES----------")
print(f"Numero de Estudiantes: {df.shape[0]}")

print("\n-------EDAD PROMEDIO DE ESTUDIANTES----------")
print(f"Edad Promedio: ", df["Edad"].mean())

print("\n-------CALIFICACION PROMEDIO DE ESTUDIANTES INGLES----------")
print(f"Calificacion Promedio: ", df["Calificacion_Ing"].mean())

print("\n-------CALIFICACION PROMEDIO DE ESTUDIANTES DESARROLLO----------")
print(f"Calificacion Promedio: ", df["Calificacion_Desarrollo"].mean())

print("\n-------ESTUDIANTE MAS JOVEN----------")
EstJoven= df.loc[df["Edad"].idxmin(), "Nombre"]
print(f"Estudiante mas joven: {EstJoven}")

print("\n-------ESTUDIANTE MAS CALIFICACION MAYOR INGLES----------")
EstCalifMayorIng= df.loc[df["Calificacion_Ing"].idxmax(), "Nombre"]
print(f"Estudiante con calificacion mayor Ingles: {EstCalifMayorIng}")

print("\n-------ESTUDIANTE MAS CALIFICACION MAYOR DESARROLLO----------")
EstCalifMayorDes= df.loc[df["Calificacion_Desarrollo"].idxmax(), "Nombre"]
print(f"Estudiante con calificacion mayor Desarrollo: {EstCalifMayorIng}")

#Crear nuevo DataFrame
newdf = df['Nombre'][df['Calificacion_Desarrollo'] >= 90]

print("\n-------CANTIDAD DE ESTUDIANTES CON CALIFICACION MAYOR A 90 DESARROLLO----------")
print(f"Numero de Estudiantes: {newdf.shape[0]}")

#CrearNuevoCSV
newdf.to_csv('estudiantes_destacados.csv')