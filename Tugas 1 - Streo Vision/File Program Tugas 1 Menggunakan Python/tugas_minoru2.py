import cv2
import numpy as np

camera_left = cv2.VideoCapture(0)
camera_right = cv2.VideoCapture(1)  

while True:
    ret_left, frame_left = camera_left.read()
    ret_right, frame_right = camera_right.read()

    if not ret_left or not ret_right:
        break
    gray_left = cv2.cvtColor(frame_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(frame_right, cv2.COLOR_BGR2GRAY)

    # Menghitung citra disparitas
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(gray_left, gray_right)
    disparity = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)
    disparity = disparity.astype(np.uint8)
    baseline = 10.0  
    focal_length = 200.0  
    
    Q = np.float32([[1, 0, 0, -baseline],
                    [0, 1, 0, 0],
                    [0, 0, 0, focal_length],
                    [0, 0, -1/baseline, 0]])

    depth_map = cv2.reprojectImageTo3D(disparity, Q)

    threshold_distance = 100 
    object_mask = (depth_map[:, :, 2] < threshold_distance).astype(np.uint8) * 255

    # Menampilkan citra
    cv2.imshow('Left Camera', frame_left)
    cv2.imshow('Right Camera', frame_right)
    cv2.imshow('Object Mask', object_mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera_left.release()
camera_right.release()
cv2.destroyAllWindows()
