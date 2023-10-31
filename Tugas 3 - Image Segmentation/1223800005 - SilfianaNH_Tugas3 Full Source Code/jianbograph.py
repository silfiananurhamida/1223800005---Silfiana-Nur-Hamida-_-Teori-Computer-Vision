import networkx as nx
import numpy as np
from sklearn.cluster import spectral_clustering

G = nx.karate_club_graph()

matrix_conv = nx.to_numpy_matrix(G)

array_conv = np.array(matrix_conv)

num_clusters = 2  
labels = spectral_clustering(array_conv, n_clusters=num_clusters)

# Hasil partisi graf
for node, label in enumerate(labels):
    print(f"Node {node} berada di Kelompok {label}")
