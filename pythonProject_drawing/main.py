<<<<<<< HEAD
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
=======
import cv2
import numpy as np

green=(0,255,0)
blue=(255,0,0)
red= (0,0,255)
image = cv2.imread('mountain.jpg')
height, width, _ = image.shape
cv2.line(image,(width//2,height//2),(width,height),blue,2)
#cv2.imshow("ZDJ", image)
#cv2.waitKey(0);

canvas = np.zeros((400, 400, 3), dtype="uint8")

cv2.rectangle(canvas,(0,0),(100,50), green)
cv2.rectangle(canvas,(300,350),(400,400), red,3)
#cv2.imshow("ZDJ2", canvas)
#cv2.waitKey(0);

canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.circle(canvas, (40, 40), 40, blue)
cv2.circle(canvas, (150, 150), 60, red)
#cv2.imshow("ZDJ2", canvas)
#cv2.waitKey(0);

canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.rectangle(canvas, (100,100),(200,200), blue)
cv2.circle(canvas, (150, 150), 30, red)
#cv2.imshow("ZDJ2", canvas)
#cv2.waitKey(0);

canvas = np.zeros((300, 300, 3), dtype="uint8")
for length in range(0,150,20):
    cv2.rectangle(canvas, (150-length,150-length),(150+length,150+length), blue)
#cv2.imshow("ZDJ2", canvas)
#cv2.waitKey(0);

image = cv2.imread('user.jpg')
height, width, _ = image.shape
cv2.circle(image, (450,420),5,red, 10)
cv2.circle(image, (550,420),5,red, 10)
cv2.rectangle(image, (450,500),(550,550), green,-1)
cv2.circle(image, (width//2, height//2-35),145, blue, 5)
cv2.imshow("ZDJ2", image)
cv2.waitKey(0);
>>>>>>> opencv_basic_drawing
