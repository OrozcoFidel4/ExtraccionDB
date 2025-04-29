import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

datos = pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\parcial2\practicasPython\datos01.csv')

#asginar las columnas del csv 
X= datos[['Publicidad']].values
Y = datos['Ventas'].values

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
nuevo_valor_publicidad = 6
prediccion = modelo.predict([[nuevo_valor_publicidad]])
print(f'Prediccion de ventas para una publicidad de ${nuevo_valor_publicidad},000 Dlls: {prediccion[0]} mil unidades\n')

plt.scatter(X,Y, color='blue', label='Datos Reales')
plt.plot(X, modelo.predict(X), color='red', label='Linea De Regresion')
plt.xlabel('Publicidad')
plt.ylabel('Ventas')
plt.title('Regresion Lineal: Publicidad vs Ventas')
plt.legend()
plt.show()

