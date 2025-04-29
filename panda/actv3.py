import pandas as pd
import matplotlib.pyplot as plt

ventas_manzanas = pd.Series([120, 130, 115, 140, 125, 135, 150], 
index = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

ventas_platanos= pd.Series([100, 105, 110, 95, 180, 110, 115],
index = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

ventas_peras= pd.Series([50, 29, 58, 120, 100, 94, 83],
index = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

ventas_sandias= pd.Series([51, 72, 28, 67, 74, 122, 64],
index = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

ventas_naranjas= pd.Series([120, 93, 102, 154, 67, 109, 125],
index = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

ventas_mangos= pd.Series([99, 84, 82, 106, 167, 87, 63],
index = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'])

#TOTAL DE VENTAS DE LA SEMANA
total_manzanas= ventas_manzanas.sum()
total_platano= ventas_platanos.sum()
total_peras = ventas_peras.sum()
total_sandias = ventas_sandias.sum()
total_naranjas = ventas_naranjas.sum()
total_mangos = ventas_mangos.sum()

print('\n--------TOTAL DE VENTAS--------\n')
print(f'Manzanas: {total_manzanas}')
print(f'Platanos: {total_platano}')
print(f'Peras: {total_peras}')
print(f'Sandias: {total_sandias}')
print(f'Naranjas: {total_naranjas}')
print(f'Mangos: {total_mangos}')


#DIAS CON LA VENTA MAS ALTA Y BAJA
venta_alta_manzanas= ventas_manzanas.idxmax()
venta_baja_manzanas= ventas_manzanas.idxmin()

venta_alta_platanos =ventas_platanos.idxmax()
venta_baja_platanos= ventas_platanos.idxmin()

venta_alta_peras =ventas_peras.idxmax()
venta_baja_peras= ventas_peras.idxmin()

venta_alta_sandias=ventas_sandias.idxmax()
venta_baja_sandias= ventas_sandias.idxmin()

venta_alta_naranjas =ventas_naranjas.idxmax()
venta_baja_naranjas= ventas_naranjas.idxmin()

venta_alta_mangos =ventas_mangos.idxmax()
venta_baja_mangos= ventas_mangos.idxmin()

print('\n--------DIAS CON MAS VENTA--------\n')
print(f'Manzanas: {venta_alta_manzanas}')
print(f'Platanos: {venta_alta_platanos}')
print(f'Peras: {venta_alta_peras}')
print(f'Sandias: {venta_alta_sandias}')
print(f'Naranjas: {venta_alta_naranjas}')
print(f'Mangos: {venta_alta_mangos}')

print('\n--------DIAS CON MENOS VENTA--------\n')
print(f'Manzanas: {venta_baja_manzanas}')
print(f'Platanos: {venta_baja_platanos}')
print(f'Peras: {venta_baja_peras}')
print(f'Sandias: {venta_baja_sandias}')
print(f'Naranjas: {venta_baja_naranjas}')
print(f'Mangos: {venta_baja_mangos}')

#PROMEDIO SUPERIOR A 100
prom_manzanas= ventas_manzanas.mean()
prom_platano= ventas_platanos.mean()
prom_peras = ventas_peras.mean()
prom_sandias = ventas_sandias.mean()
prom_naranjas = ventas_naranjas.mean()
prom_mangos = ventas_mangos.sum()

print("\n--------PROMEDIO MAYOR A 100--------\n")
if prom_manzanas >= 100:
    print(f"Manzanas: {round(prom_manzanas,2)}")
if prom_platano >= 100:
    print(f"Platanos: {round(prom_platano,2)}")
if prom_peras >= 100:
    print(f"Peras: {round(prom_peras,2)}")
if prom_sandias >= 100:
    print(f"Sandias: {round(prom_sandias,2)}")
if prom_naranjas >= 100:
    print(f"Naranjas: {round(prom_naranjas,2)}")
if prom_mangos >= 100:
    print(f"Mangos: {round(prom_mangos,2)}")

#VENTAS MENORES A 70
print("\n--------VENTAS MENORES A 70 (MANZANAS)--------\n")
cont = 0
for i in zip(ventas_manzanas):
    dato = int(i[0])
    if dato <= 70:
        print(f'--> {ventas_manzanas.index[cont]}: {dato}')
    else:
        print(f'{ventas_manzanas.index[cont]}: Mayor a 70')
    cont = cont + 1

print("\n--------VENTAS MENORES A 70 (PLATANOS)--------\n")
cont = 0
for i in zip(ventas_platanos):
    dato = int(i[0])
    if dato <= 70:
        print(f'--> {ventas_platanos.index[cont]}: {dato}')
    else:
        print(f'{ventas_platanos.index[cont]}: Mayor a 70')
    cont = cont + 1


print("\n--------VENTAS MENORES A 70 (PERAS)--------\n")
cont = 0
for i in zip(ventas_peras):
    dato = int(i[0])
    if dato <= 70:
        print(f'--> {ventas_peras.index[cont]}: {dato}')
    else:
        print(f'{ventas_peras.index[cont]}: Mayor a 70')
    cont = cont + 1

print("\n--------VENTAS MENORES A 70 (SANDIAS)--------\n")
cont = 0
for i in zip(ventas_sandias):
    dato = int(i[0])
    if dato <= 70:
        print(f'--> {ventas_sandias.index[cont]}: {dato}')
    else:
        print(f'{ventas_sandias.index[cont]}: Mayor a 70')
    cont = cont + 1

print("\n--------VENTAS MENORES A 70 (NARANJAS)--------\n")
cont = 0
for i in zip(ventas_naranjas):
    dato = int(i[0])
    if dato <= 70:
        print(f'--> {ventas_naranjas.index[cont]}: {dato}')
    else:
        print(f'{ventas_naranjas.index[cont]}: Mayor a 70')
    cont = cont + 1

print("\n--------VENTAS MENORES A 70 (MANGOS)--------\n")
cont = 0
for i in zip(ventas_mangos):
    dato = int(i[0])
    if dato <= 70:
        print(f'--> {ventas_mangos.index[cont]}: {dato}')
    else:
        print(f'{ventas_mangos.index[cont]}: Mayor a 70')
    cont = cont + 1
    

#SI EL PRODUCTO NO LLEGO A 500 VENTAS
print("\n--------INCREMENTO DEL 10% DE VENTAS--------\n")
if total_manzanas < 500:
    incremento = total_manzanas *.10
    nuevo_total_manzanas = total_manzanas + incremento
    print(f"Nuevo total Manzanas: {int(nuevo_total_manzanas)}")
else:
    print("Total de ventas (Manzanas): Mayor a 500 ")

if total_platano < 500:
    incremento = total_platano *.10
    nuevo_total_platano = total_platano + incremento
    print(f"Nuevo total Platano: {int(nuevo_total_platano)}")
else:
    print("Total de ventas (Platano): Mayor a 500 ")

if total_peras < 500:
    incremento = total_peras *.10
    nuevo_total_peras = total_peras + incremento
    print(f"Nuevo total Peras: {int(nuevo_total_peras)}")
else:
    print("Total de ventas (Peras): Mayor a 500 ")

if total_sandias < 500:
    incremento = total_sandias * .10
    nuevo_total_sandias = total_sandias + incremento
    print(f"Nuevo total Sandias: {int(nuevo_total_sandias)}")
else:
    print("Total de ventas (Sandias): Mayor a 500 ")

if total_naranjas < 500:
    incremento = total_naranjas * .10
    nuevo_total_naranjas = total_naranjas + incremento
    print(f"Nuevo total Naranjas: {int(nuevo_total_naranjas)}")
else:
    print("Total de ventas (Naranjas): Mayor a 500 ")

if total_mangos < 500:
    incremento = total_mangos * .10
    nuevo_total_mangos = total_mangos + incremento
    print(f"Nuevo total Mangos: {int(nuevo_total_mangos)}")
else:
    print("Total de ventas (Mangos): Mayor a 500 ")

#SUMA LAS VENTAS DE TODOS LOS PRODUCTOS POR DIA Y CHECA CUAL DIA SE VENDIO MAS
print("\n--------VENTA DE TODOS LOS PRODUCTOS Y DIA MAXIMO--------\n")
cont = 0
max = 0
dia = ""
for i in range(7):
    total_dia = ventas_manzanas.iloc[cont] + ventas_platanos.iloc[cont] + ventas_peras.iloc[cont] + ventas_sandias.iloc[cont] + ventas_naranjas.iloc[cont] + ventas_mangos[cont]
    #print(f"{ventas_manzanas.index[cont]}: {total_dia}")
    if total_dia > max:
        max = total_dia
        dia = ventas_manzanas.index[cont]
    cont = cont +1

print(f"\n{dia}: {max}")

#VENTAS CRECIENTES 3 DIAS 
print("\n--------CRECIENTES--------\n")
dias = []
cont = 0 
cre = 0
for i in zip(ventas_manzanas):
    dato = int(i[0])
    if cont == 0:
        anterior = dato
        dias.append(ventas_manzanas.index[cont])
        cre = cre +1
    if anterior <= dato or cre ==1:
        dias.append(ventas_manzanas.index[cont])
        anterior = dato
        cre = cre +1
    else: 
        cre = 0
        anterior = dato
        dias = []
    cont = cont +1 
if len(dias) >= 4:
    dias.pop(0)
if cre >= 3: 
    print("Manzanas: "+", ".join(dias))

dias = []
cont = 0 
cre = 0
for i in zip(ventas_platanos):
    dato = int(i[0])
    if cont == 0:
        anterior = dato
        dias.append(ventas_platanos.index[cont])
        cre = cre +1
    if cre >= 4:
        dias.pop(0)
        print("Platanos: "+", ".join(dias))
        break
    if anterior <= dato or cre ==1:
        dias.append(ventas_platanos.index[cont])
        anterior = dato
        cre = cre +1
    else: 
        cre = 0
        anterior = dato
        dias = []
    cont = cont +1 

dias = []
cont = 0 
cre = 0
for i in zip(ventas_peras):
    dato = int(i[0])
    if cont == 0:
        anterior = dato
        dias.append(ventas_peras.index[cont])
        cre = cre +1
    elif cre >= 4:
        dias.pop(0)
        print("Peras: "+", ".join(dias))
        break
    elif anterior <= dato or cre ==1:
        dias.append(ventas_peras.index[cont])
        anterior = dato
        cre = cre +1
    else: 
        cre = 0
        anterior = dato
        dias = []
    cont = cont +1 

dias = []
cont = 0 
cre = 0
for i in zip(ventas_sandias):
    dato = int(i[0])
    if cont == 0:
        anterior = dato
        dias.append(ventas_sandias.index[cont])
        cre = cre +1
    elif cre >= 4:
        dias.pop(0)
        print("Sandias: "+", ".join(dias))
        break
    elif anterior <= dato or cre ==1:
        dias.append(ventas_sandias.index[cont])
        anterior = dato
        cre = cre +1
    else: 
        cre = 0
        anterior = dato
        dias = []
    cont = cont +1 
print(dias)