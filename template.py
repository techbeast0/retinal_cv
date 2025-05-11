import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

list_of_files = [
    
    "data/aptos/.gitkeep",
    "data/drive/.gitkeep",

    
    "classification/preprocess.py",
    "classification/train.py",
    "classification/evaluate.py",

   
    "segmentation/preprocess.py",
    "segmentation/train_unet.py",
    "segmentation/evaluate_unet.py",

   
    "utils/augmentations.py",
    "utils/metrics.py",

   
    "explainability/gradcam.py",

    
    "config/config.yaml",

    
    "notebooks/classification_eda.ipynb",
    "notebooks/segmentation_eda.ipynb",

    
    "research/trials.ipynb",

    
    "templates/index.html",

    
    ".gitignore",
    "README.md",
    "requirements.txt",
    "setup.py",
    "dvc.yaml",
    "params.yaml",
    "main.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists.")
