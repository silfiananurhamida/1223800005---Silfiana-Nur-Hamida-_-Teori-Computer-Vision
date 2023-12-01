import cv2

def calculate_SAD(image1, image2):
    img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)

    if img1 is None or img2 is None:
        print("Gambar tidak dapat dibaca. Pastikan path file benar.")
        return
    if img1.shape != img2.shape:
        print("Ukuran gambar tidak sama.")
        return
    sad_value = cv2.absdiff(img1, img2).sum()

    return sad_value

if __name__ == "__main__":
    image_path1 = 'mybest.jpg'  
    image_path2 = 'myfriend.jpg'  

    # Hitung SAD antara kedua gambar
    sad = calculate_SAD(image_path1, image_path2)

    if sad is not None:
        print(f"Nilai SAD antara kedua gambar adalah: {sad}")
