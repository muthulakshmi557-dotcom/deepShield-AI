import cv2

# Load Image
image = cv2.imread("assets/test.jpeg")

# Check Image
if image is None:
    print("Image not found!")
    exit()

print("Image Loaded Successfully!")

# Resize Image
resized = cv2.resize(image, (224, 224))

print("Original Size:", image.shape)
print("Resized Size :", resized.shape)