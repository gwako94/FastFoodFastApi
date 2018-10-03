""" function to perform validations"""
import re
from flask import jsonify


def validate_register(data):
    # validate username
    if validate_username(data):
        return validate_username(data)

    # validate email
    if validate_email(data):
        return validate_email(data)

    # validate password
    if validate_password(data):
        return validate_password(data)


def validate_username(data):
    """Validate username"""
    if not re.match(r'^[a-zA-Z0-9]{5,15}$', data['username']):
        msg = "Username should have letters or numbers or a combination of both and should be 5 or more characters long"
        return jsonify({'message': msg}), 400


def validate_email(data):
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', data['email']):
        msg = "Please input a valid email!"
        return jsonify({'message': msg}), 400


def validate_password(data):
    if not re.match(r'^[\w\W]{6,}$', data['password']):
        msg = "Password must be atlist 6 characters long"
        return jsonify({'message': msg}), 400
