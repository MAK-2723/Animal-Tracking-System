import torch
from ultralytics import YOLO
import cv2
import numpy as np
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MODEL_PATH = os.getenv("YOLO_MODEL_PATH", "models/best.pt")

# Load YOLO model
def load_model(model_path=MODEL_PATH):
    """Loads the YOLOv8 model from the specified path."""
    return YOLO(model_path)

def detect_animals(frame, model):
    """Detects animals in a given frame using YOLOv8."""
    results = model(frame)
    detections = []
    for *box, conf, cls in results.xyxy[0].tolist():
        x1, y1, x2, y2 = map(int, box)
        species = model.names[int(cls)]
        confidence = float(conf)
        detections.append({
            "bbox": (x1, y1, x2, y2),
            "species": species,
            "confidence": confidence
        })
    return detections

# Load model instance
model = load_model()

if __name__ == "__main__":
    img_path = "test.jpg"  # Example test image
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    detections = detect_animals(img_rgb, model)
    print("Detections:", detections)