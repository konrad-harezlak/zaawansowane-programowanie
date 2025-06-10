import cv2
import numpy as np

# Z1 - Wizualizacja składowych RGB i HSV

image = cv2.imread("example.jpg")
cv2.imshow("Original - RGB", image)

b, g, r = cv2.split(image)
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

h, s, v = cv2.split(hsv)
cv2.imshow("Hue Channel", h)
cv2.imshow("Saturation Channel", s)
cv2.imshow("Value Channel", v)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Z2 - Modyfikacja jednego kanału (np. Saturation)

image = cv2.imread("example.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

s = cv2.add(s, 30)  # zwiększenie nasycenia
merged = cv2.merge([h, s, v])
modified = cv2.cvtColor(merged, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", image)
cv2.imshow("Modified - Saturation +30", modified)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Z3 - Wykrywanie niebieskich obiektów

image = cv2.imread("example.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original", image)
cv2.imshow("Blue Mask", mask)
cv2.imshow("Detected Blue", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Z4 - Manipulacja barwy (zmiana H)

image = cv2.imread("example.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)
h = (h + 30) % 180

merged = cv2.merge([h, s, v])
modified = cv2.cvtColor(merged, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", image)
cv2.imshow("Hue +30", modified)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Z5 - Wykrywanie zielonych obiektów

image = cv2.imread("example.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_green = np.array([35, 40, 40])
upper_green = np.array([85, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original", image)
cv2.imshow("Green Mask", mask)
cv2.imshow("Detected Green", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Z6 - Rozpoznawanie koloru skóry

image = cv2.imread("example.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_skin = np.array([0, 20, 70])
upper_skin = np.array([20, 255, 255])
mask = cv2.inRange(hsv, lower_skin, upper_skin)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original", image)
cv2.imshow("Skin Mask", mask)
cv2.imshow("Detected Skin", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Z7 - Analiza nasycenia

image = cv2.imread("example.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

s_lower = cv2.subtract(s, 50)
s_higher = cv2.add(s, 50)

img_low = cv2.cvtColor(cv2.merge([h, s_lower, v]), cv2.COLOR_HSV2BGR)
img_high = cv2.cvtColor(cv2.merge([h, s_higher, v]), cv2.COLOR_HSV2BGR)

cv2.imshow("Original", image)
cv2.imshow("Lower Saturation", img_low)
cv2.imshow("Higher Saturation", img_high)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Z8 - Segmentacja kolorów (niebieski, czerwony, zielony)

image = cv2.imread("example.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Blue
blue_mask = cv2.inRange(hsv, (100, 150, 50), (140, 255, 255))
# Red
red_mask1 = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))
red_mask2 = cv2.inRange(hsv, (160, 100, 100), (180, 255, 255))
red_mask = cv2.bitwise_or(red_mask1, red_mask2)
# Green
green_mask = cv2.inRange(hsv, (35, 40, 40), (85, 255, 255))

combined_mask = cv2.bitwise_or(cv2.bitwise_or(blue_mask, red_mask), green_mask)
result = cv2.bitwise_and(image, image, mask=combined_mask)

cv2.imshow("Original", image)
cv2.imshow("Combined Mask", combined_mask)
cv2.imshow("Segmented Colors", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
