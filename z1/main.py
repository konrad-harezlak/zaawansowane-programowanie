import cv2
import os

# Pobranie ścieżki do folderu, w którym znajduje się main.py
current_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_directory, "cat.jpg")

# Zadanie 1: Wczytaj i wyświetl obraz
image = cv2.imread(image_path)
if image is None:
    print("Błąd: nie można wczytać obrazu! Sprawdź ścieżkę.")
else:
    print("Obraz wczytano poprawnie.")
    cv2.imshow("Obraz", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Zadanie 2: Wczytaj zdjęcie w kolorze i wyświetl liczbę kanałów
(h, w, c) = image.shape  # Pobranie wymiarów i liczby kanałów
print(f'Kolorowy obraz: szerokość={w}, wysokość={h}, liczba kanałów={c}')

# Zadanie 3: Wczytaj zdjęcie w odcieniach szarości i wyświetl liczbę kanałów
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
(h_gray, w_gray) = image_gray.shape  # Tylko dwa wymiary (brak kanału kolorów)
print(f'Obraz w skali szarości: szerokość={w_gray}, wysokość={h_gray}, liczba kanałów=1')

# Zadanie 4: Zapisz obraz w skali szarości jako nowy plik
output_path = os.path.join(current_directory, "cat_gray.jpg")
cv2.imwrite(output_path, image_gray)
print(f'Obraz w skali szarości zapisano jako {output_path}')

# Zadanie 5: Otwórz dwa obrazy jednocześnie w osobnych oknach
cv2.imshow("Kolorowy obraz", image)
cv2.imshow("Obraz w skali szarości", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Zadanie 6: Wyświetl obraz w oknie o zmiennym rozmiarze
cv2.namedWindow("Obraz z dostosowaniem okna", cv2.WINDOW_NORMAL)
cv2.imshow("Obraz z dostosowaniem okna", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
