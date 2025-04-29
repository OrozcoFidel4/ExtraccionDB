import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\parcial3\python\datos21.csv')

x = data[["HorasEstudio", "PromedioCalificaciones"]].values
# modelo de kmeans con 3 clusters
kmeans = KMeans(n_clusters=4, random_state=42) #random_state = 42 no se mueve asi se queda 
kmeans.fit(x)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.figure(figsize=(8, 6))

colors = ['cyan', 'lightgreen', 'blue', 'pink']
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