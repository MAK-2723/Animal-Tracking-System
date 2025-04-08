from flask import Blueprint, request, jsonify
import os
import cv2
import datetime
from detection import detect_animals,load_model
from database import db
from alert import send_alert

# Blueprint for detection routes
detect_bp = Blueprint("detect_bp", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

MODEL_PATH=os.getenv("animal-tracking-system/backend/models","yolov8.pt")
model=load_model(MODEL_PATH)

@detect_bp.route("/detect", methods=["POST"])
def detect():
    """Endpoint to process image and detect animals."""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file and file.filename:
        image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(image_path)
    
    frame = cv2.imread(image_path)
    detections = detect_animals(frame,model)
    
    detected_data = []
    for detection in detections:
        species = detection['species']
        confidence = detection['confidence']
        category = classify_animal(species)
        timestamp = datetime.datetime.now().isoformat()
        location = "Unknown"  # Placeholder, GPS integration needed
        
        db.save_detection(species, category, image_path, timestamp, location, confidence)
        
        if category in ["Harmful", "Lethal"]:
            send_alert(species, category, timestamp, location)
        
        detected_data.append({
            "species": species,
            "confidence": confidence,
            "category": category,
            "timestamp": timestamp,
            "location": location
        })
    
    return jsonify({"detections": detected_data})

# Helper function to classify animals
def classify_animal(species):
    """Classifies the detected animal into a category."""
    classification = {
        "Deer": "Safe",
        "Dog": "Moderate",
        "Tiger": "Harmful",
        "Snake": "Lethal"
    }
    return classification.get(species, "Unknown")