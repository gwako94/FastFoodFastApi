from flask import request, jsonify, Blueprint, make_response
from app.v1.models.userModel import User
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
import jwt
import datetime
from app.v1.auth import userAuth
v1_user = Blueprint('users', __name__)

users = User()  # User class instance


@v1_user.route('', methods=['POST'])
def register_user():
    data = request.get_json()

    users.register_user(
        username=data["username"],
        email=data["email"],
        password=data["password"]
    )
    return jsonify({'message': 'User Registered successfully!'}), 201


@v1_user.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('*Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    name = auth.username
    user = users.users[name]
        

    if not user:
        return make_response('#Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if check_password_hash(user["password"], auth.password):
        token = jwt.encode({'public_id' : user["public_id"], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)})
        return jsonify({'token' : token.decode('UTF-8')})
    
    return make_response('@Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})