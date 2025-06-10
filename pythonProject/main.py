import cv2
import numpy as np

image = cv2.imread('example.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Binary Image", binary_image)


kernel = np.ones((3, 3), np.uint8)


for i in range(0, 3):
    eroded = cv2.erode(binary_image.copy(), kernel, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()
for i in range(0, 3):
    dilated = cv2.dilate(binary_image.copy(), None, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = image.copy()
    total_pixels = image.size

    num_salt = int(salt_prob * total_pixels)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1]] = 255

    num_pepper = int(pepper_prob * total_pixels)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0

    return noisy_image
noisy_image = add_salt_and_pepper_noise(image, salt_prob=0.05, pepper_prob=0.05)

cv2.destroyAllWindows()
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(noisy_image, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Opening with kernel {kernelSize}", opening)

cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Opening with 3x3 kernel", cv2.morphologyEx(noisy_image, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)))
cv2.destroyAllWindows()

broken = cv2.imread('broken.png')

gray = cv2.cvtColor(broken, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)
closed_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Original Image', broken)
cv2.imshow('Binary Image', binary_image)
cv2.imshow('Closed Image', closed_image)

kernel_rect = np.ones((5, 5), np.uint8)
closed_image_rect = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel_rect)
cv2.imshow('Closed Image (Rectangular Kernel)', closed_image_rect)

kernel_elliptical = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
closed_image_elliptical = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel_elliptical)
cv2.imshow('Closed Image (Elliptical Kernel)', closed_image_elliptical)

kernel_rect_7 = np.ones((7, 7), np.uint8)
closed_image_rect_7 = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel_rect_7)
cv2.imshow('Closed Image (Rectangular Kernel 7x7)', closed_image_rect_7)

kernel_elliptical_7 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
closed_image_elliptical_7 = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel_elliptical_7)
cv2.imshow('Closed Image (Elliptical Kernel 7x7)', closed_image_elliptical_7)


cv2.waitKey(0)
cv2.destroyAllWindows()

kernel_sizes = [(3, 3), (5, 5), (7, 7)]
kernels = {
    "Rectangular": [np.ones(size, np.uint8) for size in kernel_sizes],
    "Elliptical": [cv2.getStructuringElement(cv2.MORPH_ELLIPSE, size) for size in kernel_sizes],
    "Cross": [cv2.getStructuringElement(cv2.MORPH_CROSS, size) for size in kernel_sizes]
}

# Funkcja do wykonywania podstawowych operacji morfologicznych
def apply_morph_operations(binary_image, kernels):
    for shape, kernel_list in kernels.items():
        for kernel in kernel_list:
            eroded = cv2.erode(binary_image, kernel)
            cv2.imshow(f"Erosion - {shape} - Kernel {kernel.shape}", eroded)

            dilated = cv2.dilate(binary_image, kernel)
            cv2.imshow(f"Dilation - {shape} - Kernel {kernel.shape}", dilated)

            opened = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
            cv2.imshow(f"Opening - {shape} - Kernel {kernel.shape}", opened)

            closed = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
            cv2.imshow(f"Closing - {shape} - Kernel {kernel.shape}", closed)

            gradient = cv2.morphologyEx(binary_image, cv2.MORPH_GRADIENT, kernel)
            cv2.imshow(f"Gradient - {shape} - Kernel {kernel.shape}", gradient)

apply_morph_operations(binary_image, kernels)

image = cv2.imread('tablica.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Zastosowanie progowania, aby uzyskać obraz binarny
_, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Dodanie szumu typu solny i pieprzowy do obrazu
def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = image.copy()
    total_pixels = image.size

    num_salt = int(salt_prob * total_pixels)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1]] = 255

    num_pepper = int(pepper_prob * total_pixels)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0

    return noisy_image

# Dodanie szumu typu solny i pieprzowy
noisy_image = add_salt_and_pepper_noise(binary_image, salt_prob=0.05, pepper_prob=0.05)
cv2.imshow("Noisy Image", noisy_image)

# Zastosowanie otwarcia (Opening) do usuwania szumu
kernel_sizes = [(3, 3), (5, 5), (7, 7)]
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    opening_image = cv2.morphologyEx(noisy_image, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Opening with kernel {kernel_size}", opening_image)

# Zastosowanie otwarcia z eliptycznym elementem strukturalnym
for kernel_size in kernel_sizes:
    kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, kernel_size)
    opening_image_ellipse = cv2.morphologyEx(noisy_image, cv2.MORPH_OPEN, kernel_ellipse)
    cv2.imshow(f"Opening with elliptical kernel {kernel_size}", opening_image_ellipse)

# Zastosowanie otwarcia z krzyżowym elementem strukturalnym
for kernel_size in kernel_sizes:
    kernel_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, kernel_size)
    opening_image_cross = cv2.morphologyEx(noisy_image, cv2.MORPH_OPEN, kernel_cross)
    cv2.imshow(f"Opening with cross-shaped kernel {kernel_size}", opening_image_cross)

# Wyświetlenie oryginalnego obrazu oraz binarnego
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
