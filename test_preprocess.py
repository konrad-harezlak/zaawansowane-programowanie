import cv2
from detect_and_ocr import detect_plate, preprocess_for_ocr
import pytesseract
import numpy as np


def show_preprocessed_plate(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Nie udało się wczytać: ", image_path)
        return

    boxes = detect_plate(image_path)
    if len(boxes) == 0:
        print("Nie wykryto żadnej tablicy na: ", image_path)
        return


    cfg = r'--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = map(int, box)

        h, w = img.shape[:2]
        x1, x2 = max(0, x1), min(w, x2)
        y1, y2 = max(0, y1), min(h, y2)
        if x2 <= x1 or y2 <= y1:
            continue

        plate = img[y1:y2, x1:x2]
        proc = preprocess_for_ocr(plate)

        cv2.imshow(f"Original Plate {i+1}", plate)
        cv2.imshow(f"Preprocessed Plate {i+1}", proc)


        text = pytesseract.image_to_string(proc, config=cfg).strip()
        if len(text) > 7:
            text = text[1:].upper()

        print(f"Plate {i+1} OCR result: {text}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":

    show_preprocessed_plate("data/photos/129.jpg")
