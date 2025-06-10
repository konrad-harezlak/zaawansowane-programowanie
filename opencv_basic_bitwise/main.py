# import the necessary packages
import numpy as np
import cv2

triangle = np.zeros((300, 300), dtype="uint8")
pts = np.array([[150, 0], [0, 250], [300, 250]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(triangle, [pts], 255)
cv2.imshow("Triangle", triangle)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAnd = cv2.bitwise_and(triangle, circle)
bitwiseOr = cv2.bitwise_or(triangle, circle)
bitwiseXor = cv2.bitwise_xor(triangle, circle)
bitwiseNot = cv2.bitwise_not(triangle)

cv2.imshow("AND", bitwiseAnd)
cv2.imshow("Or", bitwiseOr)
cv2.imshow("Xor", bitwiseXor)
cv2.imshow("Not", bitwiseNot)
cv2.waitKey(0)

image = cv2.imread(r'D:\Szkola\zaawansowane-programowanie\example.jpg')

# Sprawdź, czy obraz został wczytany poprawnie
if image is None:
    print("Błąd: Nie można wczytać obrazu. Sprawdź ścieżkę do pliku!")
    exit()

height, width = image.shape[:2]
shifted_image = np.zeros_like(image)
shifted_image[:, 10:] = image[:, :-10]


cv2.imshow('Original Image', image)
cv2.imshow('Shifted Image', shifted_image)


difference = cv2.bitwise_xor(image, shifted_image)
cv2.imshow('Difference (XOR)', difference)

cv2.waitKey(0)
cv2.destroyAllWindows()