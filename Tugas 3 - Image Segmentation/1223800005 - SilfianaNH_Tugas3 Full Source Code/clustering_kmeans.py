import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from PIL import Image
gambar = np.array(Image.open('favorit.jpg'))

gambar = gambar / 255.0  

w, h, d = original_shape = tuple(gambar.shape)
assert d == 3 

image_array = np.reshape(gambar, (w * h, d))

n_colors = 3
kmeans = KMeans(n_clusters=n_colors, random_state=0).fit(image_array)
labels = kmeans.predict(image_array)
centers = kmeans.cluster_centers_

compressed_image = centers[labels].reshape(gambar.shape)
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.axis('off')
plt.title('Citra Gambar Asli')
plt.imshow(gambar)

plt.subplot(1, 2, 2)
plt.axis('off')
plt.title('Citra Gambar Menggunakan K-means')
plt.imshow(compressed_image)
plt.show()
