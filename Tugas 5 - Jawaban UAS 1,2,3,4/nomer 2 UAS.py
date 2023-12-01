import cv2
import numpy as np

def apply_gaussian_filter(image):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Filter Gaussian
    filtered_image = cv2.GaussianBlur(image, (15, 15), 0) 
    return filtered_image

# Fungsi filter
def reconstruct_image(filtered_image, original_shape):
    reconstructed_image = cv2.resize(filtered_image, original_shape[:2][::-1])

    return reconstructed_image
input_image = cv2.imread('bestie.png') 
original_shape = input_image.shape

filtered_image = apply_gaussian_filter(input_image)
reconstructed_image = reconstruct_image(filtered_image, original_shape)
cv2.imshow('Original Image', input_image)
cv2.imshow('Filtered Image', filtered_image)
cv2.imshow('Reconstructed Image', reconstructed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
