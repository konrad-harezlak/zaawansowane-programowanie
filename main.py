import cv2
import numpy as np

def salt_and_pepper(image, salt_prob, pepper_prob):
    noisy = np.copy(image)
    total_pixels = image.size // 3  # Liczba pikseli dla obrazu RGB

    # Dodanie białych (solnych) pikseli
    num_salt = int(total_pixels * salt_prob)
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape[:2]]
    noisy[coords[0], coords[1], :] = 255

    # Dodanie czarnych (pieprznych) pikseli
    num_pepper = int(total_pixels * pepper_prob)
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape[:2]]
    noisy[coords[0], coords[1], :] = 0

    return noisy

image = cv2.imread('morty.jpg')
scale_percent = 50  # Procent oryginalnego rozmiaru
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
image = cv2.resize(image, (width, height))


cv2.imshow("Original", image)
blurred = cv2.blur(image, (3, 3))
cv2.imshow("Average ({}, {})".format(3, 3), blurred)


blurred = cv2.GaussianBlur(image, (3, 3), 0)
cv2.imshow("Gaussian ({}, {})".format(3, 3), blurred)


blurred = cv2.medianBlur(image, 3)
cv2.imshow("Median {}".format(3), blurred)


blurred = cv2.bilateralFilter(image, 11, 30, 7)
title = "Blurred d={}, sc={}, ss={}".format(11, 30, 7)
cv2.imshow(title, blurred)

blurred = cv2.blur(image, (5, 5))
cv2.imshow("Average (5, 5)", blurred)

blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Gaussian (5, 5)", blurred)

blurred = cv2.medianBlur(image, 5)
cv2.imshow("Median 5", blurred)

blurred = cv2.bilateralFilter(image, d=15, sigmaColor=100, sigmaSpace=100)
cv2.imshow("Bilateral d=15, sc=100, ss=100", blurred)
"""
Odpowiedzi na pytania:

1. Która metoda najlepiej usuwa szum?
   - Rozmycie medianowe (cv2.medianBlur) jest najlepsze do usuwania szumu solnego i pieprzowego, ponieważ zastępuje każdy piksel medianą sąsiednich pikseli.

2. Która metoda zachowuje najwięcej szczegółów?
   - Rozmycie dwustronne (cv2.bilateralFilter) zachowuje najwięcej szczegółów, ponieważ nie ma różnicy

3. Zalety i wady każdej metody:
   - cv2.blur (proste rozmycie): 
     + Zalety: szybkie, skuteczne dla prostych obrazów
     - Wady: utrata szczegółów, niewystarczające dla obrazów z dużą ilością szumu

   - cv2.GaussianBlur:
     + Zalety: bardziej naturalne rozmycie niż proste, skuteczne w redukcji szumu
     - Wady: nadal powoduje pewną utratę szczegółów

   - cv2.medianBlur:
     + Zalety: najlepsze dla usuwania szumu solnego i pieprzowego
     - Wady: mniej skuteczne dla ogólnego rozmycia

   - cv2.bilateralFilter:
     nie dziala
     
"""

cv2.waitKey(0)
cv2.destroyAllWindows()

kernel_sizes = [3, 5, 9, 15]

for k in kernel_sizes:
    avg_blur = cv2.blur(image, (k, k))
    cv2.imshow(f"Average ({k}x{k})", avg_blur)

    gauss_blur = cv2.GaussianBlur(image, (k, k), 0)
    cv2.imshow(f"Gaussian ({k}x{k})", gauss_blur)

    if k % 2 != 0:
        median_blur = cv2.medianBlur(image, k)
        cv2.imshow(f"Median {k}", median_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('grafiti.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = salt_and_pepper(image, 0.02, 0.02)

blur_gaussian = cv2.GaussianBlur(image, (5, 5), 0)
blur_median = cv2.medianBlur(image, 5)
blur_bilateral_1 = cv2.bilateralFilter(image, 9, 75, 75)
blur_bilateral_2 = cv2.bilateralFilter(image, 15, 150, 150)


cv2.imshow("Oryginalny", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
cv2.imshow("Gaussowskie", cv2.cvtColor(blur_gaussian, cv2.COLOR_RGB2BGR))
cv2.imshow("Medianowe", cv2.cvtColor(blur_median, cv2.COLOR_RGB2BGR))
cv2.imshow("Bilateralne (9,75,75)", cv2.cvtColor(blur_bilateral_1, cv2.COLOR_RGB2BGR))
cv2.imshow("Bilateralne (15,150,150)", cv2.cvtColor(blur_bilateral_2, cv2.COLOR_RGB2BGR))

cv2.waitKey(0)
cv2.destroyAllWindows()

# Komentarze do analizy wyników:
# 1. Rozmycie dwustronne nie działa
# 2. W porównaniu do rozmycia gaussowskiego i medianowego, lepiej utrzymuje krawędzie.
# 3. Różne wartosci daja te same rezultaty


cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('grafiti.png')

blur = cv2.blur(image, (5, 5))
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
median = cv2.medianBlur(image, 5)
bilateral = cv2.bilateralFilter(image, 9, 75, 75)


cv2.imshow('Original', image)
cv2.imshow('Blur', blur)
cv2.imshow('GaussianBlur', gaussian)
cv2.imshow('MedianBlur', median)
cv2.imshow('BilateralFilter', bilateral)


# 1. Najmocniej rozmywają tekst: cv2.blur i cv2.GaussianBlur, ponieważ rozmywają wszystkie krawędzie.
# 2. Najlepiej zachowują czytelność: cv2.medianBlur i cv2.bilateralFilter, ponieważ dobrze utrzymują krawędzie.
#  cv2.bilateralFilter pokazuje orginalny obraz bez rozmycia

cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('grafiti.png')
image=salt_and_pepper(image,0.2,0.2)

for k in kernel_sizes:
    avg_blur = cv2.blur(image, (k, k))
    cv2.imshow(f"Average ({k}x{k})", avg_blur)

    gauss_blur = cv2.GaussianBlur(image, (k, k), 0)
    cv2.imshow(f"Gaussian ({k}x{k})", gauss_blur)

    if k % 2 != 0:
        median_blur = cv2.medianBlur(image, k)
        cv2.imshow(f"Median {k}", median_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread('corolla.jpg')
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# Określenie współrzędnych głównego obiektu (należy dostosować)
roi = (60, 100, 900, 500)  # (x, y, szerokość, wysokość)
x, y, w, h = roi
mask[y:y + h, x:x + w] = 255  # Tworzenie prostokątnej maski

# Rozmycie całego obrazu
blurred = cv2.GaussianBlur(image, (21, 21), 0)

# Wstawienie ostrego obiektu z powrotem
result = np.where(mask[:, :, None] == 255, image, blurred)

# Wyświetlenie wyników
cv2.imshow("Original", image)
cv2.imshow("Depth of Field Effect", result)

cv2.waitKey(0)
cv2.destroyAllWindows()