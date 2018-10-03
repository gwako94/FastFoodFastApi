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
from app.v2.models.userModel import User
from app.v2.migration import Database
db = Database()
cur = db.cur


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'access-token' in request.headers:
            token = request.headers['access-token']

        if not token:
            return jsonify({'message': 'Token not found'}), 401

        try:
            data = jwt.decode(token, os.getenv('SECRET_KEY'))
            query = "SELECT * from users WHERE username=%s;"
            cur.execute(query, (data['username'],))
            current_user = cur.fetchone()

        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
