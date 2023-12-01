import cv2
import numpy as np

gambar = cv2.imread('bestie.png', cv2.IMREAD_GRAYSCALE)
result_sobel_vertikal = np.array([[-1, 0, 1],
                                  [-2, 0, 2],
                                  [-1, 0, 1]])

result_sobel_horizontal = np.array([[-1, -2, -1],
                                    [0, 0, 0],
                                    [1, 2, 1]])

hasil_vertikal = cv2.filter2D(gambar, -1, result_sobel_vertikal)

hasil_horizontal = cv2.filter2D(gambar, -1, result_sobel_horizontal)

cv2.imshow('Hasil Sobel Vertikal', hasil_vertikal)
cv2.imshow('Hasil Sobel Horizontal', hasil_horizontal)

cv2.waitKey(0)
cv2.destroyAllWindows()
