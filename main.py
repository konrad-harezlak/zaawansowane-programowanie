import cv2
import numpy as np

image = cv2.imread("example.png")

(B, G, R) = cv2.split(image)


cv2.imshow("Blue Channel", B)
cv2.imshow("Green Channel", G)
cv2.imshow("Red Channel", R)
cv2.imwrite("blue_channel.jpg", B)
cv2.imwrite("green_channel.jpg", G)
cv2.imwrite("red_channel.jpg", R)

cv2.waitKey(0)


swapped = cv2.merge([R, B, G])
cv2.imshow("Swapped R-B-G", swapped)
cv2.waitKey(0)


B_zero = np.zeros_like(B)
no_blue = cv2.merge([B_zero, G, R])
cv2.imshow("Without Blue Channel", no_blue)
cv2.waitKey(0)

R_boosted = cv2.add(R, 50)
boosted_image = cv2.merge([B, G, R_boosted])
cv2.imshow("Red Boosted", boosted_image)
cv2.waitKey(0)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

mask_red1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask_red2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask_red1, mask_red2)

R_masked_boosted = cv2.add(R, 100, mask=red_mask)
masked_boosted_image = cv2.merge([B, G, R_masked_boosted])
cv2.imshow("Selective Red Boost", masked_boosted_image)
cv2.waitKey(0)

opencv_logo = cv2.imread("example.png")


(B_logo, G_logo, R_logo) = cv2.split(opencv_logo)

swapped_logo = cv2.merge([R_logo, G_logo, B_logo])
cv2.imshow("Swapped OpenCV Logo", swapped_logo)

G_logo_zero = np.zeros_like(G_logo)
no_green_logo = cv2.merge([B_logo, G_logo_zero, R_logo])
cv2.imshow("OpenCV Logo Without Green", no_green_logo)

cv2.waitKey(0)
cv2.destroyAllWindows()
