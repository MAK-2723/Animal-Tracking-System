import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Database Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/animal_tracking")

# YOLOv8 Model Path
YOLO_MODEL_PATH = os.getenv("YOLO_MODEL_PATH", "backend/models/best.pt")

# Twilio SMS Configuration
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# Google Maps API Key
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")