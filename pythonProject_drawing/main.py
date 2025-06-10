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
