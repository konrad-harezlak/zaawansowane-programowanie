import cv2
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
