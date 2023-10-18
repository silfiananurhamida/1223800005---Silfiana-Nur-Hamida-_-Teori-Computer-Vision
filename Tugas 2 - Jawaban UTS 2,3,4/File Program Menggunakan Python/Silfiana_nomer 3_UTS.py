import numpy as np

# matriks 3x3 dan 4x4
H = np.array([[1, 1, 1],
              [1, 4, 1],
              [1, 1, 1]])

X = np.array([[1, 0, 0, 0],
              [1, 1, 1, 0],
              [1, 1, 1, 0],
              [1, 0, 0, 0]])
NilaiY = 0

# Perhitungan konvolusi
for m in range(-1, 2):
    for n in range(-1, 2):
        if 0 <= (2 - m) < X.shape[0] and 0 <= (3 - n) < X.shape[1]:
            NilaiY += X[2 - m, 3 - n] * H[m + 1, n + 1]

# Cetak nilai Y(2,3)
print("Nilai Y(2,3) adalah:", NilaiY)
