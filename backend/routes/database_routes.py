from flask import Blueprint, jsonify
from database import db

# Blueprint for database routes
database_bp = Blueprint("database_bp", __name__)

@database_bp.route("/recent_detections", methods=["GET"])
def get_recent_detections():
    """Fetches recent detections from the database."""
    return jsonify(db.get_recent_detections())