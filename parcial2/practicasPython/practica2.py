import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

datos = pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\parcial2\practicasPython\datos02.csv')

#asginar las columnas del csv 
X= datos[['Horas']].values
Y = datos['Calificacion'].values

#modelo de regesion lineal
modelo = LinearRegression()

#entrenar modelo
modelo.fit(X,Y)

#obtener la pendiente (coeficiente) y la interseccion 
pendiente = modelo.coef_[0]
interseccion = modelo.intercept_

#imprimir valores
print(f'Pendiente: {pendiente}\n')
print(f'Interseccion: {interseccion}\n')

#prediccion para un nuevo valor de publicidad
nuevo_valor_hora = [3, 6, 8.5, 10]
for i in nuevo_valor_hora:
    prediccion = modelo.predict([[i]])
    print(f'Prediccion de calificacion para un estudio de {i} horas: {prediccion[0]} %')


plt.scatter(X,Y, color='blue', label='Datos Reales')
plt.plot(X, modelo.predict(X), color='red', label='Linea De Regresion')
plt.xlabel('Horas')
plt.ylabel('Calificacion')
plt.title('Regresion Lineal: Horas vs Calificacion')
plt.legend()
plt.show()

