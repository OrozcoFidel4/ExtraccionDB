import pandas as pd

calificaciones = pd.Series([87,33,94,97,100,37],
index = ['Juanito', 'Memeo', 'Aaronzito', 'Makanazo', 'JuanCamaney', 'RiquitoSoto'])

promedio = calificaciones.mean()
calificacionAlta = calificaciones.max()
calificacionBaja = calificaciones.min()

print(f'Promedio = {promedio} \nCalificacion Alta = {calificacionAlta} \nCalificacion Baja = {calificacionBaja}' )