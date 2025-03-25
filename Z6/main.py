import cv2
import imutils

image = cv2.imread("mouse.jpg")
cv2.imshow("Original", image)


height, width = image.shape[:2]
new_width = width // 2
new_height = height // 2
resized_image = cv2.resize(image, (new_width, new_height))
#cv2.imshow("Zmniejszony obraz", resized_image)

resized_image = cv2.resize(image, (new_width * 4, new_height * 4), interpolation=cv2.INTER_LINEAR)
#cv2.imshow("Powiekszony obraz", resized_image)

resized_image = cv2.resize(image, (200, 300))
#cv2.imshow("200x300 obraz", resized_image)

resized_nearest = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_NEAREST)
resized_linear = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)
resized_cubic = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
resized_lanczos4 = cv2.resize(image, None, fx=3, fy=3, interpolation=cv2.INTER_LANCZOS4)

#cv2.imshow("INTER_NEAREST", resized_nearest)
#cv2.imshow("INTER_LINEAR", resized_linear)
#cv2.imshow("INTER_CUBIC", resized_cubic)
#cv2.imshow("INTER_LANCZOS4", resized_lanczos4)

resized_image = imutils.resize(image, width=500)
#cv2.imshow("Resized width", resized_image)
resized_image = imutils.resize(image, height=400)
#cv2.imshow("Resized height", resized_image)

resized_area = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
#cv2.imshow("INTER_AREA", resized_area)

resized_cubic = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
resized_lanczos4 = cv2.resize(image, None, fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)

#cv2.imshow("INTER_CUBIC", resized_cubic)
#cv2.imshow("INTER_LANCZOS4", resized_lanczos4)

for scale in range(100, 301, 20):
    fx = scale / 100
    fy = scale / 100
    resized_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(f"Resized {scale}%", resized_image)
    cv2.waitKey(500)

resized_image = imutils.resize(image, width=800)

cv2.imwrite("resized_output.jpg", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()