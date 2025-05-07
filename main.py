import cv2
import numpy as np
import imutils
import os

# Wczytaj obrazy
image = cv2.imread('fanta.jpg')
template = cv2.imread('fanta_logo.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
(tH, tW) = gray_template.shape[:2]

# // 1. Wykrywanie logo w butelce Fanty
result = cv2.matchTemplate(gray_image, gray_template, cv2.TM_CCOEFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
top_left = maxLoc
bottom_right = (top_left[0] + tW, top_left[1] + tH)
cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
print(f"// 1. Współrzędne: {top_left}, Wartość dopasowania: {maxVal}")
cv2.imshow("Detected Logo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# // 2. Wrażliwość na obrót
for angle in [30, 45]:
    rotated = imutils.rotate(gray_image, angle)
    result = cv2.matchTemplate(rotated, gray_template, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    print(f"// 2. Obrót: {angle}°, Wartość dopasowania: {maxVal}")
    top_left = maxLoc
    bottom_right = (top_left[0] + tW, top_left[1] + tH)
    rotated_color = imutils.rotate(image, angle)
    cv2.rectangle(rotated_color, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imshow(f"Rotated {angle}°", rotated_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# // 3. Wrażliwość na skalowanie
for scale in [0.5, 1.5]:
    resized = cv2.resize(gray_image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    result = cv2.matchTemplate(resized, gray_template, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    print(f"// 3. Skala: {scale}, Wartość dopasowania: {maxVal}")
    top_left = maxLoc
    bottom_right = (top_left[0] + tW, top_left[1] + tH)
    resized_color = cv2.resize(image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    cv2.rectangle(resized_color, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imshow(f"Scaled {scale}", resized_color)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# // 4. Porównanie metod dopasowania
methods = [
    ('cv2.TM_CCOEFF', cv2.TM_CCOEFF),
    ('cv2.TM_CCOEFF_NORMED', cv2.TM_CCOEFF_NORMED),
    ('cv2.TM_CCORR', cv2.TM_CCORR),
    ('cv2.TM_CCORR_NORMED', cv2.TM_CCORR_NORMED),
    ('cv2.TM_SQDIFF', cv2.TM_SQDIFF),
    ('cv2.TM_SQDIFF_NORMED', cv2.TM_SQDIFF_NORMED)
]

for name, method in methods:
    result = cv2.matchTemplate(gray_image, gray_template, method)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = minLoc
        match_val = minVal
    else:
        top_left = maxLoc
        match_val = maxVal
    bottom_right = (top_left[0] + tW, top_left[1] + tH)
    image_copy = image.copy()
    cv2.rectangle(image_copy, top_left, bottom_right, (0, 255, 0), 2)
    print(f"// 4. Metoda: {name}, Wartość dopasowania: {match_val}")
    cv2.imshow(f"Method: {name}", image_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# // 5. Detekcja małych ikon interfejsu
screenshot = cv2.imread('screen.png')
icon_template = cv2.imread('template.png')
gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
gray_icon = cv2.cvtColor(icon_template, cv2.COLOR_BGR2GRAY)
(tH, tW) = gray_icon.shape[:2]
result = cv2.matchTemplate(gray_screenshot, gray_icon, cv2.TM_CCOEFF_NORMED)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
top_left = maxLoc
bottom_right = (top_left[0] + tW, top_left[1] + tH)
cv2.rectangle(screenshot, top_left, bottom_right, (0, 255, 0), 2)
cv2.imshow("Detected Icon", screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()

# // 6. Odporność na fałszywe trafienia
objects_image = cv2.imread('screen.png')
object_template = cv2.imread('template.png')
gray_objects = cv2.cvtColor(objects_image, cv2.COLOR_BGR2GRAY)
gray_object_template = cv2.cvtColor(object_template, cv2.COLOR_BGR2GRAY)
(tH, tW) = gray_object_template.shape[:2]
result = cv2.matchTemplate(gray_objects, gray_object_template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(result >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(objects_image, pt, (pt[0] + tW, pt[1] + tH), (0, 255, 0), 2)
cv2.imshow("Detected Objects", objects_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# // 7. Połączenie konturów i dopasowania szablonów
image = cv2.imread('fanta.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
template = cv2.imread('fanta_logo.jpg', 0)
(tH, tW) = template.shape[:2]
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    roi = gray[y:y+h, x:x+w]
    if roi.shape[0] < tH or roi.shape[1] < tW:
        continue
    result = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    if maxVal >= 0.8:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow("Matched Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
