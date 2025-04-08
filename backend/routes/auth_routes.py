from flask import Blueprint, request, jsonify
from auth import register_user, login_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """Registers a new user."""
    try:
        data = request.json
        if not data:
            return jsonify({"error":"Invalid request, JSON expected"}),400
        username = data.get("username")
        password = data.get("password")
    
        if not username or not password:
            return jsonify({"error": "Username and password required"}), 400
    
        return register_user(username, password)
    except Exception as e:
        return jsonify({"error":str(e)}),500

@auth_bp.route('/login', methods=['POST'])
def login():
    """Logs in a user and returns a JWT token."""
    try:
        data = request.json
        if not data:
            return jsonify({"error":"Invalid request, JSON expected"}),400
        username = data.get("username")
        password = data.get("password")
    
        if not username or not password:
            return jsonify({"error": "Username and password required"}), 400
    
        return login_user(username, password)
    except Exception as e:
        return jsonify({"error":str(e)}),500