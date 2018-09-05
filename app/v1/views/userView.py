from flask import request, jsonify, Blueprint
from app.v1.models.userModel import User
import datetime
v1_user = Blueprint('users', __name__)

user = User() # User class instance

@v1_user.route('', methods=['POST'])
def register_user():
    data = request.get_json()

    user.register_user(
        username = data["username"],
        email = data["email"],
        password = data["password"],
        confirm_password = data["confirm_password"]
    )
    return jsonify({'message': 'User Registered successfully!'}), 201

@v1_user.route('', methods=['GET'])
def get_users():
    all_users = user.get_users()

    return jsonify({'Users': all_users})