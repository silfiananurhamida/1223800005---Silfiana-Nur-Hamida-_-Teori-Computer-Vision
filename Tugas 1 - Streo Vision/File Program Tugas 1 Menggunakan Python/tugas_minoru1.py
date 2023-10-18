import numpy as np
import cv2

camera_right = cv2.VideoCapture(0)
camera_left = cv2.VideoCapture(2)

# Check if the cameras opened successfully
if not camera_left.isOpened() or not camera_right.isOpened():
    print("Gagal membuka kamera")
    exit()

stereo = cv2.StereoSGBM_create(numDisparities=18, blockSize=5)

while True:
    ret1, frame1 = camera_left.read()
    ret2, frame2 = camera_right.read()

    if not (ret1 and ret2):
        break

    left_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    right_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Disparitasi Map
    disparity = stereo.compute(left_gray, right_gray)
    disparity = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)
    disparity = disparity.astype(np.uint8)

    cv2.imshow('Camera Minoro Kiri', frame1)
    cv2.imshow('Camera Laptop', frame2)
    cv2.imshow('Depth Map', disparity)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera_left.release()
camera_right.release()
cv2.destroyAllWindows()
