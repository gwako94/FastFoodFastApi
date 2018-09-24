from flask import request, jsonify, Blueprint, make_response
from app.v1.models.userModel import User
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import os
import jwt
v1_user = Blueprint('users', __name__)

users = User()  # User class instance


@v1_user.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data["username"].strip()
    email = data["email"].strip()
    passsword = data["password"].strip()

    if not username:
        return jsonify({'message': 'Username cannot be empty!'}), 400
    if not email:
        return jsonify({'message': 'Email cannot be empty!'}), 400
    if not passsword:
        return jsonify({'message': 'Password cannot be empty!'}), 400

    hashed_password = generate_password_hash(passsword, method='sha256')

    users.register_user(
            username=username,
            email=email,
            password=hashed_password
        )
    return jsonify({'message': 'User Registered successfully!'}), 201

@v1_user.route('/login', methods=['POST'])
def login():
    auth = request.get_json()

    if not auth or not auth["username"] or not auth["password"]:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    
    name = auth["username"]
    user = users.users[name]

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user["password"], auth["password"]):
        token = jwt.encode({"username": user["username"], "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, os.getenv('SECRET_KEY'))
        return jsonify({'message': 'Login success!',
                        'token' : token.decode('UTF-8')})
    
    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

@v1_user.route('/users', methods=['GET'])
def get_users():
    all_users = users.get_users()
    if not all_users:
        return jsonify({'message': 'No users found!'})
    return jsonify({'Users': all_users})


        

