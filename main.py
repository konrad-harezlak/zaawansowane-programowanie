import cv2
import numpy as np

#z1
image = cv2.imread("example.jpg")
cv2.imshow("Original", image)

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# threshold T=30
(T, thresh30) = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh T=30", thresh30)
cv2.waitKey(0)
cv2.destroyAllWindows()

# threshold T=100
(T, thresh100) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh T=100", thresh100)
cv2.waitKey(0)
cv2.destroyAllWindows()

# threshold T=200
(T, thresh200) = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh T=200", thresh200)
cv2.waitKey(0)
cv2.destroyAllWindows()

#z2
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
(T, thresh_blur) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh after Blur", thresh_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

#z3
kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(thresh_blur, kernel, iterations=1)
cv2.imshow("Erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

#z4
bright = cv2.add(gray, 50)
cv2.imshow("Brightened", bright)
(T, thresh_bright) = cv2.threshold(bright, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh Brightened", thresh_bright)
cv2.waitKey(0)
cv2.destroyAllWindows()

#z5
(T, otsu) = cv2.threshold(bright, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu", otsu)
print("[INFO] Otsu's threshold value:", T)
cv2.waitKey(0)
cv2.destroyAllWindows()

#z6
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
otsu_val = int(T)
hist_img = np.zeros((300, 256), dtype=np.uint8)
cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
for x in range(256):
    cv2.line(hist_img, (x, 300), (x, 300 - int(hist[x][0])), 255)
cv2.line(hist_img, (otsu_val, 0), (otsu_val, 300), 127)
cv2.imshow("Histogram (Otsu line)", hist_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#z7
masked = cv2.bitwise_and(image, image, mask=otsu.astype(np.uint8))
cv2.imshow("Masked Object", masked)
cv2.waitKey(0)
cv2.destroyAllWindows()

#z8
kostka = cv2.imread("kostka.jpg")
if kostka is None:
    print("[ERROR] Failed to load 'kostka.jpg'. Check the file path.")
else:
    kostka_gray = cv2.cvtColor(kostka, cv2.COLOR_BGR2GRAY)
    kostka_blur = cv2.GaussianBlur(kostka_gray, (7, 7), 0)

    # manual T=100
    (T, kostka_thresh) = cv2.threshold(kostka_blur, 100, 255, cv2.THRESH_BINARY)
    cv2.imshow("Kostka Thresh T=100", kostka_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # otsu
    (T, kostka_otsu) = cv2.threshold(kostka_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow("Kostka Otsu", kostka_otsu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # erosion for kostka
    kostka_eroded = cv2.erode(kostka_otsu, kernel, iterations=1)
    cv2.imshow("Kostka Otsu + Erosion", kostka_eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
