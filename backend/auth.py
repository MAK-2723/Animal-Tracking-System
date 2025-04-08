from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import config
from database.db import insert_user, find_user

def register_user(username, password):
    """Registers a new user with hashed password."""
    if find_user(username):
        return {"error": "User already exists"}, 400
    
    password_hash = generate_password_hash(password)
    insert_user(username, password_hash)
    return {"message": "User registered successfully"}, 201

def login_user(username, password):
    """Authenticates user and returns JWT token."""
    user = find_user(username)
    if not user or not check_password_hash(user['password_hash'], password):
        return {"error": "Invalid credentials"}, 401
    
    token = jwt.encode({
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, config.SECRET_KEY, algorithm="HS256")
    
    return {"token": token}, 200

def verify_token(token):
    """Verifies JWT token and returns username."""
    try:
        decoded_token = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        return decoded_token["username"]
    except jwt.ExpiredSignatureError:
        return None