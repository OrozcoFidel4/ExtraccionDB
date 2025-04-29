import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv(r'C:\Users\fidel\Desktop\TURNO VESPERTINO\IDGS9-1\DB\parcial3\python\datos1.csv')

x = data[["GastoAlimentos", "GastoEntretenimiento"]].values
# modelo de kmeans con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(x)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_

plt.figure(figsize=(8, 6))

colors = ['red', 'green', 'blue', 'pink']
for i in range(len(x)):
    plt.scatter(x[i, 0], x[i, 1],
                color=colors[labels[i]], s=100,
                label=f'Cluster {labels[i] + 1}'
                if f'Cluster {labels[i] + 1}'
                not in plt.gca().get_legend_handles_labels()[1]
                else '')

plt.scatter(centroids[:, 0], centroids[:, 1],
            color='yellow', marker='x', s=200, label='Centroides')

plt.title("Segmentación de clientes con k-means")
plt.xlabel("Gasto alimenticio")
plt.ylabel("Gasto en entretenimiento")
plt.legend()
plt.grid(True)
plt.show()