from flask import request, jsonify, Blueprint, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import datetime
import jwt
import os

# import locals files
from app.v2.models.userModel import User
from app.v2.utilities import validate_register
from app.v2.auth import token_required
from app.v2.migration import Database
db = Database()
cur = db.cur

v2_user = Blueprint('v2_users', __name__)


@v2_user.route('/auth/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if validate_register(data):
        return validate_register(data)

    query = "SELECT email from users;"
    cur.execute(query)
    emails = cur.fetchall()
    for email in emails:
        if email['email'] == data['email']:
            return jsonify({'message': 'User already exists!'}), 409
            
    hashed_password = generate_password_hash(data['password'], method='sha256')
    user_details = User(
        data['username'],
        data['email'],
        hashed_password
    )

    if user_details.register_user():
        return jsonify({'message': 'User Registered successfully!'}), 201
    return jsonify({'message': 'User already exists!'}), 409


@v2_user.route('/user/<user_id>', methods=['PUT'])
@token_required
def promote_user(current_user, user_id):
    user = User.get_user_by_id(user_id)
    if current_user['admin']:
        if user:
            query = "UPDATE users SET admin='true' WHERE id=%s"
            cur.execute(query, (user_id, ))
            db.conn.commit()
            return jsonify({'message': 'User promoted to an admin'})
        return jsonify({'message': 'User not found!'})
    return jsonify({'message': 'You are not authorized to perform this function!'})


@v2_user.route('/auth/login', methods=['POST'])
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
        token = jwt.encode(
            {"username": user['username'],
             "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=720)},
            os.getenv('SECRET_KEY'))
        return jsonify({'message': 'Login success!',
                        'token': token.decode('UTF-8')}), 200

    return jsonify({'message': 'Could not verify!'})
