import yolov5
import cv2
import pytesseract
import torch
import os
import numpy as np

#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = yolov5.load('keremberke/yolov5n-license-plate')

model.conf = 0.2


def detect_plate(image_path):
    results = model(image_path, size=640)
    return results.pred[0][:, :4].cpu().numpy()


def preprocess_for_ocr(img):
    h, w = img.shape[:2]
    scale = 200 / h
    img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # thr = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
    #                          cv2.THRESH_BINARY_INV, 91, 50)
    # gray = cv2.bitwise_not(thr)
    
    gray = cv2.bilateralFilter(gray, 11, 19,19)
    #gray = cv2.medianBlur(gray, 1)


    #_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    # opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)
    #cleaned = remove_small_blobs(binary, min_area_black=500, min_area_white=1000)
    return gray
def extract_plate_and_ocr(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return [], []

    h, w = img.shape[:2]
    boxes = detect_plate(image_path)
    # if len(boxes) == 0:
    #     model.conf = 0.2
    #     boxes = detect_plate(image_path)
    #     model.conf = 0.5

    texts = []

    for box in boxes:
        x1, y1, x2, y2 = map(int, box)
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w, x2), min(h, y2)
        if x2 <= x1 or y2 <= y1:
            continue

        crop = img[y1:y2, x1:x2]
        proc = preprocess_for_ocr(crop)
        filename = os.path.basename(image_path)
        print(f"Przetwarzanie obrazu: {filename}")
        cfg = r'--oem 3 --psm 8 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        text = pytesseract.image_to_string(proc, config=cfg).strip()

        if len(text) > 7:
            text = text[1:]
            text = text.upper()
        texts.append(text)
  
    return texts, boxes
