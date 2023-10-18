import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('mybest.jpg', cv2.IMREAD_GRAYSCALE)

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

# Normalisasi histogram
normalisasi = hist / sum(hist)

# Hitung CDF
cdf = np.cumsum(normalisasi)

proces_equalized = np.interp(img.flatten(), range(256), 255 * cdf).astype(np.uint8)

result_equalized = proces_equalized.reshape(img.shape)

hist_eq, bins_eq = np.histogram(result_equalized.flatten(), 256, [0, 256])

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')

plt.subplot(1, 2, 2)
plt.imshow(result_equalized, cmap='gray')
plt.title('Hasil Citra Setelah Histogram Equalization')

plt.show()
