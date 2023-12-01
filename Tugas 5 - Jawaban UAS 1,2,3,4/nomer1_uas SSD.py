import cv2
import numpy as np

def ssd(image1, image2):
    if image1.shape != image2.shape:
        raise ValueError("Ukuran citra tidak sama")

    squared_diff = np.square(image1.astype(np.float64) - image2.astype(np.float64))
    ssd_value = np.sum(squared_diff)

    return ssd_value

# Baca dua citra
img1 = cv2.imread('mybest.jpg'  , cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('myfriend.jpg' , cv2.IMREAD_GRAYSCALE)

# Hitung SSD antara kedua citra
ssd_value = ssd(img1, img2)
print(f"Hasil SSD antara kedua citra: {ssd_value}")
