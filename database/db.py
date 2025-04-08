from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "animal_tracking")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
detections_collection = db["detections"]
users_collection=db["users"]

def initialize_db():
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    client = MongoClient(mongo_uri)
    db = client["animal_tracking"]
    
    # Collections
    detections = db["detections"]
    users = db["users"]
    
    # Indexes for faster querying
    detections.create_index("timestamp")
    detections.create_index([("location", "2dsphere")])
    users.create_index("email", unique=True)
    
    print("Database initialized successfully.")
    return db

def insert_user(username, password_hash):
    """Insert a new user into the database."""
    users_collection.insert_one({"username": username, "password": password_hash})

def find_user(username):
    """Find a user by username."""
    return users_collection.find_one({"username": username})

def save_detection(species, category, image_path, timestamp, location, confidence):
    """Saves detection data to MongoDB."""
    detection_data = {
        "species": species,
        "category": category,
        "image_path": image_path,
        "timestamp": timestamp,
        "location": location,
        "confidence": confidence
    }
    detections_collection.insert_one(detection_data)

def get_recent_detections(limit=10):
    """Fetches recent detections from MongoDB."""
    detections = detections_collection.find().sort("timestamp", -1).limit(limit)
    return [{
        "species": d["species"],
        "category": d["category"],
        "image_path": d["image_path"],
        "timestamp": d["timestamp"],
        "location": d["location"],
        "confidence": d.get("confidence", "N/A")
    } for d in detections]