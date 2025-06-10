import cv2
<<<<<<< HEAD


image = cv2.imread("example.jpg")
cv2.imshow("Original", image)

print("[INFO] flipping image horizontally...")
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
print("[INFO] flipping image vertically...")
cv2.imshow("Flipped Vertically", flipped)
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped both vert and horiz",flipped)

(h, w) = image.shape[:2]
right_half = image[:, w // 2:]
flipped_right = cv2.flip(right_half, 1)
image[:, w // 2:] = flipped_right


image = cv2.imread("example.jpg")
cv2.imshow("Modified Image", image)
print("Wybierz odbicie:  0 – pionowe, 1 – poziome, -1 – oba")
choice = int(input())
cv2.waitKey(0)
flipped = cv2.flip(image, choice)
cv2.imshow("Flipped by the choice", flipped)
cv2.waitKey(0)
=======
import numpy as np

image = cv2.imread("face.jpg")

mask_face = np.zeros(image.shape[:2], dtype="uint8")


cv2.ellipse(mask_face, (1050, 500), (300, 350), 0, 0, 360, 255, -1)

masked_face = cv2.bitwise_and(image, image, mask=mask_face)
cv2.imshow("Maska na twarz", masked_face)

mask_eyes = np.ones(image.shape[:2], dtype="uint8") * 255
cv2.rectangle(mask_eyes, (900, 350), (1200, 450), 0, -1)

masked_eyes = cv2.bitwise_and(image, image, mask=mask_eyes)
cv2.imshow("Zasłonięte oczy", masked_eyes)

color_image = cv2.imread("face.jpg")


hsv_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)


lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

mask_red1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask_red2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask_red1, mask_red2)

red_extracted = cv2.bitwise_and(color_image, color_image, mask=red_mask)
cv2.imshow("Ekstrakcja czerwieni", red_extracted)

cv2.waitKey(0)
cv2.destroyAllWindows()
>>>>>>> opencv_basic_masking
