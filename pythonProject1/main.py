import cv2
import numpy as np


image=cv2.imread('example.png')
M = np.ones(image.shape, dtype="uint8") * 50
image_numpy_bright = np.clip(image + M, 0, 255)

image_cv2_bright = cv2.add(image, (50, 50, 50))

cv2.imshow("Original Image", image)
cv2.imshow("Brightness (NumPy)", image_numpy_bright)
cv2.imshow("Brightness (OpenCV)", image_cv2_bright)


image_numpy_burn = np.clip(image + 150, 0, 255)

image_cv2_burn = cv2.add(image, (150, 150, 150))

cv2.imshow("Burn Effect (NumPy)", image_numpy_burn)
cv2.imshow("Burn Effect (OpenCV)", image_cv2_burn)

M = np.ones(image.shape, dtype="uint8") * 80
image_numpy_darker = np.clip(image - M, 0, 255)  # Odejmowanie jasności przy użyciu NumPy

image_cv2_darker = cv2.subtract(image, M)

cv2.imshow("Original Image", image)
cv2.imshow("Darker (NumPy)", image_numpy_darker)
cv2.imshow("Darker (OpenCV)", image_cv2_darker)

image_instagram = image.copy()

image_instagram[:, :, 2] = np.clip(image_instagram[:, :, 2] + 30, 0, 255)  # Czerwony kanał
image_instagram[:, :, 1] = np.clip(image_instagram[:, :, 1] - 20, 0, 255)  # Zielony kanał
image_instagram[:, :, 0] = np.clip(image_instagram[:, :, 0] + 10, 0, 255)  # Niebieski kanał

cv2.imshow("Instagram Filter", image_instagram)



image2 = np.roll(image, 10, axis=1)

diff = cv2.absdiff(image, image2)

cv2.imshow("Difference", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()