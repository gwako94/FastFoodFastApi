from flask import request, jsonify, Blueprint, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from app.v2.models.userModel import User


v2_user = Blueprint('v2_users', __name__)

@v2_user.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user_details = User(
        data['username'],
        data['email'],
        data['password']
    )
    try:
        user_details.register_user()
        return jsonify({'message': 'User registered successfully!'})
    except:
        return jsonify({'message': 'User already exists!'})

