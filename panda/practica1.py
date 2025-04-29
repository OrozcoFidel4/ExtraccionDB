import pandas as pd

precios = pd.Series([100,200,300,400],
index = ['Producto1', 'Producto2', 'Producto3', 'Producto4'])

promedioPrecio = precios.mean() #.mean=promedio
print(promedioPrecio)