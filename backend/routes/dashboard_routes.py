from flask import Blueprint, jsonify
from auth_routes import token_required
from database import db

dashboard_bp = Blueprint("dashboard_bp", __name__)

@dashboard_bp.route("/dashboard_data", methods=["GET"])
@token_required
def get_dashboard_data():
    """Fetch summarized data for the dashboard visualization."""
    recent_detections = db.get_recent_detections(limit=50)
    return jsonify({"recent_detections": recent_detections})