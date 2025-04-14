from pymongo import MongoClient
import os

MONGO_URI = "mongodb://localhost:27017/animal_tracking"

class Database:
    """Handles MongoDB operations for storing and retrieving detections."""
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client.get_database()
        self.detections = self.db["detections"]
    
    def save_detection(self, species, category, image_path, timestamp, location, confidence):
        """Stores detection details in MongoDB."""
        detection_data = {
            "species": species,
            "category": category,
            "image_path": image_path,
            "timestamp": timestamp,
            "location": location,
            "confidence": confidence
        }
        self.detections.insert_one(detection_data)
    
    def get_recent_detections(self, limit=10):
        """Fetches recent animal detections sorted by timestamp."""
        return list(self.detections.find().sort("timestamp", -1).limit(limit))
    
# Initialize Database instance
db = Database()
