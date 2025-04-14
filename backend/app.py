from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from routes.detect_routes import detect_bp
from routes.auth_routes import auth_bp
from routes.alert_routes import alert_bp
from routes.dashboard_routes import dashboard_bp
import config
import os
from database.db import initialize_db
from dotenv import load_dotenv
from camera_feed import CameraStream
from detection import load_model

#Load environment variables
load_dotenv()

app = Flask(__name__,static_folder="animal-tracking-system/frontend/static",template_folder="animal-tracking-system/frontend")
CORS(app,resources={r"/api/*":{"origins":"*"}})

# Load configuration
app.config.from_object(config)

#Load YOLO model
MODEL_PATH=os.getenv("animal-tracking-system/backend/models","models/best.pt")
model=load_model(MODEL_PATH)

#Start camera stream
camera=CameraStream()
camera.start()

#Initialize Database
initialize_db()

# Register Blueprints (API Routes)
app.register_blueprint(detect_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(alert_bp, url_prefix='/api')
app.register_blueprint(dashboard_bp, url_prefix='/api')
app.register_blueprint(database_bp, url_prefix='/api')

@app.route('/')
def home():
    return jsonify({"message": "Animal Tracking System API is running"})

# Serve frontend pages
@app.route('/')
def serve_index():
    return send_from_directory(app.template_folder, "index.html")

@app.route('/about')
def serve_about():
    return send_from_directory(app.template_folder, "about.html")

@app.route('/contact')
def serve_contact():
    return send_from_directory(app.template_folder, "contact.html")

@app.route('/login')
def serve_login():
    return send_from_directory(app.template_folder, "login.html")

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.template_folder, path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 10000))
