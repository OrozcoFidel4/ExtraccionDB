import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Definición del problema
# Definimos el problema: busca predecir la calificación de los estudiantes en función de las horas que dedican al estudio.

# 2. Recolección y preparación de datos
# Recolectamos los datos desde un archivo CSV ubicado en la ruta especificada.
datos = pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\parcial2\practicasPython\datos02.csv')

X = datos[['Horas']].values  
Y = datos['Calificacion'].values  

# 3. División del conjunto de datos
# Dividiríamos los datos en un conjunto de entrenamiento y uno de prueba pero no es el caso.


# 4. Selección del modelo
# Seleccionamos el modelo de regresión lineal
modelo = LinearRegression()

# 5. Entrenamiento del modelo
# Entrenamos el modelo utilizando los datos de entrada X (Horas) y la variable objetivo Y (Calificación).
modelo.fit(X, Y)

# 6. Evaluación del modelo
# Evaluamos el rendimiento del modelo observando los parámetros aprendidos.
pendiente = modelo.coef_[0]  
interseccion = modelo.intercept_ 

print(f'Pendiente: {pendiente}\n')  
print(f'Interseccion: {interseccion}\n') 
print(f'R^2: {modelo.score(X, Y)}')

# 7. Ajuste del modelo
# Si el modelo no estuviera ajustando bien los datos se puede cambiar el modelo o agregar mas caracteristicas

# 8. Implementación y despliegue
# En un escenario real, este modelo podría ser implementado en un sistema que permita a los usuarios predecir calificaciones

# 9. Monitoreo y actualización
# Después de desplegar el modelo, es importante monitorear su desempeño y asegurarse de que las predicciones sean precisas.
# Si el modelo comienza a perder precisión con el tiempo debido a cambios en los datos, será necesario reentrenarlo.

nuevo_valor_hora = [3, 6, 8.5, 10] 
for i in nuevo_valor_hora:
    prediccion = modelo.predict([[i]])  # Realizamos la predicción para cada valor de horas
    print(f'Prediccion de calificacion para un estudio de {i} horas: {prediccion[0]} %')  # Imprimimos la predicción

plt.scatter(X, Y, color='blue', label='Datos Reales') 
plt.plot(X, modelo.predict(X), color='red', label='Linea De Regresion') 
plt.xlabel('Horas')  
plt.ylabel('Calificacion')
plt.title('Regresion Lineal: Horas vs Calificacion') 
plt.legend() 
plt.show() 
