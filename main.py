import os
from glob import glob
from evaluate import evaluate

# Ścieżki do zdjęć i etykiet (zakładamy: nazwa pliku = ground truth)
image_paths = sorted(glob("data/photos/*.jpg"))
ground_truths = [os.path.basename(p).split("_")[0] for p in image_paths]

# Przetestuj na pierwszych 100 zdjęciach
evaluate(image_paths[:100], ground_truths[:100])
