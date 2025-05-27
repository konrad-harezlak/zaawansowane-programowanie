import cv2
from ultralytics import YOLO
import easyocr

# Inicjalizacja modeli
yolo_model = YOLO("yolov8s.pt").to('cuda')
ocr_reader = easyocr.Reader(['pl'], gpu=False)

def detect_plate(image_path):
    results = yolo_model(image_path)
    boxes = results[0].boxes.xyxy.cpu().numpy()
    return boxes

def extract_plate_and_ocr(image_path):
    img = cv2.imread(image_path)
    boxes = detect_plate(image_path)
    
    texts = []
    for box in boxes:
        x1, y1, x2, y2 = map(int, box)
        plate_crop = img[y1:y2, x1:x2]
        ocr_result = ocr_reader.readtext(plate_crop)
        text = ocr_result[0][1] if ocr_result else ""
        texts.append(text)
    
    return texts, boxes
