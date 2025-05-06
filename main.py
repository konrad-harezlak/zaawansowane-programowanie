import cv2
import numpy as np

# 1.
img = cv2.imread('tekst.png', cv2.IMREAD_GRAYSCALE)
_, thresh_simple = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
_, thresh_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
thresh_adaptive_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                             cv2.THRESH_BINARY, 11, 2)
thresh_adaptive_gauss = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 11, 2)
cv2.imshow('1. Simple', thresh_simple)
cv2.imshow('1. Otsu', thresh_otsu)
cv2.imshow('1. Adaptive Mean', thresh_adaptive_mean)
cv2.imshow('1. Adaptive Gauss', thresh_adaptive_gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 2.
for block_size in [11, 21, 31, 41]:
    result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, block_size, 2)
    cv2.imshow(f'2. blockSize={block_size}', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 3.
for method in [cv2.ADAPTIVE_THRESH_MEAN_C, cv2.ADAPTIVE_THRESH_GAUSSIAN_C]:
    for c in [2, 5, 10, 15]:
        name = f'3. {"Mean" if method == 0 else "Gaussian"} C={c}'
        result = cv2.adaptiveThreshold(img, 255, method,
                                       cv2.THRESH_BINARY, 21, c)
        cv2.imshow(name, result)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 4.
doc = cv2.imread('tekst.png', cv2.IMREAD_GRAYSCALE)
doc_thresh = cv2.adaptiveThreshold(doc, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 21, 10)
cv2.imshow('4. Dokument binarny', doc_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 5.
image = cv2.imread('tekst.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                             cv2.THRESH_BINARY_INV, 21, 10)
foreground = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('5. Maska', mask)
cv2.imshow('5. Foreground', foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 6.
def nothing(x):
    pass

cv2.namedWindow('6. Interactive')
cv2.createTrackbar('blockSize', '6. Interactive', 11, 51, nothing)
cv2.createTrackbar('C', '6. Interactive', 10, 40, nothing)

while True:
    b = cv2.getTrackbarPos('blockSize', '6. Interactive')
    c = cv2.getTrackbarPos('C', '6. Interactive') - 20
    if b % 2 == 0:
        b += 1
    if b < 3:
        b = 3
    adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY, b, c)
    cv2.imshow('6. Interactive', adaptive)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
