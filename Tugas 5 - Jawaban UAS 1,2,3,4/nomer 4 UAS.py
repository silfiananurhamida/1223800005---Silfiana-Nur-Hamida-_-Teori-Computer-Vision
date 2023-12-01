import cv2
import numpy as np

# Baca gambar
image = cv2.imread('bestie.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)  # Blur mengurangi noise
edges = cv2.Canny(blur, 50, 150)  # Deteksi tepi dengan Canny edge detection

# Transformasi Hough
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=50,
                           param1=100, param2=30, minRadius=20, maxRadius=100)

if circles is not None:
    circles = np.uint16(np.around(circles))

    for circle in circles[0, :]:
        center = (circle[0], circle[1])
        radius = circle[2]
        cv2.circle(image, center, radius, (0, 255, 0), 2)
cv2.imshow('Hasil Deteksi Lingkaran dengan Transformasi Hough', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
