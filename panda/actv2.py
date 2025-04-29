import pandas as pd
import matplotlib.pyplot as plt

ventas_manzanas = pd.Series([120, 130, 115, 140, 125, 135, 150], 
index = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])
ventas_platano= pd.Series([100, 105, 110, 95, 180, 110, 115],
index = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

#DATOS DE MANZANA
total_manzanas = ventas_manzanas.sum() #sum funcion de suma
promedio_manzana = ventas_manzanas.mean() #mean funcion de promedio

#DATOS DE PLATANO
total_platano = ventas_platano.sum() #sum funcion de suma
promedio_platano = ventas_platano.mean() #mean funcion de promedio

print(f'Total de ventas (Manzanas): {total_manzanas}')
print(f"Promedio de venta (Manzanas): {promedio_manzana}\n")

print(f'Total de ventas (Platanos): {total_platano}')
print(f"Promedio de venta (Platanos): {promedio_platano}\n")

#DIAS CON MAS VENTA
dia_max_manzana = ventas_manzanas.idxmax() #idmax index mayor
dia_max_platano = ventas_platano.idxmax() 

print(f'Dia con mas ventas (Manzana): {dia_max_manzana}')
print(f"Dia con mas venta (Platanos): {dia_max_platano}\n")

#GRAFICA DE LAS VENTAS DIARIAS DE AMBOS PRODUCTOS
plt.figure(figsize=(8,5))
plt.plot(ventas_manzanas,label='Manzana',marker='o', linestyle="--", color="red")
plt.plot(ventas_platano,label='Platano',marker='o', linestyle="--", color="yellow")
plt.xlabel('Dia')
plt.ylabel('Ventas (Unidades)')
plt.title("VENTAS (MANZANA Y PLATANO)")
plt.legend()
plt.grid(True)
plt.show()

