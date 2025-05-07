import cv2
import numpy as np
import os

# Wczytanie obrazu
image = cv2.imread('kostka.png')

# Przeskalowanie obrazu do szerokości 300 px
scale_percent = 300 / image.shape[1] * 100
width = 300
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# 1. Klasyczne progowanie
threshold_values = [100, 140, 180]
for T in threshold_values:
    _, thresh = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)
    cv2.imshow(f'Progowanie klasyczne T={T}', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Eksperymentuj z metodą cv2.findContours
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

modes = {
    'RETR_EXTERNAL': cv2.RETR_EXTERNAL,
    'RETR_TREE': cv2.RETR_TREE,
    'RETR_LIST': cv2.RETR_LIST
}

for mode_name, mode in modes.items():
    contours, hierarchy = cv2.findContours(thresh.copy(), mode, cv2.CHAIN_APPROX_SIMPLE)
    contour_image = resized.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 0, 255), 2)
    cv2.imshow(f'Kontury - {mode_name}', contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 3. Eksperymentuj z rozdzielczością obrazu
scales = [0.5, 1.0, 1.5]
for scale in scales:
    new_width = int(resized.shape[1] * scale)
    new_height = int(resized.shape[0] * scale)
    dim = (new_width, new_height)
    scaled_image = cv2.resize(resized, dim, interpolation=cv2.INTER_AREA)
    gray_scaled = cv2.cvtColor(scaled_image, cv2.COLOR_BGR2GRAY)
    _, thresh_scaled = cv2.threshold(gray_scaled, 140, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh_scaled.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_image = scaled_image.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 0, 255), 2)
    cv2.imshow(f'Kontury - skala {scale}', contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 4. Numeryzacja kostek
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
numbered_image = resized.copy()
os.makedirs('kostki', exist_ok=True)
for i, cnt in enumerate(contours):
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.putText(numbered_image, str(i+1), (x + w//2, y + h//2),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    kostka = resized[y:y+h, x:x+w]
    cv2.imwrite(f'kostki/kostka_{i+1:02d}.png', kostka)
cv2.imshow('Numeryzacja kostek', numbered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. Pomiar wymiarów kostek
dimensioned_image = resized.copy()
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(dimensioned_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(dimensioned_image, f'{w}x{h}px', (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
cv2.imshow('Wymiary kostek', dimensioned_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Filtrowanie konturów po wielkości
filtered_image = resized.copy()
filtered_contours = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if 500 < area < 5000:
        filtered_contours.append(cnt)
cv2.drawContours(filtered_image, filtered_contours, -1, (255, 0, 0), 2)
cv2.imshow('Filtrowane kontury', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. Liczenie i raportowanie kostek
widths = []
heights = []
for cnt in filtered_contours:
    x, y, w, h = cv2.boundingRect(cnt)
    widths.append(w)
    heights.append(h)

if widths and heights:
    avg_width = sum(widths) / len(widths)
    avg_height = sum(heights) / len(heights)
    min_size = min(min(widths), min(heights))
    max_size = max(max(widths), max(heights))
    print(f'Liczba wykrytych kostek: {len(filtered_contours)}')
    print(f'Średnia szerokość: {avg_width:.2f}px')
    print(f'Średnia wysokość: {avg_height:.2f}px')
    print(f'Minimalny rozmiar: {min_size}px')
    print(f'Maksymalny rozmiar: {max_size}px')
else:
    print('Brak konturów spełniających kryteria filtracji.')
