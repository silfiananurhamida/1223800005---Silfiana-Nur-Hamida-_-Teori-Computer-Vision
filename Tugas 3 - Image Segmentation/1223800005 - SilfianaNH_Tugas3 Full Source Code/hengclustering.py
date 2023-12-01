import numpy as np
from sklearn.cluster import KMeans
from skimage.feature import graycomatrix, graycoprops
from skimage import io, color, img_as_ubyte

def extract_texture_features(image_path):
    image = io.imread(image_path)
    gray_image = img_as_ubyte(color.rgb2gray(image))
    glcm = graycomatrix(gray_image, [1], [0], symmetric=True, normed=True)
    contrast = graycoprops(glcm, prop='contrast')
    correlation = graycoprops(glcm, prop='correlation')
    
    return [contrast[0, 0], correlation[0, 0]]
image_paths = ["best.jpg", "love.jpg", "kayu.jpg", "download.jpg"]
features = [extract_texture_features(path) for path in image_paths]
kmeans = KMeans(n_clusters=2)
kmeans.fit(features)
labels = kmeans.labels_
for i, path in enumerate(image_paths):
    print(f"Gambar {path} termasuk dalam klaster {labels[i]}")
