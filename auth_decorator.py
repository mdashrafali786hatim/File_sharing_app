from flask import jsonify
from flask_jwt_extended import get_jwt_identity

def role_required(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user = get_jwt_identity()
            if user['role'] != role:
                return jsonify({"message": "Access denied"}), 403
            return func(*args, **kwargs)
        return wrapper
    return decorator
