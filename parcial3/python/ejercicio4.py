import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from kneed import KneeLocator

data = pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\parcial3\python\datos21.csv')

x = data[["HorasEstudio", "PromedioCalificaciones"]].values

#Ejercicio 4 Inertia
inertia = []
k_values = range(1,10)

#Codigo para determinar los clusters optimos 
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(x)
    inertia.append(kmeans.inertia_)

knee_locator = KneeLocator(k_values, inertia, curve='convex', direction='decreasing')
optimal_k = knee_locator.knee

print(f'El numero optimo de clusters es: {optimal_k}')

# modelo de kmeans con 3 clusters
kmeans = KMeans(n_clusters=optimal_k, random_state=42) #random_state = 42 no se mueve asi se queda 
kmeans.fit(x)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.figure(figsize=(8, 6))

colors = ['cyan', 'lightgreen', 'blue', 'pink', 'orange', 'green', 'gray', 'purple', 'yellow']
for i in range(len(x)):
    plt.scatter(x[i, 0], x[i, 1],
                color=colors[labels[i]], s=10,
                label=f'Cluster {labels[i] + 1}'
                if f'Cluster {labels[i] + 1}'
                not in plt.gca().get_legend_handles_labels()[1]
                else '')

plt.scatter(centroids[:, 0], centroids[:, 1],
            color='red', marker='x', s=200, label='Centroides')

plt.title("Segmentación de clientes con k-means")
plt.xlabel("Horas Estudio")
plt.ylabel("Promedio Calificaciones")
plt.legend()
plt.grid(True)
plt.show()

#mandar etiquetas al df original 
data['cluster'] = labels

data.to_csv('Resultados_Clusters.csv', index=False)
print('Resultados guardados en "Resultados_Clusters.csv"')