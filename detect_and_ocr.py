import cv2
import easyocr
import yolov5
import torch
import re
import warnings

warnings.filterwarnings("ignore", category=FutureWarning) 
warnings.filterwarnings("ignore") 

model = yolov5.load('keremberke/yolov5n-license-plate')
model.conf = 0.1
model.iou = 0.1
model.to('cuda' if torch.cuda.is_available() else 'cpu')

gpu_enabled = torch.cuda.is_available()
reader = easyocr.Reader(['en'], gpu=gpu_enabled)

def preprocess_plate(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 19, 19)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opened = cv2.morphologyEx(bfilter, cv2.MORPH_OPEN, kernel)   
    
    return opened

def preprocess_unreadable(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 19, 19)
    thresh, im_bw = cv2.threshold(bfilter, 210, 250, cv2.THRESH_BINARY)

    return im_bw

def clean_plate_text(text):
    text = text.upper()
    chars = list(text)
    for i in range(min(2, len(chars))):
        if chars[i] == '0':
            chars[i] = 'O'
        elif chars[i] == '5':
            chars[i] = 'S'
        elif chars[i] == '2':
            chars[i] = 'Z'
        elif chars[i] == '6':
            chars[i] = 'G'
        elif chars[i] == ']':
            chars[i] = 'J'
        elif chars[i] == 'Q':
            chars[i] = 'O'
    text = ''.join(chars)

    text = re.sub(r'[^A-Z0-9]', '', text)
    if text.startswith("PL"):
      text = text[2:]

    if len(text) >8:
        text = text[:8]
    return text

def detect_plates(image):
    results = model(image, size=640)
    boxes = results.pred[0][:, :4].cpu().numpy().astype(int)
    return boxes

def extract_plate_and_ocr(image_path):
    image = cv2.imread(image_path)
    boxes = detect_plates(image)
    texts = []
    h, w = image.shape[:2]

    for (x1, y1, x2, y2) in boxes:
      x1, y1 = max(0, x1), max(0, y1)
      x2, y2 = min(w, x2), min(h, y2) 
      crop = image[y1:y2-5, x1+25:x2-10]
      crop = preprocess_plate(crop)
      result = reader.readtext(crop, detail=0, paragraph=False, min_size=200)
      text = ''.join(result) if result else '<unreadable>'
      if text == '<unreadable>':
        result = reader.readtext(crop, detail=0)
        text = ''.join(result) if result else '<unreadable>'
      if text == '<unreadable>':
        processed_image = preprocess_unreadable(image[y1:y2-5, x1+25:x2])
        result = reader.readtext(processed_image, detail=0, paragraph=False,)
        text=''.join(result) if result else '<still unreadable>'

      text = clean_plate_text(text)
      texts.append(text)
    return texts, boxes  

