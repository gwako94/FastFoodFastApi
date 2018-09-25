import jwt
from functools import wraps
from flask import jsonify, request
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from app.v1.models.userModel import User
user = User()
users = user.users

def auth_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token not found'}), 401

        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY'))
            current_user = data["username"]

        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
