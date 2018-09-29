from flask import request, jsonify, Blueprint, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import datetime
import jwt
import os

#import locals files
from app.v2.models.userModel import User
from app.v2.utilities import validate_register
from app.v2.migration import Database
db = Database()
cur = db.cur

v2_user = Blueprint('v2_users', __name__)

@v2_user.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if validate_register(data):
        return validate_register(data)

    hashed_password = generate_password_hash(data['password'], method='sha256')
    user_details = User(
        data['username'],
        data['email'],
        hashed_password
    )
  
    if user_details.register_user():
        return jsonify({'message': 'User Registered successfully!'}), 201
    return jsonify({'message': 'User already exists!'}), 400

@v2_user.route('/login', methods=['POST'])
def login():
    auth = request.get_json()

    if not auth or not auth["username"] or not auth["password"]:
        return jsonify({'message': 'Could not verify'}), 401

    query = "SELECT username, password from users WHERE username=%s;"
    cur.execute(query, (auth['username'],))
    user = cur.fetchone()

    if not user:
        return jsonify({'message': 'Could not verify'}), 401
    
    if check_password_hash(user['password'], auth["password"]):
        token = jwt.encode({"username": user['username'], "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, os.getenv('SECRET_KEY'))
        return jsonify({'message': 'Login success!',
                        'token' : token.decode('UTF-8')})

    return jsonify({'message': 'Could not verify!'})

    

