import cv2


image = cv2.imread("example.jpg")
cv2.imshow("Original", image)

print("[INFO] flipping image horizontally...")
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

flipped = cv2.flip(image, 0)
print("[INFO] flipping image vertically...")
cv2.imshow("Flipped Vertically", flipped)
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped both vert and horiz",flipped)

(h, w) = image.shape[:2]
right_half = image[:, w // 2:]
flipped_right = cv2.flip(right_half, 1)
image[:, w // 2:] = flipped_right


image = cv2.imread("example.jpg")
cv2.imshow("Modified Image", image)
print("Wybierz odbicie:  0 – pionowe, 1 – poziome, -1 – oba")
choice = int(input())
cv2.waitKey(0)
flipped = cv2.flip(image, choice)
cv2.imshow("Flipped by the choice", flipped)
cv2.waitKey(0)