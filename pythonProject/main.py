import cv2
import numpy as np
import imutils

green=(0,255,0)
blue=(255,0,0)
red= (0,0,255)
image = cv2.imread('mountain.jpg')
height, width, _ = image.shape
#cv2.imshow("ZDJ", image)

M = np.float32([
[1, 0, 30],
[0, 1, 40]
])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
#cv2.imshow("Shifted Down and Right", shifted)

image2 = cv2.imread('mountain.jpg')
M2 = np.float32([
[1, 0, -20],
[0, 1, -50]
])
shifted2 = cv2.warpAffine(image2, M2, (image2.shape[1], image2.shape[0]))
#cv2.imshow("Shifted up and left", shifted2)

M2 = np.float32([
[1, 0, -1000],
[0, 1, -500]
])
shifted2 = cv2.warpAffine(image2, M2, (image2.shape[1], image2.shape[0]))
#cv2.imshow("Shifted more than half", shifted2)

image = cv2.imread('mountain.jpg')
shifted = imutils.translate(image,100,50)
cv2.imshow("shifted", shifted);
cv2.waitKey(0)
x=input('podaj x')
y=input('podaj y')
cv2.waitKey(0)
image = cv2.imread('mountain.jpg')
shifted = imutils.translate(image,x,y)
cv2.imshow("shifted", shifted);

cv2.waitKey(0)
cv2.destroyAllWindows()


