import time
from detect_and_ocr import extract_plate_and_ocr


def calculate_final_grade(accuracy_percent: float, processing_time_sec: float) -> float:
    if accuracy_percent < 60 or processing_time_sec > 60:
        return 2.0

    accuracy_norm = (accuracy_percent - 60) / 40
    time_norm = (60 - processing_time_sec) / 50
    score = 0.7 * accuracy_norm + 0.3 * time_norm
    grade = 2.0 + 3.0 * score
    return round(grade * 2) / 2


def evaluate(image_paths, ground_truths):
    assert len(image_paths) == len(ground_truths), "Mismatch in number of images and labels"
    correct = 0
    total = len(image_paths)

    start_time = time.time()

    for img_path, gt_text in zip(image_paths, ground_truths):
        pred_texts, _ = extract_plate_and_ocr(img_path)
        pred_text = pred_texts[0] if pred_texts else ""
        print(f"GT: {gt_text}, OCR: {pred_text}")

        if pred_text.replace(" ", "").upper() == gt_text.replace(" ", "").upper():
            correct += 1

    end_time = time.time()
    processing_time = end_time - start_time
    accuracy_percent = (correct / total) * 100

    print(f"OCR Accuracy: {accuracy_percent:.2f}%")
    print(f"Processing Time: {processing_time:.2f}s")

    grade = calculate_final_grade(accuracy_percent, processing_time)
    print(f"Final Grade: {grade:.1f}")
print(calculate_final_grade(62,20))