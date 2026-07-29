import cv2

image_path = "assets/test.jpeg"

image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
else:
    print("Image loaded successfully!")
    print("Height:", image.shape[0])
    print("Width :", image.shape[1])
    print("Channels:", image.shape[2])