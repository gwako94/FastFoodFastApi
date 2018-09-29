from flask import request, jsonify, Blueprint, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from app.v2.models.userModel import User
from app.v2.utilities import validate_register


v2_user = Blueprint('v2_users', __name__)

@v2_user.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if validate_register(data):
        return validate_register(data)
        
    user_details = User(
        data['username'],
        data['email'],
        data['password']
    )
  
    user_details.register_user()
    return jsonify({'message': 'User registered successfully!'})

