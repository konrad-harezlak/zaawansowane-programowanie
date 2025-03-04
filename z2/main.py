import cv2
import numpy as np

# Wczytanie obrazu
image = cv2.imread('mouse.jpg')
height, width, _ = image.shape
print("Wysokość obrazu: ", height,"Szerokość obrazu: ", width);
# 1. Odczyt wartości piksela
# a. Pobranie wartości piksela w lewym górnym rogu (0,0)
pixel_value = image[0, 0]
print("Wartość piksela w lewym górnym rogu (0,0):", pixel_value)

# b. Wyświetlenie składowych koloru (R, G, B)
B, G, R = pixel_value
print("R:", R, "G:", G, "B:", B)

# 2. Modyfikacja pojedynczego piksela
# a. Zmieniamy kolor piksela w prawym dolnym rogu na czerwony (0, 0, 255)
image[height-10, width-10] = [0, 0, 255]

# b. Wyświetlenie obrazu przed i po zmianie
cv2.imshow("Przed zmianą", cv2.imread('mouse.jpg'))
cv2.imshow("Po zmianie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Znajdowanie środka obrazu
# a. Obliczanie współrzędnych środka
center_x, center_y = width // 2, height // 2

# b. Pobranie wartości piksela w tym miejscu
center_pixel = image[center_y, center_x]
print("Wartość piksela w środku obrazu:", center_pixel)

# 4. Zamiana wartości piksela na czarny
# a. Pobranie współrzędnych od użytkownika
x = int(input("Podaj współrzędną x: "))
y = int(input("Podaj współrzędną y: "))

# b. Sprawdzenie, czy współrzędne są w obrębie obrazu
if 0 <= x < width and 0 <= y < height:
    image[y, x] = [0, 0, 0]  # Ustawiamy piksel na czarny
else:
    print("Współrzędne wychodzą poza zakres obrazu.")

# Wyświetlenie obrazu po zmianie
cv2.imshow("Obraz po zmianie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. Kolorowanie fragmentu obrazu
# a. Podział obrazu na 4 ćwiartki i wypełnienie lewą górną ćwiartkę na niebiesko
quarter_height, quarter_width = height // 2, width // 2
image[0:quarter_height, 0:quarter_width] = [255, 0, 0]  # Niebieski

# Wyświetlenie obrazu po zmianach
cv2.imshow("Obraz po zmianach", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Wypełnienie konkretnego obszaru obrazu jednolitym kolorem
# a. Wypełnienie kwadratu o wymiarach 100x100 px na czerwono
image[center_y-50:center_y+50, center_x-50:center_x+50] = [0, 0, 255]

# Wyświetlenie obrazu po zmianie
cv2.imshow("Obraz po zmianie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. Wycięcie fragmentu obrazu
# a. Podział obrazu na 9 części i wycięcie fragmentu obejmującego środek
crop_x1, crop_y1 = width // 3, height // 3
crop_x2, crop_y2 = width * 2 // 3, height * 2 // 3
cropped_image = image[crop_y1:crop_y2, crop_x1:crop_x2]

# Wyświetlenie wyciętego fragmentu
cv2.imshow("Wycięty fragment", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8. Modyfikacja całego wiersza pikseli
# a. Zmiana koloru 100. wiersza na zielony (0, 255, 0)
image[99, :] = [0, 255, 0]  # Zielony

# Wyświetlenie obrazu przed i po zmianie
cv2.imshow("Przed zmianą", cv2.imread('mouse.jpg'))
cv2.imshow("Po zmianie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 9. Zmiana wartości pikseli w określonym zakresie
# a. Wypełnienie obszaru od (50,50) do (100,100) kolorem białym (255, 255, 255)
image[50:100, 50:100] = [255, 255, 255]

# Wyświetlenie obrazu przed i po zmianie
cv2.imshow("Przed zmianą", cv2.imread('mouse.jpg'))
cv2.imshow("Po zmianie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 10. Sprawdzenie różnicy wartości pikseli
# a. Porównanie wartości pikseli w dwóch miejscach obrazu
pixel_1 = image[50, 50]
pixel_2 = image[200, 200]

# b. Obliczanie różnicy w wartościach R, G, B
diff = pixel_1 - pixel_2
print(f"Różnice w wartościach R, G, B: {diff}")

# 11. Znajdowanie najjaśniejszego piksela w obrazie
# a. Funkcja do obliczania jasności piksela
def brightness(pixel):
    # Upewnij się, że każdy składnik RGB mieści się w przedziale 0-255
    pixel = np.array(pixel, dtype=np.int32)
    return sum(pixel) / 3  # Średnia wartość RGB


max_brightness = 0
max_pixel = (0, 0)
height, width, _ = image.shape  # Pobieranie wymiarów obrazu

for y in range(height):
    for x in range(width):
        pixel = image[y, x]
        pixel_brightness = brightness(pixel)
        if pixel_brightness > max_brightness:
            max_brightness = pixel_brightness
            max_pixel = (x, y)

print(f"Najjaśniejszy piksel znajduje się w {max_pixel} o jasności {max_brightness}")

