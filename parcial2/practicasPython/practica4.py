import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

datos = pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\parcial2\practicasPython\datos04.csv')

#asginar las columnas del csv 
X= datos[['HorasEstudio', 'HorasSueno', 'Participacion']].values
Y = datos['Calificacion'].values

#modelo de regesion lineal
modelo = LinearRegression()

#entrenar modelo
modelo.fit(X,Y)

#obtener la pendiente (coeficiente) y la interseccion 
pendiente = modelo.coef_[0]
interseccion = modelo.intercept_

#imprimir valores
print('-------------------PENDIENTE E INTERSECCION-------------------\n')
print(f'Pendiente: {pendiente}')
print(f'Interseccion: {interseccion}\n')

#prediccion para un nuevos valores
""" nuevo_valor_hora_estudio = [3,5,7]
print('-------------------ESTUDIO-------------------\n')
for i in nuevo_valor_hora_estudio:
    prediccion = modelo.predict([[i, 0, 0]])
    print(f'Prediccion de calificacion para {i} horas de estudio: {prediccion[0]} %\n')

nuevo_valor_hora_sueno = [4,6,8]
print('-------------------SUENO-------------------\n')
for i in nuevo_valor_hora_sueno:
    prediccion = modelo.predict([[0, i, 0]])
    print(f'Prediccion de calificacion para {i} horas de sueño: {prediccion[0]} %\n') """

nuevo_valor_part = [5,7,9]
predicciones_part = []
print('-------------------PARTICIPACION-------------------\n')
for i in nuevo_valor_part:
    prediccion = modelo.predict([[0, 0, i]])
    intPrediccion= int(prediccion)
    prediccionLista = []
    prediccionLista.append(i)
    prediccionLista.append(intPrediccion)
    predicciones_part.append(prediccionLista)
    print(f'Prediccion de calificacion para {i} participacion: {prediccion[0]} %\n')
    prediccionLista = []

dfPart = pd.DataFrame(predicciones_part, columns=['Participacion', 'Calificacion'])
print(dfPart)

#evaluar el modelo
r2 = modelo.score(X,Y)
print(f'Coeficiente de determinacion R²: {r2}\n')

#obtener el mse
Y_pred = modelo.predict(X)
mse = mean_squared_error(Y, Y_pred)
print(f'Error cuadratico medio (mse): {mse}')


plt.plot(dfPart)
plt.show()