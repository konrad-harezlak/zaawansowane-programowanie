import os
from glob import glob
from evaluate import evaluate
from utils import load_ground_truths_from_cvat_xml

 
gt_dict = load_ground_truths_from_cvat_xml('data/annotations.xml')
image_paths = sorted(glob('data/photos/*.jpg'))
ground_truths = [gt_dict[img_path.split()[-1]] for img_path in image_paths]

evaluate(image_paths[100], ground_truths[100])