import xml.etree.ElementTree as ET

def load_ground_truths_from_cvat_xml(xml_path: str) -> dict:
    tree = ET.parse(xml_path)
    root = tree.getroot()

    gt_dict = {}
    for image in root.findall('image'):
        filename = image.get('name')
        plate_number = None
        for box in image.findall('box'):
            for attr in box.findall('attribute'):
                if attr.get('name') == 'plate number':
                    plate_number = attr.text.strip()
                    break
            if plate_number:
                break
        if plate_number:
            gt_dict[filename] = plate_number
    return gt_dict