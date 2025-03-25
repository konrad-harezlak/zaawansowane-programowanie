import argparse
import imutils
import cv2

image = cv2.imread("mouse.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("Rotated by 45 Degrees", rotated)

M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("Rotated by -90 Degrees", rotated)

M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("Rotated by 30 Degrees", rotated)

#cv2.waitKey(0)
#print("podaj o ile obrot: ")
#degrees=float(input())
#M = cv2.getRotationMatrix2D((cX, cY), degrees, 1.0)
#rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("Rotated by "+ str(degrees) +" Degrees", rotated)

rotated = imutils.rotate(image, 180)
#cv2.imshow("Rotated by 180 Degrees", rotated)

rotated = imutils.rotate_bound(image, -33)
#cv2.imshow("Rotated by 180 Degrees", rotated)


M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("wrap affine: Rotated by 60 Degrees", rotated)

rotated = imutils.rotate_bound(image, 60)
#cv2.imshow("imutils: Rotated by 180 Degrees", rotated)

rotated = imutils.rotate_bound(image, 30)
rotated = imutils.rotate_bound(rotated, 30)
rotated = imutils.rotate_bound(rotated, 30)
#cv2.imshow("imutils: Rotated by 3x30 Degrees", rotated)
rotated = imutils.rotate_bound(image, 90)
#cv2.imshow("imutils: Rotated by 90 Degrees", rotated)
rotated = imutils.rotate_bound(image, 75)
cv2.imwrite("rotated_output.jpg", rotated)


for i in range(0, 361, 15):
    print(i)
    rotated = imutils.rotate_bound(image, i)
    cv2.waitKey(500)
    cv2.imshow("imutils: Rotated by 90 Degrees", rotated)


cv2.waitKey(0)