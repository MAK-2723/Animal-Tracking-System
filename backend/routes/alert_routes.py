from flask import Blueprint, request, jsonify
from alert import send_alert
from auth_routes import token_required
from database import db

alert_bp = Blueprint("alert_bp", __name__)

@alert_bp.route("/send_alert", methods=["POST"])
def trigger_alert():
    """Triggers an alert based on detected animal category."""
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data received"}), 400
    
    species = data.get("species")
    category = data.get("category")
    timestamp = data.get("timestamp")
    location = data.get("location")
    
    if not all([species, category, timestamp, location]):
        return jsonify({"error": "Missing required data"}), 400
    
    send_alert(species, category, timestamp, location)
    return jsonify({"message": "Alert sent successfully"})

@alert_bp.route("/alerts",methods=["GET"])
@token_required
def get_alerts(current_user):
    db=get_database()
    alerts=db.alerts.find({},{'_id':0})
    return jsonify(list(alerts))
